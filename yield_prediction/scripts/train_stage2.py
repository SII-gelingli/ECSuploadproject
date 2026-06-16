"""
Stage-2 训练: 7 个用量字段的回归（masked MSE）。

输入: reaction FP + Stage-1 种类的 ground-truth embedding (teacher forcing)
输出: 7 个归一化用量值
"""
import sys
import json
import argparse
from pathlib import Path
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

from models.condition_stage2 import ConditionStage2, AMOUNT_FIELDS, HEAD_KEYS

DEFAULT_DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


def transform_amount(values: np.ndarray, stats: dict) -> np.ndarray:
    """对一个 field 的原值数组应用 transform + 标准化 (norm_mean/norm_std)。"""
    if stats['transform'] == 'log':
        t = np.log(values + stats['offset'])
    elif stats['transform'] == 'temperature':
        t = (values - 25) / 30.0
    else:
        t = values
    return (t - stats['norm_mean']) / max(1e-8, stats['norm_std'])


def inverse_transform(norm_values: np.ndarray, stats: dict) -> np.ndarray:
    """归一化值 → 原单位。"""
    t = norm_values * stats['norm_std'] + stats['norm_mean']
    if stats['transform'] == 'log':
        return np.exp(t) - stats['offset']
    if stats['transform'] == 'temperature':
        return t * 30.0 + 25.0
    return t


class Stage2Dataset(Dataset):
    def __init__(self, records, amount_stats, xtb_mean=None, xtb_std=None,
                  fg_mean=None, fg_std=None):
        self.records = records
        self.xtb_mean, self.xtb_std = xtb_mean, xtb_std
        self.fg_mean, self.fg_std = fg_mean, fg_std
        # 预先把 amount_values 转成归一化 target
        norm_targets = []
        for r in records:
            normed = np.zeros(len(AMOUNT_FIELDS), dtype=np.float32)
            for i, f in enumerate(AMOUNT_FIELDS):
                if r['amount_mask'][i] > 0:
                    s = amount_stats[f]
                    normed[i] = transform_amount(np.array([r['amount_values'][i]]), s)[0]
            norm_targets.append(normed)
        self.norm_targets = norm_targets

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        fp = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
        if self.xtb_mean is not None and 'xtb_feat' in r:
            xtb = (np.asarray(r['xtb_feat'], dtype=np.float32) - self.xtb_mean) / self.xtb_std
            fp = np.concatenate([fp, xtb.astype(np.float32)])
        if self.fg_mean is not None and 'fg_feat' in r:
            fg = (np.asarray(r['fg_feat'], dtype=np.float32) - self.fg_mean) / self.fg_std
            fp = np.concatenate([fp, fg.astype(np.float32)])
        item = {
            'fp': torch.from_numpy(fp).float(),
            'targets': torch.from_numpy(self.norm_targets[idx]).float(),
            'mask': torch.from_numpy(r['amount_mask']).float(),
        }
        for k in HEAD_KEYS:
            item[k] = torch.tensor(r['labels'][k], dtype=torch.long)
        return item


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=40)
    parser.add_argument('--batch_size', type=int, default=256)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--use_xtb', action='store_true', help='拼接 33 维 xTB 特征')
    parser.add_argument('--use_fg', action='store_true', help='拼接 72 维 RDKit FG 计数')
    parser.add_argument('--data_dir', default=str(DEFAULT_DATA_DIR))
    parser.add_argument('--ckpt_name', default='stage2_best.pt')
    args = parser.parse_args()
    DATA_DIR = Path(args.data_dir)

    print(f"device={args.device}, epochs={args.epochs}, batch={args.batch_size}, lr={args.lr}")
    print(f"timestamp={datetime.now().isoformat()}")

    print("Loading data ...")
    train_records = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    val_records = torch.load(DATA_DIR / 'val.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    amount_stats = json.loads((DATA_DIR / 'amount_stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}")

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

    train_ds = Stage2Dataset(train_records, amount_stats, xtb_mean=xtb_mean, xtb_std=xtb_std,
                              fg_mean=fg_mean, fg_std=fg_std)
    val_ds = Stage2Dataset(val_records, amount_stats, xtb_mean=xtb_mean, xtb_std=xtb_std,
                            fg_mean=fg_mean, fg_std=fg_std)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                               num_workers=2, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)

    model = ConditionStage2(num_classes=nc, fp_dim=fp_dim,
                             hidden_dims=(512, 256), dropout=args.dropout).to(args.device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model params: {n_params/1e6:.1f}M")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    def masked_mse(pred, tgt, mask):
        sqerr = (pred - tgt) ** 2 * mask
        denom = mask.sum().clamp(min=1)
        return sqerr.sum() / denom

    def eval_split(loader, name):
        model.eval()
        # 收集预测 / target / mask 用于按字段算 MAE
        all_preds = {f: [] for f in AMOUNT_FIELDS}
        all_tgts = {f: [] for f in AMOUNT_FIELDS}
        all_masks = {f: [] for f in AMOUNT_FIELDS}
        with torch.no_grad():
            for batch in loader:
                fp = batch['fp'].to(args.device)
                cats = {k: batch[k].to(args.device) for k in HEAD_KEYS}
                preds = model(fp, cats)
                tgts = batch['targets'].to(args.device)
                masks = batch['mask'].to(args.device)
                for i, f in enumerate(AMOUNT_FIELDS):
                    all_preds[f].append(preds[f].cpu().numpy())
                    all_tgts[f].append(tgts[:, i].cpu().numpy())
                    all_masks[f].append(masks[:, i].cpu().numpy())
        # 反归一化算原单位 MAE
        report = {}
        for f in AMOUNT_FIELDS:
            p_norm = np.concatenate(all_preds[f])
            t_norm = np.concatenate(all_tgts[f])
            m = np.concatenate(all_masks[f]).astype(bool)
            if m.sum() == 0:
                report[f] = {'n': 0, 'mae': None, 'rmse': None, 'r2': None}
                continue
            p_real = inverse_transform(p_norm[m], amount_stats[f])
            t_real = inverse_transform(t_norm[m], amount_stats[f])
            mae = float(np.mean(np.abs(p_real - t_real)))
            rmse = float(np.sqrt(np.mean((p_real - t_real) ** 2)))
            ss_res = np.sum((t_real - p_real) ** 2)
            ss_tot = np.sum((t_real - t_real.mean()) ** 2) + 1e-8
            r2 = float(1 - ss_res / ss_tot)
            report[f] = {'n': int(m.sum()), 'mae': mae, 'rmse': rmse, 'r2': r2}
        print(f"\n[{name}] 用量 MAE / RMSE / R²:")
        print(f"  {'field':<20} {'n':>6} {'MAE':>10} {'RMSE':>10} {'R²':>8}")
        for f in AMOUNT_FIELDS:
            r = report[f]
            if r['n'] == 0:
                print(f"  {f:<20} {'-':>6} {'-':>10} {'-':>10} {'-':>8}")
            else:
                print(f"  {f:<20} {r['n']:>6} {r['mae']:>10.3f} {r['rmse']:>10.3f} {r['r2']:>8.3f}")
        avg_mae_norm = np.mean([r['mae'] / max(amount_stats[f]['raw_std'], 1e-6)
                                 for f, r in report.items() if r['n'] > 0])
        print(f"  Average MAE / raw_std = {avg_mae_norm:.3f}  (lower is better)")
        return report, avg_mae_norm

    best_score = 1e9
    best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = 0.0
        n_batches = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['fp'].to(args.device)
            cats = {k: batch[k].to(args.device) for k in HEAD_KEYS}
            tgts = batch['targets'].to(args.device)
            masks = batch['mask'].to(args.device)
            preds = model(fp, cats)
            # 把 dict of [B] 拼成 [B, F]
            pred_mat = torch.stack([preds[f] for f in AMOUNT_FIELDS], dim=1)
            loss = masked_mse(pred_mat, tgts, masks)
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += loss.item()
            n_batches += 1
            pbar.set_postfix(loss=f"{loss.item():.4f}")
        scheduler.step()
        train_loss = running / max(1, n_batches)
        print(f"Epoch {epoch}: train_loss={train_loss:.4f}  lr={optimizer.param_groups[0]['lr']:.2e}")

        report, score = eval_split(val_loader, 'VAL')
        history.append({'epoch': epoch, 'train_loss': train_loss, 'val_score': score,
                        **{f: report[f] for f in AMOUNT_FIELDS}})
        if score < best_score:
            best_score = score
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc,
                'fp_dim': fp_dim,
                'use_xtb': args.use_xtb,
                'use_fg': args.use_fg,
                'hidden_dims': (512, 256),
                'dropout': args.dropout,
                'epoch': epoch,
                'val_score': score,
                'val_per_field': report,
            }, CKPT_DIR / args.ckpt_name)
            print(f"  -> Saved best (val avg MAE/std = {score:.3f})")

    print(f"\nFinished. Best epoch = {best_epoch}, val score = {best_score:.3f}")
    with open(CKPT_DIR / 'stage2_history.json', 'w') as f:
        json.dump({'best_epoch': best_epoch, 'best_score': best_score,
                   'history': history}, f, indent=2, default=str)


if __name__ == "__main__":
    main()
