"""Stage-1 Set Prediction 训练。

3 个 set head (solvent, reagent, catalyst) 用 Hungarian matching loss。
其他 6 head (anode/cathode/cell_type/electrolyte/ligand/additive) 加可选 reagent_class 用普通 CE。
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

from models.condition_stage1_set import (
    ConditionStage1Set, hungarian_set_loss, decode_set, decode_set_topk,
    PARALLEL_HEADS, SET_HEADS, K_SLOTS,
)
from models.condition_stage1 import HEAD_KEYS

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class SetDataset(Dataset):
    def __init__(self, records, extra_keys=None, k_slots=K_SLOTS):
        self.records = records
        self.extra_keys = list(extra_keys or [])
        self.k_slots = k_slots

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        item = {'fp': torch.from_numpy(fp).float()}
        # 单标签 head (含 extra_keys 如 reagent_class)
        for k in list(PARALLEL_HEADS) + self.extra_keys:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        # ligand / additive 仍然单标签
        for k in ['ligand', 'additive']:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        # set head: 用 set_labels, padding 到 K_slots, padding 用 no_obj (放在 collate 时填)
        for k in SET_HEADS:
            sl = r['set_labels'][k][:self.k_slots]
            item[f'{k}_set'] = sl  # list of int
            item[f'{k}_len'] = len(sl)
        return item


def collate_fn(batch, num_classes):
    """把 batch 里的 set 转成 (B, K) padding tensor + (B,) lengths."""
    K = K_SLOTS
    out = {}
    out['fp'] = torch.stack([d['fp'] for d in batch])
    keys = ['anode','cathode','cell_type','electrolyte','ligand','additive','reagent_class']
    for k in keys:
        if k in batch[0]:
            out[k] = torch.stack([d[k] for d in batch])
    for h in SET_HEADS:
        no_obj = num_classes[h]  # idx N = no_obj
        padded = []
        lens = []
        for d in batch:
            sl = d[f'{h}_set']
            # padding with no_obj_idx (= num_classes[h])
            p = sl + [no_obj] * (K - len(sl))
            padded.append(p)
            lens.append(d[f'{h}_len'])
        out[f'{h}_set'] = torch.tensor(padded, dtype=torch.long)
        out[f'{h}_len'] = torch.tensor(lens, dtype=torch.long)
    return out


def topk_accuracy_single(logits, targets, ks=(1, 3, 5)):
    maxk = min(max(ks), logits.size(-1))
    _, pred = logits.topk(maxk, dim=-1)
    pred = pred.t()
    correct = pred.eq(targets.view(1, -1).expand_as(pred))
    return {f'top{k}': int(correct[:k].any(dim=0).float().sum().item()) for k in ks if k <= maxk}


def set_metrics(pred_sets: list, true_sets: list):
    """Set 级 Recall / Precision / F1。"""
    recalls, precs = [], []
    for p, t in zip(pred_sets, true_sets):
        p_set = set(p); t_set = set(t)
        if not t_set:
            recalls.append(1.0)  # ground truth 是空, recall 定义为 1
            precs.append(1.0 if not p_set else 0.0)
            continue
        if not p_set:
            recalls.append(0.0); precs.append(0.0)
            continue
        inter = len(p_set & t_set)
        recalls.append(inter / len(t_set))
        precs.append(inter / len(p_set))
    r = np.mean(recalls); p = np.mean(precs)
    f1 = 2 * r * p / max(1e-8, r + p)
    return r, p, f1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=80)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--use_reagent_class', action='store_true')
    args = parser.parse_args()

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}")

    extra_keys = ['reagent_class'] if args.use_reagent_class else []
    train_ds = SetDataset(train_records, extra_keys=extra_keys)
    val_ds = SetDataset(val_records, extra_keys=extra_keys)
    coll = lambda b: collate_fn(b, nc)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True, collate_fn=coll)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False,
                             num_workers=2, collate_fn=coll)

    # class weights for single heads (去重)
    weights = {}
    single_heads = list(dict.fromkeys(list(PARALLEL_HEADS) + ['ligand', 'additive'] + extra_keys))
    for k in single_heads:
        cnt = Counter([r['labels'][k] for r in train_records])
        n_cls = nc[k]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[k] = torch.from_numpy(w).to(args.device)

    model = ConditionStage1Set(num_classes=nc, fp_dim=6144,
                                hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                extra_heads=extra_keys).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    single_criterion = {}
    for k in single_heads:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        single_criterion[k] = nn.CrossEntropyLoss(weight=weights[k], label_smoothing=ls)

    def eval_split(loader, name):
        model.eval()
        # 单标签 head: per-head Top-K
        sums = {k: {'top1': 0, 'top3': 0, 'top5': 0}
                 for k in single_heads}
        # set head: F1
        set_preds = {h: [] for h in SET_HEADS}
        set_gts = {h: [] for h in SET_HEADS}
        # 跨 slot Top-K 召回
        topk_recall = {h: {f'top{kk}': 0 for kk in [5, 10, 20]} for h in SET_HEADS}
        n = 0
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                out = model(fp)
                bsz = fp.size(0); n += bsz
                for k in single_heads:
                    tgt = batch[k].to(args.device)
                    res = topk_accuracy_single(out[k], tgt, ks=(1,3,5))
                    for kk, v in res.items():
                        sums[k][kk] += v
                for h in SET_HEADS:
                    slots = out[h]  # (B, K, N+1)
                    no_obj = nc[h]
                    pred_sets = decode_set(slots, no_obj)
                    set_preds[h].extend(pred_sets)
                    # GT set
                    gt_padded = batch[f'{h}_set'].cpu().numpy()
                    gt_lens = batch[f'{h}_len'].cpu().numpy()
                    for i in range(bsz):
                        set_gts[h].append(gt_padded[i, :gt_lens[i]].tolist())
                    # Top-K recall
                    topk_cand = decode_set_topk(slots, no_obj, K_total=20)
                    for kk in [5, 10, 20]:
                        for i in range(bsz):
                            gt_set = set(gt_padded[i, :gt_lens[i]].tolist())
                            if not gt_set: continue
                            cand_set = set(topk_cand[i][:kk])
                            if gt_set & cand_set:  # 任一覆盖
                                topk_recall[h][f'top{kk}'] += 1
        # 报告
        print(f"\n[{name}] 单标签 head Top-1/3/5:")
        for k in single_heads:
            r = sums[k]
            print(f"  {k:<15}  Top1={r['top1']/n*100:5.2f}%  Top3={r['top3']/n*100:5.2f}%  Top5={r['top5']/n*100:5.2f}%")
        single_avg = np.mean([sums[k]['top1']/n for k in single_heads])
        print(f"  {'AVG single':<15}  {single_avg*100:5.2f}%")

        print(f"\n[{name}] Set head 评估:")
        set_avg_recall = 0; set_avg_f1 = 0
        for h in SET_HEADS:
            r, p, f1 = set_metrics(set_preds[h], set_gts[h])
            set_avg_recall += r; set_avg_f1 += f1
            print(f"  {h:<10}  Recall={r*100:6.2f}%  Precision={p*100:6.2f}%  F1={f1*100:6.2f}%  "
                  f"Top5_recall={topk_recall[h]['top5']/n*100:5.2f}%  "
                  f"Top10={topk_recall[h]['top10']/n*100:5.2f}%  "
                  f"Top20={topk_recall[h]['top20']/n*100:5.2f}%")
        set_avg_recall /= len(SET_HEADS); set_avg_f1 /= len(SET_HEADS)
        print(f"  {'AVG set':<10}  Recall={set_avg_recall*100:5.2f}%  F1={set_avg_f1*100:5.2f}%")
        return single_avg, set_avg_recall, set_avg_f1

    best_val = 0.0; best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = 0.0; running_single = 0.0; running_set = 0.0
        n_b = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            out = model(fp)
            # 单标签 loss
            single_loss = 0.0
            for k in single_heads:
                tgt = batch[k].to(args.device)
                single_loss = single_loss + single_criterion[k](out[k], tgt)
            # Set loss
            set_loss = 0.0
            for h in SET_HEADS:
                slots = out[h]  # (B, K, N+1)
                tgt = batch[f'{h}_set'].to(args.device)
                lens = batch[f'{h}_len'].to(args.device)
                set_loss = set_loss + hungarian_set_loss(slots, tgt, lens, no_obj_idx=nc[h])
            total = single_loss + set_loss
            optimizer.zero_grad()
            total.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += float(total.detach())
            running_single += float(single_loss.detach())
            running_set += float(set_loss.detach())
            n_b += 1
            pbar.set_postfix(single=f"{single_loss.item():.2f}", set=f"{set_loss.item():.2f}")
        scheduler.step()
        print(f"Epoch {epoch}: total={running/n_b:.3f} single={running_single/n_b:.3f} set={running_set/n_b:.3f} lr={optimizer.param_groups[0]['lr']:.2e}")

        single_avg, set_recall, set_f1 = eval_split(val_loader, name='VAL')
        # 用 set_f1 * 0.5 + single_avg * 0.5 当指标
        score = 0.5 * single_avg + 0.5 * set_f1
        history.append({'epoch': epoch, 'val_single_avg': single_avg,
                         'val_set_recall': set_recall, 'val_set_f1': set_f1, 'score': score})
        if score > best_val:
            best_val = score; best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc, 'fp_dim': 6144,
                'hidden_dims': (1024,768,512), 'dropout': args.dropout,
                'k_slots': K_SLOTS,
                'use_reagent_class': args.use_reagent_class,
                'set_prediction': True,
                'epoch': epoch,
                'val_single_avg': single_avg,
                'val_set_recall': set_recall,
                'val_set_f1': set_f1,
                'val_avg_top1': single_avg,  # 兼容 eval 脚本字段
            }, CKPT_DIR / 'stage1_best.pt')
            print(f"  -> Saved best (single={single_avg*100:.2f}% set_f1={set_f1*100:.2f}%)")
    out = {'best_epoch': best_epoch, 'best_val_score': best_val, 'history': history}
    json.dump(out, open(CKPT_DIR / 'stage1_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, score = {best_val:.4f}")


if __name__ == "__main__":
    main()
