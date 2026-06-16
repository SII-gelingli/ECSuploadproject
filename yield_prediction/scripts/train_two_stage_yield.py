"""
两阶段产率预测模型 (Two-Stage Yield Prediction)

核心思想：
1. 第一阶段：使用一个路由模型预测样本属于哪个产率范围
2. 第二阶段：根据预测的产率范围选择对应的专家模型进行精细预测

解决的问题：
- 之前用反应指纹预测聚类不准确
- 现在直接用神经网络学习"选择哪个专家"这个任务

两种变体：
1. 硬路由：路由模型输出聚类ID，选择单一专家
2. 软路由 (MoE风格)：路由模型输出权重，加权组合多个专家

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
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset, Subset
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class YieldRangeDataset(Dataset):
    """带产率范围标签的数据集"""

    def __init__(self, data_path: str, yield_bins=None):
        self.data = torch.load(data_path, weights_only=False)
        self.yield_bins = yield_bins  # 产率分箱边界

    def __len__(self):
        return len(self.data)

    def set_yield_bins(self, bins):
        self.yield_bins = bins

    def _get_yield_bin(self, y):
        """获取产率所属的分箱"""
        for i in range(len(self.yield_bins) - 1):
            if self.yield_bins[i] <= y < self.yield_bins[i + 1]:
                return i
        return len(self.yield_bins) - 2

    def __getitem__(self, idx):
        item = self.data[idx]

        full_features = (
            item['reactant_fp'] + item['product_fp'] + item['diff_fp'] +
            item['solvent_fp'] + item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']] +
            item['reactant_xtb'] + item['product_xtb'] +
            item['solvent_xtb'] + item['electrolyte_xtb'] + item['reaction_diff_xtb']
        )

        yield_value = item['yield']
        yield_bin = self._get_yield_bin(yield_value) if self.yield_bins is not None else 0

        return {
            'features': torch.tensor(full_features, dtype=torch.float32),
            'yield': torch.tensor(yield_value / 100.0, dtype=torch.float32),
            'yield_raw': yield_value,
            'yield_bin': yield_bin,
        }


class Router(nn.Module):
    """路由网络：预测样本属于哪个产率范围"""

    def __init__(self, input_dim: int, n_experts: int, hidden_dims: list = [256, 128]):
        super().__init__()

        layers = []
        prev_dim = input_dim
        for h_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, h_dim),
                nn.LayerNorm(h_dim),
                nn.GELU(),
                nn.Dropout(0.2),
            ])
            prev_dim = h_dim
        layers.append(nn.Linear(prev_dim, n_experts))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        """返回每个专家的权重（softmax归一化）"""
        logits = self.net(x)
        return F.softmax(logits, dim=-1)


class Expert(nn.Module):
    """专家网络：预测特定产率范围内的产率"""

    def __init__(self, input_dim: int, hidden_dims: list = [256, 128], dropout: float = 0.3):
        super().__init__()

        layers = []
        prev_dim = input_dim
        for h_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, h_dim),
                nn.LayerNorm(h_dim),
                nn.GELU(),
                nn.Dropout(dropout),
            ])
            prev_dim = h_dim
        layers.append(nn.Linear(prev_dim, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return torch.sigmoid(self.net(x))


class TwoStageYieldPredictor(nn.Module):
    """两阶段产率预测模型"""

    def __init__(self, input_dim: int, n_experts: int,
                 router_hidden: list = [256, 128],
                 expert_hidden: list = [256, 128],
                 dropout: float = 0.3,
                 routing_mode: str = 'soft'):
        """
        Args:
            routing_mode: 'soft' (加权组合) 或 'hard' (选择top-1)
        """
        super().__init__()

        self.n_experts = n_experts
        self.routing_mode = routing_mode

        # 路由器
        self.router = Router(input_dim, n_experts, router_hidden)

        # 专家网络
        self.experts = nn.ModuleList([
            Expert(input_dim, expert_hidden, dropout)
            for _ in range(n_experts)
        ])

    def forward(self, x, return_routing=False):
        # 获取路由权重
        routing_weights = self.router(x)  # [batch, n_experts]

        # 获取所有专家的预测
        expert_outputs = torch.stack([
            expert(x).squeeze(-1) for expert in self.experts
        ], dim=1)  # [batch, n_experts]

        if self.routing_mode == 'soft':
            # 加权组合所有专家的输出
            output = (routing_weights * expert_outputs).sum(dim=1)  # [batch]
        else:
            # 选择最高权重的专家
            top_expert = routing_weights.argmax(dim=1)  # [batch]
            output = expert_outputs[torch.arange(x.size(0)), top_expert]

        if return_routing:
            return output, routing_weights
        return output


class TwoStageTrainer:
    """两阶段训练器"""

    def __init__(self, model, device, args):
        self.model = model
        self.device = device
        self.args = args

        self.optimizer = optim.AdamW(
            model.parameters(),
            lr=args.lr,
            weight_decay=args.weight_decay
        )
        self.scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(
            self.optimizer, T_0=20, T_mult=2, eta_min=1e-6
        )

    def train_epoch(self, train_loader, yield_bins):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0
        total_yield_loss = 0
        total_route_loss = 0

        for batch in train_loader:
            features = batch['features'].to(self.device)
            yields = batch['yield'].to(self.device)
            yield_bins_batch = batch['yield_bin'].to(self.device)

            self.optimizer.zero_grad()

            # 前向传播
            pred_yield, routing_weights = self.model(features, return_routing=True)

            # 产率预测损失 (MSE)
            yield_loss = F.mse_loss(pred_yield, yields)

            # 路由辅助损失 (鼓励路由到正确的专家)
            route_loss = F.cross_entropy(
                routing_weights.log(),  # 已经是softmax后的，用log
                yield_bins_batch
            )

            # 负载均衡损失 (鼓励均匀使用专家)
            avg_routing = routing_weights.mean(dim=0)  # [n_experts]
            balance_loss = (avg_routing * torch.log(avg_routing + 1e-8)).sum()
            balance_loss = -balance_loss  # 最大化熵 = 均匀分布

            # 总损失
            loss = yield_loss + self.args.route_weight * route_loss + 0.01 * balance_loss

            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()

            total_loss += loss.item()
            total_yield_loss += yield_loss.item()
            total_route_loss += route_loss.item()

        n_batches = len(train_loader)
        return {
            'loss': total_loss / n_batches,
            'yield_loss': total_yield_loss / n_batches,
            'route_loss': total_route_loss / n_batches
        }

    def evaluate(self, data_loader):
        """评估模型"""
        self.model.eval()
        all_preds = []
        all_labels = []
        all_routing = []

        with torch.no_grad():
            for batch in data_loader:
                features = batch['features'].to(self.device)
                yields = batch['yield'].to(self.device)

                pred, routing = self.model(features, return_routing=True)

                all_preds.extend((pred * 100).cpu().tolist())
                all_labels.extend((yields * 100).cpu().tolist())
                all_routing.append(routing.cpu())

        preds = np.array(all_preds)
        labels = np.array(all_labels)

        mae = np.mean(np.abs(preds - labels))
        rmse = np.sqrt(np.mean((preds - labels)**2))
        r2 = 1 - np.sum((preds - labels)**2) / np.sum((labels - labels.mean())**2)

        # 路由分析
        all_routing = torch.cat(all_routing, dim=0)
        expert_usage = all_routing.argmax(dim=1)
        usage_counts = torch.bincount(expert_usage, minlength=self.model.n_experts)

        return {
            'mae': mae,
            'rmse': rmse,
            'r2': r2,
            'predictions': preds,
            'labels': labels,
            'expert_usage': usage_counts.numpy(),
            'routing_weights': all_routing.numpy()
        }


def create_yield_bins(yields, n_bins):
    """创建产率分箱"""
    percentiles = np.linspace(0, 100, n_bins + 1)
    bins = np.percentile(yields, percentiles)
    bins[0] = -0.1
    bins[-1] = 100.1
    return bins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'two_stage'))

    # 模型参数
    parser.add_argument('--n_experts', type=int, default=4, help='专家数量')
    parser.add_argument('--routing_mode', type=str, default='soft', choices=['soft', 'hard'])
    parser.add_argument('--router_hidden', type=str, default='256,128')
    parser.add_argument('--expert_hidden', type=str, default='512,256,128')
    parser.add_argument('--dropout', type=float, default=0.3)

    # 训练参数
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--route_weight', type=float, default=0.1, help='路由损失权重')
    parser.add_argument('--epochs', type=int, default=200)
    parser.add_argument('--patience', type=int, default=30)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    router_hidden = [int(x) for x in args.router_hidden.split(',')]
    expert_hidden = [int(x) for x in args.expert_hidden.split(',')]
    device = torch.device(args.device)
    print(f"Device: {device}")

    # 创建输出目录
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n" + "=" * 70)
    print("加载数据...")
    print("=" * 70)

    train_dataset = YieldRangeDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = YieldRangeDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = YieldRangeDataset(data_dir / 'test_xtb_cat.pt')

    print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    # 创建产率分箱
    train_yields = np.array([train_dataset.data[i]['yield'] for i in range(len(train_dataset))])
    yield_bins = create_yield_bins(train_yields, args.n_experts)

    print(f"\n产率分箱 ({args.n_experts} 个专家):")
    for i in range(len(yield_bins) - 1):
        bin_mask = (train_yields >= yield_bins[i]) & (train_yields < yield_bins[i + 1])
        count = bin_mask.sum()
        print(f"  Expert {i}: 产率 [{yield_bins[i]:.1f}, {yield_bins[i + 1]:.1f}), N={count}")

    # 设置分箱
    train_dataset.set_yield_bins(yield_bins)
    val_dataset.set_yield_bins(yield_bins)
    test_dataset.set_yield_bins(yield_bins)

    # 创建数据加载器
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size*2, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size*2, shuffle=False, num_workers=4)

    # 创建模型
    print("\n" + "=" * 70)
    print("创建两阶段模型...")
    print("=" * 70)

    model = TwoStageYieldPredictor(
        input_dim=10301,
        n_experts=args.n_experts,
        router_hidden=router_hidden,
        expert_hidden=expert_hidden,
        dropout=args.dropout,
        routing_mode=args.routing_mode
    ).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    n_router_params = sum(p.numel() for p in model.router.parameters())
    n_expert_params = sum(p.numel() for p in model.experts.parameters())
    print(f"  总参数: {n_params:,}")
    print(f"  路由器参数: {n_router_params:,}")
    print(f"  专家参数: {n_expert_params:,}")
    print(f"  路由模式: {args.routing_mode}")

    # 训练
    print("\n" + "=" * 70)
    print("开始训练...")
    print("=" * 70)

    trainer = TwoStageTrainer(model, device, args)

    best_val_r2 = -float('inf')
    best_state = None
    patience_counter = 0
    start_time = datetime.now()

    for epoch in range(args.epochs):
        # 训练
        train_metrics = trainer.train_epoch(train_loader, yield_bins)

        # 验证
        val_results = trainer.evaluate(val_loader)

        # 学习率调度
        trainer.scheduler.step()

        # 保存最佳模型
        if val_results['r2'] > best_val_r2:
            best_val_r2 = val_results['r2']
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            patience_counter = 0
            marker = "* BEST"
        else:
            patience_counter += 1
            marker = ""

        if (epoch + 1) % 10 == 0 or marker:
            print(f"Epoch {epoch+1:3d} | "
                  f"Loss: {train_metrics['loss']:.4f} | "
                  f"Val MAE: {val_results['mae']:.2f}%, R²: {val_results['r2']:.4f} {marker}")
            expert_usage = val_results['expert_usage']
            usage_str = ", ".join([f"E{i}:{c}" for i, c in enumerate(expert_usage)])
            print(f"          Experts: {usage_str}")

        if patience_counter >= args.patience:
            print(f"\n早停: {args.patience} epochs 无改善")
            break

    elapsed = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed}")

    # 加载最佳模型
    if best_state is not None:
        model.load_state_dict(best_state)

    # 测试
    print("\n" + "=" * 70)
    print("在测试集上评估")
    print("=" * 70)

    test_results = trainer.evaluate(test_loader)

    print(f"\n测试结果:")
    print(f"  Test MAE:  {test_results['mae']:.2f}%")
    print(f"  Test RMSE: {test_results['rmse']:.2f}%")
    print(f"  Test R²:   {test_results['r2']:.4f}")

    print(f"\n专家使用分布:")
    for i, count in enumerate(test_results['expert_usage']):
        pct = count / len(test_dataset) * 100
        print(f"  Expert {i}: {count:4d} ({pct:.1f}%)")

    # 与基线比较
    baseline_r2 = 0.363
    baseline_mae = 12.43
    r2_imp = test_results['r2'] - baseline_r2
    mae_imp = baseline_mae - test_results['mae']

    print(f"\n与基线比较 (MLP+xTB: R²=0.363, MAE=12.43%):")
    print(f"  R² 变化: {r2_imp:+.4f} ({baseline_r2:.3f} → {test_results['r2']:.3f})")
    print(f"  MAE 变化: {mae_imp:+.2f}% ({baseline_mae:.2f}% → {test_results['mae']:.2f}%)")

    if r2_imp > 0 and mae_imp > 0:
        print(f"\n🎉 成功超越基线! R² 提升 {r2_imp:.4f}, MAE 降低 {mae_imp:.2f}%")
    elif r2_imp > 0:
        print(f"\n✅ R² 提升 {r2_imp:.4f}")
    else:
        print(f"\n未超越基线")

    # 分析每个产率区间的预测效果
    print("\n按产率区间分析:")
    preds = test_results['predictions']
    labels = test_results['labels']
    for i in range(len(yield_bins) - 1):
        mask = (labels >= yield_bins[i]) & (labels < yield_bins[i + 1])
        if mask.sum() > 0:
            bin_mae = np.mean(np.abs(preds[mask] - labels[mask]))
            bin_r2 = 1 - np.sum((preds[mask] - labels[mask])**2) / np.sum((labels[mask] - labels[mask].mean())**2) if np.var(labels[mask]) > 0 else 0
            print(f"  产率 [{yield_bins[i]:.0f}, {yield_bins[i + 1]:.0f}): N={mask.sum():3d}, MAE={bin_mae:.2f}%, R²={bin_r2:.4f}")

    # 保存模型和结果
    torch.save({
        'model_state_dict': model.state_dict(),
        'yield_bins': yield_bins.tolist(),
        'args': vars(args),
    }, output_dir / 'best_model.pt')

    results = {
        'model': 'TwoStageYieldPredictor',
        'n_experts': args.n_experts,
        'routing_mode': args.routing_mode,
        'test_mae': float(test_results['mae']),
        'test_rmse': float(test_results['rmse']),
        'test_r2': float(test_results['r2']),
        'r2_improvement': float(r2_imp),
        'mae_improvement': float(mae_imp),
        'expert_usage': test_results['expert_usage'].tolist(),
        'yield_bins': yield_bins.tolist(),
        'training_time': str(elapsed),
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")

    return results


if __name__ == "__main__":
    main()
