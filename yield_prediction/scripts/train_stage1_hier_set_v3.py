"""训练 ConditionStage1HierSetV3 — 用 V3 化学分类 label。

- v3 single head (7): anode_material/cathode_material/cell_class_v3/
  electrolyte_cation/electrolyte_anion/ligand_class_v3/additive_class_v3
- v3 hier head (3): reagent_class_v3/catalyst_class_v3/solvent_class_v3 → set head 输入
- catalyst tags multi-label (4 bits): mediator/photoredox/HAT/chiral (BCE)
- 3 个 set head (具体 SMILES vocab, Hungarian matching, 与 v2 一致)
"""
import sys, json, argparse
from pathlib import Path
from collections import Counter
from datetime import datetime

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3,
    SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS, FINE_ELECTRODE_HEADS,
)
# SMI 单 head 名 (具体 SMILES vocab): ligand, additive
SMI_HEADS = list(SMI_FROM_CLASS.keys())  # ['ligand', 'additive']
# 细粒度电极 head label key 映射 (head_name → label_key in records)
FINE_LABEL_KEY = {'anode_fine': 'anode_fine', 'cathode_fine': 'cathode_fine'}
from models.condition_stage1_set import hungarian_set_loss, decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single

DEFAULT_DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class HierSetV3Dataset(Dataset):
    def __init__(self, records, k_slots=K_SLOTS):
        self.records = records
        self.k_slots = k_slots

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        item = {'fp': torch.from_numpy(fp).float()}
        for k in SINGLE_HEADS_V3 + HIER_KEYS:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        # catalyst tags: int bitmask 0-15 → 4-d float vector
        bits = int(r['labels'][CAT_TAG_KEY])
        tag_vec = [float((bits >> b) & 1) for b in range(CAT_TAG_BITS)]
        item[CAT_TAG_KEY] = torch.tensor(tag_vec, dtype=torch.float32)
        # set labels (具体 SMILES vocab, 不变)
        for h in SET_HEADS:
            sl = r['set_labels'][h][:self.k_slots]
            item[f'{h}_set'] = sl
            item[f'{h}_len'] = len(sl)
        # ligand / additive 具体 SMILES idx (用于 single SMILES head)
        for k in SMI_HEADS:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        # V2 细粒度电极 label
        for fh in FINE_ELECTRODE_HEADS:
            item[fh] = torch.tensor(r['labels'][FINE_LABEL_KEY[fh]], dtype=torch.long)
        return item


def collate_fn(batch, num_classes):
    K = K_SLOTS
    out = {'fp': torch.stack([d['fp'] for d in batch])}
    for k in SINGLE_HEADS_V3 + HIER_KEYS:
        out[k] = torch.stack([d[k] for d in batch])
    out[CAT_TAG_KEY] = torch.stack([d[CAT_TAG_KEY] for d in batch])
    for h in SET_HEADS:
        no_obj = num_classes[h]
        padded = []; lens = []
        for d in batch:
            sl = d[f'{h}_set']
            p = sl + [no_obj] * (K - len(sl))
            padded.append(p); lens.append(d[f'{h}_len'])
        out[f'{h}_set'] = torch.tensor(padded, dtype=torch.long)
        out[f'{h}_len'] = torch.tensor(lens, dtype=torch.long)
    for k in SMI_HEADS:
        out[k] = torch.stack([d[k] for d in batch])
    for fh in FINE_ELECTRODE_HEADS:
        out[fh] = torch.stack([d[fh] for d in batch])
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=80)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--class_embed_dim', type=int, default=32)
    parser.add_argument('--cat_tag_embed_dim', type=int, default=8)
    parser.add_argument('--teacher_forcing_p', type=float, default=1.0)
    parser.add_argument('--ckpt_name', default='stage1_hier_set_v3.pt')
    parser.add_argument('--data_dir', default=str(DEFAULT_DATA_DIR))
    args = parser.parse_args()
    DATA_DIR = Path(args.data_dir)

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    nc_v3 = stats['num_classes_v3']
    print(f"train={len(train_records)}, val={len(val_records)}")
    print(f"v3 single sizes: " + ", ".join(f"{k}={nc_v3[k]}" for k in SINGLE_HEADS_V3))
    print(f"v3 hier sizes: " + ", ".join(f"{k}={nc_v3[k]}" for k in HIER_KEYS))
    print(f"set head SMILES vocab: solvent={nc['solvent']}, reagent={nc['reagent']}, catalyst={nc['catalyst']}")

    train_ds = HierSetV3Dataset(train_records)
    val_ds = HierSetV3Dataset(val_records)
    coll = lambda b: collate_fn(b, nc)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True, collate_fn=coll)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                             num_workers=2, collate_fn=coll)

    # Class weights for v3 single + hier heads + SMI single heads (1/sqrt(freq))
    weights = {}
    for k in SINGLE_HEADS_V3 + HIER_KEYS:
        cnt = Counter([r['labels'][k] for r in train_records])
        n_cls = nc_v3[k]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[k] = torch.from_numpy(w).to(args.device)
    for k in SMI_HEADS:
        cnt = Counter([r['labels'][k] for r in train_records])
        n_cls = nc[k]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[k] = torch.from_numpy(w).to(args.device)
    # V2 fine electrode heads
    for fh in FINE_ELECTRODE_HEADS:
        cnt = Counter([r['labels'][FINE_LABEL_KEY[fh]] for r in train_records])
        n_cls = nc[FINE_LABEL_KEY[fh]]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[fh] = torch.from_numpy(w).to(args.device)

    # catalyst tag pos weight (BCE): pos_weight = neg / pos
    tag_counts = np.zeros(CAT_TAG_BITS, dtype=np.float64)
    total = len(train_records)
    for r in train_records:
        bits = int(r['labels'][CAT_TAG_KEY])
        for b in range(CAT_TAG_BITS):
            if (bits >> b) & 1:
                tag_counts[b] += 1
    pos_weight = (total - tag_counts) / np.maximum(tag_counts, 1)
    pos_weight = torch.from_numpy(pos_weight.astype(np.float32)).to(args.device)
    print(f"catalyst tag pos_weight: {pos_weight.tolist()}")

    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=args.dropout,
        class_embed_dim=args.class_embed_dim,
        cat_tag_embed_dim=args.cat_tag_embed_dim,
    ).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    # Single + hier CE
    single_criterion = {}
    for k in SINGLE_HEADS_V3 + HIER_KEYS:
        ls = args.label_smoothing if nc_v3[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)
    for k in SMI_HEADS:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)
    for fh in FINE_ELECTRODE_HEADS:
        single_criterion[fh] = nn.CrossEntropyLoss(weight=weights[fh], label_smoothing=0.0)
    tag_criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    def eval_split(loader, name):
        model.eval()
        all_keys = SINGLE_HEADS_V3 + HIER_KEYS + SMI_HEADS + FINE_ELECTRODE_HEADS
        sums = {k: {'top1': 0, 'top3': 0, 'top5': 0} for k in all_keys}
        tag_correct = np.zeros(CAT_TAG_BITS); tag_total = np.zeros(CAT_TAG_BITS)
        tag_pred_pos = np.zeros(CAT_TAG_BITS); tag_gt_pos = np.zeros(CAT_TAG_BITS)
        tag_tp = np.zeros(CAT_TAG_BITS)
        set_preds = {h: [] for h in SET_HEADS}
        set_gts = {h: [] for h in SET_HEADS}
        topk_recall = {h: {f'top{kk}': 0 for kk in [5, 10, 20]} for h in SET_HEADS}
        n = 0
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                out = model(fp, teacher=None)  # 推理无 teacher forcing
                bsz = fp.size(0); n += bsz
                for k in all_keys:
                    tgt = batch[k].to(args.device)
                    r = topk_accuracy_single(out[k], tgt, ks=(1, 3, 5))
                    for kk, v in r.items(): sums[k][kk] += v
                # tags
                tag_logits = out[CAT_TAG_KEY]
                tag_pred = (torch.sigmoid(tag_logits) > 0.5).float().cpu().numpy()
                tag_gt = batch[CAT_TAG_KEY].numpy()
                tag_correct += (tag_pred == tag_gt).sum(axis=0)
                tag_total += bsz
                tag_pred_pos += tag_pred.sum(axis=0)
                tag_gt_pos += tag_gt.sum(axis=0)
                tag_tp += ((tag_pred == 1) & (tag_gt == 1)).sum(axis=0)
                # set
                for h in SET_HEADS:
                    slots = out[h]; no_obj = nc[h]
                    set_preds[h].extend(decode_set(slots, no_obj))
                    gt_p = batch[f'{h}_set'].cpu().numpy()
                    gt_l = batch[f'{h}_len'].cpu().numpy()
                    cand = decode_set_topk(slots, no_obj, K_total=20)
                    for i in range(bsz):
                        set_gts[h].append(gt_p[i, :gt_l[i]].tolist())
                        gt_set = set(gt_p[i, :gt_l[i]].tolist())
                        if not gt_set: continue
                        for kk in [5, 10, 20]:
                            if gt_set & set(cand[i][:kk]):
                                topk_recall[h][f'top{kk}'] += 1

        print(f"\n[{name}] v3 single + hier + SMI + V2 fine electrode Top-K:")
        for k in SINGLE_HEADS_V3 + FINE_ELECTRODE_HEADS + HIER_KEYS + SMI_HEADS:
            print(f"  {k:<22} Top1={sums[k]['top1']/n*100:5.2f}% Top3={sums[k]['top3']/n*100:5.2f}% Top5={sums[k]['top5']/n*100:5.2f}%")
        single_avg = float(np.mean([sums[k]['top1'] / n for k in SINGLE_HEADS_V3]))
        hier_avg = float(np.mean([sums[k]['top1'] / n for k in HIER_KEYS]))
        smi_avg = float(np.mean([sums[k]['top1'] / n for k in SMI_HEADS]))
        print(f"  AVG single (7) = {single_avg*100:.2f}%, AVG hier (3) = {hier_avg*100:.2f}%, AVG smi (2) = {smi_avg*100:.2f}%")

        TAG_NAMES = ['mediator', 'photoredox', 'HAT', 'chiral']
        print(f"\n[{name}] catalyst tag multi-label:")
        tag_f1s = []
        for b in range(CAT_TAG_BITS):
            acc = tag_correct[b] / tag_total[b]
            p = tag_tp[b] / max(tag_pred_pos[b], 1)
            r = tag_tp[b] / max(tag_gt_pos[b], 1)
            f1 = 2*p*r / max(p+r, 1e-6)
            tag_f1s.append(f1)
            print(f"  {TAG_NAMES[b]:<12} acc={acc*100:5.2f}% prec={p*100:5.2f}% recall={r*100:5.2f}% F1={f1*100:5.2f}%  (gt_pos={int(tag_gt_pos[b])}/{int(tag_total[b])})")
        tag_avg_f1 = float(np.mean(tag_f1s))
        print(f"  AVG tag F1 = {tag_avg_f1*100:.2f}%")

        print(f"\n[{name}] set heads (具体 SMILES, K-slot):")
        set_avg_f1 = 0
        for h in SET_HEADS:
            r, p, f1 = set_metrics(set_preds[h], set_gts[h])
            set_avg_f1 += f1
            print(f"  {h:<10} Recall={r*100:6.2f}% Precision={p*100:6.2f}% F1={f1*100:6.2f}%  "
                  f"Top5={topk_recall[h]['top5']/n*100:5.2f}%  Top10={topk_recall[h]['top10']/n*100:5.2f}%  Top20={topk_recall[h]['top20']/n*100:5.2f}%")
        set_avg_f1 /= len(SET_HEADS)
        # score: 加权 single + hier + smi + tag + set
        score = 0.35 * single_avg + 0.15 * hier_avg + 0.1 * smi_avg + 0.1 * tag_avg_f1 + 0.3 * set_avg_f1
        return single_avg, hier_avg, smi_avg, tag_avg_f1, set_avg_f1, score

    best_val = 0.0; best_epoch = -1; history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = {'single': 0.0, 'hier': 0.0, 'smi': 0.0, 'tag': 0.0, 'set': 0.0}
        n_b = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            teacher = {}
            for k in HIER_KEYS:
                teacher[k] = batch[k].to(args.device)
            # ligand_class_v3 / additive_class_v3 也是 teacher forcing 目标 (喂 smi single head)
            for cls_name in SMI_FROM_CLASS.values():
                teacher[cls_name] = batch[cls_name].to(args.device)
            teacher[CAT_TAG_KEY] = batch[CAT_TAG_KEY].to(args.device)
            # scheduled sampling
            use_tf = (np.random.rand() < args.teacher_forcing_p)
            out = model(fp, teacher=teacher if use_tf else None)

            # losses
            single_loss = 0.0
            for k in SINGLE_HEADS_V3:
                tgt = batch[k].to(args.device)
                single_loss = single_loss + single_criterion[k](out[k], tgt)
            # V2 细粒度电极 loss
            for fh in FINE_ELECTRODE_HEADS:
                tgt = batch[fh].to(args.device)
                single_loss = single_loss + single_criterion[fh](out[fh], tgt)
            hier_loss = 0.0
            for k in HIER_KEYS:
                tgt = batch[k].to(args.device)
                hier_loss = hier_loss + single_criterion[k](out[k], tgt)
            smi_loss = 0.0
            for k in SMI_HEADS:
                tgt = batch[k].to(args.device)
                smi_loss = smi_loss + single_criterion[k](out[k], tgt)
            tag_loss = tag_criterion(out[CAT_TAG_KEY], batch[CAT_TAG_KEY].to(args.device))
            set_loss = 0.0
            for h in SET_HEADS:
                slots = out[h]
                tgt = batch[f'{h}_set'].to(args.device)
                lens = batch[f'{h}_len'].to(args.device)
                set_loss = set_loss + hungarian_set_loss(slots, tgt, lens, no_obj_idx=nc[h])

            total = single_loss + hier_loss + smi_loss + tag_loss + set_loss
            optimizer.zero_grad()
            total.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running['single'] += float(single_loss.detach())
            running['hier'] += float(hier_loss.detach())
            running['smi'] += float(smi_loss.detach())
            running['tag'] += float(tag_loss.detach())
            running['set'] += float(set_loss.detach())
            n_b += 1
            pbar.set_postfix(s=f"{single_loss.item():.2f}", h=f"{hier_loss.item():.2f}",
                              sm=f"{smi_loss.item():.2f}",
                              tg=f"{tag_loss.item():.2f}", st=f"{set_loss.item():.2f}")
        scheduler.step()
        print(f"Epoch {epoch}: single={running['single']/n_b:.3f} hier={running['hier']/n_b:.3f} "
              f"smi={running['smi']/n_b:.3f} tag={running['tag']/n_b:.3f} set={running['set']/n_b:.3f} "
              f"lr={optimizer.param_groups[0]['lr']:.2e}")

        single_avg, hier_avg, smi_avg, tag_avg_f1, set_f1, score = eval_split(val_loader, 'VAL')
        history.append({'epoch': epoch, 'val_single_avg': single_avg,
                         'val_hier_avg': hier_avg, 'val_smi_avg': smi_avg,
                         'val_tag_f1': tag_avg_f1, 'val_set_f1': set_f1, 'score': score})
        if score > best_val:
            best_val = score; best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc, 'num_classes_v3': nc_v3,
                'fp_dim': 6144, 'hidden_dims': (1024, 768, 512),
                'dropout': args.dropout, 'k_slots': K_SLOTS,
                'class_embed_dim': args.class_embed_dim,
                'cat_tag_embed_dim': args.cat_tag_embed_dim,
                'hier_set_v3': True, 'has_smi_heads': True,
                'epoch': epoch,
                'val_single_avg': single_avg, 'val_hier_avg': hier_avg,
                'val_smi_avg': smi_avg,
                'val_tag_f1': tag_avg_f1, 'val_set_f1': set_f1,
            }, CKPT_DIR / args.ckpt_name)
            print(f"  -> Saved best (single={single_avg*100:.2f}% hier={hier_avg*100:.2f}% "
                  f"smi={smi_avg*100:.2f}% tag_f1={tag_avg_f1*100:.2f}% set_f1={set_f1*100:.2f}%)")

    out = {'best_epoch': best_epoch, 'best_val_score': best_val, 'history': history}
    json.dump(out, open(CKPT_DIR / 'experiments' / 'stage1_hier_set_v3_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, score = {best_val:.4f}")


if __name__ == '__main__':
    main()
