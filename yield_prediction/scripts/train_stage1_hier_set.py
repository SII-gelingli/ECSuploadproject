"""训练 ConditionStage1HierSet — hier + Set 联合架构。

- 单标签 head: anode/cathode/cell_type/electrolyte/ligand/additive (CE loss)
- reagent_class head: 47 类 (CE loss)
- Set head: solvent/catalyst (Hungarian matching loss)
- reagent set head: 接收 reagent_class embedding (teacher forcing) + Hungarian loss
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

from models.condition_stage1_hier_set import (
    ConditionStage1HierSet, PARALLEL_HEADS, SET_HEADS, K_SLOTS,
)
from models.condition_stage1_set import hungarian_set_loss, decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class HierSetDataset(Dataset):
    def __init__(self, records, k_slots=K_SLOTS):
        self.records = records
        self.k_slots = k_slots

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        item = {'fp': torch.from_numpy(fp).float()}
        for k in list(PARALLEL_HEADS) + ['reagent_class']:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        for h in SET_HEADS:
            sl = r['set_labels'][h][:self.k_slots]
            item[f'{h}_set'] = sl
            item[f'{h}_len'] = len(sl)
        return item


def collate_fn(batch, num_classes):
    K = K_SLOTS
    out = {'fp': torch.stack([d['fp'] for d in batch])}
    for k in list(PARALLEL_HEADS) + ['reagent_class']:
        out[k] = torch.stack([d[k] for d in batch])
    for h in SET_HEADS:
        no_obj = num_classes[h]
        padded = []; lens = []
        for d in batch:
            sl = d[f'{h}_set']
            p = sl + [no_obj] * (K - len(sl))
            padded.append(p); lens.append(d[f'{h}_len'])
        out[f'{h}_set'] = torch.tensor(padded, dtype=torch.long)
        out[f'{h}_len'] = torch.tensor(lens, dtype=torch.long)
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
    parser.add_argument('--teacher_forcing_p', type=float, default=1.0,
                        help='以多大概率用 GT class label (1.0=完全 teacher forcing)')
    args = parser.parse_args()

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}")
    print(f"vocab sizes: solvent={nc['solvent']}, reagent={nc['reagent']}, catalyst={nc['catalyst']}, reagent_class={nc['reagent_class']}")

    train_ds = HierSetDataset(train_records)
    val_ds = HierSetDataset(val_records)
    coll = lambda b: collate_fn(b, nc)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True, collate_fn=coll)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                             num_workers=2, collate_fn=coll)

    # Class weights for single heads (含 reagent_class)
    weights = {}
    for k in list(PARALLEL_HEADS) + ['reagent_class']:
        cnt = Counter([r['labels'][k] for r in train_records])
        n_cls = nc[k]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[k] = torch.from_numpy(w).to(args.device)

    model = ConditionStage1HierSet(num_classes=nc, fp_dim=6144,
                                    hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                    class_embed_dim=args.class_embed_dim).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    single_criterion = {}
    for k in list(PARALLEL_HEADS) + ['reagent_class']:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)

    def eval_split(loader, name):
        model.eval()
        single_keys = list(PARALLEL_HEADS) + ['reagent_class']
        sums = {k: {'top1': 0, 'top3': 0, 'top5': 0} for k in single_keys}
        set_preds = {h: [] for h in SET_HEADS}
        set_gts = {h: [] for h in SET_HEADS}
        topk_recall = {h: {f'top{kk}': 0 for kk in [5, 10, 20]} for h in SET_HEADS}
        n = 0
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                # 推理时不用 teacher forcing — 自己预测 class
                out = model(fp, teacher_class=None)
                bsz = fp.size(0); n += bsz
                for k in single_keys:
                    tgt = batch[k].to(args.device)
                    r = topk_accuracy_single(out[k], tgt, ks=(1,3,5))
                    for kk, v in r.items(): sums[k][kk] += v
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
        print(f"\n[{name}] 单标签 head Top-1:")
        for k in single_keys:
            print(f"  {k:<14} Top1={sums[k]['top1']/n*100:5.2f}% Top3={sums[k]['top3']/n*100:5.2f}% Top5={sums[k]['top5']/n*100:5.2f}%")
        single_avg = np.mean([sums[k]['top1']/n for k in list(PARALLEL_HEADS)])  # 6 head, no reagent_class
        rc_top1 = sums['reagent_class']['top1']/n
        print(f"  AVG (6 single)  {single_avg*100:5.2f}%, reagent_class Top-1 = {rc_top1*100:5.2f}%")

        print(f"\n[{name}] Set heads:")
        set_avg_f1 = 0
        for h in SET_HEADS:
            r, p, f1 = set_metrics(set_preds[h], set_gts[h])
            set_avg_f1 += f1
            print(f"  {h:<10} Recall={r*100:6.2f}% Precision={p*100:6.2f}% F1={f1*100:6.2f}%  "
                  f"Top5={topk_recall[h]['top5']/n*100:5.2f}%  Top10={topk_recall[h]['top10']/n*100:5.2f}%  Top20={topk_recall[h]['top20']/n*100:5.2f}%")
        set_avg_f1 /= len(SET_HEADS)
        score = 0.5 * single_avg + 0.5 * set_avg_f1
        return single_avg, set_avg_f1, rc_top1, score

    best_val = 0.0; best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running_single = 0.0; running_set = 0.0; running_rc = 0.0
        n_b = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            # teacher forcing: 用 GT reagent_class
            rc_label = batch['reagent_class'].to(args.device)
            # Schedule sampling: 概率使用 teacher_forcing
            use_tf = (np.random.rand() < args.teacher_forcing_p)
            out = model(fp, teacher_class=rc_label if use_tf else None)

            # 单标签 loss (含 reagent_class)
            single_loss = 0.0; rc_loss_v = 0.0
            for k in list(PARALLEL_HEADS):
                tgt = batch[k].to(args.device)
                single_loss = single_loss + single_criterion[k](out[k], tgt)
            rc_loss = single_criterion['reagent_class'](out['reagent_class'], rc_label)
            rc_loss_v = float(rc_loss.detach())
            # Set loss
            set_loss = 0.0
            for h in SET_HEADS:
                slots = out[h]
                tgt = batch[f'{h}_set'].to(args.device)
                lens = batch[f'{h}_len'].to(args.device)
                set_loss = set_loss + hungarian_set_loss(slots, tgt, lens, no_obj_idx=nc[h])
            total = single_loss + rc_loss + set_loss
            optimizer.zero_grad()
            total.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running_single += float(single_loss.detach())
            running_set += float(set_loss.detach())
            running_rc += rc_loss_v
            n_b += 1
            pbar.set_postfix(single=f"{single_loss.item():.2f}", rc=f"{rc_loss.item():.2f}", set=f"{set_loss.item():.2f}")
        scheduler.step()
        print(f"Epoch {epoch}: single={running_single/n_b:.3f} rc={running_rc/n_b:.3f} set={running_set/n_b:.3f} lr={optimizer.param_groups[0]['lr']:.2e}")

        single_avg, set_f1, rc_top1, score = eval_split(val_loader, 'VAL')
        history.append({'epoch': epoch, 'val_single_avg': single_avg,
                         'val_set_f1': set_f1, 'val_rc_top1': rc_top1, 'score': score})
        if score > best_val:
            best_val = score; best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc, 'fp_dim': 6144,
                'hidden_dims': (1024,768,512), 'dropout': args.dropout,
                'k_slots': K_SLOTS,
                'class_embed_dim': args.class_embed_dim,
                'hier_set': True,
                'epoch': epoch,
                'val_single_avg': single_avg,
                'val_set_f1': set_f1,
                'val_rc_top1': rc_top1,
                'val_avg_top1': single_avg,  # 兼容字段
            }, CKPT_DIR / 'stage1_best.pt')
            print(f"  -> Saved best (single={single_avg*100:.2f}% rc={rc_top1*100:.2f}% set_f1={set_f1*100:.2f}%)")

    out = {'best_epoch': best_epoch, 'best_val_score': best_val, 'history': history}
    json.dump(out, open(CKPT_DIR / 'stage1_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, score = {best_val:.4f}")


if __name__ == "__main__":
    main()
