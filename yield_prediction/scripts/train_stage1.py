"""
Stage-1 训练: 8 个种类 head 的多任务分类。
"""
import sys
import json
import argparse
from pathlib import Path
from collections import Counter
from datetime import datetime

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1 import ConditionStage1, HEAD_KEYS
from models.condition_stage1_cond import ConditionStage1Cond, HEAD_ORDER as COND_HEAD_ORDER
from models.condition_stage1_chain import ConditionStage1Chain, CHAIN_HEADS
from models.condition_stage1_moe import ConditionStage1MoE

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class Stage1Dataset(Dataset):
    def __init__(self, records, xtb_mean=None, xtb_std=None,
                  fg_mean=None, fg_std=None, extra_keys=None):
        self.records = records
        self.xtb_mean, self.xtb_std = xtb_mean, xtb_std
        self.fg_mean, self.fg_std = fg_mean, fg_std
        self.extra_keys = list(extra_keys or [])

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        # 可选: 拼接 33 维归一化 xTB 特征
        if self.xtb_mean is not None and 'xtb_feat' in r:
            xtb = (np.asarray(r['xtb_feat'], dtype=np.float32) - self.xtb_mean) / self.xtb_std
            fp = np.concatenate([fp, xtb.astype(np.float32)])
        # 可选: 拼接 72 维归一化 FG 计数
        if self.fg_mean is not None and 'fg_feat' in r:
            fg = (np.asarray(r['fg_feat'], dtype=np.float32) - self.fg_mean) / self.fg_std
            fp = np.concatenate([fp, fg.astype(np.float32)])
        item = {'fp': torch.from_numpy(fp).float()}
        for k in HEAD_KEYS:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        for k in self.extra_keys:
            item[k] = torch.tensor(r['labels'].get(k, 0), dtype=torch.long)
        item['yield'] = torch.tensor(float(r['yield']) / 100.0, dtype=torch.float32)
        return item


def compute_class_weights(records, num_classes):
    """每个 head 的类别权重 = 1 / sqrt(freq+1), 标准化到平均 1。"""
    weights = {}
    for k in HEAD_KEYS:
        cnt = Counter([r['labels'][k] for r in records])
        n = num_classes[k]
        w = np.zeros(n, dtype=np.float32)
        for i in range(n):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        weights[k] = torch.from_numpy(w)
    return weights


def topk_accuracy(logits, targets, ks=(1, 3, 5)):
    maxk = min(max(ks), logits.size(-1))
    _, pred = logits.topk(maxk, dim=-1)
    pred = pred.t()
    correct = pred.eq(targets.view(1, -1).expand_as(pred))
    res = {}
    for k in ks:
        if k <= maxk:
            res[f'top{k}'] = correct[:k].any(dim=0).float().sum().item()
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=80)
    parser.add_argument('--batch_size', type=int, default=256)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--use_yield_weight', action='store_true',
                        help='按 yield 加权 CE (高产率反应权重更大)')
    parser.add_argument('--use_xtb', action='store_true',
                        help='拼接 33 维 xTB 特征')
    parser.add_argument('--use_fg', action='store_true',
                        help='拼接 72 维 RDKit 官能团计数特征')
    parser.add_argument('--cond_decode', action='store_true',
                        help='使用 conditional decoding (9 head 顺序预测)')
    parser.add_argument('--chain', action='store_true',
                        help='只对 solvent→electrolyte→reagent 链做 cond decoding, 其他并行')
    parser.add_argument('--use_reagent_class', action='store_true',
                        help='加一个 reagent_class (47 类) 并行 head, 辅助 reagent 长尾')
    parser.add_argument('--moe', action='store_true',
                        help='MoE: 共享 encoder + N expert head sets + soft router')
    parser.add_argument('--moe_experts', type=int, default=4)
    parser.add_argument('--moe_lb_weight', type=float, default=0.01,
                        help='Load balancing loss 权重')
    parser.add_argument('--cond_embed_dim', type=int, default=32)
    args = parser.parse_args()

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}, lr={args.lr}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}")
    print(f"num_classes = {nc}")

    xtb_mean = xtb_std = None
    fg_mean = fg_std = None
    fp_dim = 6144
    if args.use_xtb:
        xtb_stats = json.loads((DATA_DIR / 'xtb_stats.json').read_text())
        xtb_mean = np.asarray(xtb_stats['mean'], dtype=np.float32)
        xtb_std = np.asarray(xtb_stats['std'], dtype=np.float32)
        fp_dim += xtb_stats['dim']
        print(f"  +xTB ({xtb_stats['dim']}D)")
    if args.use_fg:
        fg_stats = json.loads((DATA_DIR / 'fg_stats.json').read_text())
        fg_mean = np.asarray(fg_stats['mean'], dtype=np.float32)
        fg_std = np.asarray(fg_stats['std'], dtype=np.float32)
        fp_dim += fg_stats['dim']
        print(f"  +FG ({fg_stats['dim']}D)")
    print(f"  fp_dim = {fp_dim}")

    extra_keys = ['reagent_class'] if args.use_reagent_class else []
    train_ds = Stage1Dataset(train_records, xtb_mean=xtb_mean, xtb_std=xtb_std,
                              fg_mean=fg_mean, fg_std=fg_std, extra_keys=extra_keys)
    val_ds = Stage1Dataset(val_records, xtb_mean=xtb_mean, xtb_std=xtb_std,
                            fg_mean=fg_mean, fg_std=fg_std, extra_keys=extra_keys)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)

    print("Computing class weights ...")
    class_weights = compute_class_weights(train_records, nc)
    for k, w in class_weights.items():
        class_weights[k] = w.to(args.device)

    extra_heads = ['reagent_class'] if args.use_reagent_class else None
    if args.moe:
        model = ConditionStage1MoE(num_classes=nc, fp_dim=fp_dim,
                                    hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                    num_experts=args.moe_experts,
                                    extra_heads=extra_heads).to(args.device)
        print(f"  使用 MoE: {args.moe_experts} experts, lb_weight={args.moe_lb_weight}")
    elif args.chain:
        model = ConditionStage1Chain(num_classes=nc, fp_dim=fp_dim,
                                      hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                      cond_embed_dim=args.cond_embed_dim).to(args.device)
        print(f"  使用 chain (solvent→electrolyte→reagent, cond_embed_dim={args.cond_embed_dim})")
    elif args.cond_decode:
        model = ConditionStage1Cond(num_classes=nc, fp_dim=fp_dim,
                                     hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                     cond_embed_dim=args.cond_embed_dim).to(args.device)
        print(f"  使用 全链 conditional decoding (cond_embed_dim={args.cond_embed_dim})")
    else:
        model = ConditionStage1(num_classes=nc, fp_dim=fp_dim,
                                 hidden_dims=(1024, 768, 512), dropout=args.dropout,
                                 extra_heads=extra_heads).to(args.device)
        if extra_heads:
            print(f"  额外 head: {extra_heads}")
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    # 每个 head 用不同 label smoothing：> 50 类的 head 用 args.label_smoothing
    all_train_heads = list(HEAD_KEYS) + (['reagent_class'] if args.use_reagent_class else [])
    # 给 reagent_class 也算 class weights
    if args.use_reagent_class:
        cnt = Counter([r['labels'].get('reagent_class', 0) for r in train_records])
        n_rc = nc['reagent_class']
        w = np.zeros(n_rc, dtype=np.float32)
        for i in range(n_rc):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        class_weights['reagent_class'] = torch.from_numpy(w).to(args.device)

    head_criterion = {}
    for k in all_train_heads:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        head_criterion[k] = nn.CrossEntropyLoss(weight=class_weights[k],
                                                  label_smoothing=ls, reduction='none')

    def eval_split(loader, name):
        model.eval()
        sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5)} for k in HEAD_KEYS}
        n = 0
        all_correct_top1 = torch.zeros(0, dtype=torch.bool, device=args.device)
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                logits = model(fp)
                bsz = fp.size(0)
                n += bsz
                # joint top-1
                per_head_correct = []
                for k in HEAD_KEYS:
                    tgt = batch[k].to(args.device)
                    res = topk_accuracy(logits[k], tgt, ks=(1, 3, 5))
                    for kk in res:
                        sums[k][kk] += res[kk]
                    pred1 = logits[k].argmax(dim=-1)
                    per_head_correct.append(pred1 == tgt)
                joint = torch.stack(per_head_correct, dim=0).all(dim=0)
                all_correct_top1 = torch.cat([all_correct_top1, joint])
        report = {k: {kk: round(sums[k][kk] / n, 4) for kk in sums[k]} for k in HEAD_KEYS}
        avg = {kk: round(np.mean([report[k][kk] for k in HEAD_KEYS]), 4) for kk in ('top1', 'top3', 'top5')}
        joint_top1 = float(all_correct_top1.float().mean().item())
        print(f"\n[{name}] Per-head Top-1/3/5  (joint Top-1 across 9 heads = {joint_top1:.4f})")
        print(f"  {'head':<13} {'Top1':>7} {'Top3':>7} {'Top5':>7}")
        for k in HEAD_KEYS:
            r = report[k]
            print(f"  {k:<13} {r['top1']:7.4f} {r['top3']:7.4f} {r['top5']:7.4f}")
        print(f"  {'AVG':<13} {avg['top1']:7.4f} {avg['top3']:7.4f} {avg['top5']:7.4f}")
        return report, avg, joint_top1

    best_avg_top1 = 0.0
    best_epoch = -1
    history = []

    for epoch in range(1, args.epochs + 1):
        model.train()
        running = 0.0
        n_batches = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            route_weights = None
            if args.cond_decode or args.chain:
                # teacher forcing: pass ground-truth labels
                tf_labels = {k: batch[k].to(args.device) for k in HEAD_KEYS}
                logits = model(fp, teacher_labels=tf_labels)
            elif args.moe:
                logits, route_weights = model(fp, return_route=True)
            else:
                logits = model(fp)
            yield_w = (batch['yield'].to(args.device)).clamp(min=0.05) if args.use_yield_weight else None
            total_loss = 0.0
            for k in all_train_heads:
                if k not in logits:
                    continue
                tgt = batch[k].to(args.device)
                per_sample = head_criterion[k](logits[k], tgt)
                if yield_w is not None:
                    per_sample = per_sample * yield_w
                total_loss = total_loss + per_sample.mean()
            # MoE load balancing loss
            if route_weights is not None and args.moe_lb_weight > 0:
                lb_loss = model.load_balancing_loss(route_weights)
                total_loss = total_loss + args.moe_lb_weight * lb_loss
            optimizer.zero_grad()
            total_loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += total_loss.item()
            n_batches += 1
            pbar.set_postfix(loss=f"{total_loss.item():.4f}")
        scheduler.step()
        train_loss = running / max(1, n_batches)
        print(f"Epoch {epoch}: train_loss={train_loss:.4f}  lr={optimizer.param_groups[0]['lr']:.2e}")

        report, avg, joint = eval_split(val_loader, 'VAL')
        history.append({'epoch': epoch, 'train_loss': train_loss,
                        'val_avg_top1': avg['top1'], 'val_joint_top1': joint})
        if avg['top1'] > best_avg_top1:
            best_avg_top1 = avg['top1']
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc,
                'fp_dim': fp_dim,
                'use_xtb': args.use_xtb,
                'use_fg': args.use_fg,
                'cond_decode': args.cond_decode,
                'chain': args.chain,
                'use_reagent_class': args.use_reagent_class,
                'moe': args.moe,
                'moe_experts': args.moe_experts,
                'cond_embed_dim': args.cond_embed_dim,
                'hidden_dims': (1024, 768, 512),
                'dropout': args.dropout,
                'epoch': epoch,
                'val_avg_top1': avg['top1'],
                'val_joint_top1': joint,
                'val_per_head': report,
            }, CKPT_DIR / 'stage1_best.pt')
            print(f"  -> Saved best (val avg Top-1 = {avg['top1']:.4f})")

    print(f"\nFinished. Best epoch = {best_epoch}, val avg Top-1 = {best_avg_top1:.4f}")
    with open(CKPT_DIR / 'stage1_history.json', 'w') as f:
        json.dump({'best_epoch': best_epoch, 'best_val_top1': best_avg_top1,
                   'history': history}, f, indent=2)


if __name__ == "__main__":
    main()
