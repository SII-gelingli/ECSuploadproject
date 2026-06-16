"""
Pairwise Ranking Yield Predictor 训练脚本

Loss = λ_rank * BPR_loss + λ_reg * MSE_loss

对于每个训练反应 i，找到相似反应 j (cosine sim > threshold)：
  - 构建 pair: (rxn_fp_i + cond_i) vs (rxn_fp_i + cond_j)
  - 两个 item 共享反应指纹，只有条件不同
  - BPR loss 强制模型学习：高产率条件 > 低产率条件

不使用 xTB 特征 (input_dim = 10246)，避免 sigmoid 饱和问题。

用法:
    cd yield_prediction
    python scripts/train_yield_pairwise.py --device cuda
    python scripts/train_yield_pairwise.py --device cuda --sim_threshold 0.6 --yield_margin 10
"""
import sys
import argparse
import json
import time
import warnings
from pathlib import Path
from datetime import datetime

warnings.filterwarnings('ignore')

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.yield_predictor import YieldPredictor

FP_SIZE = 2048
INPUT_DIM = 3 * FP_SIZE + 2 * FP_SIZE + 6  # 10246: rxn(6144) + sol(2048) + elec(2048) + echem(6)


# ── 特征构建 ──────────────────────────────────────────────────

def build_feature_vector(item, use_conditions_from=None):
    """构建 10246D 特征向量

    Args:
        item: train.pt 中的反应记录 (rxn_fp 来源)
        use_conditions_from: 如果提供，使用该记录的条件 (condition swap)
    """
    cond = use_conditions_from if use_conditions_from is not None else item
    features = (
        item['reactant_fp'] + item['product_fp'] + item['diff_fp']  # 6144
        + list(cond['solvent_fp'])     # 2048
        + list(cond['electrolyte_fp']) # 2048
        + [
            float(cond['anode']),
            float(cond['cathode']),
            0.0,  # current_mA (unknown)
            0.0,  # current_density (unknown)
            0.0,  # potential_V (unknown)
            float(cond['cell_type']),
        ]  # 6
    )
    return features


# ── 数据集 ────────────────────────────────────────────────────

class PairwiseReactionDataset(Dataset):
    """Pairwise 数据集: 返回 (feat_A, feat_B, yield_A, yield_B)

    对于每个 pair (anchor_i, neighbor_j):
      feat_A = rxn_fp_i + cond_i (原始)
      feat_B = rxn_fp_i + cond_j (条件交换)
      yield_A = y_i, yield_B = y_j (proxy)
    """

    def __init__(self, data, sim_threshold=0.7, yield_margin=5.0, max_pairs_per_anchor=10):
        self.data = data
        self.yields = np.array([d['yield'] for d in data], dtype=np.float32)
        n = len(data)

        # 构建 6144D 反应指纹矩阵
        print(f"  Building {n} reaction fingerprints...")
        rxn_fps = np.zeros((n, 3 * FP_SIZE), dtype=np.float32)
        for i, d in enumerate(data):
            rxn_fps[i] = d['reactant_fp'] + d['product_fp'] + d['diff_fp']

        # L2 归一化
        norms = np.linalg.norm(rxn_fps, axis=1, keepdims=True) + 1e-8
        rxn_fps_norm = rxn_fps / norms

        # 分批计算相似度，找 pairs
        print(f"  Finding pairs (sim>{sim_threshold}, margin>{yield_margin}%)...")
        self.pairs = []
        batch_size = 512

        for start in tqdm(range(0, n, batch_size), desc="  Pair search", leave=False):
            end = min(start + batch_size, n)
            # [batch, N]
            sims = rxn_fps_norm[start:end] @ rxn_fps_norm.T

            for local_idx in range(end - start):
                i = start + local_idx
                sim_row = sims[local_idx]
                sim_row[i] = 0  # 排除自身

                # 找相似且产率差异足够大的邻居
                candidates = np.where(
                    (sim_row > sim_threshold) &
                    (np.abs(self.yields - self.yields[i]) > yield_margin)
                )[0]

                # 限制每个 anchor 的 pair 数量
                if len(candidates) > max_pairs_per_anchor:
                    # 优先选相似度最高的
                    top_k_idx = np.argsort(sim_row[candidates])[::-1][:max_pairs_per_anchor]
                    candidates = candidates[top_k_idx]

                for j in candidates:
                    self.pairs.append((i, int(j)))

        print(f"  Total pairs: {len(self.pairs)} from {n} reactions "
              f"(avg {len(self.pairs)/n:.1f} per reaction)")

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        anchor_idx, neighbor_idx = self.pairs[idx]

        # A: anchor 的 rxn_fp + anchor 的条件
        feat_A = build_feature_vector(self.data[anchor_idx])
        yield_A = self.yields[anchor_idx] / 100.0

        # B: anchor 的 rxn_fp + neighbor 的条件 (swap)
        feat_B = build_feature_vector(self.data[anchor_idx],
                                       use_conditions_from=self.data[neighbor_idx])
        yield_B = self.yields[neighbor_idx] / 100.0  # proxy

        return (
            torch.tensor(feat_A, dtype=torch.float32),
            torch.tensor(feat_B, dtype=torch.float32),
            torch.tensor(yield_A, dtype=torch.float32),
            torch.tensor(yield_B, dtype=torch.float32),
        )


class PointwiseReactionDataset(Dataset):
    """标准单样本数据集，用于 MSE 回归"""

    def __init__(self, data):
        self.data = data
        self.yields = np.array([d['yield'] for d in data], dtype=np.float32)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        feat = build_feature_vector(self.data[idx])
        yield_val = self.yields[idx] / 100.0
        return (
            torch.tensor(feat, dtype=torch.float32),
            torch.tensor(yield_val, dtype=torch.float32),
        )


# ── 训练 ──────────────────────────────────────────────────────

def train_epoch(model, pair_loader, point_loader, optimizer,
                lambda_rank, lambda_reg, margin_scale, device):
    model.train()
    total_loss = 0
    total_rank_loss = 0
    total_reg_loss = 0
    n_steps = 0

    pair_iter = iter(pair_loader)
    point_iter = iter(point_loader)
    steps = max(len(pair_loader), len(point_loader))

    for _ in range(steps):
        optimizer.zero_grad()

        # ── Ranking loss (BPR) ──
        try:
            feat_A, feat_B, yield_A, yield_B = next(pair_iter)
        except StopIteration:
            pair_iter = iter(pair_loader)
            feat_A, feat_B, yield_A, yield_B = next(pair_iter)

        feat_A = feat_A.to(device)
        feat_B = feat_B.to(device)
        yield_A = yield_A.to(device)
        yield_B = yield_B.to(device)

        score_A = model.forward_raw(feat_A).squeeze(-1)
        score_B = model.forward_raw(feat_B).squeeze(-1)

        # 排序: higher yield 应该得到更高 score
        yield_diff = yield_A - yield_B  # 可正可负
        higher_score = torch.where(yield_diff > 0, score_A, score_B)
        lower_score = torch.where(yield_diff > 0, score_B, score_A)
        margin = torch.abs(yield_diff) * margin_scale

        rank_loss = -F.logsigmoid(higher_score - lower_score - margin).mean()

        # ── Regression loss (MSE) on pointwise data ──
        try:
            feat_p, yield_p = next(point_iter)
        except StopIteration:
            point_iter = iter(point_loader)
            feat_p, yield_p = next(point_iter)

        feat_p = feat_p.to(device)
        yield_p = yield_p.to(device)

        pred_p = model(feat_p).squeeze(-1)  # sigmoid output [0,1]
        reg_loss = F.mse_loss(pred_p, yield_p)

        # 也对 pair 中的两个 item 做 MSE (anchor 的真实产率)
        pred_A = torch.sigmoid(score_A)
        reg_loss_pair = F.mse_loss(pred_A, yield_A)

        loss = lambda_rank * rank_loss + lambda_reg * (reg_loss + 0.5 * reg_loss_pair)

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        total_loss += loss.item()
        total_rank_loss += rank_loss.item()
        total_reg_loss += reg_loss.item()
        n_steps += 1

    return total_loss / n_steps, total_rank_loss / n_steps, total_reg_loss / n_steps


# ── 验证 ──────────────────────────────────────────────────────

@torch.no_grad()
def evaluate(model, point_loader, pair_loader, device):
    model.eval()

    # 1. Regression metrics
    all_preds, all_labels = [], []
    for feat, yield_val in point_loader:
        feat = feat.to(device)
        pred = model(feat).squeeze(-1) * 100  # → percentage
        all_preds.append(pred.cpu())
        all_labels.append(yield_val * 100)

    preds = torch.cat(all_preds)
    labels = torch.cat(all_labels)
    mae = torch.abs(preds - labels).mean().item()
    rmse = torch.sqrt(((preds - labels) ** 2).mean()).item()
    ss_res = ((preds - labels) ** 2).sum()
    ss_tot = ((labels - labels.mean()) ** 2).sum()
    r2 = (1 - ss_res / ss_tot).item() if ss_tot > 0 else 0.0

    # 2. Pairwise ranking accuracy
    correct = 0
    total = 0
    for feat_A, feat_B, yield_A, yield_B in pair_loader:
        feat_A = feat_A.to(device)
        feat_B = feat_B.to(device)
        score_A = model(feat_A).squeeze(-1)
        score_B = model(feat_B).squeeze(-1)

        # 模型是否正确排序?
        model_prefers_A = score_A > score_B
        true_A_better = yield_A > yield_B
        correct += (model_prefers_A.cpu() == true_A_better).sum().item()
        total += len(yield_A)

    pair_acc = correct / total if total > 0 else 0.0

    return {
        'mae': mae, 'rmse': rmse, 'r2': r2,
        'pair_accuracy': pair_acc,
        'composite': r2 + pair_acc,  # early stopping criterion
    }


# ── 学习率 warmup ─────────────────────────────────────────────

class WarmupCosineScheduler:
    def __init__(self, optimizer, warmup_epochs, total_epochs, min_lr=1e-6):
        self.optimizer = optimizer
        self.warmup_epochs = warmup_epochs
        self.total_epochs = total_epochs
        self.base_lrs = [pg['lr'] for pg in optimizer.param_groups]
        self.min_lr = min_lr

    def step(self, epoch):
        if epoch < self.warmup_epochs:
            # Linear warmup
            factor = (epoch + 1) / self.warmup_epochs
        else:
            # Cosine annealing
            progress = (epoch - self.warmup_epochs) / max(1, self.total_epochs - self.warmup_epochs)
            factor = 0.5 * (1 + np.cos(np.pi * progress))

        for pg, base_lr in zip(self.optimizer.param_groups, self.base_lrs):
            pg['lr'] = max(self.min_lr, base_lr * factor)


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Pairwise Ranking Yield Predictor')
    parser.add_argument('--device', default=None)
    parser.add_argument('--output_dir', default=str(project_root / 'checkpoints' / 'pairwise'))
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=20)
    parser.add_argument('--warmup_epochs', type=int, default=5)
    parser.add_argument('--hidden_dims', type=int, nargs='+', default=[512, 256, 128])
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--sim_threshold', type=float, default=0.7)
    parser.add_argument('--yield_margin', type=float, default=5.0)
    parser.add_argument('--max_pairs', type=int, default=10, help='Max pairs per anchor')
    parser.add_argument('--lambda_rank', type=float, default=1.0)
    parser.add_argument('--lambda_reg', type=float, default=0.5)
    parser.add_argument('--margin_scale', type=float, default=2.0)
    args = parser.parse_args()

    device = args.device or ('cuda' if torch.cuda.is_available() else 'cpu')
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Device: {device}")
    print(f"Output: {output_dir}")

    # ── 加载数据 ──
    print(f"\n{'=' * 70}")
    print(f"  Loading data...")
    print(f"{'=' * 70}")

    all_data = torch.load(project_root / 'data' / 'train.pt', map_location='cpu', weights_only=False)
    train_data, temp = train_test_split(all_data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp, test_size=0.5, random_state=42)

    print(f"  Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}")

    yields = np.array([d['yield'] for d in train_data])
    print(f"  Train yield: mean={yields.mean():.1f}, std={yields.std():.1f}, "
          f"range=[{yields.min():.0f}, {yields.max():.0f}]")

    # ── 构建数据集 ──
    print(f"\n{'=' * 70}")
    print(f"  Building pairwise dataset...")
    print(f"{'=' * 70}")

    train_pair_ds = PairwiseReactionDataset(
        train_data, sim_threshold=args.sim_threshold,
        yield_margin=args.yield_margin, max_pairs_per_anchor=args.max_pairs,
    )
    train_point_ds = PointwiseReactionDataset(train_data)

    val_pair_ds = PairwiseReactionDataset(
        val_data, sim_threshold=args.sim_threshold,
        yield_margin=args.yield_margin, max_pairs_per_anchor=args.max_pairs,
    )
    val_point_ds = PointwiseReactionDataset(val_data)

    train_pair_loader = DataLoader(train_pair_ds, batch_size=args.batch_size,
                                    shuffle=True, num_workers=0, drop_last=True)
    train_point_loader = DataLoader(train_point_ds, batch_size=args.batch_size,
                                     shuffle=True, num_workers=0, drop_last=True)
    val_pair_loader = DataLoader(val_pair_ds, batch_size=args.batch_size,
                                  shuffle=False, num_workers=0)
    val_point_loader = DataLoader(val_point_ds, batch_size=args.batch_size,
                                   shuffle=False, num_workers=0)

    if len(train_pair_ds) == 0:
        print("  ERROR: No training pairs found! Try lowering sim_threshold or yield_margin.")
        return

    print(f"\n  Train pairs: {len(train_pair_ds)}, pointwise: {len(train_point_ds)}")
    print(f"  Val pairs: {len(val_pair_ds)}, pointwise: {len(val_point_ds)}")

    # ── 构建模型 ──
    print(f"\n{'=' * 70}")
    print(f"  Building model (input_dim={INPUT_DIM}, no xTB)")
    print(f"{'=' * 70}")

    model = YieldPredictor(
        input_dim=INPUT_DIM,
        hidden_dims=args.hidden_dims,
        dropout=args.dropout,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"  Parameters: {num_params:,}")

    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.lr, weight_decay=args.weight_decay,
    )
    scheduler = WarmupCosineScheduler(optimizer, args.warmup_epochs, args.epochs)

    # ── 训练 ──
    print(f"\n{'=' * 70}")
    print(f"  Training (λ_rank={args.lambda_rank}, λ_reg={args.lambda_reg}, "
          f"margin_scale={args.margin_scale})")
    print(f"{'=' * 70}")

    best_composite = -float('inf')
    patience_counter = 0
    history = []

    for epoch in range(args.epochs):
        t0 = time.time()
        scheduler.step(epoch)
        lr = optimizer.param_groups[0]['lr']

        train_loss, rank_loss, reg_loss = train_epoch(
            model, train_pair_loader, train_point_loader, optimizer,
            args.lambda_rank, args.lambda_reg, args.margin_scale, device,
        )

        val_metrics = evaluate(model, val_point_loader, val_pair_loader, device)
        elapsed = time.time() - t0

        history.append({
            'epoch': epoch + 1, 'lr': lr,
            'train_loss': train_loss, 'rank_loss': rank_loss, 'reg_loss': reg_loss,
            **val_metrics,
        })

        print(f"  Epoch {epoch+1:3d}/{args.epochs} | lr={lr:.2e} | "
              f"loss={train_loss:.4f} (rank={rank_loss:.4f} reg={reg_loss:.4f}) | "
              f"val MAE={val_metrics['mae']:.2f} R2={val_metrics['r2']:.4f} "
              f"PairAcc={val_metrics['pair_accuracy']:.4f} | {elapsed:.1f}s")

        # Early stopping on composite score (r2 + pair_accuracy)
        if val_metrics['composite'] > best_composite:
            best_composite = val_metrics['composite']
            patience_counter = 0

            checkpoint = {
                'epoch': epoch + 1,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'metrics': val_metrics,
                'config': {
                    'model': {
                        'predictor': {
                            'hidden_dims': args.hidden_dims,
                            'dropout': args.dropout,
                        }
                    }
                },
                'args': vars(args),
            }
            torch.save(checkpoint, output_dir / 'best_model.pt')
            print(f"    ★ New best (composite={best_composite:.4f}), saved checkpoint")
        else:
            patience_counter += 1
            if patience_counter >= args.patience:
                print(f"\n  Early stopping at epoch {epoch+1} (patience={args.patience})")
                break

    # ── 最终评估 ──
    print(f"\n{'=' * 70}")
    print(f"  Final evaluation on test set")
    print(f"{'=' * 70}")

    # Load best checkpoint
    best_ckpt = torch.load(output_dir / 'best_model.pt', map_location=device, weights_only=False)
    model.load_state_dict(best_ckpt['model_state_dict'])

    test_pair_ds = PairwiseReactionDataset(
        test_data, sim_threshold=args.sim_threshold,
        yield_margin=args.yield_margin, max_pairs_per_anchor=args.max_pairs,
    )
    test_point_ds = PointwiseReactionDataset(test_data)
    test_pair_loader = DataLoader(test_pair_ds, batch_size=args.batch_size, shuffle=False)
    test_point_loader = DataLoader(test_point_ds, batch_size=args.batch_size, shuffle=False)

    test_metrics = evaluate(model, test_point_loader, test_pair_loader, device)

    print(f"  Test MAE:        {test_metrics['mae']:.2f}%")
    print(f"  Test RMSE:       {test_metrics['rmse']:.2f}%")
    print(f"  Test R2:         {test_metrics['r2']:.4f}")
    print(f"  Test Pair Acc:   {test_metrics['pair_accuracy']:.4f}")
    print(f"  Test Composite:  {test_metrics['composite']:.4f}")

    # 保存训练历史
    history_path = output_dir / f"training_history_{datetime.now():%Y%m%d_%H%M%S}.json"
    with open(history_path, 'w') as f:
        json.dump(history, f, indent=2)
    print(f"\n  History saved to: {history_path}")
    print(f"  Best checkpoint: {output_dir / 'best_model.pt'}")

    print(f"\n{'=' * 70}")
    print(f"  Training complete.")
    print(f"  Next: cp {output_dir}/best_model.pt checkpoints/best_model.pt")
    print(f"  Then: python scripts/eval_yield_ranking.py --device cuda")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
