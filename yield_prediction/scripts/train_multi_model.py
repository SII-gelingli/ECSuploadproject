"""
多模型训练脚本：支持不同架构的对比实验
"""
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.architectures import create_model, get_model_info, MODEL_REGISTRY


class YieldDataset(Dataset):
    """产率预测数据集"""

    def __init__(self, data_path: str):
        self.data = torch.load(data_path, weights_only=False)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        # 组合特征
        features = (
            item['reactant_fp'] +
            item['product_fp'] +
            item['diff_fp'] +
            item['solvent_fp'] +
            item['electrolyte_fp'] +
            [item['anode'], item['cathode'], item['cell_type'],
             item['electrolyte_label'], item['solvent_label'], item['reagent_label']]
        )

        return (
            torch.tensor(features, dtype=torch.float32),
            torch.tensor(item['yield'] / 100.0, dtype=torch.float32)
        )


class MultiModelTrainer:
    """多模型训练器"""

    def __init__(self, model_name: str, data_dir: str, output_dir: str, device: str = None):
        self.model_name = model_name
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir) / model_name
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.writer = SummaryWriter(self.output_dir / f'logs_{timestamp}')

        print(f"Model: {model_name}")
        print(f"Device: {self.device}")

    def setup_data(self, batch_size: int = 32):
        """加载数据"""
        print("Loading data...")

        train_dataset = YieldDataset(self.data_dir / 'train.pt')
        val_dataset = YieldDataset(self.data_dir / 'val.pt')
        test_dataset = YieldDataset(self.data_dir / 'test.pt')

        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)

        # 获取输入维度
        sample_x, _ = train_dataset[0]
        self.input_dim = sample_x.shape[0]

        print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")
        print(f"Input dim: {self.input_dim}")

        return self.input_dim

    def setup_model(self, input_dim: int, lr: float = 0.001, weight_decay: float = 0.0001, **model_kwargs):
        """创建模型"""
        self.model = create_model(self.model_name, input_dim, **model_kwargs).to(self.device)

        num_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"Model parameters: {num_params:,}")

        self.optimizer = optim.AdamW(self.model.parameters(), lr=lr, weight_decay=weight_decay)
        self.scheduler = optim.lr_scheduler.CosineAnnealingLR(self.optimizer, T_max=100)
        self.criterion = nn.MSELoss()

    def train_epoch(self, epoch: int):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0.0

        for features, labels in tqdm(self.train_loader, desc=f"Epoch {epoch}"):
            features = features.to(self.device)
            labels = labels.to(self.device).unsqueeze(1)

            self.optimizer.zero_grad()
            predictions = self.model(features)
            loss = self.criterion(predictions, labels)

            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()

            total_loss += loss.item()

        self.scheduler.step()
        return total_loss / len(self.train_loader)

    def validate(self):
        """验证"""
        self.model.eval()
        total_loss = 0.0
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for features, labels in self.val_loader:
                features = features.to(self.device)
                labels = labels.to(self.device).unsqueeze(1)

                predictions = self.model(features)
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
        r2 = (1 - ss_res / ss_tot).item()

        return {
            'loss': total_loss / len(self.val_loader),
            'mae': mae,
            'rmse': rmse,
            'r2': r2
        }

    def train(self, epochs: int = 100, patience: int = 15):
        """完整训练"""
        print(f"\nTraining {self.model_name}...")

        best_val_loss = float('inf')
        patience_counter = 0
        best_metrics = {}

        for epoch in range(1, epochs + 1):
            train_loss = self.train_epoch(epoch)
            val_metrics = self.validate()

            # 日志
            self.writer.add_scalar('Loss/train', train_loss, epoch)
            self.writer.add_scalar('Loss/val', val_metrics['loss'], epoch)
            self.writer.add_scalar('Metrics/MAE', val_metrics['mae'], epoch)
            self.writer.add_scalar('Metrics/RMSE', val_metrics['rmse'], epoch)
            self.writer.add_scalar('Metrics/R2', val_metrics['r2'], epoch)

            print(f"Epoch {epoch}: Train={train_loss:.4f}, Val={val_metrics['loss']:.4f}, "
                  f"MAE={val_metrics['mae']:.2f}%, RMSE={val_metrics['rmse']:.2f}%, R²={val_metrics['r2']:.4f}")

            # Early stopping
            if val_metrics['loss'] < best_val_loss:
                best_val_loss = val_metrics['loss']
                best_metrics = val_metrics.copy()
                patience_counter = 0

                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'metrics': val_metrics,
                    'model_name': self.model_name
                }, self.output_dir / 'best_model.pt')
            else:
                patience_counter += 1
                if patience_counter >= patience:
                    print(f"Early stopping at epoch {epoch}")
                    break

        self.writer.close()
        return best_metrics

    def test(self):
        """测试"""
        # 加载最佳模型
        checkpoint = torch.load(self.output_dir / 'best_model.pt', weights_only=False)
        self.model.load_state_dict(checkpoint['model_state_dict'])

        self.model.eval()
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for features, labels in tqdm(self.test_loader, desc="Testing"):
                features = features.to(self.device)
                predictions = self.model(features)

                all_preds.extend(predictions.cpu().flatten().tolist())
                all_labels.extend(labels.tolist())

        preds = torch.tensor(all_preds) * 100
        labels = torch.tensor(all_labels) * 100

        mae = torch.mean(torch.abs(preds - labels)).item()
        rmse = torch.sqrt(torch.mean((preds - labels) ** 2)).item()
        ss_res = torch.sum((preds - labels) ** 2)
        ss_tot = torch.sum((labels - torch.mean(labels)) ** 2)
        r2 = (1 - ss_res / ss_tot).item()

        results = {'mae': mae, 'rmse': rmse, 'r2': r2}

        print(f"\n{self.model_name} Test Results:")
        print(f"  MAE:  {mae:.2f}%")
        print(f"  RMSE: {rmse:.2f}%")
        print(f"  R²:   {r2:.4f}")

        with open(self.output_dir / 'test_results.json', 'w') as f:
            json.dump(results, f, indent=2)

        return results


def compare_models(data_dir: str, output_dir: str, models: list = None, epochs: int = 50):
    """比较多个模型"""
    models = models or list(MODEL_REGISTRY.keys())
    results = {}

    for model_name in models:
        print(f"\n{'='*60}")
        print(f"Training: {model_name}")
        print('='*60)

        try:
            trainer = MultiModelTrainer(model_name, data_dir, output_dir)
            input_dim = trainer.setup_data(batch_size=32)
            trainer.setup_model(input_dim)
            trainer.train(epochs=epochs, patience=10)
            test_results = trainer.test()
            results[model_name] = test_results
        except Exception as e:
            print(f"Error training {model_name}: {e}")
            results[model_name] = {'error': str(e)}

    # 汇总结果
    print("\n" + "="*60)
    print("MODEL COMPARISON RESULTS")
    print("="*60)
    print(f"{'Model':<20} {'MAE':>10} {'RMSE':>10} {'R²':>10}")
    print("-"*60)

    for model_name, res in sorted(results.items(), key=lambda x: x[1].get('mae', 999)):
        if 'error' in res:
            print(f"{model_name:<20} {'ERROR':>10}")
        else:
            print(f"{model_name:<20} {res['mae']:>10.2f}% {res['rmse']:>10.2f}% {res['r2']:>10.4f}")

    # 保存比较结果
    with open(Path(output_dir) / 'comparison_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    return results


def main():
    parser = argparse.ArgumentParser(description='Train yield prediction models')
    parser.add_argument('--model', type=str, default='mlp',
                        choices=list(MODEL_REGISTRY.keys()),
                        help='Model architecture')
    parser.add_argument('--compare', action='store_true',
                        help='Compare all models')
    parser.add_argument('--models', type=str, nargs='+',
                        help='Models to compare (if --compare)')
    parser.add_argument('--data-dir', type=str, default='data',
                        help='Data directory')
    parser.add_argument('--output-dir', type=str, default='checkpoints',
                        help='Output directory')
    parser.add_argument('--epochs', type=int, default=100,
                        help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--lr', type=float, default=0.001)

    args = parser.parse_args()

    data_dir = project_root / args.data_dir
    output_dir = project_root / args.output_dir

    if args.compare:
        compare_models(str(data_dir), str(output_dir), args.models, args.epochs)
    else:
        trainer = MultiModelTrainer(args.model, str(data_dir), str(output_dir))
        input_dim = trainer.setup_data(batch_size=args.batch_size)
        trainer.setup_model(input_dim, lr=args.lr)
        trainer.train(epochs=args.epochs)
        trainer.test()


if __name__ == "__main__":
    main()
