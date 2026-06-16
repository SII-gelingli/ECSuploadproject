"""
Pure GNN V2 训练脚本

使用改进的数据预处理：
- 电极 Embedding（20类）
- 电解池类型 Embedding（5类）
- 去掉无用的 current_density 和 potential
"""
import sys
import json
from pathlib import Path

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

from models.pure_gnn_v2 import PureGNNv2


class YieldDatasetV2(Dataset):
    """V2 数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def collate_fn_v2(batch):
    """V2 数据整理函数"""
    # 合并分子图
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

    reactant_graphs = merge_graphs([d['reactant_graph'] for d in batch])
    product_graphs = merge_graphs([d['product_graph'] for d in batch])
    solvent_graphs = merge_graphs([d['solvent_graph'] for d in batch])
    electrolyte_graphs = merge_graphs([d['electrolyte_graph'] for d in batch])

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
        'anode_id': anode_ids,
        'cathode_id': cathode_ids,
        'cell_type_id': cell_type_ids,
        'current': currents,
        'yield': yields,
    }


def move_graph_to_device(graph, device):
    """将图数据移动到指定设备"""
    return {
        k: v.to(device) if isinstance(v, torch.Tensor) else v
        for k, v in graph.items()
    }


def train_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    total_mae = 0
    n_batches = 0

    for batch in tqdm(loader, desc="Training", leave=False):
        # 移动数据到设备
        reactant_graph = move_graph_to_device(batch['reactant_graph'], device)
        product_graph = move_graph_to_device(batch['product_graph'], device)
        solvent_graph = move_graph_to_device(batch['solvent_graph'], device)
        electrolyte_graph = move_graph_to_device(batch['electrolyte_graph'], device)

        anode_id = batch['anode_id'].to(device)
        cathode_id = batch['cathode_id'].to(device)
        cell_type_id = batch['cell_type_id'].to(device)
        current = batch['current'].to(device)
        yields = batch['yield'].to(device)

        optimizer.zero_grad()
        pred = model(
            reactant_graph=reactant_graph,
            product_graph=product_graph,
            solvent_graph=solvent_graph,
            electrolyte_graph=electrolyte_graph,
            anode_id=anode_id,
            cathode_id=cathode_id,
            cell_type_id=cell_type_id,
            current=current,
        )

        loss = criterion(pred, yields)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        total_loss += loss.item()
        total_mae += (pred - yields).abs().mean().item() * 100
        n_batches += 1

    return total_loss / n_batches, total_mae / n_batches


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0
    total_mae = 0
    n_batches = 0

    for batch in loader:
        reactant_graph = move_graph_to_device(batch['reactant_graph'], device)
        product_graph = move_graph_to_device(batch['product_graph'], device)
        solvent_graph = move_graph_to_device(batch['solvent_graph'], device)
        electrolyte_graph = move_graph_to_device(batch['electrolyte_graph'], device)

        anode_id = batch['anode_id'].to(device)
        cathode_id = batch['cathode_id'].to(device)
        cell_type_id = batch['cell_type_id'].to(device)
        current = batch['current'].to(device)
        yields = batch['yield'].to(device)

        pred = model(
            reactant_graph=reactant_graph,
            product_graph=product_graph,
            solvent_graph=solvent_graph,
            electrolyte_graph=electrolyte_graph,
            anode_id=anode_id,
            cathode_id=cathode_id,
            cell_type_id=cell_type_id,
            current=current,
        )

        total_loss += criterion(pred, yields).item()
        total_mae += (pred - yields).abs().mean().item() * 100
        n_batches += 1

    return total_loss / n_batches, total_mae / n_batches


def main():
    # 配置
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    data_dir = project_root / 'data'
    output_dir = project_root / 'checkpoints'
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载数据
    print("\n加载 V2 数据...")
    train_dataset = YieldDatasetV2(data_dir / 'train_v2.pt')
    val_dataset = YieldDatasetV2(data_dir / 'val_v2.pt')
    test_dataset = YieldDatasetV2(data_dir / 'test_v2.pt')

    print(f"  Train: {len(train_dataset)}")
    print(f"  Val:   {len(val_dataset)}")
    print(f"  Test:  {len(test_dataset)}")

    # 加载统计信息
    with open(data_dir / 'stats_v2.json', 'r') as f:
        stats = json.load(f)

    # DataLoader
    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True,
        collate_fn=collate_fn_v2,
        num_workers=0,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=64,
        shuffle=False,
        collate_fn=collate_fn_v2,
        num_workers=0,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=64,
        shuffle=False,
        collate_fn=collate_fn_v2,
        num_workers=0,
    )

    # 创建模型
    model = PureGNNv2(
        atom_feat_dim=stats['atom_feat_dim'],
        edge_feat_dim=stats['bond_feat_dim'],
        gnn_hidden_dim=128,
        gnn_num_layers=3,
        num_electrode_types=stats['num_electrode_types'],
        num_cell_types=stats['num_cell_types'],
        electrode_embed_dim=32,
        cell_embed_dim=16,
        dropout=0.2,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

    # 优化器和损失
    optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=10
    )
    criterion = nn.MSELoss()

    # 训练
    print("\n" + "=" * 60)
    print("开始训练 Pure GNN V2")
    print("=" * 60)

    best_val_mae = float('inf')
    patience_counter = 0
    max_patience = 30
    n_epochs = 150

    history = {
        'train_loss': [], 'train_mae': [],
        'val_loss': [], 'val_mae': [],
    }

    for epoch in range(n_epochs):
        train_loss, train_mae = train_epoch(model, train_loader, optimizer, criterion, device)
        val_loss, val_mae = evaluate(model, val_loader, criterion, device)

        scheduler.step(val_loss)

        history['train_loss'].append(train_loss)
        history['train_mae'].append(train_mae)
        history['val_loss'].append(val_loss)
        history['val_mae'].append(val_mae)

        improved = ""
        if val_mae < best_val_mae:
            best_val_mae = val_mae
            patience_counter = 0
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_mae': val_mae,
                'stats': stats,
            }, output_dir / 'pure_gnn_v2_best.pt')
            improved = " *"
        else:
            patience_counter += 1

        if (epoch + 1) % 5 == 0 or improved:
            print(f"Epoch {epoch+1:3d} | "
                  f"Train Loss: {train_loss:.4f}, MAE: {train_mae:.2f}% | "
                  f"Val Loss: {val_loss:.4f}, MAE: {val_mae:.2f}%{improved}")

        if patience_counter >= max_patience:
            print(f"\n早停: {max_patience} epochs 无改善")
            break

    # 加载最佳模型测试
    print("\n" + "=" * 60)
    print("在测试集上评估最佳模型")
    print("=" * 60)

    checkpoint = torch.load(output_dir / 'pure_gnn_v2_best.pt')
    model.load_state_dict(checkpoint['model_state_dict'])

    test_loss, test_mae = evaluate(model, test_loader, criterion, device)
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test MAE:  {test_mae:.2f}%")

    # 保存结果
    results = {
        'model': 'PureGNNv2',
        'best_epoch': checkpoint['epoch'],
        'best_val_mae': best_val_mae,
        'test_mae': test_mae,
        'test_loss': test_loss,
        'num_params': num_params,
        'history': history,
    }

    with open(output_dir / 'pure_gnn_v2_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到 {output_dir}")
    print(f"  模型: pure_gnn_v2_best.pt")
    print(f"  结果: pure_gnn_v2_results.json")

    return results


if __name__ == "__main__":
    main()
