"""
优化版 MoE 产率预测模型 - 针对过拟合问题

优化策略：
1. 更小的专家网络（减少参数量）
2. 更强的正则化（Dropout + Weight Decay + Label Smoothing）
3. Top-K 稀疏路由（只激活部分专家，减少过拟合）
4. 专家负载均衡损失（防止专家塌缩）
5. 梯度裁剪 + 学习率warmup
6. 早停策略
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import numpy as np

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from sklearn.cluster import KMeans

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class LightExpertNetwork(nn.Module):
    """轻量级专家网络"""

    def __init__(self, input_dim: int, hidden_dim: int = 128, dropout: float = 0.4):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.LayerNorm(hidden_dim // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, 1),
        )

    def forward(self, x):
        return torch.sigmoid(self.net(x))


class OptimizedMoEYieldPredictor(nn.Module):
    """
    优化版 MoE 产率预测模型

    改进：
    1. 更小的专家网络
    2. Top-K 稀疏路由
    3. 残差连接（主干预测 + 专家修正）
    4. 输入特征降维
    """

    def __init__(
        self,
        full_input_dim: int = 10301,
        reaction_fp_dim: int = 6144,
        num_experts: int = 4,
        expert_hidden_dim: int = 128,
        gate_hidden_dim: int = 128,
        dropout: float = 0.4,
        top_k: int = 2,
        use_residual: bool = True,
    ):
        super().__init__()

        self.num_experts = num_experts
        self.top_k = min(top_k, num_experts)
        self.use_residual = use_residual
        self.reaction_fp_dim = reaction_fp_dim

        # 输入特征压缩（降维减少过拟合）
        self.input_compressor = nn.Sequential(
            nn.Linear(full_input_dim, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.LayerNorm(256),
            nn.GELU(),
            nn.Dropout(dropout),
        )

        # 主干预测网络（所有样本共享）
        self.backbone = nn.Sequential(
            nn.Linear(256, 128),
            nn.LayerNorm(128),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(128, 1),
        )

        # 门控网络（基于反应指纹）
        self.gate = nn.Sequential(
            nn.Linear(reaction_fp_dim, gate_hidden_dim),
            nn.LayerNorm(gate_hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(gate_hidden_dim, num_experts),
        )

        # 轻量级专家网络（用于修正）
        self.experts = nn.ModuleList([
            LightExpertNetwork(256, expert_hidden_dim, dropout)
            for _ in range(num_experts)
        ])

        # 专家修正权重（可学习，初始化为小值）
        self.expert_scale = nn.Parameter(torch.ones(1) * 0.1)

    def forward(self, full_features, reaction_fp=None):
        batch_size = full_features.size(0)

        if reaction_fp is None:
            reaction_fp = full_features[:, :self.reaction_fp_dim]

        # 1. 输入压缩
        compressed = self.input_compressor(full_features)  # [B, 256]

        # 2. 主干预测
        backbone_pred = torch.sigmoid(self.backbone(compressed))  # [B, 1]

        # 3. 计算门控权重
        gate_logits = self.gate(reaction_fp)  # [B, num_experts]

        # Top-K 稀疏路由
        topk_weights, topk_indices = torch.topk(gate_logits, self.top_k, dim=-1)
        topk_weights = F.softmax(topk_weights, dim=-1)  # 归一化

        # 4. 只计算 top-k 专家的输出
        expert_outputs = torch.zeros(batch_size, 1, device=full_features.device)

        for i in range(self.top_k):
            expert_idx = topk_indices[:, i]  # [B]
            weight = topk_weights[:, i:i+1]  # [B, 1]

            # 批量处理同一专家的样本
            for e in range(self.num_experts):
                mask = (expert_idx == e)
                if mask.any():
                    expert_out = self.experts[e](compressed[mask])
                    expert_outputs[mask] += weight[mask] * expert_out

        # 5. 残差连接：主干 + 专家修正
        if self.use_residual:
            # 专家输出作为修正项（中心化到0附近）
            expert_correction = (expert_outputs - 0.5) * self.expert_scale
            final_pred = backbone_pred + expert_correction
            final_pred = torch.clamp(final_pred, 0, 1)
        else:
            final_pred = expert_outputs

        # 构建完整的专家权重用于负载均衡
        full_weights = torch.zeros(batch_size, self.num_experts, device=full_features.device)
        full_weights.scatter_(1, topk_indices, topk_weights)

        return final_pred, full_weights

    def get_load_balance_loss(self, expert_weights):
        """负载均衡损失"""
        # 计算每个专家的使用频率
        expert_usage = expert_weights.mean(dim=0)  # [num_experts]
        # 理想均匀分布
        target = torch.ones_like(expert_usage) / self.num_experts
        # KL散度
        loss = F.kl_div(
            torch.log(expert_usage + 1e-8),
            target,
            reduction='sum'
        )
        return loss

    def get_expert_entropy_loss(self, expert_weights):
        """专家选择熵损失（鼓励确定性选择）"""
        # 计算每个样本的专家权重熵
        entropy = -(expert_weights * torch.log(expert_weights + 1e-8)).sum(dim=-1)
        return entropy.mean()


class MoEDataset(Dataset):
    """MoE 数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        reaction_fp = item['reactant_fp'] + item['product_fp'] + item['diff_fp']

        full_features = (
            item['reactant_fp'] + item['product_fp'] + item['diff_fp'] +
            item['solvent_fp'] + item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']] +
            item['reactant_xtb'] + item['product_xtb'] +
            item['solvent_xtb'] + item['electrolyte_xtb'] + item['reaction_diff_xtb']
        )

        return {
            'reaction_fp': torch.tensor(reaction_fp, dtype=torch.float32),
            'full_features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(item['yield'] / 100.0, dtype=torch.float32),
        }


def collate_fn(batch):
    return {
        'reaction_fp': torch.stack([b['reaction_fp'] for b in batch]),
        'full_features': torch.stack([b['full_features'] for b in batch]),
        'yield': torch.stack([b['yield'] for b in batch]),
    }


class LabelSmoothingMSELoss(nn.Module):
    """带标签平滑的MSE损失"""

    def __init__(self, smoothing: float = 0.05):
        super().__init__()
        self.smoothing = smoothing

    def forward(self, pred, target):
        # 将目标向0.5平滑
        smoothed_target = target * (1 - self.smoothing) + 0.5 * self.smoothing
        return F.mse_loss(pred, smoothed_target)


def train_epoch(model, loader, optimizer, criterion, device, lb_weight=0.01, grad_clip=1.0):
    model.train()
    total_loss = 0
    total_mse = 0
    total_lb = 0
    total_mae = 0
    n_batches = 0

    for batch in tqdm(loader, desc="Training", leave=False):
        features = batch['full_features'].to(device)
        reaction_fp = batch['reaction_fp'].to(device)
        labels = batch['yield'].to(device).unsqueeze(1)

        optimizer.zero_grad()
        pred, expert_weights = model(features, reaction_fp)

        mse_loss = criterion(pred, labels)
        lb_loss = model.get_load_balance_loss(expert_weights)
        loss = mse_loss + lb_weight * lb_loss

        loss.backward()
        if grad_clip > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
        optimizer.step()

        total_loss += loss.item()
        total_mse += mse_loss.item()
        total_lb += lb_loss.item()
        total_mae += (pred - labels).abs().mean().item() * 100
        n_batches += 1

    return {
        'loss': total_loss / n_batches,
        'mse': total_mse / n_batches,
        'lb': total_lb / n_batches,
        'mae': total_mae / n_batches,
    }


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    all_preds = []
    all_labels = []
    all_experts = []
    n_batches = 0

    for batch in loader:
        features = batch['full_features'].to(device)
        reaction_fp = batch['reaction_fp'].to(device)
        labels = batch['yield'].to(device).unsqueeze(1)

        pred, expert_weights = model(features, reaction_fp)
        total_loss += criterion(pred, labels).item()

        all_preds.extend((pred.cpu().flatten() * 100).tolist())
        all_labels.extend((labels.cpu().flatten() * 100).tolist())
        all_experts.extend(expert_weights.argmax(dim=-1).cpu().tolist())
        n_batches += 1

    preds = torch.tensor(all_preds)
    labels = torch.tensor(all_labels)
    mae = (preds - labels).abs().mean().item()
    rmse = ((preds - labels) ** 2).mean().sqrt().item()
    ss_res = ((preds - labels) ** 2).sum()
    ss_tot = ((labels - labels.mean()) ** 2).sum()
    r2 = (1 - ss_res / ss_tot).item()

    expert_dist = {}
    for e in all_experts:
        expert_dist[e] = expert_dist.get(e, 0) + 1

    return {
        'loss': total_loss / n_batches,
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'expert_dist': expert_dist,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'moe_optimized'))
    parser.add_argument('--num_experts', type=int, default=4)
    parser.add_argument('--top_k', type=int, default=2)
    parser.add_argument('--expert_hidden', type=int, default=128)
    parser.add_argument('--gate_hidden', type=int, default=128)
    parser.add_argument('--dropout', type=float, default=0.4)
    parser.add_argument('--use_residual', action='store_true', default=True)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--weight_decay', type=float, default=1e-3)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--patience', type=int, default=10)
    parser.add_argument('--lb_weight', type=float, default=0.02)
    parser.add_argument('--label_smoothing', type=float, default=0.05)
    parser.add_argument('--warmup_epochs', type=int, default=5)
    parser.add_argument('--grad_clip', type=float, default=1.0)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = torch.device(args.device)
    print(f"Device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n" + "=" * 70)
    print("加载数据...")
    print("=" * 70)

    train_dataset = MoEDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = MoEDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = MoEDataset(data_dir / 'test_xtb_cat.pt')

    print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True,
                              collate_fn=collate_fn, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size*2, shuffle=False,
                            collate_fn=collate_fn, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size*2, shuffle=False,
                             collate_fn=collate_fn, num_workers=4)

    # 创建模型
    print("\n" + "=" * 70)
    print("创建优化版 MoE 模型...")
    print("=" * 70)

    model = OptimizedMoEYieldPredictor(
        full_input_dim=10301,
        reaction_fp_dim=6144,
        num_experts=args.num_experts,
        expert_hidden_dim=args.expert_hidden,
        gate_hidden_dim=args.gate_hidden,
        dropout=args.dropout,
        top_k=args.top_k,
        use_residual=args.use_residual,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"  参数量: {num_params:,} (优化前: ~27M)")
    print(f"  专家数: {args.num_experts}, Top-K: {args.top_k}")
    print(f"  Dropout: {args.dropout}, Weight Decay: {args.weight_decay}")
    print(f"  残差连接: {args.use_residual}")

    # 优化器
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

    # 学习率调度器（带warmup）
    def lr_lambda(epoch):
        if epoch < args.warmup_epochs:
            return (epoch + 1) / args.warmup_epochs
        else:
            progress = (epoch - args.warmup_epochs) / (args.epochs - args.warmup_epochs)
            return 0.5 * (1 + np.cos(np.pi * progress))

    scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    # 损失函数（带标签平滑）
    criterion = LabelSmoothingMSELoss(smoothing=args.label_smoothing)

    # 训练
    print("\n" + "=" * 70)
    print("开始训练（优化版）")
    print(f"目标: 超越 MLP+xTB 基线 (R²=0.363, MAE=12.43%)")
    print("=" * 70)

    best_val_r2 = -float('inf')
    patience_counter = 0
    history = {'train_mae': [], 'val_mae': [], 'val_r2': []}

    start_time = datetime.now()

    for epoch in range(args.epochs):
        train_metrics = train_epoch(model, train_loader, optimizer, criterion, device,
                                    args.lb_weight, args.grad_clip)
        val_metrics = evaluate(model, val_loader, criterion, device)

        scheduler.step()
        lr = optimizer.param_groups[0]['lr']

        history['train_mae'].append(train_metrics['mae'])
        history['val_mae'].append(val_metrics['mae'])
        history['val_r2'].append(val_metrics['r2'])

        improved = ""
        if val_metrics['r2'] > best_val_r2:
            best_val_r2 = val_metrics['r2']
            patience_counter = 0
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'val_r2': val_metrics['r2'],
                'val_mae': val_metrics['mae'],
                'args': vars(args),
            }, output_dir / 'best_model.pt')
            improved = " * BEST"
        else:
            patience_counter += 1

        expert_str = ", ".join([f"E{k}:{v}" for k, v in sorted(val_metrics['expert_dist'].items())])
        print(f"Epoch {epoch+1:2d} | Train MAE: {train_metrics['mae']:.2f}% | "
              f"Val MAE: {val_metrics['mae']:.2f}%, R²: {val_metrics['r2']:.4f} | "
              f"LR: {lr:.2e}{improved}")
        print(f"         Experts: {expert_str}")

        if patience_counter >= args.patience:
            print(f"\n早停: {args.patience} epochs 无改善")
            break

    elapsed = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed}")

    # 测试
    print("\n" + "=" * 70)
    print("测试最佳模型")
    print("=" * 70)

    checkpoint = torch.load(output_dir / 'best_model.pt', weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])

    test_metrics = evaluate(model, test_loader, criterion, device)

    print(f"Test MAE:  {test_metrics['mae']:.2f}%")
    print(f"Test RMSE: {test_metrics['rmse']:.2f}%")
    print(f"Test R²:   {test_metrics['r2']:.4f}")

    baseline_r2 = 0.363
    baseline_mae = 12.43
    r2_imp = test_metrics['r2'] - baseline_r2
    mae_imp = baseline_mae - test_metrics['mae']

    print(f"\n与基线比较:")
    print(f"  R² 变化: {r2_imp:+.4f} ({baseline_r2:.3f} → {test_metrics['r2']:.3f})")
    print(f"  MAE 变化: {mae_imp:+.2f}% ({baseline_mae:.2f}% → {test_metrics['mae']:.2f}%)")

    if r2_imp > 0:
        print(f"\n🎉 成功超越基线! R² 提升 {r2_imp:.4f}")
    else:
        print(f"\n未超越基线")

    # 保存结果
    results = {
        'model': 'OptimizedMoE',
        'num_experts': args.num_experts,
        'top_k': args.top_k,
        'num_params': num_params,
        'best_epoch': checkpoint['epoch'],
        'best_val_r2': best_val_r2,
        'test_mae': test_metrics['mae'],
        'test_rmse': test_metrics['rmse'],
        'test_r2': test_metrics['r2'],
        'r2_improvement': r2_imp,
        'mae_improvement': mae_imp,
        'training_time': str(elapsed),
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")
    return results


if __name__ == "__main__":
    main()
