"""
训练脚本：Categorical CVAE 条件推荐模型 (使用预处理数据)

使用 *_xtb_cat.pt 预处理数据文件训练CVAE模型，包含催化剂预测。

用法:
    python scripts/train_cvae_cat.py
    python scripts/train_cvae_cat.py --epochs 100 --device cuda
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

from models.condition_cvae import CategoricalCVAE


class CVAEDataset(Dataset):
    """CVAE条件推荐数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 反应指纹 (反应物 + 产物 + 差异 = 6144D)
        fp_features = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp']
        )

        # xTB特征 (反应物 + 产物 + 差异 = 33D)
        xtb_features = (
            item['reactant_xtb'] +
            item['product_xtb'] +
            item['reaction_diff_xtb']
        )

        # 合并为reaction_fp (6144 + 33 = 6177D)
        reaction_fp = fp_features + xtb_features

        # 条件标签
        labels = {
            'anode': item['anode'],
            'cathode': item['cathode'],
            'cell_type': item['cell_type'],
            'electrolyte': item['electrolyte_label'],
            'solvent': item['solvent_label'],
            'reagent': item['reagent_label'],
            'catalyst': item.get('catalyst_label', 0),
        }

        return torch.tensor(reaction_fp, dtype=torch.float32), labels


def collate_fn(batch):
    fps = torch.stack([b[0] for b in batch])
    labels = {
        'anode': torch.tensor([b[1]['anode'] for b in batch], dtype=torch.long),
        'cathode': torch.tensor([b[1]['cathode'] for b in batch], dtype=torch.long),
        'cell_type': torch.tensor([b[1]['cell_type'] for b in batch], dtype=torch.long),
        'electrolyte': torch.tensor([b[1]['electrolyte'] for b in batch], dtype=torch.long),
        'solvent': torch.tensor([b[1]['solvent'] for b in batch], dtype=torch.long),
        'reagent': torch.tensor([b[1]['reagent'] for b in batch], dtype=torch.long),
        'catalyst': torch.tensor([b[1]['catalyst'] for b in batch], dtype=torch.long),
    }
    return fps, labels


class KLAnnealingScheduler:
    """β warmup 调度器"""
    def __init__(self, warmup_epochs: int = 20, beta_max: float = 0.1):
        self.warmup_epochs = warmup_epochs
        self.beta_max = beta_max

    def get_beta(self, epoch: int) -> float:
        if epoch >= self.warmup_epochs:
            return self.beta_max
        return self.beta_max * (epoch / self.warmup_epochs)


CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']


def compute_loss(model, predictions, labels, mu, logvar, beta, device):
    """计算 CVAE 损失: L = Σ CE_i + β × KL"""
    ce_loss = nn.CrossEntropyLoss()

    recon_loss = torch.tensor(0.0, device=device)
    for key in CONDITION_KEYS:
        logits = predictions[f'{key}_logits']
        recon_loss = recon_loss + ce_loss(logits, labels[key])

    # KL 散度
    kl_loss = -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp())

    total_loss = recon_loss + beta * kl_loss
    return total_loss, recon_loss, kl_loss


def train_epoch(model, loader, optimizer, device, beta):
    model.train()
    total_loss = 0.0
    total_recon = 0.0
    total_kl = 0.0
    correct = {k: 0 for k in CONDITION_KEYS}
    total = 0

    for fps, labels in tqdm(loader, desc="Training", leave=False):
        fps = fps.to(device)
        labels = {k: v.to(device) for k, v in labels.items()}

        optimizer.zero_grad()

        # 前向传播 (训练模式需要所有条件标签)
        predictions, mu, logvar = model(
            fps,
            labels['anode'],
            labels['cathode'],
            labels['cell_type'],
            labels['electrolyte'],
            labels['solvent'],
            labels['reagent'],
            labels['catalyst'],
        )

        loss, recon_loss, kl_loss = compute_loss(
            model, predictions, labels, mu, logvar, beta, device
        )

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
        optimizer.step()

        total_loss += loss.item()
        total_recon += recon_loss.item()
        total_kl += kl_loss.item()

        # 计算准确率
        batch_size = fps.size(0)
        total += batch_size
        for key in CONDITION_KEYS:
            pred_labels = predictions[f'{key}_logits'].argmax(dim=-1)
            correct[key] += (pred_labels == labels[key]).sum().item()

    n = len(loader)
    acc = {k: v / total * 100 for k, v in correct.items()}
    return {
        'total': total_loss / n,
        'recon': total_recon / n,
        'kl': total_kl / n,
        'acc': acc,
    }


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct = {k: 0 for k in CONDITION_KEYS}
    top3_correct = {k: 0 for k in CONDITION_KEYS}
    total = 0

    for fps, labels in loader:
        fps = fps.to(device)
        labels = {k: v.to(device) for k, v in labels.items()}

        # z=0 确定性预测
        predictions = model.recommend(fps)

        batch_size = fps.size(0)
        total += batch_size

        for key in CONDITION_KEYS:
            logits = predictions[f'{key}_logits']
            # Top-1
            pred_labels = logits.argmax(dim=-1)
            correct[key] += (pred_labels == labels[key]).sum().item()
            # Top-3
            _, top3_preds = logits.topk(min(3, logits.size(-1)), dim=-1)
            for i in range(batch_size):
                if labels[key][i] in top3_preds[i]:
                    top3_correct[key] += 1

    acc = {k: v / total * 100 for k, v in correct.items()}
    top3_acc = {k: v / total * 100 for k, v in top3_correct.items()}
    return {'acc': acc, 'top3_acc': top3_acc}


def main():
    parser = argparse.ArgumentParser(description='训练 CVAE 条件推荐模型')
    parser.add_argument('--data_dir', type=str, default='data', help='数据目录')
    parser.add_argument('--output_dir', type=str, default='checkpoints/cvae_cat', help='输出目录')
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--warmup_epochs', type=int, default=20)
    parser.add_argument('--beta_max', type=float, default=0.1)
    parser.add_argument('--patience', type=int, default=20)
    parser.add_argument('--hidden_dim', type=int, default=256)
    parser.add_argument('--latent_dim', type=int, default=64)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    device = args.device
    print(f"Using device: {device}")

    # 创建输出目录
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载数据
    print("\n加载数据...")
    data_dir = Path(args.data_dir)

    train_dataset = CVAEDataset(data_dir / "train_xtb_cat.pt")
    val_dataset = CVAEDataset(data_dir / "val_xtb_cat.pt")
    test_dataset = CVAEDataset(data_dir / "test_xtb_cat.pt")

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)

    # 从vocab.json加载类别数
    vocab_path = data_dir / "vocab.json"
    with open(vocab_path) as f:
        vocab = json.load(f)

    num_electrolyte = len(vocab['electrolyte']) + 1
    num_solvent = len(vocab['solvent']) + 1
    num_reagent = len(vocab['reagent']) + 1
    num_catalyst = len(vocab['catalyst']) + 1

    print(f"\n从vocab.json加载类别数:")
    print(f"  electrolyte: {num_electrolyte}, solvent: {num_solvent}")
    print(f"  reagent: {num_reagent}, catalyst: {num_catalyst}")

    # 创建模型
    reaction_dim = 6144 + 33  # fp + xtb
    model = CategoricalCVAE(
        reaction_dim=reaction_dim,
        repr_dim=args.hidden_dim,
        latent_dim=args.latent_dim,
        num_anode_materials=19,
        num_cathode_materials=19,
        num_cell_types=6,
        num_electrolytes=num_electrolyte,
        num_solvents=num_solvent,
        num_reagents=num_reagent,
        num_catalysts=num_catalyst,
        dropout=args.dropout,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"\n模型参数量: {num_params:,}")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    kl_scheduler = KLAnnealingScheduler(warmup_epochs=args.warmup_epochs, beta_max=args.beta_max)

    # 训练
    print("\n" + "=" * 70)
    print("开始训练 CVAE 条件推荐模型")
    print("=" * 70)

    best_val_acc = 0
    patience_counter = 0
    start_time = datetime.now()

    for epoch in range(1, args.epochs + 1):
        beta = kl_scheduler.get_beta(epoch)

        train_result = train_epoch(model, train_loader, optimizer, device, beta)
        val_result = evaluate(model, val_loader, device)
        scheduler.step()

        avg_val_acc = sum(val_result['acc'].values()) / len(CONDITION_KEYS)
        avg_val_top3 = sum(val_result['top3_acc'].values()) / len(CONDITION_KEYS)
        lr = optimizer.param_groups[0]['lr']

        is_best = avg_val_acc > best_val_acc
        if is_best:
            best_val_acc = avg_val_acc
            patience_counter = 0
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'accuracy': val_result,
                'avg_accuracy': avg_val_acc,
                'num_classes': model.num_classes,
            }, output_dir / "best_model.pt")
        else:
            patience_counter += 1

        mark = " * BEST" if is_best else ""
        print(f"Epoch {epoch:3d} | Loss: {train_result['total']:.4f} (recon={train_result['recon']:.4f}, kl={train_result['kl']:.4f}) | "
              f"Val Acc: {avg_val_acc:.1f}%, Top3: {avg_val_top3:.1f}% | β={beta:.3f} | LR: {lr:.2e}{mark}")

        if patience_counter >= args.patience:
            print(f"\nEarly stopping at epoch {epoch}")
            break

    training_time = datetime.now() - start_time

    # 测试
    print("\n" + "=" * 70)
    print("测试最佳模型")
    print("=" * 70)

    checkpoint = torch.load(output_dir / "best_model.pt", map_location=device, weights_only=False)
    model.load_state_dict(checkpoint['model_state_dict'])
    test_result = evaluate(model, test_loader, device)

    print("\n测试集结果 (Top-1 / Top-3):")
    for key in CONDITION_KEYS:
        print(f"  {key:12s}: {test_result['acc'][key]:6.2f}% / {test_result['top3_acc'][key]:6.2f}%")

    avg_test_acc = sum(test_result['acc'].values()) / len(CONDITION_KEYS)
    avg_test_top3 = sum(test_result['top3_acc'].values()) / len(CONDITION_KEYS)
    print(f"\n  平均: {avg_test_acc:.2f}% / {avg_test_top3:.2f}%")

    # 保存结果
    results = {
        "model": "CategoricalCVAE+Catalyst",
        "best_epoch": checkpoint['epoch'],
        "test_acc": test_result['acc'],
        "test_top3_acc": test_result['top3_acc'],
        "avg_test_acc": avg_test_acc,
        "avg_test_top3_acc": avg_test_top3,
        "num_params": num_params,
        "training_time": str(training_time),
        "args": vars(args),
    }
    with open(output_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n训练完成! 用时: {training_time}")
    print(f"最佳模型保存至: {output_dir / 'best_model.pt'}")


if __name__ == "__main__":
    main()
