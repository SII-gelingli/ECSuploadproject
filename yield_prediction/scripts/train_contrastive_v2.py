"""
对比学习产率预测模型 v2

改进：
1. 增加失败反应的采样权重
2. 添加二分类辅助任务（成功/失败）
3. 使用焦点损失处理类别不平衡
"""
import sys
import json
import argparse
from pathlib import Path

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from tqdm import tqdm
import numpy as np

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class FocalLoss(nn.Module):
    """焦点损失 - 处理类别不平衡"""
    def __init__(self, alpha=0.25, gamma=2.0):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, inputs, targets):
        bce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none')
        pt = torch.exp(-bce_loss)
        focal_loss = self.alpha * (1 - pt) ** self.gamma * bce_loss
        return focal_loss.mean()


class MultiTaskYieldModel(nn.Module):
    """多任务产率预测模型

    任务1: 产率回归
    任务2: 成功/失败二分类
    """
    def __init__(
        self,
        input_dim: int = 6144,
        hidden_dim: int = 256,
        dropout: float = 0.3
    ):
        super().__init__()

        # 共享编码器
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

        # 回归头 - 产率预测
        self.regression_head = nn.Sequential(
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

        # 分类头 - 成功/失败
        self.classifier_head = nn.Sequential(
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 1),
        )

    def forward(self, x):
        h = self.encoder(x)
        yield_pred = self.regression_head(h)
        success_logit = self.classifier_head(h)
        return yield_pred, success_logit


class YieldDataset(Dataset):
    """产率数据集"""

    def __init__(self, data_path: str, failure_threshold: float = 5.0):
        self.data = torch.load(data_path, weights_only=False)
        self.failure_threshold = failure_threshold

        # 预计算采样权重
        self.weights = []
        for item in self.data:
            yield_value = item.get('yield', item.get('product_yield', 0))
            if isinstance(yield_value, str):
                yield_value = float(yield_value) if yield_value else 0
            # 失败反应权重更高
            weight = 10.0 if yield_value < failure_threshold else 1.0
            self.weights.append(weight)

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

        # 产率
        yield_value = item.get('yield', item.get('product_yield', 0))
        if isinstance(yield_value, str):
            yield_value = float(yield_value) if yield_value else 0

        # 成功/失败标签
        is_success = 1.0 if yield_value >= self.failure_threshold else 0.0

        return (
            torch.tensor(fp_features, dtype=torch.float32),
            torch.tensor(yield_value, dtype=torch.float32),
            torch.tensor(is_success, dtype=torch.float32)
        )


def train_epoch(model, loader, optimizer, device, focal_loss_fn,
                regression_weight=1.0, classification_weight=2.0):
    """训练一个epoch"""
    model.train()
    total_loss = 0
    total_reg_loss = 0
    total_cls_loss = 0

    pbar = tqdm(loader, desc="Training")
    for features, yields, success_labels in pbar:
        features = features.to(device)
        yields = yields.to(device)
        success_labels = success_labels.to(device)

        optimizer.zero_grad()

        # 前向传播
        yield_pred, success_logit = model(features)
        yield_pred = yield_pred.squeeze() * 100

        # 回归损失
        reg_loss = F.mse_loss(yield_pred, yields)

        # 分类损失 (焦点损失)
        cls_loss = focal_loss_fn(success_logit.squeeze(), success_labels)

        # 总损失
        loss = regression_weight * reg_loss + classification_weight * cls_loss

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_reg_loss += reg_loss.item()
        total_cls_loss += cls_loss.item()

        pbar.set_postfix({
            'loss': f'{loss.item():.4f}',
            'reg': f'{reg_loss.item():.4f}',
            'cls': f'{cls_loss.item():.4f}'
        })

    n = len(loader)
    return total_loss / n, total_reg_loss / n, total_cls_loss / n


def evaluate(model, loader, device, threshold=5.0):
    """评估模型"""
    model.eval()
    all_yield_preds = []
    all_yield_labels = []
    all_success_preds = []
    all_success_labels = []

    with torch.no_grad():
        for features, yields, success_labels in loader:
            features = features.to(device)
            yield_pred, success_logit = model(features)
            yield_pred = yield_pred.squeeze() * 100

            all_yield_preds.extend(yield_pred.cpu().tolist())
            all_yield_labels.extend(yields.tolist())
            all_success_preds.extend(torch.sigmoid(success_logit.squeeze()).cpu().tolist())
            all_success_labels.extend(success_labels.tolist())

    all_yield_preds = torch.tensor(all_yield_preds)
    all_yield_labels = torch.tensor(all_yield_labels)
    all_success_preds = torch.tensor(all_success_preds)
    all_success_labels = torch.tensor(all_success_labels)

    # 回归指标
    mae = torch.mean(torch.abs(all_yield_preds - all_yield_labels)).item()
    rmse = torch.sqrt(torch.mean((all_yield_preds - all_yield_labels) ** 2)).item()
    ss_res = torch.sum((all_yield_preds - all_yield_labels) ** 2)
    ss_tot = torch.sum((all_yield_labels - torch.mean(all_yield_labels)) ** 2)
    r2 = (1 - ss_res / ss_tot).item()

    # 分类指标 (失败反应识别)
    pred_success = all_success_preds > 0.5
    true_success = all_success_labels > 0.5

    # 对于失败反应: 预测失败=正类
    pred_failed = ~pred_success
    true_failed = ~true_success

    accuracy = (pred_success == true_success).float().mean().item()

    tp = (pred_failed & true_failed).sum().item()
    fp = (pred_failed & true_success).sum().item()
    fn = (~pred_failed & true_failed).sum().item()
    tn = (~pred_failed & true_success).sum().item()

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)

    return {
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'accuracy': accuracy,
        'failed_precision': precision,
        'failed_recall': recall,
        'failed_f1': f1,
        'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'multitask'))
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=20)
    parser.add_argument('--hidden_dim', type=int, default=256)
    parser.add_argument('--regression_weight', type=float, default=1.0)
    parser.add_argument('--classification_weight', type=float, default=2.0)
    parser.add_argument('--failure_threshold', type=float, default=5.0)
    parser.add_argument('--use_weighted_sampler', action='store_true')
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Using device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n加载数据...")
    train_dataset = YieldDataset(data_dir / 'train_xtb_cat.pt', args.failure_threshold)
    val_dataset = YieldDataset(data_dir / 'val_xtb_cat.pt', args.failure_threshold)
    test_dataset = YieldDataset(data_dir / 'test_xtb_cat.pt', args.failure_threshold)

    # 统计
    failed_train = sum(1 for i in range(len(train_dataset)) if train_dataset[i][1] < args.failure_threshold)
    failed_val = sum(1 for i in range(len(val_dataset)) if val_dataset[i][1] < args.failure_threshold)
    failed_test = sum(1 for i in range(len(test_dataset)) if test_dataset[i][1] < args.failure_threshold)

    print(f"  Train: {len(train_dataset)} (失败: {failed_train}, {100*failed_train/len(train_dataset):.1f}%)")
    print(f"  Val:   {len(val_dataset)} (失败: {failed_val}, {100*failed_val/len(val_dataset):.1f}%)")
    print(f"  Test:  {len(test_dataset)} (失败: {failed_test}, {100*failed_test/len(test_dataset):.1f}%)")

    # 创建DataLoader
    if args.use_weighted_sampler:
        sampler = WeightedRandomSampler(train_dataset.weights, len(train_dataset))
        train_loader = DataLoader(train_dataset, batch_size=args.batch_size, sampler=sampler, num_workers=4)
        print("  使用加权采样器")
    else:
        train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=4)

    val_loader = DataLoader(val_dataset, batch_size=args.batch_size * 2, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size * 2, shuffle=False, num_workers=4)

    # 创建模型
    model = MultiTaskYieldModel(
        input_dim=6144,
        hidden_dim=args.hidden_dim,
        dropout=0.3,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

    # 损失函数
    focal_loss_fn = FocalLoss(alpha=0.75, gamma=2.0)  # alpha高=更关注失败样本

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs, eta_min=1e-6)

    # 训练
    print("\n" + "=" * 70)
    print("开始多任务学习训练")
    print(f"  失败阈值: {args.failure_threshold}%")
    print(f"  回归损失权重: {args.regression_weight}")
    print(f"  分类损失权重: {args.classification_weight}")
    print("=" * 70)

    best_val_score = -float('inf')
    patience_counter = 0
    history = []

    for epoch in range(1, args.epochs + 1):
        train_loss, reg_loss, cls_loss = train_epoch(
            model, train_loader, optimizer, device, focal_loss_fn,
            args.regression_weight, args.classification_weight
        )

        val_metrics = evaluate(model, val_loader, device, args.failure_threshold)
        scheduler.step()

        # 综合评分: R² + 0.5 * Failed F1
        val_score = val_metrics['r2'] + 0.5 * val_metrics['failed_f1']

        print(f"Epoch {epoch:3d} | "
              f"Loss: {train_loss:.4f} | "
              f"Val R²: {val_metrics['r2']:.4f}, MAE: {val_metrics['mae']:.2f}% | "
              f"Failed: P={val_metrics['failed_precision']:.2f} R={val_metrics['failed_recall']:.2f} F1={val_metrics['failed_f1']:.3f}")

        history.append({
            'epoch': epoch,
            'train_loss': train_loss,
            'reg_loss': reg_loss,
            'cls_loss': cls_loss,
            **val_metrics
        })

        # Early stopping
        if val_score > best_val_score:
            best_val_score = val_score
            patience_counter = 0

            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'val_metrics': val_metrics,
                'args': vars(args),
            }, output_dir / 'best_model.pt')
            print(f"  * 保存最佳模型 (score={best_val_score:.4f})")
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

    test_metrics = evaluate(model, test_loader, device, args.failure_threshold)

    print(f"\n测试集结果:")
    print(f"  MAE:  {test_metrics['mae']:.2f}%")
    print(f"  RMSE: {test_metrics['rmse']:.2f}%")
    print(f"  R²:   {test_metrics['r2']:.4f}")
    print(f"\n失败反应识别 (yield<{args.failure_threshold}%):")
    print(f"  TP: {test_metrics['tp']}, FP: {test_metrics['fp']}, FN: {test_metrics['fn']}, TN: {test_metrics['tn']}")
    print(f"  Precision: {test_metrics['failed_precision']:.3f}")
    print(f"  Recall:    {test_metrics['failed_recall']:.3f}")
    print(f"  F1 Score:  {test_metrics['failed_f1']:.3f}")

    # 保存结果
    results = {
        'model': 'MultiTaskYieldModel',
        'test_metrics': test_metrics,
        'best_epoch': checkpoint['epoch'],
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")


if __name__ == "__main__":
    main()
