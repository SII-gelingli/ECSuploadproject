"""Stage-1 CVAE 训练。

CVAE loss = reconstruction CE (9 heads) + β * KL(q(z|x) || N(0,I))
β annealing: 前 10 epoch 线性增到 β_max, 之后保持。
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

from models.condition_stage1_cvae import ConditionStage1CVAE, HEAD_KEYS

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


class CVAEDataset(Dataset):
    def __init__(self, records):
        self.records = records

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        item = {'fp': torch.from_numpy(fp).float()}
        for k in HEAD_KEYS:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        return item


def topk_accuracy(logits, targets, ks=(1, 3, 5)):
    maxk = min(max(ks), logits.size(-1))
    _, pred = logits.topk(maxk, dim=-1)
    pred = pred.t()
    correct = pred.eq(targets.view(1, -1).expand_as(pred))
    out = {}
    for k in ks:
        if k <= maxk:
            out[f'top{k}'] = int(correct[:k].any(dim=0).float().sum().item())
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=80)
    parser.add_argument('--batch_size', type=int, default=256)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--latent_dim', type=int, default=64)
    parser.add_argument('--repr_dim', type=int, default=256)
    parser.add_argument('--beta_max', type=float, default=0.1)
    parser.add_argument('--beta_warmup', type=int, default=10)
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}, lr={args.lr}")
    print(f"CVAE: latent={args.latent_dim}, repr={args.repr_dim}, β_max={args.beta_max}, warmup={args.beta_warmup}ep")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}")

    train_ds = CVAEDataset(train_records)
    val_ds = CVAEDataset(val_records)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)

    # Class weights (与 baseline 一致)
    class_weights = {}
    for k in HEAD_KEYS:
        cnt = Counter([r['labels'][k] for r in train_records])
        n_cls = nc[k]
        w = np.zeros(n_cls, dtype=np.float32)
        for i in range(n_cls):
            w[i] = 1.0 / np.sqrt(cnt.get(i, 0) + 1)
        w = w / max(1e-6, w.mean())
        class_weights[k] = torch.from_numpy(w).to(args.device)

    model = ConditionStage1CVAE(num_classes=nc, fp_dim=6144,
                                 repr_dim=args.repr_dim, latent_dim=args.latent_dim,
                                 dropout=args.dropout).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    head_criterion = {}
    for k in HEAD_KEYS:
        ls = args.label_smoothing if nc[k] > 50 else 0.0
        head_criterion[k] = nn.CrossEntropyLoss(weight=class_weights[k],
                                                  label_smoothing=ls, reduction='none')

    def eval_split(loader, name):
        """评估两种模式: (a) teacher forcing 重构 acc; (b) prior 采样多样性"""
        model.eval()
        sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5)} for k in HEAD_KEYS}
        n = 0
        joint_top1_recon = 0
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                labels = {k: batch[k].to(args.device) for k in HEAD_KEYS}
                logits = model.reconstruct(fp, labels)
                bsz = fp.size(0); n += bsz
                per_head = []
                for k in HEAD_KEYS:
                    res = topk_accuracy(logits[k], labels[k], ks=(1, 3, 5))
                    for kk in res: sums[k][kk] += res[kk]
                    per_head.append(logits[k].argmax(dim=-1) == labels[k])
                joint_top1_recon += int(torch.stack(per_head, dim=0).all(dim=0).sum())
        report = {k: {kk: round(sums[k][kk]/n, 4) for kk in sums[k]} for k in HEAD_KEYS}
        avg = {kk: round(np.mean([report[k][kk] for k in HEAD_KEYS]), 4) for kk in ('top1','top3','top5')}
        joint = round(joint_top1_recon/n, 4)
        print(f"\n[{name}] Reconstruction Top-1/3/5  (joint={joint:.4f})")
        for k in HEAD_KEYS:
            r = report[k]
            print(f"  {k:<13} {r['top1']:7.4f} {r['top3']:7.4f} {r['top5']:7.4f}")
        print(f"  {'AVG':<13} {avg['top1']:7.4f} {avg['top3']:7.4f} {avg['top5']:7.4f}")
        return report, avg, joint

    best_avg_top1 = 0.0
    best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        # β annealing: 0 → β_max in first beta_warmup epochs
        beta = args.beta_max * min(1.0, epoch / max(1, args.beta_warmup))

        model.train()
        running_ce, running_kl = 0.0, 0.0
        n_batches = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs} (β={beta:.3f})")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            labels = {k: batch[k].to(args.device) for k in HEAD_KEYS}
            logits, mu, logvar = model(fp, labels)
            # Reconstruction CE
            ce = 0.0
            for k in HEAD_KEYS:
                ce = ce + head_criterion[k](logits[k], labels[k]).mean()
            # KL divergence: 0.5 * sum(mu^2 + sigma^2 - logvar - 1) per sample, mean over batch
            kl = -0.5 * torch.mean(torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1))
            loss = ce + beta * kl
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running_ce += float(ce.detach())
            running_kl += float(kl.detach())
            n_batches += 1
            pbar.set_postfix(ce=f"{ce.item():.3f}", kl=f"{kl.item():.3f}")
        scheduler.step()
        train_ce = running_ce / max(1, n_batches)
        train_kl = running_kl / max(1, n_batches)
        print(f"Epoch {epoch}: train_ce={train_ce:.4f}  train_kl={train_kl:.4f}  β={beta:.3f}  lr={optimizer.param_groups[0]['lr']:.2e}")

        report, avg, joint = eval_split(val_loader, name='VAL')
        history.append({'epoch': epoch, 'train_ce': train_ce, 'train_kl': train_kl,
                         'beta': beta, 'val_avg_top1': avg['top1'], 'val_joint_top1': joint})
        if avg['top1'] > best_avg_top1:
            best_avg_top1 = avg['top1']
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc,
                'fp_dim': 6144,
                'repr_dim': args.repr_dim,
                'latent_dim': args.latent_dim,
                'dropout': args.dropout,
                'cvae': True,
                'epoch': epoch,
                'val_avg_top1': avg['top1'],
                'val_joint_top1': joint,
            }, CKPT_DIR / 'stage1_best.pt')
            print(f"  -> Saved best (val avg Top-1 = {avg['top1']:.4f})")

    out = {'best_epoch': best_epoch, 'best_val_top1': best_avg_top1, 'history': history}
    json.dump(out, open(CKPT_DIR / 'stage1_history.json', 'w'), indent=2)
    print(f"\nFinished. Best epoch = {best_epoch}, val avg Top-1 = {best_avg_top1:.4f}")


if __name__ == "__main__":
    main()
