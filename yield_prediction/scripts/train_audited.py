"""
基于 data_audited/*.pt 训练:
  1. ConditionRecommender (7 个条件分类头)
  2. YieldPredictor (MLP 回归)

测试集 = 2025+ 论文 (paper-level isolated)。
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

from models.condition_recommender import ConditionRecommender
from models.yield_predictor import YieldPredictor

DATA_DIR = project_root / 'data_audited'
CKPT_DIR = project_root / 'checkpoints' / 'audited'
CKPT_DIR.mkdir(parents=True, exist_ok=True)


CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']
LABEL_FIELD = {
    'anode': 'anode',
    'cathode': 'cathode',
    'cell_type': 'cell_type',
    'electrolyte': 'electrolyte_label',
    'solvent': 'solvent_label',
    'reagent': 'reagent_label',
    'catalyst': 'catalyst_label',
}
# 训练数据中的 Unknown index (推理时屏蔽)
UNKNOWN_INDEX = {
    'anode': 22,
    'cathode': 22,
    'cell_type': 5,
    'electrolyte': 0,
    'solvent': 0,
    'reagent': 0,
    'catalyst': 0,
}


class PreparedConditionDataset(Dataset):
    """从 prepare_data_audited 输出的 dict-list 构造的 dataset"""

    def __init__(self, records, mode='condition'):
        # mode: 'condition' → 输出 reaction_fp (6144) + labels
        #       'yield'     → 输出 full feature (10246) + yield value
        self.records = records
        self.mode = mode

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        r = self.records[idx]
        reactant = torch.tensor(r['reactant_fp'], dtype=torch.float32)
        product = torch.tensor(r['product_fp'], dtype=torch.float32)
        diff = torch.tensor(r['diff_fp'], dtype=torch.float32)
        reaction_fp = torch.cat([reactant, product, diff])
        out = {'reaction_fp': reaction_fp,
               'yield_value': torch.tensor(r.get('yield', 0.0) or 0.0, dtype=torch.float32)}
        if self.mode == 'condition':
            for k in CONDITION_KEYS:
                out[k] = torch.tensor(r[LABEL_FIELD[k]], dtype=torch.long)
        elif self.mode == 'yield':
            solvent_fp = torch.tensor(r['solvent_fp'], dtype=torch.float32)
            electrolyte_fp = torch.tensor(r['electrolyte_fp'], dtype=torch.float32)
            ec_params = torch.tensor([
                r['anode'] / 22.0,
                r['cathode'] / 22.0,
                r['cell_type'] / 5.0,
                0.0, 0.0, 0.0,  # placeholders for current/density/potential (not extracted yet)
            ], dtype=torch.float32)
            out['features'] = torch.cat([reaction_fp, solvent_fp, electrolyte_fp, ec_params])
        return out


def load_pt(path):
    obj = torch.load(path, weights_only=False)
    if isinstance(obj, list):
        return obj
    return obj


def yield_weighted_ce(logits_list, targets_list, yield_values, condition_keys):
    """yield 加权交叉熵: weight = clamp(yield/100, min=0.05).

    返回 (total_loss, per_key_loss_dict)
    """
    weights = (yield_values / 100.0).clamp(min=0.05)
    total = 0.0
    per_key = {}
    for k, logits, targets in zip(condition_keys, logits_list, targets_list):
        ce = nn.functional.cross_entropy(logits, targets, reduction='none')
        loss = (ce * weights).mean()
        total = total + loss
        per_key[k] = loss.item()
    return total, per_key


def topk_accuracy(logits, targets, ks=(1, 3, 5, 10), mask_idx=None):
    """计算 Top-k 准确率。如果指定 mask_idx, 把该 idx 的 logit 设为 -inf 再算。"""
    if mask_idx is not None:
        logits = logits.clone()
        logits[..., mask_idx] = -float('inf')
    maxk = max(ks)
    maxk = min(maxk, logits.size(-1))
    _, pred = logits.topk(maxk, dim=-1)
    pred = pred.t()
    correct = pred.eq(targets.view(1, -1).expand_as(pred))
    res = {}
    for k in ks:
        if k <= maxk:
            correct_k = correct[:k].any(dim=0).float().sum().item()
            res[f'top{k}'] = correct_k
    return res


def train_condition_model(args):
    print(f"\n=== Training ConditionRecommender on data_audited ===")
    device = args.device
    train_records = load_pt(DATA_DIR / 'train.pt')
    val_records = load_pt(DATA_DIR / 'val.pt')
    test_records = load_pt(DATA_DIR / 'test.pt')
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"train={len(train_records)}, val={len(val_records)}, test={len(test_records)}")
    print(f"num_classes = {nc}")

    train_ds = PreparedConditionDataset(train_records, mode='condition')
    val_ds = PreparedConditionDataset(val_records, mode='condition')
    test_ds = PreparedConditionDataset(test_records, mode='condition')

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)

    model = ConditionRecommender(
        reaction_dim=6144,
        hidden_dim=args.hidden_dim,
        num_anode_materials=nc['anode'],
        num_cathode_materials=nc['cathode'],
        num_cell_types=nc['cell_type'],
        num_electrolytes=nc['electrolyte'],
        num_solvents=nc['solvent'],
        num_reagents=nc['reagent'],
        num_catalysts=nc['catalyst'],
        dropout=args.dropout,
    ).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    def eval_split(loader, name=''):
        model.eval()
        total_n = 0
        topk_sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5, 10)} for k in CONDITION_KEYS}
        with torch.no_grad():
            for batch in loader:
                fp = batch['reaction_fp'].to(device)
                preds = model(fp)
                bsz = fp.size(0)
                total_n += bsz
                for k in CONDITION_KEYS:
                    logits = preds[f'{k}_logits']
                    tgt = batch[k].to(device)
                    res = topk_accuracy(logits, tgt, ks=(1, 3, 5, 10), mask_idx=UNKNOWN_INDEX[k])
                    for kk, v in res.items():
                        topk_sums[k][kk] += v
        # normalize
        report = {}
        for k in CONDITION_KEYS:
            report[k] = {kk: round(topk_sums[k][kk] / total_n, 4) for kk in topk_sums[k]}
        avg = {kk: round(np.mean([report[k][kk] for k in CONDITION_KEYS]), 4) for kk in ('top1', 'top3', 'top5', 'top10')}
        print(f"\n[{name}] Top-k accuracy (Unknown idx masked):")
        print(f"  {'Condition':<13} {'Top1':>7} {'Top3':>7} {'Top5':>7} {'Top10':>7}")
        for k in CONDITION_KEYS:
            r = report[k]
            print(f"  {k:<13} {r['top1']:7.4f} {r['top3']:7.4f} {r['top5']:7.4f} {r['top10']:7.4f}")
        print(f"  {'AVG':<13} {avg['top1']:7.4f} {avg['top3']:7.4f} {avg['top5']:7.4f} {avg['top10']:7.4f}")
        return report, avg

    best_val_top1 = 0.0
    best_epoch = -1
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        running = 0.0
        per_key_total = {k: 0.0 for k in CONDITION_KEYS}
        n_batches = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            fp = batch['reaction_fp'].to(device)
            yield_values = batch['yield_value'].to(device)
            preds = model(fp)
            logits_list = [preds[f'{k}_logits'] for k in CONDITION_KEYS]
            targets_list = [batch[k].to(device) for k in CONDITION_KEYS]
            loss, per_key = yield_weighted_ce(logits_list, targets_list, yield_values, CONDITION_KEYS)
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += loss.item()
            for k, v in per_key.items():
                per_key_total[k] += v
            n_batches += 1
            pbar.set_postfix(loss=f"{loss.item():.4f}")
        scheduler.step()
        train_loss = running / max(1, n_batches)
        print(f"Epoch {epoch}: train_loss={train_loss:.4f}, lr={optimizer.param_groups[0]['lr']:.2e}")

        val_report, val_avg = eval_split(val_loader, name='VAL')
        history.append({'epoch': epoch, 'train_loss': train_loss, 'val_top1': val_avg['top1'], 'val_top3': val_avg['top3']})
        if val_avg['top1'] > best_val_top1:
            best_val_top1 = val_avg['top1']
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'num_classes': nc,
                'reaction_dim': 6144,
                'hidden_dim': args.hidden_dim,
                'epoch': epoch,
                'val_top1': val_avg['top1'],
                'val_top3': val_avg['top3'],
            }, CKPT_DIR / 'condition_best.pt')
            print(f"  -> Saved best (val avg top1 = {val_avg['top1']:.4f})")

    # final test
    ckpt = torch.load(CKPT_DIR / 'condition_best.pt', weights_only=False)
    model.load_state_dict(ckpt['model_state_dict'])
    print(f"\nLoaded best epoch={ckpt['epoch']} (val top1={ckpt['val_top1']:.4f})")
    test_report, test_avg = eval_split(test_loader, name='TEST (2025+ papers)')
    result = {
        'best_epoch': best_epoch,
        'val_top1': best_val_top1,
        'test_report': test_report,
        'test_avg': test_avg,
        'history': history,
    }
    with open(CKPT_DIR / 'condition_test_metrics.json', 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {CKPT_DIR / 'condition_test_metrics.json'}")


def train_yield_model(args):
    print(f"\n=== Training YieldPredictor on data_audited ===")
    device = args.device
    train_records = load_pt(DATA_DIR / 'train.pt')
    val_records = load_pt(DATA_DIR / 'val.pt')
    test_records = load_pt(DATA_DIR / 'test.pt')
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    input_dim = stats['feature_dims']['total']  # 10246
    print(f"train={len(train_records)}, val={len(val_records)}, test={len(test_records)}, input_dim={input_dim}")

    train_ds = PreparedConditionDataset(train_records, mode='yield')
    val_ds = PreparedConditionDataset(val_records, mode='yield')
    test_ds = PreparedConditionDataset(test_records, mode='yield')

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, drop_last=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, shuffle=False, num_workers=2)

    model = YieldPredictor(input_dim=input_dim, hidden_dims=[512, 256, 128], dropout=0.2).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.yield_epochs)
    criterion = nn.MSELoss()

    def eval_split(loader, name=''):
        model.eval()
        preds_all, tgts_all = [], []
        with torch.no_grad():
            for batch in loader:
                x = batch['features'].to(device)
                y = batch['yield_value'].to(device) / 100.0
                pred = model(x).squeeze(-1)
                preds_all.append(pred.cpu().numpy())
                tgts_all.append(y.cpu().numpy())
        preds = np.concatenate(preds_all) * 100.0
        tgts = np.concatenate(tgts_all) * 100.0
        mae = float(np.mean(np.abs(preds - tgts)))
        rmse = float(np.sqrt(np.mean((preds - tgts) ** 2)))
        ss_res = np.sum((tgts - preds) ** 2)
        ss_tot = np.sum((tgts - tgts.mean()) ** 2) + 1e-8
        r2 = float(1 - ss_res / ss_tot)
        print(f"[{name}] MAE={mae:.3f}%  RMSE={rmse:.3f}%  R²={r2:.4f}")
        return {'mae': mae, 'rmse': rmse, 'r2': r2}

    best_val_mae = 1e9
    best_epoch = -1
    history = []
    for epoch in range(1, args.yield_epochs + 1):
        model.train()
        running = 0.0
        n = 0
        pbar = tqdm(train_loader, desc=f"Yield epoch {epoch}/{args.yield_epochs}")
        for batch in pbar:
            x = batch['features'].to(device)
            y = (batch['yield_value'].to(device) / 100.0).clamp(0, 1)
            pred = model(x).squeeze(-1)
            loss = criterion(pred, y)
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            running += loss.item() * x.size(0)
            n += x.size(0)
            pbar.set_postfix(loss=f"{loss.item():.4f}")
        scheduler.step()
        train_mse = running / max(1, n)
        print(f"Epoch {epoch}: train_mse={train_mse:.5f}")
        val_r = eval_split(val_loader, name='VAL')
        history.append({'epoch': epoch, 'train_mse': train_mse, **{f'val_{k}': v for k, v in val_r.items()}})
        if val_r['mae'] < best_val_mae:
            best_val_mae = val_r['mae']
            best_epoch = epoch
            torch.save({
                'model_state_dict': model.state_dict(),
                'input_dim': input_dim,
                'hidden_dims': [512, 256, 128],
                'epoch': epoch,
                'val_mae': val_r['mae'],
                'val_r2': val_r['r2'],
            }, CKPT_DIR / 'yield_best.pt')
            print(f"  -> Saved best (val MAE = {val_r['mae']:.3f})")

    ckpt = torch.load(CKPT_DIR / 'yield_best.pt', weights_only=False)
    model.load_state_dict(ckpt['model_state_dict'])
    print(f"\nLoaded best yield model epoch={ckpt['epoch']} (val MAE={ckpt['val_mae']:.3f})")
    test_r = eval_split(test_loader, name='TEST (2025+ papers)')
    result = {
        'best_epoch': best_epoch,
        'val_mae': best_val_mae,
        'test': test_r,
        'history': history,
    }
    with open(CKPT_DIR / 'yield_test_metrics.json', 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {CKPT_DIR / 'yield_test_metrics.json'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', choices=['condition', 'yield', 'both'], default='both')
    parser.add_argument('--epochs', type=int, default=80)
    parser.add_argument('--yield_epochs', type=int, default=40)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--hidden_dim', type=int, default=512)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    print(f"device={args.device}")
    print(f"timestamp={datetime.now().isoformat()}")

    if args.task in ('condition', 'both'):
        train_condition_model(args)
    if args.task in ('yield', 'both'):
        train_yield_model(args)


if __name__ == "__main__":
    main()
