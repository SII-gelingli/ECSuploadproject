"""
纯GNN模型训练脚本：只使用分子图，不使用指纹和xTB特征
"""
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.graph_features import batch_graphs, ATOM_FEAT_DIM, BOND_FEAT_DIM
from models.pure_gnn_model import PureGNNYieldPredictor, PureGNNWithAttention


class PureGNNDataset(Dataset):
    """纯GNN数据集：复用现有数据，使用图和电化学特征"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return {
            'reactant_graph': item['reactant_graph'],
            'product_graph': item['product_graph'],
            'solvent_graph': item.get('solvent_graph'),
            'electrolyte_graph': item.get('electrolyte_graph'),
            'echem_features': item['echem_features'],
            'yield': item['yield'],
        }


def collate_fn(batch):
    """批处理函数"""
    reactant_graphs = [item['reactant_graph'] for item in batch]
    product_graphs = [item['product_graph'] for item in batch]
    solvent_graphs = [item['solvent_graph'] for item in batch]
    electrolyte_graphs = [item['electrolyte_graph'] for item in batch]

    batched_reactant = batch_graphs(reactant_graphs)
    batched_product = batch_graphs(product_graphs)
    batched_solvent = batch_graphs(solvent_graphs)
    batched_electrolyte = batch_graphs(electrolyte_graphs)

    echem_features = torch.stack([item['echem_features'] for item in batch])
    yields = torch.tensor([item['yield'] / 100.0 for item in batch], dtype=torch.float32)

    return {
        'reactant_graph': batched_reactant,
        'product_graph': batched_product,
        'solvent_graph': batched_solvent,
        'electrolyte_graph': batched_electrolyte,
        'echem_features': echem_features,
        'yields': yields,
    }


def move_graph_to_device(graph, device):
    """将图数据移动到设备"""
    return {
        'node_feats': graph['node_feats'].to(device),
        'edge_index': graph['edge_index'].to(device),
        'edge_feats': graph['edge_feats'].to(device),
        'batch': graph['batch'].to(device),
        'num_graphs': graph['num_graphs'],
    }


class PureGNNTrainer:
    """纯GNN训练器"""

    def __init__(self, data_dir: str, output_dir: str, model_type: str = 'base', device: str = None):
        self.data_dir = Path(data_dir)
        self.model_type = model_type
        self.output_dir = Path(output_dir) / f'pure_gnn_{model_type}'
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')

        print(f"=" * 60)
        print(f"纯GNN训练器 (只使用分子图，不使用指纹/xTB)")
        print(f"=" * 60)
        print(f"Device: {self.device}")
        print(f"Model type: {model_type}")
        print(f"Output: {self.output_dir}")

    def setup_data(self, batch_size: int = 32):
        """加载数据"""
        print("\n加载数据（复用现有GNN数据）...")

        train_dataset = PureGNNDataset(self.data_dir / 'train_gnn.pt')
        val_dataset = PureGNNDataset(self.data_dir / 'val_gnn.pt')
        test_dataset = PureGNNDataset(self.data_dir / 'test_gnn.pt')

        self.train_loader = DataLoader(
            train_dataset, batch_size=batch_size, shuffle=True,
            num_workers=0, collate_fn=collate_fn
        )
        self.val_loader = DataLoader(
            val_dataset, batch_size=batch_size, shuffle=False,
            num_workers=0, collate_fn=collate_fn
        )
        self.test_loader = DataLoader(
            test_dataset, batch_size=batch_size, shuffle=False,
            num_workers=0, collate_fn=collate_fn
        )

        print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

    def setup_model(
        self,
        hidden_dim: int = 128,
        num_layers: int = 3,
        lr: float = 0.001,
        weight_decay: float = 0.001,
        epochs: int = 100,
    ):
        """创建模型"""
        if self.model_type == 'base':
            # base: 只用反应物+产物
            self.model = PureGNNYieldPredictor(
                atom_feat_dim=ATOM_FEAT_DIM,
                edge_feat_dim=BOND_FEAT_DIM,
                gnn_hidden_dim=hidden_dim,
                gnn_num_layers=num_layers,
                echem_feat_dim=6,
                dropout=0.2,
                use_solvent=False,
                use_electrolyte=False,
            ).to(self.device)
        elif self.model_type == 'full':
            # full: 反应物+产物+溶剂+电解质（共享编码器）
            self.model = PureGNNYieldPredictor(
                atom_feat_dim=ATOM_FEAT_DIM,
                edge_feat_dim=BOND_FEAT_DIM,
                gnn_hidden_dim=hidden_dim,
                gnn_num_layers=num_layers,
                echem_feat_dim=6,
                dropout=0.2,
                use_solvent=True,
                use_electrolyte=True,
                separate_encoder=False,
            ).to(self.device)
        elif self.model_type == 'separate':
            # separate: 反应物+产物+溶剂+电解质（独立编码器）
            self.model = PureGNNYieldPredictor(
                atom_feat_dim=ATOM_FEAT_DIM,
                edge_feat_dim=BOND_FEAT_DIM,
                gnn_hidden_dim=hidden_dim,
                gnn_num_layers=num_layers,
                echem_feat_dim=6,
                dropout=0.2,
                use_solvent=True,
                use_electrolyte=True,
                separate_encoder=True,  # 独立编码器
            ).to(self.device)
        elif self.model_type == 'attention':
            self.model = PureGNNWithAttention(
                atom_feat_dim=ATOM_FEAT_DIM,
                edge_feat_dim=BOND_FEAT_DIM,
                gnn_hidden_dim=hidden_dim,
                gnn_num_layers=num_layers,
                echem_feat_dim=6,
                num_attention_heads=4,
                dropout=0.2,
            ).to(self.device)
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")

        num_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"\n模型参数量: {num_params:,}")
        print(f"隐藏维度: {hidden_dim}, 层数: {num_layers}")

        self.optimizer = optim.AdamW(
            self.model.parameters(), lr=lr, weight_decay=weight_decay
        )
        self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=epochs, eta_min=1e-6
        )
        self.criterion = nn.MSELoss()

        # 保存配置
        self.config = {
            'model_type': self.model_type,
            'hidden_dim': hidden_dim,
            'num_layers': num_layers,
            'lr': lr,
            'weight_decay': weight_decay,
            'num_params': num_params,
        }

    def train_epoch(self, epoch: int):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0.0

        for batch_data in tqdm(self.train_loader, desc=f"Epoch {epoch}", leave=False):
            reactant_g = move_graph_to_device(batch_data['reactant_graph'], self.device)
            product_g = move_graph_to_device(batch_data['product_graph'], self.device)
            solvent_g = move_graph_to_device(batch_data['solvent_graph'], self.device)
            electrolyte_g = move_graph_to_device(batch_data['electrolyte_graph'], self.device)
            echem_feat = batch_data['echem_features'].to(self.device)
            labels = batch_data['yields'].to(self.device).unsqueeze(1)

            self.optimizer.zero_grad()

            if self.model_type in ['full', 'separate']:
                predictions = self.model(reactant_g, product_g, echem_feat, solvent_g, electrolyte_g)
            elif self.model_type == 'attention':
                predictions = self.model(reactant_g, product_g, echem_feat)
            else:  # base
                predictions = self.model(reactant_g, product_g, echem_feat)

            loss = self.criterion(predictions, labels)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()

            total_loss += loss.item()

        self.scheduler.step()
        return total_loss / len(self.train_loader)

    def validate(self, loader=None):
        """验证"""
        loader = loader or self.val_loader
        self.model.eval()
        total_loss = 0.0
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch_data in loader:
                reactant_g = move_graph_to_device(batch_data['reactant_graph'], self.device)
                product_g = move_graph_to_device(batch_data['product_graph'], self.device)
                solvent_g = move_graph_to_device(batch_data['solvent_graph'], self.device)
                electrolyte_g = move_graph_to_device(batch_data['electrolyte_graph'], self.device)
                echem_feat = batch_data['echem_features'].to(self.device)
                labels = batch_data['yields'].to(self.device).unsqueeze(1)

                if self.model_type in ['full', 'separate']:
                    predictions = self.model(reactant_g, product_g, echem_feat, solvent_g, electrolyte_g)
                elif self.model_type == 'attention':
                    predictions = self.model(reactant_g, product_g, echem_feat)
                else:  # base
                    predictions = self.model(reactant_g, product_g, echem_feat)

                loss = self.criterion(predictions, labels)
                total_loss += loss.item()
                all_preds.extend(predictions.cpu().flatten().tolist())
                all_labels.extend(labels.cpu().flatten().tolist())

        # 计算指标
        preds = torch.tensor(all_preds) * 100
        labels = torch.tensor(all_labels) * 100

        mae = torch.mean(torch.abs(preds - labels)).item()
        rmse = torch.sqrt(torch.mean((preds - labels) ** 2)).item()
        ss_res = torch.sum((preds - labels) ** 2)
        ss_tot = torch.sum((labels - torch.mean(labels)) ** 2)
        r2 = (1 - ss_res / ss_tot).item() if ss_tot > 0 else 0.0

        return {
            'loss': total_loss / len(loader),
            'mae': mae,
            'rmse': rmse,
            'r2': r2,
        }

    def train(self, epochs: int = 100, patience: int = 20):
        """训练"""
        print(f"\n{'=' * 60}")
        print(f"开始训练纯GNN模型 ({self.model_type})")
        print(f"{'=' * 60}")

        best_val_loss = float('inf')
        patience_counter = 0
        best_metrics = {}
        history = {'train_loss': [], 'val_loss': [], 'val_mae': [], 'val_r2': []}

        for epoch in range(1, epochs + 1):
            train_loss = self.train_epoch(epoch)
            val_metrics = self.validate()

            history['train_loss'].append(train_loss)
            history['val_loss'].append(val_metrics['loss'])
            history['val_mae'].append(val_metrics['mae'])
            history['val_r2'].append(val_metrics['r2'])

            print(f"Epoch {epoch:3d}: "
                  f"Train={train_loss:.4f}, Val={val_metrics['loss']:.4f}, "
                  f"MAE={val_metrics['mae']:.2f}%, R²={val_metrics['r2']:.4f}")

            if val_metrics['loss'] < best_val_loss:
                best_val_loss = val_metrics['loss']
                best_metrics = val_metrics.copy()
                best_metrics['epoch'] = epoch
                patience_counter = 0

                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'optimizer_state_dict': self.optimizer.state_dict(),
                    'metrics': val_metrics,
                    'config': self.config,
                }, self.output_dir / 'best_model.pt')
                print(f"  >>> 保存最佳模型")
            else:
                patience_counter += 1
                if patience_counter >= patience:
                    print(f"\nEarly stopping at epoch {epoch}")
                    break

        # 保存训练历史
        with open(self.output_dir / 'history.json', 'w') as f:
            json.dump(history, f)

        print(f"\n训练完成！最佳验证指标 (epoch {best_metrics.get('epoch', 0)}):")
        print(f"  MAE:  {best_metrics['mae']:.2f}%")
        print(f"  RMSE: {best_metrics['rmse']:.2f}%")
        print(f"  R²:   {best_metrics['r2']:.4f}")

        return best_metrics

    def test(self):
        """测试"""
        print(f"\n{'=' * 60}")
        print(f"测试纯GNN模型 ({self.model_type})")
        print(f"{'=' * 60}")

        checkpoint = torch.load(self.output_dir / 'best_model.pt', weights_only=False)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        print(f"加载最佳模型 (epoch {checkpoint['epoch']})")

        test_metrics = self.validate(self.test_loader)

        print(f"\n纯GNN测试结果:")
        print(f"  MAE:  {test_metrics['mae']:.2f}%")
        print(f"  RMSE: {test_metrics['rmse']:.2f}%")
        print(f"  R²:   {test_metrics['r2']:.4f}")

        # 保存结果
        results = {
            'model': f'pure_gnn_{self.model_type}',
            'mae': test_metrics['mae'],
            'rmse': test_metrics['rmse'],
            'r2': test_metrics['r2'],
            'best_epoch': checkpoint['epoch'],
            'config': self.config,
        }

        with open(self.output_dir / 'test_results.json', 'w') as f:
            json.dump(results, f, indent=2)

        # 更新对比结果
        comparison_path = project_root / 'checkpoints' / 'comparison_results.json'
        if comparison_path.exists():
            with open(comparison_path) as f:
                all_results = json.load(f)
        else:
            all_results = {}

        all_results[f'pure_gnn_{self.model_type}'] = {
            'mae': test_metrics['mae'],
            'rmse': test_metrics['rmse'],
            'r2': test_metrics['r2'],
        }

        with open(comparison_path, 'w') as f:
            json.dump(all_results, f, indent=2)

        # 打印对比
        print(f"\n{'=' * 60}")
        print("与其他模型对比")
        print(f"{'=' * 60}")
        print(f"{'Model':<25} {'MAE':>10} {'RMSE':>10} {'R²':>10}")
        print(f"{'-' * 60}")
        for name, res in sorted(all_results.items(), key=lambda x: x[1].get('mae', 999)):
            if 'error' in res:
                print(f"{name:<25} {'ERROR':>10}")
            else:
                print(f"{name:<25} {res['mae']:>10.2f}% {res['rmse']:>10.2f}% {res['r2']:>10.4f}")

        return test_metrics


def main():
    parser = argparse.ArgumentParser(description='Train Pure GNN yield prediction model')
    parser.add_argument('--data-dir', type=str, default='data')
    parser.add_argument('--output-dir', type=str, default='checkpoints')
    parser.add_argument('--model-type', type=str, default='separate',
                        choices=['base', 'full', 'separate', 'attention'],
                        help='Model type: base, full (共享编码器), separate (独立编码器), attention')
    parser.add_argument('--hidden-dim', type=int, default=128)
    parser.add_argument('--num-layers', type=int, default=3)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--weight-decay', type=float, default=0.001)
    parser.add_argument('--patience', type=int, default=20)

    args = parser.parse_args()

    data_dir = project_root / args.data_dir
    output_dir = project_root / args.output_dir

    trainer = PureGNNTrainer(str(data_dir), str(output_dir), model_type=args.model_type)
    trainer.setup_data(batch_size=args.batch_size)
    trainer.setup_model(
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        lr=args.lr,
        weight_decay=args.weight_decay,
        epochs=args.epochs,
    )
    trainer.train(epochs=args.epochs, patience=args.patience)
    trainer.test()


if __name__ == "__main__":
    main()
