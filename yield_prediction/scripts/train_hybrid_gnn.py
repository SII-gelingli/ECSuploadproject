"""
Hybrid GNN 训练脚本

目标：超越MLP基线 (MAE 12.36)

特点：
1. GNN学习局部分子结构
2. xTB提供全局量子化学特征
3. 反应变化Transformer建模
4. 多尺度特征融合
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
import numpy as np

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.hybrid_gnn import HybridGNNYieldPredictor


class HybridDataset(Dataset):
    """Hybrid GNN 数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def collate_fn_hybrid(batch):
    """Hybrid GNN 数据整理函数"""

    def merge_graphs(graphs):
        all_nodes = []
        all_edges = []
        all_edge_feats = []
        batch_idx = []
        node_offset = 0

        for i, g in enumerate(graphs):
            nodes = g['node_feats']
            edges = g['edge_index']
            edge_feats = g['edge_feats']

            all_nodes.append(nodes)
            if edges.shape[1] > 0:
                all_edges.append(edges + node_offset)
                all_edge_feats.append(edge_feats)
            batch_idx.extend([i] * nodes.shape[0])
            node_offset += nodes.shape[0]

        return {
            'node_feats': torch.cat(all_nodes, dim=0),
            'edge_index': torch.cat(all_edges, dim=1) if all_edges else torch.zeros(2, 0, dtype=torch.long),
            'edge_feats': torch.cat(all_edge_feats, dim=0) if all_edge_feats else torch.zeros(0, 10),
            'batch': torch.tensor(batch_idx, dtype=torch.long),
            'num_graphs': len(graphs),
        }

    # 图数据
    reactant_graphs = merge_graphs([d['reactant_graph'] for d in batch])
    product_graphs = merge_graphs([d['product_graph'] for d in batch])
    solvent_graphs = merge_graphs([d['solvent_graph'] for d in batch])
    electrolyte_graphs = merge_graphs([d['electrolyte_graph'] for d in batch])

    # xTB特征
    reactant_xtb = torch.stack([d['reactant_xtb'] for d in batch])
    product_xtb = torch.stack([d['product_xtb'] for d in batch])
    solvent_xtb = torch.stack([d['solvent_xtb'] for d in batch])
    electrolyte_xtb = torch.stack([d['electrolyte_xtb'] for d in batch])

    # 分类特征
    anode_ids = torch.tensor([d['anode_id'] for d in batch], dtype=torch.long)
    cathode_ids = torch.tensor([d['cathode_id'] for d in batch], dtype=torch.long)
    cell_type_ids = torch.tensor([d['cell_type_id'] for d in batch], dtype=torch.long)

    # 连续特征
    currents = torch.tensor([d['current_normalized'] for d in batch], dtype=torch.float32).unsqueeze(-1)

    # 标签
    yields = torch.tensor([d['yield'] for d in batch], dtype=torch.float32).unsqueeze(-1) / 100.0

    return {
        'reactant_graph': reactant_graphs,
        'product_graph': product_graphs,
        'solvent_graph': solvent_graphs,
        'electrolyte_graph': electrolyte_graphs,
        'reactant_xtb': reactant_xtb,
        'product_xtb': product_xtb,
        'solvent_xtb': solvent_xtb,
        'electrolyte_xtb': electrolyte_xtb,
        'anode_id': anode_ids,
        'cathode_id': cathode_ids,
        'cell_type_id': cell_type_ids,
        'current': currents,
        'yield': yields,
    }


def move_to_device(data, device):
    """递归移动数据到设备"""
    if isinstance(data, torch.Tensor):
        return data.to(device)
    elif isinstance(data, dict):
        return {k: move_to_device(v, device) for k, v in data.items()}
    else:
        return data


def train_epoch(model, loader, optimizer, criterion, device, grad_clip=1.0):
    model.train()
    total_loss = 0
    total_mae = 0
    n_batches = 0

    for batch in tqdm(loader, desc="Training", leave=False):
        batch = move_to_device(batch, device)

        optimizer.zero_grad()
        pred = model(
            reactant_graph=batch['reactant_graph'],
            product_graph=batch['product_graph'],
            solvent_graph=batch['solvent_graph'],
            electrolyte_graph=batch['electrolyte_graph'],
            anode_id=batch['anode_id'],
            cathode_id=batch['cathode_id'],
            cell_type_id=batch['cell_type_id'],
            current=batch['current'],
            reactant_xtb=batch['reactant_xtb'],
            product_xtb=batch['product_xtb'],
            solvent_xtb=batch['solvent_xtb'],
            electrolyte_xtb=batch['electrolyte_xtb'],
        )

        loss = criterion(pred, batch['yield'])
        loss.backward()

        if grad_clip > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=grad_clip)

        optimizer.step()

        total_loss += loss.item()
        total_mae += (pred - batch['yield']).abs().mean().item() * 100
        n_batches += 1

    return total_loss / n_batches, total_mae / n_batches


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    total_mae = 0
    all_preds = []
    all_labels = []
    n_batches = 0

    for batch in loader:
        batch = move_to_device(batch, device)

        pred = model(
            reactant_graph=batch['reactant_graph'],
            product_graph=batch['product_graph'],
            solvent_graph=batch['solvent_graph'],
            electrolyte_graph=batch['electrolyte_graph'],
            anode_id=batch['anode_id'],
            cathode_id=batch['cathode_id'],
            cell_type_id=batch['cell_type_id'],
            current=batch['current'],
            reactant_xtb=batch['reactant_xtb'],
            product_xtb=batch['product_xtb'],
            solvent_xtb=batch['solvent_xtb'],
            electrolyte_xtb=batch['electrolyte_xtb'],
        )

        total_loss += criterion(pred, batch['yield']).item()
        total_mae += (pred - batch['yield']).abs().mean().item() * 100
        all_preds.extend((pred.cpu().flatten() * 100).tolist())
        all_labels.extend((batch['yield'].cpu().flatten() * 100).tolist())
        n_batches += 1

    # 计算额外指标 (使用torch避免numpy)
    preds = torch.tensor(all_preds)
    labels = torch.tensor(all_labels)
    rmse = torch.sqrt(torch.mean((preds - labels) ** 2)).item()
    ss_res = torch.sum((preds - labels) ** 2)
    ss_tot = torch.sum((labels - labels.mean()) ** 2)
    r2 = (1 - ss_res / ss_tot).item()

    return {
        'loss': total_loss / n_batches,
        'mae': total_mae / n_batches,
        'rmse': rmse,
        'r2': r2,
        'predictions': all_preds,
        'labels': all_labels,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'hybrid_gnn'))
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=150)
    parser.add_argument('--patience', type=int, default=30)
    parser.add_argument('--gnn_hidden', type=int, default=128)
    parser.add_argument('--gnn_layers', type=int, default=4)
    parser.add_argument('--gnn_heads', type=int, default=4)
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
    print("\n加载 Hybrid GNN 数据...")
    train_dataset = HybridDataset(data_dir / 'train_hybrid.pt')
    val_dataset = HybridDataset(data_dir / 'val_hybrid.pt')
    test_dataset = HybridDataset(data_dir / 'test_hybrid.pt')

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    # 加载统计信息
    with open(data_dir / 'stats_hybrid.json', 'r') as f:
        stats = json.load(f)

    # DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        collate_fn=collate_fn_hybrid,
        num_workers=0,
        pin_memory=True if args.device == 'cuda' else False,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        collate_fn=collate_fn_hybrid,
        num_workers=0,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=args.batch_size * 2,
        shuffle=False,
        collate_fn=collate_fn_hybrid,
        num_workers=0,
    )

    # 创建模型
    model = HybridGNNYieldPredictor(
        atom_feat_dim=stats['atom_feat_dim'],
        edge_feat_dim=stats['bond_feat_dim'],
        xtb_feat_dim=stats['xtb_feat_dim'],
        gnn_hidden_dim=args.gnn_hidden,
        gnn_num_layers=args.gnn_layers,
        gnn_num_heads=args.gnn_heads,
        num_electrode_types=stats['num_electrode_types'],
        num_cell_types=stats['num_cell_types'],
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

    scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(
        optimizer, T_0=20, T_mult=2, eta_min=1e-6
    )

    criterion = nn.MSELoss()

    # 训练
    print("\n" + "=" * 70)
    print("开始训练 Hybrid GNN (目标: 超越 MLP MAE 12.36)")
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
                'stats': stats,
                'args': vars(args),
            }, output_dir / 'best_model.pt')
            improved = " * BEST"
        else:
            patience_counter += 1

        if (epoch + 1) % 5 == 0 or improved:
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

    checkpoint = torch.load(output_dir / 'best_model.pt')
    model.load_state_dict(checkpoint['model_state_dict'])

    test_metrics = evaluate(model, test_loader, criterion, device)

    print(f"Test MAE:  {test_metrics['mae']:.2f}%")
    print(f"Test RMSE: {test_metrics['rmse']:.2f}")
    print(f"Test R²:   {test_metrics['r2']:.4f}")

    # 与MLP基线比较
    mlp_mae = 12.36
    improvement = mlp_mae - test_metrics['mae']
    if improvement > 0:
        print(f"\n🎉 超越MLP基线! 改进: {improvement:.2f}% MAE")
    else:
        print(f"\n与MLP基线差距: {-improvement:.2f}% MAE")

    # 保存结果
    results = {
        'model': 'HybridGNN',
        'best_epoch': checkpoint['epoch'],
        'best_val_mae': best_val_mae,
        'test_mae': test_metrics['mae'],
        'test_rmse': test_metrics['rmse'],
        'test_r2': test_metrics['r2'],
        'num_params': num_params,
        'mlp_baseline_mae': mlp_mae,
        'improvement_over_mlp': improvement,
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
