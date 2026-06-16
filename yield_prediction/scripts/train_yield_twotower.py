"""
Two-Tower Yield Predictor + Pairwise Ranking

核心思想: 分离 reaction 和 condition 编码，强制模型学习条件对产率的影响
- Reaction tower: rxn_fp(6144) → 128D embedding
- Condition tower: solvent_fp(2048) + electrolyte_fp(2048) + echem(6) → 128D embedding
- Interaction: concat + MLP → yield score
- Reaction dropout: 训练时随机 mask rxn embedding，强制 condition 信号

Training: BPR ranking loss + MSE regression loss
- 对于相似反应 pair (i,j)，交换条件构建对比样本
- BPR 强制 correct conditions > swapped conditions

用法:
    cd yield_prediction
    python scripts/train_yield_twotower.py --device cuda
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

FP_SIZE = 2048
RXN_DIM = 3 * FP_SIZE    # 6144
COND_DIM = 2 * FP_SIZE + 6  # 4102


# ── Two-Tower Model ────────────────────────────────────────────

class TwoTowerYieldPredictor(nn.Module):
    """Two-tower yield predictor with reaction dropout."""

    def __init__(self, rxn_dim=RXN_DIM, cond_dim=COND_DIM,
                 embed_dim=128, hidden_dim=256, dropout=0.2,
                 rxn_dropout=0.5):
        super().__init__()
        self.rxn_dim = rxn_dim
        self.cond_dim = cond_dim
        self.embed_dim = embed_dim
        self.rxn_dropout_p = rxn_dropout

        # Reaction tower
        self.rxn_encoder = nn.Sequential(
            nn.Linear(rxn_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, embed_dim),
            nn.BatchNorm1d(embed_dim),
            nn.ReLU(),
        )

        # Condition tower
        self.cond_encoder = nn.Sequential(
            nn.Linear(cond_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, embed_dim),
            nn.BatchNorm1d(embed_dim),
            nn.ReLU(),
        )

        # Interaction head: concat + bilinear-like interaction
        self.interaction = nn.Sequential(
            nn.Linear(embed_dim * 2 + embed_dim, hidden_dim),  # concat + element-wise product
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
        )

    def encode(self, x):
        """Split input and encode with two towers."""
        rxn_feat = x[:, :self.rxn_dim]
        cond_feat = x[:, self.rxn_dim:]

        rxn_emb = self.rxn_encoder(rxn_feat)   # [B, embed_dim]
        cond_emb = self.cond_encoder(cond_feat) # [B, embed_dim]

        # Reaction dropout: during training, randomly zero-out rxn embedding
        if self.training and self.rxn_dropout_p > 0:
            mask = torch.bernoulli(
                torch.full((rxn_emb.size(0), 1), 1 - self.rxn_dropout_p,
                           device=rxn_emb.device)
            )
            # Scale to preserve expected value
            rxn_emb = rxn_emb * mask / (1 - self.rxn_dropout_p + 1e-8)

        return rxn_emb, cond_emb

    def score(self, rxn_emb, cond_emb):
        """Compute yield score from embeddings."""
        interaction = rxn_emb * cond_emb  # element-wise product
        combined = torch.cat([rxn_emb, cond_emb, interaction], dim=-1)
        return self.interaction(combined)

    def forward(self, x):
        """Forward pass: input [B, rxn_dim + cond_dim] → yield [B, 1] (sigmoid)."""
        rxn_emb, cond_emb = self.encode(x)
        logit = self.score(rxn_emb, cond_emb)
        return torch.sigmoid(logit)

    def forward_raw(self, x):
        """Raw logit for ranking loss."""
        rxn_emb, cond_emb = self.encode(x)
        return self.score(rxn_emb, cond_emb)


# ── Feature & Dataset ─────────────────────────────────────────

def build_feature_vector(item, use_conditions_from=None):
    """Build 10246D feature: rxn(6144) + cond(4102)."""
    cond = use_conditions_from if use_conditions_from is not None else item
    features = np.concatenate([
        np.array(item['reactant_fp'] + item['product_fp'] + item['diff_fp'], dtype=np.float32),
        np.array(cond['solvent_fp'], dtype=np.float32),
        np.array(cond['electrolyte_fp'], dtype=np.float32),
        np.array([
            float(cond['anode']), float(cond['cathode']),
            0.0, 0.0, 0.0,  # current_mA, density, potential (unknown)
            float(cond['cell_type']),
        ], dtype=np.float32),
    ])
    return features


class PairwiseDataset(Dataset):
    """Returns (feat_A, feat_B, yield_A, yield_B) for BPR training."""

    def __init__(self, data, sim_threshold=0.7, yield_margin=5.0,
                 max_pairs_per_anchor=10):
        self.data = data
        self.yields = np.array([d['yield'] for d in data], dtype=np.float32)
        n = len(data)

        # Build rxn_fp matrix
        print(f"  Building {n} reaction fingerprints...")
        rxn_fps = np.zeros((n, RXN_DIM), dtype=np.float32)
        for i, d in enumerate(data):
            rxn_fps[i] = d['reactant_fp'] + d['product_fp'] + d['diff_fp']

        norms = np.linalg.norm(rxn_fps, axis=1, keepdims=True) + 1e-8
        rxn_fps_norm = rxn_fps / norms

        # Find pairs
        print(f"  Finding pairs (sim>{sim_threshold}, margin>{yield_margin}%)...")
        self.pairs = []
        batch_size = 512

        for start in tqdm(range(0, n, batch_size), desc="  Pair search", leave=False):
            end = min(start + batch_size, n)
            sims = rxn_fps_norm[start:end] @ rxn_fps_norm.T

            for local_idx in range(end - start):
                i = start + local_idx
                sim_row = sims[local_idx]
                sim_row[i] = 0

                candidates = np.where(
                    (sim_row > sim_threshold) &
                    (np.abs(self.yields - self.yields[i]) > yield_margin)
                )[0]

                if len(candidates) > max_pairs_per_anchor:
                    top_k_idx = np.argsort(sim_row[candidates])[::-1][:max_pairs_per_anchor]
                    candidates = candidates[top_k_idx]

                for j in candidates:
                    self.pairs.append((i, int(j)))

        print(f"  Total pairs: {len(self.pairs)} from {n} reactions "
              f"(avg {len(self.pairs)/n:.1f} per reaction)")

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        i, j = self.pairs[idx]
        feat_A = build_feature_vector(self.data[i])
        feat_B = build_feature_vector(self.data[i], use_conditions_from=self.data[j])
        yield_A = self.yields[i] / 100.0
        yield_B = self.yields[j] / 100.0
        return (
            torch.from_numpy(feat_A),
            torch.from_numpy(feat_B),
            torch.tensor(yield_A, dtype=torch.float32),
            torch.tensor(yield_B, dtype=torch.float32),
        )


class PointwiseDataset(Dataset):
    """Standard MSE regression dataset."""

    def __init__(self, data):
        self.data = data
        self.yields = np.array([d['yield'] for d in data], dtype=np.float32)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        feat = build_feature_vector(self.data[idx])
        return torch.from_numpy(feat), torch.tensor(self.yields[idx] / 100.0, dtype=torch.float32)


# ── Training ──────────────────────────────────────────────────

def train_epoch(model, pair_loader, point_loader, optimizer,
                lambda_rank, lambda_reg, margin_scale, device):
    model.train()
    total_loss = total_rank = total_reg = 0.0
    n_steps = 0

    pair_iter = iter(pair_loader)
    point_iter = iter(point_loader)
    steps = max(len(pair_loader), len(point_loader))

    for _ in range(steps):
        optimizer.zero_grad()

        # ── BPR ranking loss ──
        try:
            feat_A, feat_B, yield_A, yield_B = next(pair_iter)
        except StopIteration:
            pair_iter = iter(pair_loader)
            feat_A, feat_B, yield_A, yield_B = next(pair_iter)

        feat_A, feat_B = feat_A.to(device), feat_B.to(device)
        yield_A, yield_B = yield_A.to(device), yield_B.to(device)

        score_A = model.forward_raw(feat_A).squeeze(-1)
        score_B = model.forward_raw(feat_B).squeeze(-1)

        yield_diff = yield_A - yield_B
        higher_score = torch.where(yield_diff > 0, score_A, score_B)
        lower_score = torch.where(yield_diff > 0, score_B, score_A)
        margin = torch.abs(yield_diff) * margin_scale

        rank_loss = -F.logsigmoid(higher_score - lower_score - margin).mean()

        # ── MSE regression loss ──
        try:
            feat_p, yield_p = next(point_iter)
        except StopIteration:
            point_iter = iter(point_loader)
            feat_p, yield_p = next(point_iter)

        feat_p, yield_p = feat_p.to(device), yield_p.to(device)
        pred_p = model(feat_p).squeeze(-1)
        reg_loss = F.mse_loss(pred_p, yield_p)

        # Also MSE on pair anchor
        pred_A = torch.sigmoid(score_A)
        reg_pair = F.mse_loss(pred_A, yield_A)

        loss = lambda_rank * rank_loss + lambda_reg * (reg_loss + 0.5 * reg_pair)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        total_loss += loss.item()
        total_rank += rank_loss.item()
        total_reg += reg_loss.item()
        n_steps += 1

    return total_loss / n_steps, total_rank / n_steps, total_reg / n_steps


@torch.no_grad()
def evaluate(model, point_loader, pair_loader, device):
    model.eval()

    # Regression
    all_preds, all_labels = [], []
    for feat, y in point_loader:
        pred = model(feat.to(device)).squeeze(-1) * 100
        all_preds.append(pred.cpu())
        all_labels.append(y * 100)

    preds = torch.cat(all_preds)
    labels = torch.cat(all_labels)
    mae = torch.abs(preds - labels).mean().item()
    rmse = torch.sqrt(((preds - labels) ** 2).mean()).item()
    ss_res = ((preds - labels) ** 2).sum()
    ss_tot = ((labels - labels.mean()) ** 2).sum()
    r2 = (1 - ss_res / ss_tot).item() if ss_tot > 0 else 0.0

    # Pairwise accuracy
    correct = total = 0
    for feat_A, feat_B, yield_A, yield_B in pair_loader:
        s_A = model(feat_A.to(device)).squeeze(-1)
        s_B = model(feat_B.to(device)).squeeze(-1)
        correct += ((s_A > s_B).cpu() == (yield_A > yield_B)).sum().item()
        total += len(yield_A)

    pair_acc = correct / total if total > 0 else 0.0

    return {
        'mae': mae, 'rmse': rmse, 'r2': r2,
        'pair_accuracy': pair_acc,
        'composite': r2 + pair_acc,
    }


# ── LR Scheduler ──────────────────────────────────────────────

class WarmupCosineScheduler:
    def __init__(self, optimizer, warmup_epochs, total_epochs, min_lr=1e-6):
        self.optimizer = optimizer
        self.warmup_epochs = warmup_epochs
        self.total_epochs = total_epochs
        self.base_lrs = [pg['lr'] for pg in optimizer.param_groups]
        self.min_lr = min_lr

    def step(self, epoch):
        if epoch < self.warmup_epochs:
            factor = (epoch + 1) / self.warmup_epochs
        else:
            progress = (epoch - self.warmup_epochs) / max(1, self.total_epochs - self.warmup_epochs)
            factor = 0.5 * (1 + np.cos(np.pi * progress))
        for pg, base_lr in zip(self.optimizer.param_groups, self.base_lrs):
            pg['lr'] = max(self.min_lr, base_lr * factor)


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default=None)
    parser.add_argument('--output_dir', default=str(project_root / 'checkpoints' / 'twotower'))
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=150)
    parser.add_argument('--patience', type=int, default=30)
    parser.add_argument('--warmup_epochs', type=int, default=5)
    parser.add_argument('--embed_dim', type=int, default=128)
    parser.add_argument('--hidden_dim', type=int, default=256)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--rxn_dropout', type=float, default=0.5,
                        help='Prob of zeroing rxn embedding during training')
    parser.add_argument('--sim_threshold', type=float, default=0.7)
    parser.add_argument('--yield_margin', type=float, default=5.0)
    parser.add_argument('--max_pairs', type=int, default=10)
    parser.add_argument('--lambda_rank', type=float, default=1.0)
    parser.add_argument('--lambda_reg', type=float, default=0.5)
    parser.add_argument('--margin_scale', type=float, default=0.5)
    args = parser.parse_args()

    device = args.device or ('cuda' if torch.cuda.is_available() else 'cpu')
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Device: {device}")
    print(f"Output: {output_dir}")

    # ── Load data ──
    print(f"\n{'=' * 70}")
    print(f"  Loading data...")
    print(f"{'=' * 70}")

    all_data = torch.load(project_root / 'data' / 'train.pt',
                          map_location='cpu', weights_only=False)
    train_data, temp = train_test_split(all_data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp, test_size=0.5, random_state=42)

    print(f"  Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}")
    yields = np.array([d['yield'] for d in train_data])
    print(f"  Yield: mean={yields.mean():.1f}, std={yields.std():.1f}")

    # ── Build datasets ──
    print(f"\n{'=' * 70}")
    print(f"  Building pairwise dataset...")
    print(f"{'=' * 70}")

    train_pair_ds = PairwiseDataset(train_data, args.sim_threshold,
                                     args.yield_margin, args.max_pairs)
    train_point_ds = PointwiseDataset(train_data)
    val_pair_ds = PairwiseDataset(val_data, args.sim_threshold,
                                   args.yield_margin, args.max_pairs)
    val_point_ds = PointwiseDataset(val_data)

    train_pair_loader = DataLoader(train_pair_ds, args.batch_size,
                                    shuffle=True, num_workers=0, drop_last=True)
    train_point_loader = DataLoader(train_point_ds, args.batch_size,
                                     shuffle=True, num_workers=0, drop_last=True)
    val_pair_loader = DataLoader(val_pair_ds, args.batch_size,
                                  shuffle=False, num_workers=0)
    val_point_loader = DataLoader(val_point_ds, args.batch_size,
                                   shuffle=False, num_workers=0)

    if len(train_pair_ds) == 0:
        print("  ERROR: No training pairs!")
        return

    print(f"  Train: {len(train_pair_ds)} pairs, {len(train_point_ds)} pointwise")
    print(f"  Val:   {len(val_pair_ds)} pairs, {len(val_point_ds)} pointwise")

    # ── Build model ──
    print(f"\n{'=' * 70}")
    print(f"  Building TwoTower model (rxn_dropout={args.rxn_dropout})")
    print(f"{'=' * 70}")

    model = TwoTowerYieldPredictor(
        rxn_dim=RXN_DIM, cond_dim=COND_DIM,
        embed_dim=args.embed_dim, hidden_dim=args.hidden_dim,
        dropout=args.dropout, rxn_dropout=args.rxn_dropout,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"  Parameters: {num_params:,}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr,
                                   weight_decay=args.weight_decay)
    scheduler = WarmupCosineScheduler(optimizer, args.warmup_epochs, args.epochs)

    # ── Train ──
    print(f"\n{'=' * 70}")
    print(f"  Training (λ_rank={args.lambda_rank}, λ_reg={args.lambda_reg}, "
          f"margin={args.margin_scale})")
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

        if val_metrics['composite'] > best_composite:
            best_composite = val_metrics['composite']
            patience_counter = 0
            checkpoint = {
                'epoch': epoch + 1,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'metrics': val_metrics,
                'config': {
                    'model_type': 'twotower',
                    'rxn_dim': RXN_DIM,
                    'cond_dim': COND_DIM,
                    'embed_dim': args.embed_dim,
                    'hidden_dim': args.hidden_dim,
                    'dropout': args.dropout,
                    'rxn_dropout': args.rxn_dropout,
                },
                'args': vars(args),
            }
            torch.save(checkpoint, output_dir / 'best_model.pt')
            print(f"    ★ New best (composite={best_composite:.4f})")
        else:
            patience_counter += 1
            if patience_counter >= args.patience:
                print(f"\n  Early stopping at epoch {epoch+1}")
                break

    # ── Test ──
    print(f"\n{'=' * 70}")
    print(f"  Final test evaluation")
    print(f"{'=' * 70}")

    best_ckpt = torch.load(output_dir / 'best_model.pt',
                            map_location=device, weights_only=False)
    model.load_state_dict(best_ckpt['model_state_dict'])

    test_pair_ds = PairwiseDataset(test_data, args.sim_threshold,
                                    args.yield_margin, args.max_pairs)
    test_point_ds = PointwiseDataset(test_data)
    test_pair_loader = DataLoader(test_pair_ds, args.batch_size, shuffle=False)
    test_point_loader = DataLoader(test_point_ds, args.batch_size, shuffle=False)

    test_m = evaluate(model, test_point_loader, test_pair_loader, device)
    print(f"  MAE={test_m['mae']:.2f}%  RMSE={test_m['rmse']:.2f}%  "
          f"R2={test_m['r2']:.4f}  PairAcc={test_m['pair_accuracy']:.4f}")

    # Save history
    hist_path = output_dir / f"history_{datetime.now():%Y%m%d_%H%M%S}.json"
    with open(hist_path, 'w') as f:
        json.dump(history, f, indent=2)
    print(f"  History: {hist_path}")
    print(f"  Checkpoint: {output_dir / 'best_model.pt'}")


if __name__ == "__main__":
    main()
