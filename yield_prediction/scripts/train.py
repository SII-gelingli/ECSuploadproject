"""
训练脚本：产率预测模型训练
"""
import os
import sys
import argparse
import yaml
from pathlib import Path
from datetime import datetime

# 先导入torch（使用系统numpy），再加pip_packages
import torch
import numpy

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, WeightedRandomSampler
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import ReactionFeaturizer, ReactionDataset, CompactReactionFeaturizer, CompactReactionDataset, XtbOnlyDataset
from utils.pca_reducer import FingerprintPCAReducer
from models.yield_predictor import YieldPredictor, MultiTaskYieldPredictor
from models.architectures import create_model, MODEL_REGISTRY, CompactYieldPredictor


class Trainer:
    """训练器"""

    def __init__(self, config: dict, device: str = None,
                 include_failed: bool = False, failed_weight: float = 2.0):
        self.config = config
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.include_failed = include_failed
        self.failed_weight = failed_weight
        print(f"Using device: {self.device}")
        if include_failed:
            print(f"Including failed reactions with sample weight {failed_weight}x")

        # 创建输出目录
        self.output_dir = Path(config['output']['model_dir'])
        self.log_dir = Path(config['output']['log_dir'])
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # TensorBoard
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.writer = SummaryWriter(self.log_dir / timestamp)

        # 初始化组件
        self.data_processor = None
        self.featurizer = None
        self.model = None
        self.optimizer = None
        self.scheduler = None

    def setup_data(self):
        """准备数据"""
        print("Loading and processing data...")

        # 数据处理器
        self.data_processor = ReactionDataProcessor(
            yield_data_dir=self.config['data']['yield_data_dir'],
            smiles_data_path=self.config['data']['smiles_data_path']
        )

        # 加载并划分数据
        train_data, val_data, test_data = self.data_processor.prepare_dataset(
            random_seed=self.config['data']['random_seed'],
            include_failed=self.include_failed
        )

        # 特征化器（支持xTB特征）
        xtb_config = self.config.get('xtb', {})
        self.featurizer = ReactionFeaturizer(
            fp_size=self.config['model']['mol_encoder']['fingerprint_size'],
            fp_radius=self.config['model']['mol_encoder']['fingerprint_radius'],
            xtb_csv_path=xtb_config.get('csv_path'),
            use_xtb=xtb_config.get('use_xtb', False)
        )

        # 创建数据集（训练集计算归一化统计量，验证/测试集复用）
        print("Creating datasets...")
        train_dataset = ReactionDataset(train_data, self.featurizer, normalize_xtb=True)
        xtb_stats = train_dataset.get_xtb_stats()  # 获取训练集的归一化统计量
        val_dataset = ReactionDataset(val_data, self.featurizer, normalize_xtb=True, xtb_stats=xtb_stats)
        test_dataset = ReactionDataset(test_data, self.featurizer, normalize_xtb=True, xtb_stats=xtb_stats)

        # 创建DataLoader
        batch_size = self.config['training']['batch_size']

        # 若包含失败反应，使用加权采样器对失败样本加权
        if self.include_failed:
            sample_weights = []
            for rxn in train_data:
                yield_val = rxn.get('yield', 0.0)
                if yield_val == 0.0:
                    sample_weights.append(self.failed_weight)
                else:
                    sample_weights.append(1.0)
            sampler = WeightedRandomSampler(
                weights=sample_weights,
                num_samples=len(train_dataset),
                replacement=True
            )
            self.train_loader = DataLoader(
                train_dataset, batch_size=batch_size, sampler=sampler, num_workers=4
            )
            num_failed = sum(1 for w in sample_weights if w > 1.0)
            print(f"Using WeightedRandomSampler: {num_failed} failed samples at {self.failed_weight}x weight")
        else:
            self.train_loader = DataLoader(
                train_dataset, batch_size=batch_size, shuffle=True, num_workers=4
            )

        self.val_loader = DataLoader(
            val_dataset, batch_size=batch_size, shuffle=False, num_workers=4
        )
        self.test_loader = DataLoader(
            test_dataset, batch_size=batch_size, shuffle=False, num_workers=4
        )

        print(f"Train batches: {len(self.train_loader)}")
        print(f"Val batches: {len(self.val_loader)}")
        print(f"Test batches: {len(self.test_loader)}")

        return self.featurizer.get_feature_dim()

    def setup_compact_data(self, pca_components: int = 128):
        """准备紧凑特征数据（PCA + Embedding）"""
        import json
        print("Loading data for compact model...")

        self.data_processor = ReactionDataProcessor(
            yield_data_dir=self.config['data']['yield_data_dir'],
            smiles_data_path=self.config['data']['smiles_data_path']
        )
        train_data, val_data, test_data = self.data_processor.prepare_dataset(
            random_seed=self.config['data']['random_seed']
        )

        # 加载溶剂/电解质词汇表
        vocab_path = self.output_dir / 'condition_model' / 'vocab.json'
        if vocab_path.exists():
            with open(vocab_path) as f:
                vocab = json.load(f)
            solvent_vocab = vocab.get('solvent', {})
            electrolyte_vocab = vocab.get('electrolyte', {})
            print(f"Loaded vocab: {len(solvent_vocab)} solvents, {len(electrolyte_vocab)} electrolytes")
        else:
            # 从训练数据构建词汇表
            from collections import Counter
            solvent_counter, electrolyte_counter = Counter(), Counter()
            for rxn in train_data:
                for s in rxn.get('solvents', []):
                    if s.get('smiles'):
                        solvent_counter[s['smiles']] += 1
                echem = rxn.get('electrochemistry', {})
                elec = echem.get('electrolyte', '')
                if elec:
                    electrolyte_counter[elec] += 1
            solvent_vocab = {s: i+1 for i, (s, _) in enumerate(solvent_counter.most_common(100))}
            electrolyte_vocab = {e: i+1 for i, (e, _) in enumerate(electrolyte_counter.most_common(100))}
            print(f"Built vocab: {len(solvent_vocab)} solvents, {len(electrolyte_vocab)} electrolytes")

        self.num_solvents = len(solvent_vocab) + 1
        self.num_electrolytes = len(electrolyte_vocab) + 1

        # 创建特征提取器
        xtb_config = self.config.get('xtb', {})
        featurizer = CompactReactionFeaturizer(
            fp_size=self.config['model']['mol_encoder']['fingerprint_size'],
            fp_radius=self.config['model']['mol_encoder']['fingerprint_radius'],
            xtb_csv_path=xtb_config.get('csv_path'),
            use_xtb=xtb_config.get('use_xtb', False),
            solvent_vocab=solvent_vocab,
            electrolyte_vocab=electrolyte_vocab,
        )

        # PCA降维器
        pca_reducer = FingerprintPCAReducer(n_components=pca_components)

        # 创建数据集（训练集fit PCA，验证/测试集用训练集PCA）
        print("Creating compact datasets...")
        train_dataset = CompactReactionDataset(train_data, featurizer, pca_reducer=pca_reducer)
        xtb_stats = train_dataset.get_xtb_stats()
        val_dataset = CompactReactionDataset(val_data, featurizer, pca_reducer=pca_reducer, xtb_stats=xtb_stats)
        test_dataset = CompactReactionDataset(test_data, featurizer, pca_reducer=pca_reducer, xtb_stats=xtb_stats)

        # 保存PCA
        pca_reducer.save(self.output_dir / 'pca_reducer.pkl')

        batch_size = self.config['training']['batch_size']
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)

        print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")
        continuous_dim = train_dataset.get_continuous_dim()
        print(f"Continuous dim: {continuous_dim}, Solvents: {self.num_solvents}, Electrolytes: {self.num_electrolytes}")
        return continuous_dim

    def setup_xtb_only_data(self):
        """准备仅xTB特征的数据（xTB 55D + echem 6D = 61D）"""
        print("Loading data for xTB-only model...")

        self.data_processor = ReactionDataProcessor(
            yield_data_dir=self.config['data']['yield_data_dir'],
            smiles_data_path=self.config['data']['smiles_data_path']
        )
        train_data, val_data, test_data = self.data_processor.prepare_dataset(
            random_seed=self.config['data']['random_seed']
        )

        xtb_config = self.config.get('xtb', {})
        xtb_csv_path = xtb_config.get('csv_path')

        train_dataset = XtbOnlyDataset(train_data, xtb_csv_path)
        xtb_stats = train_dataset.get_xtb_stats()
        val_dataset = XtbOnlyDataset(val_data, xtb_csv_path, xtb_stats=xtb_stats)
        test_dataset = XtbOnlyDataset(test_data, xtb_csv_path, xtb_stats=xtb_stats)

        batch_size = self.config['training']['batch_size']
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)

        print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")
        print(f"Feature dim: 61 (xTB 55D + echem 6D)")
        return 61  # 55 xTB + 6 echem

    def setup_model(self, input_dim: int, model_name: str = 'mlp'):
        """创建模型"""
        print(f"Creating model '{model_name}' with input_dim={input_dim}")

        model_config = self.config['model']['predictor']
        self.model_name = model_name

        if model_name == 'compact':
            self.model = CompactYieldPredictor(
                continuous_dim=input_dim,
                num_solvents=self.num_solvents,
                num_electrolytes=self.num_electrolytes,
                embed_dim=32,
                hidden_dims=[256, 128],
                dropout=model_config['dropout']
            ).to(self.device)
        elif model_name == 'dual_tower_xtb':
            xtb_config = self.config.get('xtb', {})
            fp_dim = 5 * self.config['model']['mol_encoder']['fingerprint_size'] + 6  # 10246
            xtb_dim = xtb_config.get('feature_dim', 55)
            self.model = create_model(
                model_name, input_dim,
                fp_dim=fp_dim, xtb_dim=xtb_dim,
                dropout=model_config['dropout']
            ).to(self.device)
        elif model_name in MODEL_REGISTRY:
            self.model = create_model(
                model_name, input_dim,
                dropout=model_config['dropout']
            ).to(self.device)
        else:
            self.model = YieldPredictor(
                input_dim=input_dim,
                hidden_dims=model_config['hidden_dims'],
                dropout=model_config['dropout']
            ).to(self.device)

        # 打印模型参数量
        num_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"Model parameters: {num_params:,}")

        # 优化器
        self.optimizer = optim.AdamW(
            self.model.parameters(),
            lr=self.config['training']['learning_rate'],
            weight_decay=self.config['training']['weight_decay']
        )

        # 学习率调度器
        total_steps = len(self.train_loader) * self.config['training']['epochs']
        warmup_steps = len(self.train_loader) * self.config['training']['scheduler']['warmup_epochs']

        self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer,
            T_max=total_steps - warmup_steps
        )

        # 损失函数
        self.criterion = nn.MSELoss()

    def _forward(self, batch):
        """统一前向传播：支持标准和compact两种数据格式"""
        if self.model_name == 'compact':
            continuous = batch['continuous'].to(self.device)
            solvent_idx = batch['solvent_idx'].to(self.device)
            electrolyte_idx = batch['electrolyte_idx'].to(self.device)
            labels = batch['label'].to(self.device).unsqueeze(1)
            predictions = self.model(continuous, solvent_idx, electrolyte_idx)
        else:
            features, label_vals = batch
            features = features.to(self.device)
            labels = label_vals.to(self.device).unsqueeze(1)
            predictions = self.model(features)
        return predictions, labels

    def train_epoch(self, epoch: int) -> float:
        """训练一个epoch"""
        self.model.train()
        total_loss = 0.0
        num_batches = 0

        pbar = tqdm(self.train_loader, desc=f"Epoch {epoch}")
        for batch in pbar:
            self.optimizer.zero_grad()
            predictions, labels = self._forward(batch)
            loss = self.criterion(predictions, labels)

            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
            self.scheduler.step()

            total_loss += loss.item()
            num_batches += 1
            pbar.set_postfix({'loss': f'{loss.item():.4f}'})

        avg_loss = total_loss / num_batches
        return avg_loss

    def validate(self) -> dict:
        """验证"""
        self.model.eval()
        total_loss = 0.0
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch in self.val_loader:
                predictions, labels = self._forward(batch)
                loss = self.criterion(predictions, labels)

                total_loss += loss.item()
                all_preds.extend(predictions.cpu().flatten().tolist())
                all_labels.extend(labels.cpu().flatten().tolist())

        # 转换为tensor计算指标
        all_preds = torch.tensor(all_preds) * 100  # 转换为百分比
        all_labels = torch.tensor(all_labels) * 100

        mae = torch.mean(torch.abs(all_preds - all_labels)).item()
        rmse = torch.sqrt(torch.mean((all_preds - all_labels) ** 2)).item()
        ss_res = torch.sum((all_preds - all_labels) ** 2)
        ss_tot = torch.sum((all_labels - torch.mean(all_labels)) ** 2)
        r2 = (1 - ss_res / ss_tot).item()

        return {
            'loss': total_loss / len(self.val_loader),
            'mae': mae,
            'rmse': rmse,
            'r2': r2
        }

    def train(self):
        """完整训练流程"""
        print("Starting training...")

        epochs = self.config['training']['epochs']
        patience = self.config['training']['early_stopping_patience']

        best_val_loss = float('inf')
        patience_counter = 0
        best_epoch = 0

        for epoch in range(1, epochs + 1):
            # 训练
            train_loss = self.train_epoch(epoch)

            # 验证
            val_metrics = self.validate()

            # 记录到TensorBoard
            self.writer.add_scalar('Loss/train', train_loss, epoch)
            self.writer.add_scalar('Loss/val', val_metrics['loss'], epoch)
            self.writer.add_scalar('Metrics/MAE', val_metrics['mae'], epoch)
            self.writer.add_scalar('Metrics/RMSE', val_metrics['rmse'], epoch)
            self.writer.add_scalar('Metrics/R2', val_metrics['r2'], epoch)
            self.writer.add_scalar('LR', self.scheduler.get_last_lr()[0], epoch)

            print(f"Epoch {epoch}: Train Loss={train_loss:.4f}, "
                  f"Val Loss={val_metrics['loss']:.4f}, "
                  f"MAE={val_metrics['mae']:.2f}%, "
                  f"RMSE={val_metrics['rmse']:.2f}%, "
                  f"R²={val_metrics['r2']:.4f}")

            # Early stopping
            if val_metrics['loss'] < best_val_loss:
                best_val_loss = val_metrics['loss']
                best_epoch = epoch
                patience_counter = 0

                # 保存最佳模型
                self.save_checkpoint(epoch, val_metrics, is_best=True)
            else:
                patience_counter += 1
                if patience_counter >= patience:
                    print(f"Early stopping at epoch {epoch}")
                    break

            # 定期保存
            if epoch % 10 == 0:
                self.save_checkpoint(epoch, val_metrics, is_best=False)

        print(f"Best model at epoch {best_epoch} with val_loss={best_val_loss:.4f}")
        self.writer.close()

    def save_checkpoint(self, epoch: int, metrics: dict, is_best: bool = False):
        """保存检查点"""
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'scheduler_state_dict': self.scheduler.state_dict(),
            'metrics': metrics,
            'config': self.config
        }

        if is_best:
            path = self.output_dir / 'best_model.pt'
        else:
            path = self.output_dir / f'checkpoint_epoch_{epoch}.pt'

        torch.save(checkpoint, path)
        print(f"Saved checkpoint to {path}")

    def test(self):
        """测试"""
        print("\nEvaluating on test set...")

        # 加载最佳模型
        checkpoint = torch.load(self.output_dir / 'best_model.pt')
        self.model.load_state_dict(checkpoint['model_state_dict'])

        self.model.eval()
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch in tqdm(self.test_loader, desc="Testing"):
                predictions, labels = self._forward(batch)
                all_preds.extend(predictions.cpu().flatten().tolist())
                all_labels.extend(labels.cpu().flatten().tolist())

        all_preds = torch.tensor(all_preds) * 100
        all_labels = torch.tensor(all_labels) * 100

        mae = torch.mean(torch.abs(all_preds - all_labels)).item()
        rmse = torch.sqrt(torch.mean((all_preds - all_labels) ** 2)).item()
        ss_res = torch.sum((all_preds - all_labels) ** 2)
        ss_tot = torch.sum((all_labels - torch.mean(all_labels)) ** 2)
        r2 = (1 - ss_res / ss_tot).item()

        print(f"\nTest Results:")
        print(f"  MAE:  {mae:.2f}%")
        print(f"  RMSE: {rmse:.2f}%")
        print(f"  R²:   {r2:.4f}")

        # 保存测试结果
        results = {
            'mae': float(mae),
            'rmse': float(rmse),
            'r2': float(r2),
            'predictions': all_preds.tolist(),
            'labels': all_labels.tolist()
        }

        import json
        with open(self.output_dir / 'test_results.json', 'w') as f:
            json.dump(results, f, indent=2)

        return results


def main():
    parser = argparse.ArgumentParser(description='Train yield prediction model')
    parser.add_argument('--config', type=str, default='configs/config.yaml',
                        help='Path to config file')
    parser.add_argument('--device', type=str, default=None,
                        help='Device to use (cuda/cpu)')
    parser.add_argument('--model', type=str, default='mlp',
                        help='Model architecture: mlp, resnet, dual_tower_xtb, etc.')
    parser.add_argument('--include_failed', action='store_true',
                        help='Include failed reactions (yield=0) from extracted_smiles.json')
    parser.add_argument('--failed_weight', type=float, default=2.0,
                        help='Sample weight multiplier for failed reactions (default: 2.0)')
    args = parser.parse_args()

    # 加载配置
    config_path = project_root / args.config
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # 创建训练器
    trainer = Trainer(config, device=args.device,
                      include_failed=args.include_failed,
                      failed_weight=args.failed_weight)

    # 准备数据
    if args.model == 'compact':
        input_dim = trainer.setup_compact_data(pca_components=128)
    elif args.model == 'xtb_only':
        input_dim = trainer.setup_xtb_only_data()
    else:
        input_dim = trainer.setup_data()

    # 创建模型
    trainer.setup_model(input_dim, model_name=args.model)

    # 训练
    trainer.train()

    # 测试
    trainer.test()


if __name__ == "__main__":
    main()
