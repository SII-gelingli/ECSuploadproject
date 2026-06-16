"""
条件推荐模型训练脚本

给定反应物和产物，推荐最优的反应条件：
- 阳极材料 (anode)
- 阴极材料 (cathode)
- 电解池类型 (cell_type)
- 电解质 (electrolyte)
- 溶剂 (solvent)
- 试剂 (reagent)
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


class ConditionRecommenderXTB(nn.Module):
    """条件推荐模型：指纹 + xTB特征"""

    def __init__(
        self,
        fp_dim: int = 6144,      # 3 * 2048 (reactant + product + diff)
        xtb_dim: int = 33,       # 3 * 11 (reactant + product + diff)
        hidden_dim: int = 256,
        num_anode: int = 19,     # 与原始模型一致
        num_cathode: int = 19,   # 与原始模型一致
        num_cell_type: int = 6,  # 与原始模型一致
        num_electrolyte: int = 101,
        num_solvent: int = 101,
        num_reagent: int = 201,
        num_catalyst: int = 101,
        dropout: float = 0.3
    ):
        super().__init__()

        # 指纹编码器
        self.fp_encoder = nn.Sequential(
            nn.Linear(fp_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
        )

        # xTB编码器
        self.xtb_encoder = nn.Sequential(
            nn.Linear(xtb_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
        )

        # 融合层
        fused_dim = hidden_dim + 64
        self.fusion = nn.Sequential(
            nn.Linear(fused_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # 预测头
        self.anode_head = nn.Linear(hidden_dim, num_anode)
        self.cathode_head = nn.Linear(hidden_dim, num_cathode)
        self.cell_type_head = nn.Linear(hidden_dim, num_cell_type)
        self.electrolyte_head = nn.Linear(hidden_dim, num_electrolyte)
        self.solvent_head = nn.Linear(hidden_dim, num_solvent)
        self.reagent_head = nn.Linear(hidden_dim, num_reagent)
        self.catalyst_head = nn.Linear(hidden_dim, num_catalyst)  # 新增：催化剂预测头

    def forward(self, fp_features, xtb_features):
        fp_h = self.fp_encoder(fp_features)
        xtb_h = self.xtb_encoder(xtb_features)

        combined = torch.cat([fp_h, xtb_h], dim=-1)
        h = self.fusion(combined)

        return {
            'anode': self.anode_head(h),
            'cathode': self.cathode_head(h),
            'cell_type': self.cell_type_head(h),
            'electrolyte': self.electrolyte_head(h),
            'solvent': self.solvent_head(h),
            'reagent': self.reagent_head(h),
            'catalyst': self.catalyst_head(h),  # 新增
        }


class ConditionDataset(Dataset):
    """条件推荐数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 反应指纹 (只用反应物、产物、差异)
        fp_features = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp']
        )

        # xTB特征 (反应物、产物、差异)
        xtb_features = (
            item['reactant_xtb'] +
            item['product_xtb'] +
            item['reaction_diff_xtb']
        )

        # 条件标签 (包含催化剂)
        labels = {
            'anode': item['anode'],
            'cathode': item['cathode'],
            'cell_type': item['cell_type'],
            'electrolyte': item['electrolyte_label'],
            'solvent': item['solvent_label'],
            'reagent': item['reagent_label'],
            'catalyst': item.get('catalyst_label', 0),  # 新增：催化剂标签
        }

        return (
            torch.tensor(fp_features, dtype=torch.float32),
            torch.tensor(xtb_features, dtype=torch.float32),
            labels
        )


def collate_fn(batch):
    fps = torch.stack([b[0] for b in batch])
    xtbs = torch.stack([b[1] for b in batch])

    labels = {
        'anode': torch.tensor([b[2]['anode'] for b in batch], dtype=torch.long),
        'cathode': torch.tensor([b[2]['cathode'] for b in batch], dtype=torch.long),
        'cell_type': torch.tensor([b[2]['cell_type'] for b in batch], dtype=torch.long),
        'electrolyte': torch.tensor([b[2]['electrolyte'] for b in batch], dtype=torch.long),
        'solvent': torch.tensor([b[2]['solvent'] for b in batch], dtype=torch.long),
        'reagent': torch.tensor([b[2]['reagent'] for b in batch], dtype=torch.long),
        'catalyst': torch.tensor([b[2]['catalyst'] for b in batch], dtype=torch.long),  # 新增
    }

    return fps, xtbs, labels


def train_epoch(model, loader, optimizer, device, condition_weights=None):
    model.train()
    total_loss = 0
    correct = {k: 0 for k in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']}
    total = 0

    criterion = nn.CrossEntropyLoss()

    for fps, xtbs, labels in tqdm(loader, desc="Training", leave=False):
        fps = fps.to(device)
        xtbs = xtbs.to(device)
        labels = {k: v.to(device) for k, v in labels.items()}

        optimizer.zero_grad()
        preds = model(fps, xtbs)

        # 计算每个条件的损失
        loss = 0
        weights = condition_weights or {k: 1.0 for k in preds.keys()}
        for key in preds.keys():
            loss += weights[key] * criterion(preds[key], labels[key])

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        # 计算准确率
        batch_size = fps.size(0)
        total += batch_size
        for key in preds.keys():
            pred_labels = preds[key].argmax(dim=-1)
            correct[key] += (pred_labels == labels[key]).sum().item()

    acc = {k: v / total * 100 for k, v in correct.items()}
    return total_loss / len(loader), acc


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    total_loss = 0
    correct = {k: 0 for k in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']}
    top3_correct = {k: 0 for k in correct.keys()}
    total = 0

    criterion = nn.CrossEntropyLoss()

    for fps, xtbs, labels in loader:
        fps = fps.to(device)
        xtbs = xtbs.to(device)
        labels = {k: v.to(device) for k, v in labels.items()}

        preds = model(fps, xtbs)

        loss = 0
        for key in preds.keys():
            loss += criterion(preds[key], labels[key])

        total_loss += loss.item()

        batch_size = fps.size(0)
        total += batch_size

        for key in preds.keys():
            # Top-1 准确率
            pred_labels = preds[key].argmax(dim=-1)
            correct[key] += (pred_labels == labels[key]).sum().item()

            # Top-3 准确率
            _, top3_preds = preds[key].topk(3, dim=-1)
            for i in range(batch_size):
                if labels[key][i] in top3_preds[i]:
                    top3_correct[key] += 1

    acc = {k: v / total * 100 for k, v in correct.items()}
    top3_acc = {k: v / total * 100 for k, v in top3_correct.items()}

    return {
        'loss': total_loss / len(loader),
        'acc': acc,
        'top3_acc': top3_acc,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=None)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=20)
    parser.add_argument('--hidden_dim', type=int, default=256)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--use_catalyst', action='store_true', help='使用带催化剂的数据集')
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Using device: {device}")

    # 设置输出目录
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        if args.use_catalyst:
            output_dir = project_root / 'checkpoints' / 'condition_recommender_cat'
        else:
            output_dir = project_root / 'checkpoints' / 'condition_recommender_xtb'
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    data_dir = Path(args.data_dir)

    # 加载数据 (根据是否使用催化剂选择数据文件)
    print("\n加载数据...")
    if args.use_catalyst:
        print("  使用带催化剂的数据集 (*_xtb_cat.pt)")
        train_dataset = ConditionDataset(data_dir / 'train_xtb_cat.pt')
        val_dataset = ConditionDataset(data_dir / 'val_xtb_cat.pt')
        test_dataset = ConditionDataset(data_dir / 'test_xtb_cat.pt')
    else:
        print("  使用原始数据集 (*_xtb.pt)")
        train_dataset = ConditionDataset(data_dir / 'train_xtb.pt')
        val_dataset = ConditionDataset(data_dir / 'val_xtb.pt')
        test_dataset = ConditionDataset(data_dir / 'test_xtb.pt')

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    train_loader = DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=True,
        collate_fn=collate_fn, num_workers=4, pin_memory=True
    )
    val_loader = DataLoader(
        val_dataset, batch_size=args.batch_size * 2, shuffle=False,
        collate_fn=collate_fn, num_workers=4
    )
    test_loader = DataLoader(
        test_dataset, batch_size=args.batch_size * 2, shuffle=False,
        collate_fn=collate_fn, num_workers=4
    )

    # 加载词汇表大小
    vocab_path = data_dir / 'vocab.json'
    if vocab_path.exists():
        with open(vocab_path) as f:
            vocab = json.load(f)
        num_electrolyte = len(vocab.get('electrolyte', {})) + 1  # +1 for UNK
        num_solvent = len(vocab.get('solvent', {})) + 1
        num_reagent = len(vocab.get('reagent', {})) + 1
        num_catalyst = len(vocab.get('catalyst', {})) + 1
        print(f"\n从vocab.json加载类别数:")
        print(f"  electrolyte: {num_electrolyte}, solvent: {num_solvent}")
        print(f"  reagent: {num_reagent}, catalyst: {num_catalyst}")
    else:
        num_electrolyte, num_solvent, num_reagent, num_catalyst = 101, 101, 201, 101

    # 创建模型
    model = ConditionRecommenderXTB(
        fp_dim=6144,
        xtb_dim=33,
        hidden_dim=args.hidden_dim,
        dropout=args.dropout,
        num_electrolyte=num_electrolyte,
        num_solvent=num_solvent,
        num_reagent=num_reagent,
        num_catalyst=num_catalyst,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs, eta_min=1e-6)

    # 训练
    print("\n" + "=" * 70)
    print("开始训练条件推荐模型")
    print("=" * 70)

    best_val_acc = 0
    patience_counter = 0
    history = {'train_loss': [], 'val_loss': [], 'val_acc': [], 'val_top3_acc': []}

    start_time = datetime.now()

    for epoch in range(args.epochs):
        train_loss, train_acc = train_epoch(model, train_loader, optimizer, device)
        val_metrics = evaluate(model, val_loader, device)

        scheduler.step()
        current_lr = optimizer.param_groups[0]['lr']

        # 计算平均准确率
        avg_train_acc = sum(train_acc.values()) / len(train_acc)
        avg_val_acc = sum(val_metrics['acc'].values()) / len(val_metrics['acc'])
        avg_val_top3 = sum(val_metrics['top3_acc'].values()) / len(val_metrics['top3_acc'])

        history['train_loss'].append(train_loss)
        history['val_loss'].append(val_metrics['loss'])
        history['val_acc'].append(val_metrics['acc'])
        history['val_top3_acc'].append(val_metrics['top3_acc'])

        improved = ""
        if avg_val_acc > best_val_acc:
            best_val_acc = avg_val_acc
            patience_counter = 0
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'val_acc': val_metrics['acc'],
                'val_top3_acc': val_metrics['top3_acc'],
                'args': vars(args),
            }, output_dir / 'best_model.pt')
            improved = " * BEST"
        else:
            patience_counter += 1

        print(f"Epoch {epoch+1:3d} | "
              f"Train Loss: {train_loss:.4f}, Acc: {avg_train_acc:.1f}% | "
              f"Val Acc: {avg_val_acc:.1f}%, Top3: {avg_val_top3:.1f}% | "
              f"LR: {current_lr:.2e}{improved}")

        if patience_counter >= args.patience:
            print(f"\n早停: {args.patience} epochs 无改善")
            break

    elapsed = datetime.now() - start_time
    print(f"\n训练完成，耗时: {elapsed}")

    # 测试
    print("\n" + "=" * 70)
    print("在测试集上评估最佳模型")
    print("=" * 70)

    checkpoint = torch.load(output_dir / 'best_model.pt', weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])

    test_metrics = evaluate(model, test_loader, device)

    print("\nTest Accuracy (Top-1 / Top-3):")
    for key in test_metrics['acc'].keys():
        print(f"  {key:15s}: {test_metrics['acc'][key]:5.1f}% / {test_metrics['top3_acc'][key]:5.1f}%")

    avg_test_acc = sum(test_metrics['acc'].values()) / len(test_metrics['acc'])
    avg_test_top3 = sum(test_metrics['top3_acc'].values()) / len(test_metrics['top3_acc'])
    print(f"\n  Average:        {avg_test_acc:.1f}% / {avg_test_top3:.1f}%")

    # 保存结果
    model_name = 'ConditionRecommenderXTB+Catalyst' if args.use_catalyst else 'ConditionRecommenderXTB'
    results = {
        'model': model_name,
        'best_epoch': checkpoint['epoch'],
        'test_acc': test_metrics['acc'],
        'test_top3_acc': test_metrics['top3_acc'],
        'avg_test_acc': avg_test_acc,
        'avg_test_top3_acc': avg_test_top3,
        'num_params': num_params,
        'training_time': str(elapsed),
        'use_catalyst': args.use_catalyst,
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")

    return results


if __name__ == "__main__":
    main()
