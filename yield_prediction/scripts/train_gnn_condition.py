"""
GNN 条件推荐模型训练脚本

架构：
1. 从SMILES动态构建分子图
2. MolecularGNN + xTB 编码反应物和产物
3. ReactionTransformer 建模反应变化
4. 多分类头预测条件
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

from models.gnn_condition_recommender import GNNConditionRecommender
from utils.graph_features import smiles_list_to_graph, get_dummy_graph


class GNNConditionDataset(Dataset):
    """GNN条件推荐数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)
        # 预处理图数据（比较耗时但只做一次）
        self._precompute_graphs()

    def _precompute_graphs(self):
        """预计算所有分子的图表示"""
        print(f"  预计算分子图 ({len(self.data)} 样本)...")
        for item in tqdm(self.data, desc="构建图"):
            # 反应物图
            r_smiles = item.get('reactant_smiles', [])
            if r_smiles and isinstance(r_smiles, list) and all(r_smiles):
                item['reactant_graph'] = smiles_list_to_graph(r_smiles)
            else:
                item['reactant_graph'] = get_dummy_graph()

            # 产物图
            p_smiles = item.get('product_smiles', [])
            if p_smiles and isinstance(p_smiles, list) and all(p_smiles):
                item['product_graph'] = smiles_list_to_graph(p_smiles)
            else:
                item['product_graph'] = get_dummy_graph()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # xTB特征
        reactant_xtb = torch.tensor(item['reactant_xtb'], dtype=torch.float32)
        product_xtb = torch.tensor(item['product_xtb'], dtype=torch.float32)

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

        return {
            'reactant_graph': item['reactant_graph'],
            'product_graph': item['product_graph'],
            'reactant_xtb': reactant_xtb,
            'product_xtb': product_xtb,
            'labels': labels,
        }


def collate_fn(batch):
    """整理batch数据"""

    def merge_graphs(graphs):
        all_nodes = []
        all_edges = []
        all_edge_feats = []
        batch_idx = []
        node_offset = 0

        for i, g in enumerate(graphs):
            if g is None:
                g = get_dummy_graph()
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

    # xTB特征
    reactant_xtb = torch.stack([d['reactant_xtb'] for d in batch])
    product_xtb = torch.stack([d['product_xtb'] for d in batch])

    # 标签
    labels = {
        'anode': torch.tensor([d['labels']['anode'] for d in batch], dtype=torch.long),
        'cathode': torch.tensor([d['labels']['cathode'] for d in batch], dtype=torch.long),
        'cell_type': torch.tensor([d['labels']['cell_type'] for d in batch], dtype=torch.long),
        'electrolyte': torch.tensor([d['labels']['electrolyte'] for d in batch], dtype=torch.long),
        'solvent': torch.tensor([d['labels']['solvent'] for d in batch], dtype=torch.long),
        'reagent': torch.tensor([d['labels']['reagent'] for d in batch], dtype=torch.long),
        'catalyst': torch.tensor([d['labels']['catalyst'] for d in batch], dtype=torch.long),
    }

    return {
        'reactant_graph': reactant_graphs,
        'product_graph': product_graphs,
        'reactant_xtb': reactant_xtb,
        'product_xtb': product_xtb,
        'labels': labels,
    }


def train_epoch(model, loader, optimizer, device):
    model.train()
    total_loss = 0
    correct = {k: 0 for k in ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']}
    total = 0

    criterion = nn.CrossEntropyLoss()

    for batch in tqdm(loader, desc="Training", leave=False):
        # 移动数据到设备
        reactant_graph = {k: v.to(device) for k, v in batch['reactant_graph'].items() if isinstance(v, torch.Tensor)}
        reactant_graph['num_graphs'] = batch['reactant_graph']['num_graphs']
        product_graph = {k: v.to(device) for k, v in batch['product_graph'].items() if isinstance(v, torch.Tensor)}
        product_graph['num_graphs'] = batch['product_graph']['num_graphs']

        reactant_xtb = batch['reactant_xtb'].to(device)
        product_xtb = batch['product_xtb'].to(device)
        labels = {k: v.to(device) for k, v in batch['labels'].items()}

        optimizer.zero_grad()
        preds = model(reactant_graph, product_graph, reactant_xtb, product_xtb)

        # 计算损失
        loss = 0
        for key in preds.keys():
            loss += criterion(preds[key], labels[key])

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        total_loss += loss.item()
        batch_size = reactant_xtb.size(0)
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

    for batch in loader:
        reactant_graph = {k: v.to(device) for k, v in batch['reactant_graph'].items() if isinstance(v, torch.Tensor)}
        reactant_graph['num_graphs'] = batch['reactant_graph']['num_graphs']
        product_graph = {k: v.to(device) for k, v in batch['product_graph'].items() if isinstance(v, torch.Tensor)}
        product_graph['num_graphs'] = batch['product_graph']['num_graphs']

        reactant_xtb = batch['reactant_xtb'].to(device)
        product_xtb = batch['product_xtb'].to(device)
        labels = {k: v.to(device) for k, v in batch['labels'].items()}

        preds = model(reactant_graph, product_graph, reactant_xtb, product_xtb)

        loss = 0
        for key in preds.keys():
            loss += criterion(preds[key], labels[key])

        total_loss += loss.item()
        batch_size = reactant_xtb.size(0)
        total += batch_size

        for key in preds.keys():
            # Top-1
            pred_labels = preds[key].argmax(dim=-1)
            correct[key] += (pred_labels == labels[key]).sum().item()

            # Top-3
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
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'checkpoints' / 'gnn_condition'))
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--patience', type=int, default=25)
    parser.add_argument('--gnn_hidden', type=int, default=128)
    parser.add_argument('--gnn_layers', type=int, default=3)
    parser.add_argument('--dropout', type=float, default=0.3)
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Using device: {device}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    data_dir = Path(args.data_dir)

    # 加载数据
    print("\n加载数据...")
    train_dataset = GNNConditionDataset(data_dir / 'train_xtb_cat.pt')
    val_dataset = GNNConditionDataset(data_dir / 'val_xtb_cat.pt')
    test_dataset = GNNConditionDataset(data_dir / 'test_xtb_cat.pt')

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

    # 创建模型
    model = GNNConditionRecommender(
        gnn_hidden_dim=args.gnn_hidden,
        gnn_num_layers=args.gnn_layers,
        dropout=args.dropout,
    ).to(device)

    num_params = sum(p.numel() for p in model.parameters())
    print(f"\n模型参数量: {num_params:,}")

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs, eta_min=1e-6)

    # 训练
    print("\n" + "=" * 70)
    print("开始训练 GNN 条件推荐模型")
    print("=" * 70)

    best_val_acc = 0
    patience_counter = 0
    start_time = datetime.now()

    for epoch in range(args.epochs):
        train_loss, train_acc = train_epoch(model, train_loader, optimizer, device)
        val_metrics = evaluate(model, val_loader, device)

        scheduler.step()
        current_lr = optimizer.param_groups[0]['lr']

        avg_train_acc = sum(train_acc.values()) / len(train_acc)
        avg_val_acc = sum(val_metrics['acc'].values()) / len(val_metrics['acc'])
        avg_val_top3 = sum(val_metrics['top3_acc'].values()) / len(val_metrics['top3_acc'])

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
    results = {
        'model': 'GNNConditionRecommender',
        'best_epoch': checkpoint['epoch'],
        'test_acc': test_metrics['acc'],
        'test_top3_acc': test_metrics['top3_acc'],
        'avg_test_acc': avg_test_acc,
        'avg_test_top3_acc': avg_test_top3,
        'num_params': num_params,
        'training_time': str(elapsed),
        'args': vars(args),
    }

    with open(output_dir / 'results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n结果已保存到: {output_dir}")

    # 对比基线
    print("\n" + "=" * 70)
    print("与 MLP+xTB 基线对比:")
    print("=" * 70)
    print(f"  MLP+xTB 基线:    81.2% Top-1, 95.6% Top-3")
    print(f"  GNN:             {avg_test_acc:.1f}% Top-1, {avg_test_top3:.1f}% Top-3")

    return results


if __name__ == "__main__":
    main()
