"""
GNN模型训练脚本：使用图神经网络训练产率预测模型
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
from torch.utils.tensorboard import SummaryWriter

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.graph_features import batch_graphs, ATOM_FEAT_DIM, BOND_FEAT_DIM
from utils.xtb_features import REACTION_XTB_FEAT_DIM
from models.gnn_model import GNNYieldPredictor, GNNv2YieldPredictor, GNNv2HybridYieldPredictor


# ============================================================
# 数据集
# ============================================================
class GNNYieldDataset(Dataset):
    """GNN产率预测数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def gnn_collate_fn(batch):
    """
    自定义batch整理函数

    将多个样本的图数据分别批处理
    """
    # 分别收集各组分的图
    reactant_graphs = [item['reactant_graph'] for item in batch]
    product_graphs = [item['product_graph'] for item in batch]
    solvent_graphs = [item['solvent_graph'] for item in batch]
    electrolyte_graphs = [item['electrolyte_graph'] for item in batch]

    # 批处理图数据
    batched_reactant = batch_graphs(reactant_graphs)
    batched_product = batch_graphs(product_graphs)
    batched_solvent = batch_graphs(solvent_graphs)
    batched_electrolyte = batch_graphs(electrolyte_graphs)

    # 堆叠其他特征
    xtb_features = torch.stack([item['xtb_features'] for item in batch])
    echem_features = torch.stack([item['echem_features'] for item in batch])
    yields = torch.tensor([item['yield'] / 100.0 for item in batch], dtype=torch.float32)

    result = {
        'reactant_graph': batched_reactant,
        'product_graph': batched_product,
        'solvent_graph': batched_solvent,
        'electrolyte_graph': batched_electrolyte,
        'xtb_features': xtb_features,
        'echem_features': echem_features,
        'yields': yields,
    }

    # 反应指纹（hybrid模型使用）
    if 'reaction_fp' in batch[0]:
        result['reaction_fp'] = torch.stack([item['reaction_fp'] for item in batch])

    return result


def move_graph_to_device(graph, device):
    """将图数据移动到指定设备"""
    return {
        'node_feats': graph['node_feats'].to(device),
        'edge_index': graph['edge_index'].to(device),
        'edge_feats': graph['edge_feats'].to(device),
        'batch': graph['batch'].to(device),
        'num_graphs': graph['num_graphs'],
    }


# ============================================================
# 训练器
# ============================================================
class GNNTrainer:
    """GNN模型训练器"""

    def __init__(self, data_dir: str, output_dir: str, model_version: str = 'v1',
                 device: str = None):
        self.data_dir = Path(data_dir)
        self.model_version = model_version
        # 不同版本存储到不同子目录
        if model_version == 'v1':
            self.output_dir = Path(output_dir) / 'gnn'
        else:
            self.output_dir = Path(output_dir) / f'gnn_{model_version}'
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.writer = SummaryWriter(self.output_dir / f'logs_{timestamp}')

        print(f"Device: {self.device}")
        print(f"Output: {self.output_dir}")

    def setup_data(self, batch_size: int = 32, num_workers: int = 0):
        """加载数据"""
        print("\n加载GNN数据...")

        train_dataset = GNNYieldDataset(self.data_dir / 'train_gnn.pt')
        val_dataset = GNNYieldDataset(self.data_dir / 'val_gnn.pt')
        test_dataset = GNNYieldDataset(self.data_dir / 'test_gnn.pt')

        # GNN数据使用自定义collate，num_workers=0避免序列化问题
        self.train_loader = DataLoader(
            train_dataset, batch_size=batch_size, shuffle=True,
            num_workers=num_workers, collate_fn=gnn_collate_fn
        )
        self.val_loader = DataLoader(
            val_dataset, batch_size=batch_size, shuffle=False,
            num_workers=num_workers, collate_fn=gnn_collate_fn
        )
        self.test_loader = DataLoader(
            test_dataset, batch_size=batch_size, shuffle=False,
            num_workers=num_workers, collate_fn=gnn_collate_fn
        )

        print(f"  Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

        # 加载统计信息
        stats_path = self.data_dir / 'gnn_stats.json'
        if stats_path.exists():
            with open(stats_path) as f:
                self.stats = json.load(f)
            print(f"  原子特征维度: {self.stats.get('atom_feat_dim', ATOM_FEAT_DIM)}")
            print(f"  键特征维度: {self.stats.get('bond_feat_dim', BOND_FEAT_DIM)}")
            print(f"  xTB特征维度: {self.stats.get('xtb_feat_dim', REACTION_XTB_FEAT_DIM)}")
        else:
            self.stats = {}

    def setup_model(self, model_version: str = 'v1', lr: float = 0.001,
                    weight_decay: float = 0.0001, epochs: int = 100):
        """创建模型"""
        self.model_version = model_version
        atom_dim = self.stats.get('atom_feat_dim', ATOM_FEAT_DIM)
        edge_dim = self.stats.get('bond_feat_dim', BOND_FEAT_DIM)
        xtb_dim = self.stats.get('xtb_feat_dim', REACTION_XTB_FEAT_DIM)

        if model_version == 'v1':
            self.model = GNNYieldPredictor(
                atom_feat_dim=atom_dim,
                edge_feat_dim=edge_dim,
                gnn_hidden_dim=256,
                gnn_num_layers=4,
                xtb_feat_dim=xtb_dim,
                echem_feat_dim=6,
                dropout=0.2,
            ).to(self.device)
        elif model_version == 'v2':
            self.model = GNNv2YieldPredictor(
                atom_feat_dim=atom_dim,
                edge_feat_dim=edge_dim,
                gnn_hidden_dim=128,
                gnn_num_layers=2,
                xtb_feat_dim=xtb_dim,
                echem_feat_dim=6,
                dropout=0.3,
            ).to(self.device)
        elif model_version == 'v2_hybrid':
            self.model = GNNv2HybridYieldPredictor(
                atom_feat_dim=atom_dim,
                edge_feat_dim=edge_dim,
                gnn_hidden_dim=128,
                gnn_num_layers=2,
                xtb_feat_dim=xtb_dim,
                echem_feat_dim=6,
                fp_dim=6144,
                dropout=0.3,
            ).to(self.device)
        else:
            raise ValueError(f"Unknown model version: {model_version}")

        num_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"\n模型版本: {model_version}")
        print(f"模型参数量: {num_params:,}")

        self.optimizer = optim.AdamW(
            self.model.parameters(), lr=lr, weight_decay=weight_decay
        )

        # v2/v2_hybrid 使用 CosineAnnealingLR，v1 保持原有策略
        if model_version == 'v1':
            self.scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(
                self.optimizer, T_0=10, T_mult=2
            )
        else:
            self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer, T_max=epochs, eta_min=1e-6
            )

        self.criterion = nn.MSELoss()

    def train_epoch(self, epoch: int):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0.0

        for batch_data in tqdm(self.train_loader, desc=f"Epoch {epoch}"):
            # 移动数据到GPU
            reactant_g = move_graph_to_device(batch_data['reactant_graph'], self.device)
            product_g = move_graph_to_device(batch_data['product_graph'], self.device)
            solvent_g = move_graph_to_device(batch_data['solvent_graph'], self.device)
            electrolyte_g = move_graph_to_device(batch_data['electrolyte_graph'], self.device)
            xtb_feat = batch_data['xtb_features'].to(self.device)
            echem_feat = batch_data['echem_features'].to(self.device)
            labels = batch_data['yields'].to(self.device).unsqueeze(1)

            self.optimizer.zero_grad()

            if self.model_version == 'v2_hybrid':
                reaction_fp = batch_data['reaction_fp'].to(self.device)
                predictions = self.model(
                    reactant_g, product_g, solvent_g, electrolyte_g,
                    xtb_feat, echem_feat, reaction_fp
                )
            else:
                predictions = self.model(
                    reactant_g, product_g, solvent_g, electrolyte_g,
                    xtb_feat, echem_feat
                )
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
                xtb_feat = batch_data['xtb_features'].to(self.device)
                echem_feat = batch_data['echem_features'].to(self.device)
                labels = batch_data['yields'].to(self.device).unsqueeze(1)

                if self.model_version == 'v2_hybrid':
                    reaction_fp = batch_data['reaction_fp'].to(self.device)
                    predictions = self.model(
                        reactant_g, product_g, solvent_g, electrolyte_g,
                        xtb_feat, echem_feat, reaction_fp
                    )
                else:
                    predictions = self.model(
                        reactant_g, product_g, solvent_g, electrolyte_g,
                        xtb_feat, echem_feat
                    )
                loss = self.criterion(predictions, labels)

                total_loss += loss.item()
                all_preds.extend(predictions.cpu().flatten().tolist())
                all_labels.extend(labels.cpu().flatten().tolist())

        # 计算指标（反归一化到百分比）
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

    def train(self, epochs: int = 100, patience: int = 15):
        """完整训练流程"""
        print(f"\n{'='*60}")
        print(f"开始训练 GNN 模型 ({self.model_version})")
        print(f"{'='*60}")

        best_val_loss = float('inf')
        patience_counter = 0
        best_metrics = {}

        for epoch in range(1, epochs + 1):
            train_loss = self.train_epoch(epoch)
            val_metrics = self.validate()

            # 记录日志
            self.writer.add_scalar('Loss/train', train_loss, epoch)
            self.writer.add_scalar('Loss/val', val_metrics['loss'], epoch)
            self.writer.add_scalar('Metrics/MAE', val_metrics['mae'], epoch)
            self.writer.add_scalar('Metrics/RMSE', val_metrics['rmse'], epoch)
            self.writer.add_scalar('Metrics/R2', val_metrics['r2'], epoch)
            self.writer.add_scalar('LR', self.optimizer.param_groups[0]['lr'], epoch)

            print(f"Epoch {epoch:3d}: "
                  f"Train={train_loss:.4f}, Val={val_metrics['loss']:.4f}, "
                  f"MAE={val_metrics['mae']:.2f}%, RMSE={val_metrics['rmse']:.2f}%, "
                  f"R²={val_metrics['r2']:.4f}")

            # Early stopping
            if val_metrics['loss'] < best_val_loss:
                best_val_loss = val_metrics['loss']
                best_metrics = val_metrics.copy()
                patience_counter = 0

                # 根据模型版本保存配置
                if self.model_version == 'v1':
                    config = {'gnn_hidden_dim': 256, 'gnn_num_layers': 4}
                else:
                    config = {'gnn_hidden_dim': 128, 'gnn_num_layers': 2}
                config.update({
                    'atom_feat_dim': self.stats.get('atom_feat_dim', ATOM_FEAT_DIM),
                    'edge_feat_dim': self.stats.get('bond_feat_dim', BOND_FEAT_DIM),
                    'xtb_feat_dim': self.stats.get('xtb_feat_dim', REACTION_XTB_FEAT_DIM),
                    'model_version': self.model_version,
                })

                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'optimizer_state_dict': self.optimizer.state_dict(),
                    'metrics': val_metrics,
                    'model_name': f'gnn_{self.model_version}',
                    'config': config,
                }, self.output_dir / 'best_model.pt')
                print(f"  >>> 保存最佳模型 (epoch {epoch})")
            else:
                patience_counter += 1
                if patience_counter >= patience:
                    print(f"\nEarly stopping at epoch {epoch}")
                    break

        self.writer.close()

        print(f"\n训练完成！最佳验证指标:")
        print(f"  MAE:  {best_metrics['mae']:.2f}%")
        print(f"  RMSE: {best_metrics['rmse']:.2f}%")
        print(f"  R²:   {best_metrics['r2']:.4f}")

        return best_metrics

    def test(self):
        """测试"""
        print(f"\n{'='*60}")
        print(f"测试 GNN 模型 ({self.model_version})")
        print(f"{'='*60}")

        # 加载最佳模型
        checkpoint = torch.load(self.output_dir / 'best_model.pt', weights_only=False)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        print(f"加载最佳模型 (epoch {checkpoint['epoch']})")

        test_metrics = self.validate(self.test_loader)

        print(f"\nGNN 测试结果:")
        print(f"  MAE:  {test_metrics['mae']:.2f}%")
        print(f"  RMSE: {test_metrics['rmse']:.2f}%")
        print(f"  R²:   {test_metrics['r2']:.4f}")

        # 保存测试结果
        model_key = f'gnn_{self.model_version}' if self.model_version != 'v1' else 'gnn'
        results = {
            'model': model_key,
            'mae': test_metrics['mae'],
            'rmse': test_metrics['rmse'],
            'r2': test_metrics['r2'],
            'best_epoch': checkpoint['epoch'],
        }
        with open(self.output_dir / 'test_results.json', 'w') as f:
            json.dump(results, f, indent=2)

        # 与现有模型对比
        comparison_path = Path(project_root) / 'checkpoints' / 'comparison_results.json'
        if comparison_path.exists():
            with open(comparison_path) as f:
                existing = json.load(f)

            print(f"\n{'='*60}")
            print(f"与现有模型对比")
            print(f"{'='*60}")
            print(f"{'Model':<20} {'MAE':>10} {'RMSE':>10} {'R²':>10}")
            print(f"{'-'*60}")

            # 添加GNN结果
            existing[model_key] = results
            all_results = existing

            for name, res in sorted(all_results.items(),
                                    key=lambda x: x[1].get('mae', 999)):
                if 'error' in res:
                    print(f"{name:<20} {'ERROR':>10}")
                else:
                    print(f"{name:<20} {res['mae']:>10.2f}% {res['rmse']:>10.2f}% {res['r2']:>10.4f}")

            # 更新对比结果
            with open(comparison_path, 'w') as f:
                json.dump(all_results, f, indent=2)

        return test_metrics


def main():
    parser = argparse.ArgumentParser(description='Train GNN yield prediction model')
    parser.add_argument('--data-dir', type=str, default='data')
    parser.add_argument('--output-dir', type=str, default='checkpoints')
    parser.add_argument('--model-version', type=str, default='v2',
                        choices=['v1', 'v2', 'v2_hybrid'],
                        help='Model version: v1(original), v2(lighter), v2_hybrid(GNN+FP)')
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--batch-size', type=int, default=None,
                        help='Batch size (default: 32 for v1, 64 for v2/v2_hybrid)')
    parser.add_argument('--lr', type=float, default=None,
                        help='Learning rate (default: 0.001 for v1, 0.0005 for v2, 0.0003 for v2_hybrid)')
    parser.add_argument('--weight-decay', type=float, default=None,
                        help='Weight decay (default: 0.0001 for v1, 0.001 for v2/v2_hybrid)')
    parser.add_argument('--patience', type=int, default=None,
                        help='Early stopping patience (default: 15 for v1, 30 for v2/v2_hybrid)')
    parser.add_argument('--num-workers', type=int, default=0,
                        help='DataLoader workers (0 for graph data)')

    args = parser.parse_args()

    # 根据模型版本设置默认超参数
    version = args.model_version
    defaults = {
        'v1':        {'batch_size': 32, 'lr': 0.001,  'weight_decay': 0.0001, 'patience': 15},
        'v2':        {'batch_size': 64, 'lr': 0.0005, 'weight_decay': 0.001,  'patience': 30},
        'v2_hybrid': {'batch_size': 64, 'lr': 0.0003, 'weight_decay': 0.001,  'patience': 30},
    }
    d = defaults[version]
    batch_size = args.batch_size or d['batch_size']
    lr = args.lr or d['lr']
    weight_decay = args.weight_decay or d['weight_decay']
    patience = args.patience or d['patience']

    print(f"模型版本: {version}")
    print(f"超参数: batch_size={batch_size}, lr={lr}, weight_decay={weight_decay}, patience={patience}")

    data_dir = project_root / args.data_dir
    output_dir = project_root / args.output_dir

    trainer = GNNTrainer(str(data_dir), str(output_dir), model_version=version)
    trainer.setup_data(batch_size=batch_size, num_workers=args.num_workers)
    trainer.setup_model(model_version=version, lr=lr, weight_decay=weight_decay,
                        epochs=args.epochs)
    trainer.train(epochs=args.epochs, patience=patience)
    trainer.test()


if __name__ == "__main__":
    main()
