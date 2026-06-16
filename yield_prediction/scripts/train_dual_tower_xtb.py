"""
双塔xTB融合模型训练脚本

目标：利用xTB特征超越MLP基线 (MAE 12.75%)

模型结构：
- 指纹塔：压缩10246维Morgan指纹
- xTB塔：增强55维量子化学特征
- 门控融合：自适应融合两类特征
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
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.architectures import DualTowerXTBPredictor


class XTBEnhancedDataset(Dataset):
    """带xTB特征的数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 指纹特征 (10246维)
        fp_features = (
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

        # 合并特征
        features = fp_features + xtb_features

        return (
            torch.tensor(features, dtype=torch.float32),
            torch.tensor(item['yield'] / 100.0, dtype=torch.float32)
        )


def train_epoch(model, loader, optimizer, criterion, device, grad_clip=1.0):
    model.train()
    total_loss = 0
    total_mae = 0
    n_batches = 0

    for features, labels in tqdm(loader, desc="Training", leave=False):
        features = features.to(device)
        labels = labels.to(device).unsqueeze(1)

        optimizer.zero_grad()
        pred = model(features)
        loss = criterion(pred, labels)
        loss.backward()

        if grad_clip > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=grad_clip)

        optimizer.step()

        total_loss += loss.item()
        total_mae += (pred - labels).abs().mean().item() * 100
        n_batches += 1

    return total_loss / n_batches, total_mae / n_batches


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    all_preds = []
    all_labels = []
    n_batches = 0

    for features, labels in loader:
        features = features.to(device)
        labels = labels.to(device).unsqueeze(1)

        pred = model(features)
        total_loss += criterion(pred, labels).item()

        all_preds.extend((pred.cpu().flatten() * 100).tolist())
        all_labels.extend((labels.cpu().flatten() * 100).tolist())
        n_batches += 1

    # 计算指标
    preds = torch.tensor(all_preds)
    labels = torch.tensor(all_labels)
    mae = torch.mean(torch.abs(preds - labels)).item()
    rmse = torch.sqrt(torch.mean((preds - labels) ** 2)).item()
    ss_res = torch.sum((preds - labels) ** 2)
    ss_tot = torch.sum((labels - labels.mean()) ** 2)
    r2 = (1 - ss_res / ss_tot).item()

    return {
        'loss': total_loss / n_batches,
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'predictions': all_preds,
        'labels': all_labels,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'dual_tower_xtb'))
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=15)
    parser.add_argument('--fp_hidden', type=int, default=256)
    parser.add_argument('--xtb_hidden', type=int, default=64)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--grad_clip', type=float, default=1.0)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    # 设置
    device = torch.device(args.device)
    print(f"Using device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n加载数据...")
    train_dataset = XTBEnhancedDataset(data_dir / 'train_xtb.pt')
    val_dataset = XTBEnhancedDataset(data_dir / 'val_xtb.pt')
    test_dataset = XTBEnhancedDataset(data_dir / 'test_xtb.pt')

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    # DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=4,
        pin_memory=True if args.device == 'cuda' else False,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        num_workers=4,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        num_workers=4,
    )

    # 创建模型
    fp_dim = 10246  # 5*2048 + 6
    xtb_dim = 55    # 5*11

    model = DualTowerXTBPredictor(
        input_dim=fp_dim + xtb_dim,  # 总输入维度
        fp_dim=fp_dim,
        xtb_dim=xtb_dim,
        fp_hidden=args.fp_hidden,
        xtb_hidden=args.xtb_hidden,
        dropout=args.dropout,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

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
    print("开始训练 DualTower XTB (目标: 超越 MLP MAE 12.75%)")
    print("=" * 70)

    best_val_mae = float('inf')
    patience_counter = 0

    history = {
        'train_loss': [], 'train_mae': [],
        'val_loss': [], 'val_mae': [], 'val_rmse': [], 'val_r2': [],
    }

    start_time = datetime.now()

    for epoch in range(args.epochs):
        train_loss, train_mae = train_epoch(
            model, train_loader, optimizer, criterion, device, args.grad_clip
        )
        val_metrics = evaluate(model, val_loader, criterion, device)

        scheduler.step()
        current_lr = optimizer.param_groups[0]['lr']

        history['train_loss'].append(train_loss)
        history['train_mae'].append(train_mae)
        history['val_loss'].append(val_metrics['loss'])
        history['val_mae'].append(val_metrics['mae'])
        history['val_rmse'].append(val_metrics['rmse'])
        history['val_r2'].append(val_metrics['r2'])

        improved = ""
        if val_metrics['mae'] < best_val_mae:
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
            }, output_dir / 'best_model.pt')
            improved = " * BEST"
        else:
            patience_counter += 1

        print(f"Epoch {epoch+1:3d} | "
              f"Train Loss: {train_loss:.4f}, MAE: {train_mae:.2f}% | "
              f"Val MAE: {val_metrics['mae']:.2f}%, RMSE: {val_metrics['rmse']:.2f}, R²: {val_metrics['r2']:.3f} | "
              f"LR: {current_lr:.2e}{improved}")

        if patience_counter >= args.patience:
            print(f"\n早停: {args.patience} epochs 无改善")
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
    mlp_mae = 12.75
    resnet_mae = 12.62
    improvement_mlp = mlp_mae - test_metrics['mae']
    improvement_resnet = resnet_mae - test_metrics['mae']

    if improvement_resnet > 0:
        print(f"\n超越所有基线!")
        print(f"  vs MLP: +{improvement_mlp:.2f}% MAE")
        print(f"  vs ResNet: +{improvement_resnet:.2f}% MAE")
    elif improvement_mlp > 0:
        print(f"\n超越MLP基线! +{improvement_mlp:.2f}% MAE")
        print(f"  距离ResNet最佳还差: {-improvement_resnet:.2f}% MAE")
    else:
        print(f"\n未超越基线，差距: MLP {-improvement_mlp:.2f}%, ResNet {-improvement_resnet:.2f}%")

    # 保存结果
    results = {
        'model': 'DualTowerXTB',
        'best_epoch': checkpoint['epoch'],
        'best_val_mae': best_val_mae,
        'test_mae': test_metrics['mae'],
        'test_rmse': test_metrics['rmse'],
        'test_r2': test_metrics['r2'],
        'num_params': num_params,
        'mlp_baseline_mae': mlp_mae,
        'resnet_baseline_mae': resnet_mae,
        'improvement_over_mlp': improvement_mlp,
        'improvement_over_resnet': improvement_resnet,
        'training_time': str(elapsed),
        'args': vars(args),
        'history': history,
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    # 保存预测结果
    test_predictions = {
        'predictions': test_metrics['predictions'],
        'labels': test_metrics['labels'],
    }
    with open(output_dir / 'test_predictions.json', 'w') as f:
        json.dump(test_predictions, f)

    print(f"\n结果已保存到: {output_dir}")

    return results


if __name__ == "__main__":
    main()
