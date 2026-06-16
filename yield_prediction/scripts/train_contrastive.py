"""
对比学习产率预测模型

思路：
1. 使用监督对比损失学习反应表示
2. yield < 5% 视为失败反应（负样本）
3. 结合对比损失和回归损失进行联合训练
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
import numpy as np

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class SupConLoss(nn.Module):
    """监督对比损失

    参考: Supervised Contrastive Learning (https://arxiv.org/abs/2004.11362)
    """
    def __init__(self, temperature=0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, features, labels):
        """
        Args:
            features: [batch_size, feature_dim] - L2 normalized embeddings
            labels: [batch_size] - 类别标签 (0=失败, 1=成功)
        """
        device = features.device
        batch_size = features.shape[0]

        # 计算相似度矩阵
        similarity_matrix = torch.matmul(features, features.T) / self.temperature

        # 创建mask: 同类为1，不同类为0
        labels = labels.contiguous().view(-1, 1)
        mask = torch.eq(labels, labels.T).float().to(device)

        # 排除自身
        logits_mask = torch.ones_like(mask) - torch.eye(batch_size).to(device)
        mask = mask * logits_mask

        # 计算log_prob
        exp_logits = torch.exp(similarity_matrix) * logits_mask
        log_prob = similarity_matrix - torch.log(exp_logits.sum(1, keepdim=True) + 1e-6)

        # 计算每个样本的平均正样本log概率
        mask_sum = mask.sum(1)
        mask_sum = torch.where(mask_sum == 0, torch.ones_like(mask_sum), mask_sum)
        mean_log_prob_pos = (mask * log_prob).sum(1) / mask_sum

        # 损失
        loss = -mean_log_prob_pos.mean()

        return loss


class YieldBinLoss(nn.Module):
    """产率区间对比损失

    将产率分为多个区间，同区间的反应互为正样本
    """
    def __init__(self, temperature=0.1, num_bins=5):
        super().__init__()
        self.temperature = temperature
        self.num_bins = num_bins
        self.supcon = SupConLoss(temperature)

    def get_yield_bin(self, yields):
        """将产率映射到区间标签

        区间: 0 (失败, <5%), 1 (低, 5-30%), 2 (中, 30-60%), 3 (高, 60-90%), 4 (优秀, >90%)
        """
        bins = torch.zeros_like(yields, dtype=torch.long)
        bins[yields < 5] = 0      # 失败
        bins[(yields >= 5) & (yields < 30)] = 1   # 低
        bins[(yields >= 30) & (yields < 60)] = 2  # 中
        bins[(yields >= 60) & (yields < 90)] = 3  # 高
        bins[yields >= 90] = 4    # 优秀
        return bins

    def forward(self, features, yields):
        """
        Args:
            features: [batch_size, feature_dim] - L2 normalized embeddings
            yields: [batch_size] - 产率值 (0-100)
        """
        labels = self.get_yield_bin(yields)
        return self.supcon(features, labels)


class ContrastiveYieldPredictor(nn.Module):
    """对比学习产率预测模型"""

    def __init__(
        self,
        input_dim: int = 6144,
        hidden_dim: int = 256,
        embedding_dim: int = 128,
        dropout: float = 0.3
    ):
        super().__init__()

        # 编码器 - 生成反应表示
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 投影头 - 用于对比学习
        self.projector = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, embedding_dim),
        )

        # 预测头 - 产率回归
        self.predictor = nn.Sequential(
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

    def forward(self, x, return_embedding=False):
        # 编码
        h = self.encoder(x)

        # 产率预测
        yield_pred = self.predictor(h)

        if return_embedding:
            # 对比学习embedding (L2 normalized)
            z = self.projector(h)
            z = F.normalize(z, dim=1)
            return yield_pred, z

        return yield_pred


class ContrastiveDataset(Dataset):
    """对比学习数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 反应指纹
        fp_features = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp']
        )

        # 产率 (0-100)
        yield_value = item.get('yield', item.get('product_yield', 0))
        if isinstance(yield_value, str):
            yield_value = float(yield_value) if yield_value else 0

        return (
            torch.tensor(fp_features, dtype=torch.float32),
            torch.tensor(yield_value, dtype=torch.float32)
        )


def train_epoch(model, loader, optimizer, device, contrastive_loss_fn,
                regression_weight=1.0, contrastive_weight=0.5):
    """训练一个epoch"""
    model.train()
    total_loss = 0
    total_reg_loss = 0
    total_con_loss = 0

    pbar = tqdm(loader, desc="Training")
    for features, yields in pbar:
        features = features.to(device)
        yields = yields.to(device)

        optimizer.zero_grad()

        # 前向传播
        pred, embeddings = model(features, return_embedding=True)
        pred = pred.squeeze() * 100  # 转换到0-100范围

        # 回归损失 (MSE)
        reg_loss = F.mse_loss(pred, yields)

        # 对比损失
        con_loss = contrastive_loss_fn(embeddings, yields)

        # 总损失
        loss = regression_weight * reg_loss + contrastive_weight * con_loss

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_reg_loss += reg_loss.item()
        total_con_loss += con_loss.item()

        pbar.set_postfix({
            'loss': f'{loss.item():.4f}',
            'reg': f'{reg_loss.item():.4f}',
            'con': f'{con_loss.item():.4f}'
        })

    n = len(loader)
    return total_loss / n, total_reg_loss / n, total_con_loss / n


def evaluate(model, loader, device):
    """评估模型"""
    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for features, yields in loader:
            features = features.to(device)
            pred = model(features).squeeze() * 100

            all_preds.extend(pred.cpu().tolist())
            all_labels.extend(yields.tolist())

    all_preds = torch.tensor(all_preds)
    all_labels = torch.tensor(all_labels)

    mae = torch.mean(torch.abs(all_preds - all_labels)).item()
    rmse = torch.sqrt(torch.mean((all_preds - all_labels) ** 2)).item()

    ss_res = torch.sum((all_preds - all_labels) ** 2)
    ss_tot = torch.sum((all_labels - torch.mean(all_labels)) ** 2)
    r2 = (1 - ss_res / ss_tot).item()

    # 计算失败反应识别准确率
    pred_failed = all_preds < 5
    true_failed = all_labels < 5
    failed_acc = (pred_failed == true_failed).float().mean().item()

    # 失败反应的precision和recall
    tp = ((pred_failed) & (true_failed)).sum().item()
    fp = ((pred_failed) & (~true_failed)).sum().item()
    fn = ((~pred_failed) & (true_failed)).sum().item()

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)

    return {
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'failed_acc': failed_acc,
        'failed_precision': precision,
        'failed_recall': recall,
        'failed_f1': f1,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'contrastive'))
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=20)
    parser.add_argument('--hidden_dim', type=int, default=256)
    parser.add_argument('--embedding_dim', type=int, default=128)
    parser.add_argument('--temperature', type=float, default=0.1)
    parser.add_argument('--regression_weight', type=float, default=1.0)
    parser.add_argument('--contrastive_weight', type=float, default=0.5)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Using device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n加载数据...")
    train_dataset = ContrastiveDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = ContrastiveDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = ContrastiveDataset(data_dir / 'test_xtb_cat.pt')

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    # 统计失败反应比例
    failed_count = sum(1 for i in range(len(train_dataset)) if train_dataset[i][1] < 5)
    print(f"  训练集失败反应 (yield<5%): {failed_count} ({100*failed_count/len(train_dataset):.1f}%)")

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size * 2, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size * 2, shuffle=False, num_workers=4)

    # 创建模型
    model = ContrastiveYieldPredictor(
        input_dim=6144,
        hidden_dim=args.hidden_dim,
        embedding_dim=args.embedding_dim,
        dropout=0.3,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

    # 对比损失
    contrastive_loss_fn = YieldBinLoss(temperature=args.temperature)

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs, eta_min=1e-6)

    # 训练
    print("\n" + "=" * 70)
    print("开始对比学习训练")
    print(f"  回归损失权重: {args.regression_weight}")
    print(f"  对比损失权重: {args.contrastive_weight}")
    print(f"  温度参数: {args.temperature}")
    print("=" * 70)

    best_val_r2 = -float('inf')
    patience_counter = 0
    history = []

    for epoch in range(1, args.epochs + 1):
        train_loss, reg_loss, con_loss = train_epoch(
            model, train_loader, optimizer, device, contrastive_loss_fn,
            args.regression_weight, args.contrastive_weight
        )

        val_metrics = evaluate(model, val_loader, device)
        scheduler.step()

        print(f"Epoch {epoch:3d} | "
              f"Loss: {train_loss:.4f} (reg:{reg_loss:.4f}, con:{con_loss:.4f}) | "
              f"Val R²: {val_metrics['r2']:.4f}, MAE: {val_metrics['mae']:.2f}% | "
              f"Failed F1: {val_metrics['failed_f1']:.3f}")

        history.append({
            'epoch': epoch,
            'train_loss': train_loss,
            'reg_loss': reg_loss,
            'con_loss': con_loss,
            **val_metrics
        })

        # Early stopping
        if val_metrics['r2'] > best_val_r2:
            best_val_r2 = val_metrics['r2']
            patience_counter = 0

            # 保存最佳模型
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_metrics': val_metrics,
                'args': vars(args),
            }, output_dir / 'best_model.pt')
            print(f"  * 保存最佳模型 (R²={best_val_r2:.4f})")
        else:
            patience_counter += 1
            if patience_counter >= args.patience:
                print(f"\n早停: {args.patience} epochs 无改善")
                break

    # 测试
    print("\n" + "=" * 70)
    print("在测试集上评估最佳模型")
    print("=" * 70)

    checkpoint = torch.load(output_dir / 'best_model.pt')
    model.load_state_dict(checkpoint['model_state_dict'])

    test_metrics = evaluate(model, test_loader, device)

    print(f"\n测试集结果:")
    print(f"  MAE:  {test_metrics['mae']:.2f}%")
    print(f"  RMSE: {test_metrics['rmse']:.2f}%")
    print(f"  R²:   {test_metrics['r2']:.4f}")
    print(f"\n失败反应识别 (yield<5%):")
    print(f"  Accuracy:  {test_metrics['failed_acc']:.1%}")
    print(f"  Precision: {test_metrics['failed_precision']:.3f}")
    print(f"  Recall:    {test_metrics['failed_recall']:.3f}")
    print(f"  F1 Score:  {test_metrics['failed_f1']:.3f}")

    # 保存结果
    results = {
        'model': 'ContrastiveYieldPredictor',
        'test_metrics': test_metrics,
        'best_epoch': checkpoint['epoch'],
        'args': vars(args),
        'history': history,
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")


if __name__ == "__main__":
    main()
