"""训练 ConditionStage1HierSetV3XTB (V3 + Ligand/Additive SMI + xTB class embed)。"""
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
from torch.utils.data import DataLoader
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_hier_set_v3_xtb import (
    ConditionStage1HierSetV3XTB,
    SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS,
)
from models.condition_stage1_set import hungarian_set_loss, decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

SMI_HEADS = list(SMI_FROM_CLASS.keys())
DEFAULT_DATA_DIR = project_root / 'data_audited_v3_clean'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


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
    parser.add_argument('--xtb_mlp_hidden', type=int, default=64)
    parser.add_argument('--teacher_forcing_p', type=float, default=1.0)
    parser.add_argument('--ckpt_name', default='stage1_hier_set_v3_xtb.pt')
    parser.add_argument('--data_dir', default=str(DEFAULT_DATA_DIR))
    args = parser.parse_args()
    DATA_DIR = Path(args.data_dir)

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}")
    print(f"timestamp={datetime.now().isoformat()}")
    print(f"data_dir={DATA_DIR}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    nc_v3 = stats['num_classes_v3']
    print(f"train={len(train_records)}, val={len(val_records)}")

    # Load xTB class table
    xtb_table = torch.load(DATA_DIR / 'xtb_class_table.pt', weights_only=False)
    print(f"Loaded xTB class table:")
    for k, d in xtb_table.items():
        print(f"  {k:<22} feat={d['feat'].shape} mask_valid={int(d['mask'].sum())}/{len(d['mask'])}")

    train_ds = HierSetV3Dataset(train_records)
    val_ds = HierSetV3Dataset(val_records)
    coll = lambda b: collate_fn(b, nc)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True, collate_fn=coll)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                             num_workers=2, collate_fn=coll)

    # Class weights
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

    # tag pos weight
    tag_counts = np.zeros(CAT_TAG_BITS, dtype=np.float64)
    total = len(train_records)
    for r in train_records:
        bits = int(r['labels'][CAT_TAG_KEY])
        for b in range(CAT_TAG_BITS):
            if (bits >> b) & 1: tag_counts[b] += 1
    pos_weight = (total - tag_counts) / np.maximum(tag_counts, 1)
    pos_weight = torch.from_numpy(pos_weight.astype(np.float32)).to(args.device)

    model = ConditionStage1HierSetV3XTB(
        num_classes=nc, num_classes_v3=nc_v3, xtb_class_table=xtb_table,
        fp_dim=6144, hidden_dims=(1024, 768, 512), dropout=args.dropout,
        class_embed_dim=args.class_embed_dim,
        cat_tag_embed_dim=args.cat_tag_embed_dim,
        xtb_mlp_hidden=args.xtb_mlp_hidden,
    ).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    single_criterion = {}
    for k in SINGLE_HEADS_V3 + HIER_KEYS:
        ls = args.label_smoothing if nc_v3[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)
    for k in SMI_HEADS:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)
    tag_criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    def eval_split(loader, name):
        model.eval()
        all_keys = SINGLE_HEADS_V3 + HIER_KEYS + SMI_HEADS
        sums = {k: {'top1': 0, 'top3': 0, 'top5': 0} for k in all_keys}
        tag_tp = np.zeros(CAT_TAG_BITS); tag_pred = np.zeros(CAT_TAG_BITS); tag_gt = np.zeros(CAT_TAG_BITS); tag_total = 0
        set_preds = {h: [] for h in SET_HEADS}
        set_gts = {h: [] for h in SET_HEADS}
        topk_recall = {h: {f'top{kk}': 0 for kk in [5,10,20]} for h in SET_HEADS}
        n = 0
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                out = model(fp, teacher=None)
                bsz = fp.size(0); n += bsz
                for k in all_keys:
                    tgt = batch[k].to(args.device)
                    r = topk_accuracy_single(out[k], tgt, ks=(1, 3, 5))
                    for kk, v in r.items(): sums[k][kk] += v
                tl = out[CAT_TAG_KEY]
                tp = (torch.sigmoid(tl) > 0.5).float().cpu().numpy()
                tg = batch[CAT_TAG_KEY].numpy()
                tag_total += bsz
                tag_pred += tp.sum(axis=0); tag_gt += tg.sum(axis=0)
                tag_tp += ((tp == 1) & (tg == 1)).sum(axis=0)
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

        print(f"\n[{name}] v3 single + hier + SMI head Top-K:")
        for k in SINGLE_HEADS_V3 + HIER_KEYS + SMI_HEADS:
            print(f"  {k:<22} Top1={sums[k]['top1']/n*100:5.2f}% Top3={sums[k]['top3']/n*100:5.2f}% Top5={sums[k]['top5']/n*100:5.2f}%")
        single_avg = float(np.mean([sums[k]['top1']/n for k in SINGLE_HEADS_V3]))
        hier_avg = float(np.mean([sums[k]['top1']/n for k in HIER_KEYS]))
        smi_avg = float(np.mean([sums[k]['top1']/n for k in SMI_HEADS]))
        print(f"  AVG single (7) = {single_avg*100:.2f}%, AVG hier (3) = {hier_avg*100:.2f}%, AVG smi (2) = {smi_avg*100:.2f}%")
        # tag F1 avg
        tag_f1s = []
        for b in range(CAT_TAG_BITS):
            p = tag_tp[b] / max(tag_pred[b], 1); r = tag_tp[b] / max(tag_gt[b], 1)
            f1 = 2*p*r / max(p+r, 1e-6); tag_f1s.append(f1)
        tag_avg_f1 = float(np.mean(tag_f1s))
        print(f"  AVG tag F1 = {tag_avg_f1*100:.2f}%")
        set_avg_f1 = 0
        for h in SET_HEADS:
            r, p, f1 = set_metrics(set_preds[h], set_gts[h])
            set_avg_f1 += f1
        set_avg_f1 /= len(SET_HEADS)
        score = 0.35*single_avg + 0.15*hier_avg + 0.1*smi_avg + 0.1*tag_avg_f1 + 0.3*set_avg_f1
        return single_avg, hier_avg, smi_avg, tag_avg_f1, set_avg_f1, score

    best_val = 0.0; best_epoch = -1; history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = {'single':0., 'hier':0., 'smi':0., 'tag':0., 'set':0.}
        n_b = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            teacher = {}
            for k in HIER_KEYS:
                teacher[k] = batch[k].to(args.device)
            for cls_name in SMI_FROM_CLASS.values():
                teacher[cls_name] = batch[cls_name].to(args.device)
            teacher[CAT_TAG_KEY] = batch[CAT_TAG_KEY].to(args.device)
            use_tf = (np.random.rand() < args.teacher_forcing_p)
            out = model(fp, teacher=teacher if use_tf else None)

            single_loss = 0.0
            for k in SINGLE_HEADS_V3:
                single_loss = single_loss + single_criterion[k](out[k], batch[k].to(args.device))
            hier_loss = 0.0
            for k in HIER_KEYS:
                hier_loss = hier_loss + single_criterion[k](out[k], batch[k].to(args.device))
            smi_loss = 0.0
            for k in SMI_HEADS:
                smi_loss = smi_loss + single_criterion[k](out[k], batch[k].to(args.device))
            tag_loss = tag_criterion(out[CAT_TAG_KEY], batch[CAT_TAG_KEY].to(args.device))
            set_loss = 0.0
            for h in SET_HEADS:
                set_loss = set_loss + hungarian_set_loss(
                    out[h], batch[f'{h}_set'].to(args.device),
                    batch[f'{h}_len'].to(args.device), no_obj_idx=nc[h])
            total_loss = single_loss + hier_loss + smi_loss + tag_loss + set_loss
            optimizer.zero_grad()
            total_loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running['single'] += float(single_loss.detach())
            running['hier'] += float(hier_loss.detach())
            running['smi'] += float(smi_loss.detach())
            running['tag'] += float(tag_loss.detach())
            running['set'] += float(set_loss.detach())
            n_b += 1
            pbar.set_postfix(s=f"{single_loss.item():.2f}", h=f"{hier_loss.item():.2f}",
                              sm=f"{smi_loss.item():.2f}", tg=f"{tag_loss.item():.2f}",
                              st=f"{set_loss.item():.2f}")
        scheduler.step()
        print(f"Epoch {epoch}: single={running['single']/n_b:.3f} hier={running['hier']/n_b:.3f} "
              f"smi={running['smi']/n_b:.3f} tag={running['tag']/n_b:.3f} set={running['set']/n_b:.3f} "
              f"lr={optimizer.param_groups[0]['lr']:.2e}")

        single_avg, hier_avg, smi_avg, tag_f1, set_f1, score = eval_split(val_loader, 'VAL')
        history.append({'epoch': epoch, 'val_single_avg': single_avg, 'val_hier_avg': hier_avg,
                         'val_smi_avg': smi_avg, 'val_tag_f1': tag_f1, 'val_set_f1': set_f1,
                         'score': score})
        if score > best_val:
            best_val = score; best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc, 'num_classes_v3': nc_v3,
                'fp_dim': 6144, 'hidden_dims': (1024,768,512),
                'dropout': args.dropout, 'k_slots': K_SLOTS,
                'class_embed_dim': args.class_embed_dim,
                'cat_tag_embed_dim': args.cat_tag_embed_dim,
                'xtb_mlp_hidden': args.xtb_mlp_hidden,
                'hier_set_v3_xtb': True,
                'epoch': epoch,
                'val_single_avg': single_avg, 'val_hier_avg': hier_avg,
                'val_smi_avg': smi_avg, 'val_tag_f1': tag_f1, 'val_set_f1': set_f1,
            }, CKPT_DIR / args.ckpt_name)
            print(f"  -> Saved best (single={single_avg*100:.2f}% hier={hier_avg*100:.2f}% "
                  f"smi={smi_avg*100:.2f}% tag={tag_f1*100:.2f}% set_f1={set_f1*100:.2f}%)")

    out = {'best_epoch': best_epoch, 'best_val_score': best_val, 'history': history}
    json.dump(out, open(CKPT_DIR / 'experiments' / 'stage1_hier_set_v3_xtb_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, score = {best_val:.4f}")


if __name__ == '__main__':
    main()
