"""
Mixture of Experts (MoE) 产率预测模型训练脚本

策略：
1. 使用反应指纹聚类来指导专家分配
2. 多个专家网络分别学习不同类型反应的产率模式
3. 门控网络决定如何组合专家的预测

目标：通过专家分化提高 R² 分数
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
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from sklearn.cluster import KMeans

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.moe_yield_predictor import (
    MoEYieldPredictor,
    ClusterAwareMoEYieldPredictor,
    HierarchicalMoEYieldPredictor,
)


class MoEDataset(Dataset):
    """MoE 模型数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 反应指纹 (6144维) - 用于门控网络
        reaction_fp = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp']
        )

        # 完整特征 (10246维 + 55维 xTB = 10301维)
        full_features = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp'] +
            item['solvent_fp'] +
            item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']]
        )

        # xTB特征 (55维)
        xtb_features = (
            item['reactant_xtb'] +
            item['product_xtb'] +
            item['solvent_xtb'] +
            item['electrolyte_xtb'] +
            item['reaction_diff_xtb']
        )

        full_features = full_features + xtb_features

        return {
            'reaction_fp': torch.tensor(reaction_fp, dtype=torch.float32),
            'full_features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(item['yield'] / 100.0, dtype=torch.float32),
        }


def collate_fn(batch):
    """批次整理函数"""
    return {
        'reaction_fp': torch.stack([b['reaction_fp'] for b in batch]),
        'full_features': torch.stack([b['full_features'] for b in batch]),
        'yield': torch.stack([b['yield'] for b in batch]),
    }


def train_epoch(
    model,
    loader,
    optimizer,
    criterion,
    device,
    load_balance_weight: float = 0.01,
    grad_clip: float = 1.0,
):
    """训练一个 epoch"""
    model.train()
    total_loss = 0
    total_mse_loss = 0
    total_lb_loss = 0
    total_mae = 0
    n_batches = 0

    for batch in tqdm(loader, desc="Training", leave=False):
        full_features = batch['full_features'].to(device)
        reaction_fp = batch['reaction_fp'].to(device)
        labels = batch['yield'].to(device).unsqueeze(1)

        optimizer.zero_grad()

        pred, expert_weights = model(full_features, reaction_fp)

        # MSE 损失
        mse_loss = criterion(pred, labels)

        # 负载均衡损失
        lb_loss = model.get_load_balance_loss(expert_weights)

        # 总损失
        loss = mse_loss + load_balance_weight * lb_loss

        loss.backward()

        if grad_clip > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=grad_clip)

        optimizer.step()

        total_loss += loss.item()
        total_mse_loss += mse_loss.item()
        total_lb_loss += lb_loss.item()
        total_mae += (pred - labels).abs().mean().item() * 100
        n_batches += 1

    return {
        'loss': total_loss / n_batches,
        'mse_loss': total_mse_loss / n_batches,
        'lb_loss': total_lb_loss / n_batches,
        'mae': total_mae / n_batches,
    }


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    """评估模型"""
    model.eval()
    total_loss = 0
    all_preds = []
    all_labels = []
    all_expert_assignments = []
    n_batches = 0

    for batch in loader:
        full_features = batch['full_features'].to(device)
        reaction_fp = batch['reaction_fp'].to(device)
        labels = batch['yield'].to(device).unsqueeze(1)

        pred, expert_weights = model(full_features, reaction_fp)
        total_loss += criterion(pred, labels).item()

        all_preds.extend((pred.cpu().flatten() * 100).tolist())
        all_labels.extend((labels.cpu().flatten() * 100).tolist())

        # 记录专家分配
        expert_assignment = expert_weights.argmax(dim=-1).cpu().tolist()
        all_expert_assignments.extend(expert_assignment)

        n_batches += 1

    # 计算指标
    preds = torch.tensor(all_preds)
    labels = torch.tensor(all_labels)
    mae = torch.mean(torch.abs(preds - labels)).item()
    rmse = torch.sqrt(torch.mean((preds - labels) ** 2)).item()
    ss_res = torch.sum((preds - labels) ** 2)
    ss_tot = torch.sum((labels - labels.mean()) ** 2)
    r2 = (1 - ss_res / ss_tot).item()

    # 专家使用分布
    expert_counts = {}
    for e in all_expert_assignments:
        expert_counts[e] = expert_counts.get(e, 0) + 1

    return {
        'loss': total_loss / n_batches,
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'expert_distribution': expert_counts,
        'predictions': all_preds,
        'labels': all_labels,
    }


def analyze_clusters(reaction_fps: np.ndarray, num_clusters: int) -> dict:
    """分析反应指纹的聚类特性"""
    print(f"\n分析反应指纹聚类 (K={num_clusters})...")

    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(reaction_fps)

    # 统计每个聚类的大小
    cluster_sizes = {}
    for l in labels:
        cluster_sizes[l] = cluster_sizes.get(l, 0) + 1

    print("  聚类分布:")
    for c in sorted(cluster_sizes.keys()):
        print(f"    Cluster {c}: {cluster_sizes[c]} ({cluster_sizes[c]/len(labels)*100:.1f}%)")

    # 计算聚类内聚性（轮廓系数的简化版本）
    inertia = kmeans.inertia_
    print(f"  聚类内平方和: {inertia:.2f}")

    return {
        'labels': labels,
        'centers': kmeans.cluster_centers_,
        'cluster_sizes': cluster_sizes,
        'inertia': inertia,
    }


def main():
    parser = argparse.ArgumentParser(description="Train MoE Yield Predictor")
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'moe_yield'))
    parser.add_argument('--model_type', type=str, default='standard',
                        choices=['standard', 'cluster_aware', 'hierarchical'])
    parser.add_argument('--num_experts', type=int, default=8)
    parser.add_argument('--expert_hidden', type=str, default='256,128')
    parser.add_argument('--gate_hidden', type=int, default=256)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--top_k', type=int, default=0, help='0=soft routing, >0=top-k experts')
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=15)
    parser.add_argument('--load_balance_weight', type=float, default=0.01)
    parser.add_argument('--grad_clip', type=float, default=1.0)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    # 设置随机种子
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    # 解析参数
    expert_hidden = [int(x) for x in args.expert_hidden.split(',')]
    device = torch.device(args.device)
    print(f"Using device: {device}")

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

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    # 分析聚类特性
    print("\n收集反应指纹用于聚类分析...")
    train_fps = []
    for i in range(len(train_dataset)):
        item = train_dataset[i]
        train_fps.append(item['reaction_fp'].numpy())
    train_fps = np.array(train_fps)

    cluster_info = analyze_clusters(train_fps, args.num_experts)

    # DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        collate_fn=collate_fn,
        num_workers=4,
        pin_memory=True if args.device == 'cuda' else False,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        collate_fn=collate_fn,
        num_workers=4,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        collate_fn=collate_fn,
        num_workers=4,
    )

    # 创建模型
    print("\n" + "=" * 70)
    print(f"创建 {args.model_type} MoE 模型...")
    print("=" * 70)

    full_input_dim = 10301  # 10246 + 55 xTB
    reaction_fp_dim = 6144

    if args.model_type == 'standard':
        model = MoEYieldPredictor(
            full_input_dim=full_input_dim,
            reaction_fp_dim=reaction_fp_dim,
            num_experts=args.num_experts,
            expert_hidden_dims=expert_hidden,
            gate_hidden_dim=args.gate_hidden,
            dropout=args.dropout,
            top_k=args.top_k,
        )
    elif args.model_type == 'cluster_aware':
        # 用 K-Means 聚类中心初始化
        cluster_centers = torch.from_numpy(cluster_info['centers']).float()
        model = ClusterAwareMoEYieldPredictor(
            full_input_dim=full_input_dim,
            reaction_fp_dim=reaction_fp_dim,
            num_clusters=args.num_experts,
            expert_hidden_dims=expert_hidden,
            dropout=args.dropout,
            cluster_centers=cluster_centers,
        )
    elif args.model_type == 'hierarchical':
        # 分层模型：4 粗类别 × 2 细专家 = 8 专家
        num_coarse = max(2, args.num_experts // 2)
        num_fine = max(2, args.num_experts // num_coarse)
        model = HierarchicalMoEYieldPredictor(
            full_input_dim=full_input_dim,
            reaction_fp_dim=reaction_fp_dim,
            num_coarse_classes=num_coarse,
            num_fine_experts=num_fine,
            expert_hidden_dims=expert_hidden,
            dropout=args.dropout,
        )

    model = model.to(device)
    num_params = sum(p.numel() for p in model.parameters())
    print(f"  参数量: {num_params:,}")
    print(f"  专家数: {args.num_experts}")
    print(f"  专家隐藏层: {expert_hidden}")

    # 优化器和调度器
    optimizer = optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=args.weight_decay,
    )

    scheduler = optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=args.epochs, eta_min=1e-6
    )

    criterion = nn.MSELoss()

    # 训练
    print("\n" + "=" * 70)
    print("开始训练 MoE 产率预测模型")
    print(f"目标: 超越 MLP+xTB 基线 (R²=0.363, MAE=12.43%)")
    print("=" * 70)

    best_val_r2 = -float('inf')
    best_val_mae = float('inf')
    patience_counter = 0

    history = {
        'train_loss': [], 'train_mae': [],
        'val_loss': [], 'val_mae': [], 'val_rmse': [], 'val_r2': [],
        'expert_distribution': [],
    }

    start_time = datetime.now()

    for epoch in range(args.epochs):
        # 重置专家统计
        if hasattr(model, 'reset_stats'):
            model.reset_stats()

        train_metrics = train_epoch(
            model, train_loader, optimizer, criterion, device,
            load_balance_weight=args.load_balance_weight,
            grad_clip=args.grad_clip,
        )
        val_metrics = evaluate(model, val_loader, criterion, device)

        scheduler.step()
        current_lr = optimizer.param_groups[0]['lr']

        history['train_loss'].append(train_metrics['loss'])
        history['train_mae'].append(train_metrics['mae'])
        history['val_loss'].append(val_metrics['loss'])
        history['val_mae'].append(val_metrics['mae'])
        history['val_rmse'].append(val_metrics['rmse'])
        history['val_r2'].append(val_metrics['r2'])
        history['expert_distribution'].append(val_metrics['expert_distribution'])

        improved = ""
        # 以 R² 作为主要指标
        if val_metrics['r2'] > best_val_r2:
            best_val_r2 = val_metrics['r2']
            best_val_mae = val_metrics['mae']
            patience_counter = 0
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_mae': val_metrics['mae'],
                'val_rmse': val_metrics['rmse'],
                'val_r2': val_metrics['r2'],
                'args': vars(args),
                'cluster_info': {
                    'centers': cluster_info['centers'].tolist() if isinstance(cluster_info['centers'], np.ndarray) else cluster_info['centers'],
                    'cluster_sizes': cluster_info['cluster_sizes'],
                },
            }, output_dir / 'best_model.pt')
            improved = " * BEST R²"
        else:
            patience_counter += 1

        # 专家使用情况
        expert_dist_str = ", ".join([
            f"E{k}:{v}" for k, v in sorted(val_metrics['expert_distribution'].items())
        ])

        print(f"Epoch {epoch+1:3d} | "
              f"Train MAE: {train_metrics['mae']:.2f}%, LB: {train_metrics['lb_loss']:.4f} | "
              f"Val MAE: {val_metrics['mae']:.2f}%, R²: {val_metrics['r2']:.4f} | "
              f"LR: {current_lr:.2e}{improved}")
        print(f"         Experts: {expert_dist_str}")

        if patience_counter >= args.patience:
            print(f"\n早停: {args.patience} epochs 无 R² 改善")
            break

    elapsed = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed}")

    # 测试最佳模型
    print("\n" + "=" * 70)
    print("在测试集上评估最佳模型")
    print("=" * 70)

    checkpoint = torch.load(output_dir / 'best_model.pt', weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])

    test_metrics = evaluate(model, test_loader, criterion, device)

    print(f"Test MAE:  {test_metrics['mae']:.2f}%")
    print(f"Test RMSE: {test_metrics['rmse']:.2f}%")
    print(f"Test R²:   {test_metrics['r2']:.4f}")

    # 与基线比较
    baseline_r2 = 0.363
    baseline_mae = 12.43
    r2_improvement = test_metrics['r2'] - baseline_r2
    mae_improvement = baseline_mae - test_metrics['mae']

    print(f"\n与 MLP+xTB 基线比较:")
    print(f"  R² 变化: {r2_improvement:+.4f} ({baseline_r2:.3f} → {test_metrics['r2']:.3f})")
    print(f"  MAE 变化: {mae_improvement:+.2f}% ({baseline_mae:.2f}% → {test_metrics['mae']:.2f}%)")

    if r2_improvement > 0:
        print(f"\n🎉 成功! R² 提升了 {r2_improvement:.4f}")
    else:
        print(f"\n未超越基线，考虑调整专家数量或模型架构")

    # 分析专家使用情况
    print(f"\n专家使用分布:")
    for k, v in sorted(test_metrics['expert_distribution'].items()):
        pct = v / len(test_dataset) * 100
        print(f"  Expert {k}: {v:4d} ({pct:.1f}%)")

    # 保存结果
    results = {
        'model': f'MoE-{args.model_type}',
        'num_experts': args.num_experts,
        'best_epoch': checkpoint['epoch'],
        'best_val_r2': best_val_r2,
        'best_val_mae': best_val_mae,
        'test_mae': test_metrics['mae'],
        'test_rmse': test_metrics['rmse'],
        'test_r2': test_metrics['r2'],
        'num_params': num_params,
        'expert_hidden': expert_hidden,
        'baseline_r2': baseline_r2,
        'baseline_mae': baseline_mae,
        'r2_improvement': r2_improvement,
        'mae_improvement': mae_improvement,
        'expert_distribution': test_metrics['expert_distribution'],
        'training_time': str(elapsed),
        'args': vars(args),
        'history': {k: v for k, v in history.items() if k != 'expert_distribution'},
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")

    return results


if __name__ == "__main__":
    main()
