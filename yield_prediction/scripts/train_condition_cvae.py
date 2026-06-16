"""
训练脚本：Categorical CVAE 条件推荐模型

复用 train_condition.py 中的 ConditionDataset 和 ConditionTrainer.build_vocabulary/setup_data，
新增 KL annealing、VAE 损失、梯度裁剪等。

用法:
    python scripts/train_condition_cvae.py
    python scripts/train_condition_cvae.py --config configs/config.yaml --epochs 60
"""
import os
import sys
import argparse
import yaml
import json
from pathlib import Path
from datetime import datetime
from collections import Counter

# 先导入torch（使用系统numpy），再加pip_packages
import torch
import numpy

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.append(LOCAL_PACKAGES)
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import MolecularFeatureExtractor
from models.condition_cvae import CategoricalCVAE
from scripts.train_condition import ConditionDataset
from utils.pca_reducer import FingerprintPCAReducer
from utils.electrode_normalizer import NUM_ELECTRODE_TYPES


# ── KL Annealing ──────────────────────────────────────────

class KLAnnealingScheduler:
    """
    β warmup 调度器：从 0 线性升至 beta_max，防止后验坍缩。

    Args:
        warmup_epochs: warmup 阶段的 epoch 数
        beta_max: β 的目标上限
    """

    def __init__(self, warmup_epochs: int = 20, beta_max: float = 0.1):
        self.warmup_epochs = warmup_epochs
        self.beta_max = beta_max

    def get_beta(self, epoch: int) -> float:
        """根据当前 epoch 返回 β 值"""
        if epoch >= self.warmup_epochs:
            return self.beta_max
        return self.beta_max * (epoch / self.warmup_epochs)


# ── CVAE Trainer ──────────────────────────────────────────

class CVAEConditionTrainer:
    """Categorical CVAE 条件推荐模型训练器"""

    CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte',
                      'solvent', 'reagent', 'catalyst']
    TOP_KS = [1, 3, 5, 10]

    def __init__(self, config: dict, device: str = None):
        self.config = config
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.use_yield_weighting = False  # 是否按产率加权损失
        print(f"Using device: {self.device}")

        self.output_dir = Path(config['output']['model_dir']) / 'condition_model'
        self.output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.writer = SummaryWriter(
            Path(config['output']['log_dir']) / f'condition_cvae_{timestamp}'
        )

        self.ce_loss = None  # 在 setup_model 或 train 前根据 use_yield_weighting 设置

    # ── 数据准备（复用 ConditionTrainer 的逻辑）──────────

    def build_vocabulary(self, reactions: list):
        """构建词汇表（与 ConditionTrainer 完全一致）"""
        electrolytes = Counter()
        solvents = Counter()
        reagents = Counter()
        catalysts = Counter()

        for rxn in reactions:
            echem = rxn.get('electrochemistry_params', {})
            elec = echem.get('electrolyte', '')
            if elec:
                electrolytes[elec] += 1

            for s in rxn.get('solvents', []):
                smiles = s.get('smiles', '')
                if smiles:
                    solvents[smiles] += 1

            for r in rxn.get('reagents', []):
                smiles = r.get('smiles', '')
                if smiles:
                    reagents[smiles] += 1

            for c in rxn.get('catalysts', []):
                smiles = c.get('smiles', '')
                if smiles:
                    catalysts[smiles] += 1

        # 全部纳入词汇表（按频率排序，index 0 保留给 UNK）
        electrolyte_vocab = {e: i + 1 for i, (e, _) in enumerate(electrolytes.most_common())}
        solvent_vocab = {s: i + 1 for i, (s, _) in enumerate(solvents.most_common())}
        reagent_vocab = {r: i + 1 for i, (r, _) in enumerate(reagents.most_common())}
        catalyst_vocab = {c: i + 1 for i, (c, _) in enumerate(catalysts.most_common())}

        return electrolyte_vocab, solvent_vocab, reagent_vocab, catalyst_vocab

    def setup_data(self):
        """准备数据（与 ConditionTrainer.setup_data 一致）"""
        print("Loading data for CVAE condition recommendation...")

        processor = ReactionDataProcessor(
            yield_data_dir=self.config['data']['yield_data_dir'],
            smiles_data_path=self.config['data']['smiles_data_path']
        )

        if self.use_yield_weighting:
            reactions = processor.load_combined_data(include_failed=True)
        else:
            reactions = processor.load_yield_data()

        # 构建词汇表（仅基于有产率的反应）
        vocab_reactions = [r for r in reactions if r.get('yield_value', 0) > 0]
        self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab, self.catalyst_vocab = \
            self.build_vocabulary(vocab_reactions)
        print(f"Electrolyte vocab size: {len(self.electrolyte_vocab)}")
        print(f"Solvent vocab size: {len(self.solvent_vocab)}")
        print(f"Reagent vocab size: {len(self.reagent_vocab)}")
        print(f"Catalyst vocab size: {len(self.catalyst_vocab)}")

        # 保存词汇表（CVAE 与默认模型共享同一 vocab）
        vocab = {
            'electrolyte': self.electrolyte_vocab,
            'solvent': self.solvent_vocab,
            'reagent': self.reagent_vocab,
            'catalyst': self.catalyst_vocab,
        }
        with open(self.output_dir / 'vocab.json', 'w') as f:
            json.dump(vocab, f, indent=2)

        # 分割数据
        from sklearn.model_selection import train_test_split
        train_rxn, temp_rxn = train_test_split(reactions, test_size=0.2, random_state=42)
        val_rxn, test_rxn = train_test_split(temp_rxn, test_size=0.5, random_state=42)

        # 特征提取器
        fp_size = self.config['model']['mol_encoder']['fingerprint_size']
        self.mol_extractor = MolecularFeatureExtractor(fp_size)

        # xTB 特征（可选）
        xtb_lookup = None
        xtb_config = self.config.get('xtb', {})
        if xtb_config.get('use_xtb', False):
            from utils.xtb_features import XTBFeatureLookup
            xtb_lookup = XTBFeatureLookup(xtb_config.get('csv_path'))
            print(f"xTB特征已加载，共 {len(xtb_lookup.xtb_lookup)} 个分子")

        # 创建数据集
        train_dataset = ConditionDataset(
            train_rxn, self.mol_extractor,
            self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
            catalyst_vocab=self.catalyst_vocab,
            xtb_lookup=xtb_lookup,
        )
        xtb_stats = train_dataset.compute_xtb_stats()

        val_dataset = ConditionDataset(
            val_rxn, self.mol_extractor,
            self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
            catalyst_vocab=self.catalyst_vocab,
            xtb_lookup=xtb_lookup, xtb_stats=xtb_stats,
        )
        test_dataset = ConditionDataset(
            test_rxn, self.mol_extractor,
            self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
            catalyst_vocab=self.catalyst_vocab,
            xtb_lookup=xtb_lookup, xtb_stats=xtb_stats,
        )

        batch_size = self.config['training']['batch_size']
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

        print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

        # 特征维度
        reaction_dim = fp_size * 3  # 6144
        if xtb_config.get('use_xtb', False):
            reaction_dim += 33
        print(f"特征总维度: {reaction_dim}")
        return reaction_dim

    def setup_model(self, reaction_dim: int):
        """创建 CategoricalCVAE 模型"""
        # 根据 yield 加权模式设置 CE loss
        self.ce_loss = nn.CrossEntropyLoss(
            reduction='none' if self.use_yield_weighting else 'mean'
        )

        self.model = CategoricalCVAE(
            reaction_dim=reaction_dim,
            repr_dim=256,
            latent_dim=64,
            num_anode_materials=NUM_ELECTRODE_TYPES,
            num_cathode_materials=NUM_ELECTRODE_TYPES,
            num_cell_types=6,
            num_electrolytes=len(self.electrolyte_vocab) + 1,
            num_solvents=len(self.solvent_vocab) + 1,
            num_reagents=len(self.reagent_vocab) + 1,
            num_catalysts=len(self.catalyst_vocab) + 1,
            dropout=0.2,
        ).to(self.device)

        self.optimizer = optim.AdamW(
            self.model.parameters(),
            lr=self.config['training']['learning_rate'],
            weight_decay=self.config['training']['weight_decay'],
        )

    # ── 训练循环 ──────────────────────────────────────────

    def compute_loss(
        self,
        predictions: dict,
        batch: dict,
        mu: torch.Tensor,
        logvar: torch.Tensor,
        beta: float,
    ) -> tuple:
        """
        计算 CVAE 损失: L = Σ CE_i + β × KL

        Returns:
            total_loss, recon_loss, kl_loss
        """
        if self.use_yield_weighting:
            # per-sample CE，按 yield 加权
            yield_weight = batch['yield_weight'].to(self.device).clamp(min=0.05)
            recon_loss_per_sample = torch.zeros(mu.size(0), device=self.device)
            for key in self.CONDITION_KEYS:
                logits = predictions[f'{key}_logits']
                labels = batch[key].to(self.device)
                recon_loss_per_sample = recon_loss_per_sample + self.ce_loss(logits, labels)
            recon_loss = (recon_loss_per_sample * yield_weight).mean()
        else:
            # 标准 mean CE
            recon_loss = torch.tensor(0.0, device=self.device)
            for key in self.CONDITION_KEYS:
                logits = predictions[f'{key}_logits']
                labels = batch[key].to(self.device)
                recon_loss = recon_loss + self.ce_loss(logits, labels)

        # KL 散度: KL(q(z|x,c) || N(0,I))
        kl_loss = -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp())

        total_loss = recon_loss + beta * kl_loss
        return total_loss, recon_loss, kl_loss

    def train_epoch(self, epoch: int, beta: float) -> dict:
        """训练一个 epoch"""
        self.model.train()
        total_loss = 0.0
        total_recon = 0.0
        total_kl = 0.0
        num_batches = 0

        for batch in tqdm(self.train_loader, desc=f"Epoch {epoch}"):
            reaction_fp = batch['reaction_fp'].to(self.device)

            self.optimizer.zero_grad()

            # 前向传播
            predictions, mu, logvar = self.model(
                reaction_fp,
                batch['anode'].to(self.device),
                batch['cathode'].to(self.device),
                batch['cell_type'].to(self.device),
                batch['electrolyte'].to(self.device),
                batch['solvent'].to(self.device),
                batch['reagent'].to(self.device),
                batch['catalyst'].to(self.device),
            )

            # 计算损失
            loss, recon_loss, kl_loss = self.compute_loss(
                predictions, batch, mu, logvar, beta
            )

            loss.backward()

            # 梯度裁剪
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=5.0)

            self.optimizer.step()

            total_loss += loss.item()
            total_recon += recon_loss.item()
            total_kl += kl_loss.item()
            num_batches += 1

        return {
            'total': total_loss / num_batches,
            'recon': total_recon / num_batches,
            'kl': total_kl / num_batches,
        }

    def validate(self) -> dict:
        """验证：z=0 确定性评估，计算 top-1/3/5/10 准确率"""
        self.model.eval()
        correct = {
            key: {k: 0 for k in self.TOP_KS}
            for key in self.CONDITION_KEYS
        }
        total = 0

        with torch.no_grad():
            for batch in self.val_loader:
                reaction_fp = batch['reaction_fp'].to(self.device)

                # z=0 确定性预测
                predictions = self.model.recommend(reaction_fp)

                total += reaction_fp.size(0)
                for key in self.CONDITION_KEYS:
                    logits = predictions[f'{key}_logits']
                    label = batch[key].to(self.device)  # [B]
                    num_cls = logits.size(-1)

                    for k in self.TOP_KS:
                        real_k = min(k, num_cls)
                        top_k_preds = logits.topk(real_k, dim=-1).indices  # [B, k]
                        hit = (top_k_preds == label.unsqueeze(1)).any(dim=1)  # [B]
                        correct[key][k] += hit.sum().item()

        accuracy = {
            key: {k: correct[key][k] / total for k in self.TOP_KS}
            for key in self.CONDITION_KEYS
        }
        return accuracy

    def train(self, epochs: int = 60, warmup_epochs: int = 20, beta_max: float = 0.1):
        """完整训练"""
        print(f"\nStarting CVAE condition model training...")
        print(f"  epochs={epochs}, warmup_epochs={warmup_epochs}, beta_max={beta_max}")

        kl_scheduler = KLAnnealingScheduler(warmup_epochs=warmup_epochs, beta_max=beta_max)
        best_acc = 0

        for epoch in range(1, epochs + 1):
            beta = kl_scheduler.get_beta(epoch)

            # 训练
            losses = self.train_epoch(epoch, beta)

            # 验证
            val_acc = self.validate()
            avg_top1 = sum(val_acc[k][1] for k in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)

            # 打印 top-1 摘要
            print(
                f"Epoch {epoch}: "
                f"Loss={losses['total']:.4f} (recon={losses['recon']:.4f}, kl={losses['kl']:.4f}), "
                f"β={beta:.4f}, "
                f"Anode={val_acc['anode'][1]:.3f}, "
                f"Cathode={val_acc['cathode'][1]:.3f}, "
                f"Cell={val_acc['cell_type'][1]:.3f}, "
                f"Elec={val_acc['electrolyte'][1]:.3f}, "
                f"Solv={val_acc['solvent'][1]:.3f}, "
                f"Reag={val_acc['reagent'][1]:.3f}, "
                f"Cata={val_acc['catalyst'][1]:.3f}, "
                f"Avg={avg_top1:.3f}"
            )

            # 打印 top-k 汇总
            for k in self.TOP_KS:
                avg_k = sum(val_acc[key][k] for key in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)
                details = " | ".join(f"{key}={val_acc[key][k]:.3f}" for key in self.CONDITION_KEYS)
                print(f"  Top-{k:<2d} Avg={avg_k:.3f}  ({details})")

            # TensorBoard
            self.writer.add_scalar('Loss/total', losses['total'], epoch)
            self.writer.add_scalar('Loss/recon', losses['recon'], epoch)
            self.writer.add_scalar('Loss/kl', losses['kl'], epoch)
            self.writer.add_scalar('Beta', beta, epoch)
            for key in self.CONDITION_KEYS:
                for k in self.TOP_KS:
                    self.writer.add_scalar(f'Accuracy_top{k}/{key}', val_acc[key][k], epoch)
            for k in self.TOP_KS:
                avg_k = sum(val_acc[key][k] for key in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)
                self.writer.add_scalar(f'Accuracy_top{k}/avg', avg_k, epoch)

            # 保存最佳模型（按 top-1 平均）
            if avg_top1 > best_acc:
                best_acc = avg_top1
                save_path = self.output_dir / 'best_cvae_condition_model.pt'
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'accuracy': val_acc,
                    'avg_accuracy': avg_top1,
                    'num_classes': self.model.num_classes,
                }, save_path)
                print(f"  -> Saved best model (avg_top1={avg_top1:.4f})")

        self.writer.close()
        print(f"\nTraining complete. Best avg top-1 accuracy: {best_acc:.4f}")
        return best_acc


# ── main ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='训练 Categorical CVAE 条件推荐模型')
    parser.add_argument('--config', type=str, default='configs/config.yaml',
                        help='配置文件路径')
    parser.add_argument('--epochs', type=int, default=60,
                        help='训练轮数 (默认: 60)')
    parser.add_argument('--warmup_epochs', type=int, default=20,
                        help='β warmup 轮数 (默认: 20)')
    parser.add_argument('--beta_max', type=float, default=0.1,
                        help='KL 权重上限 (默认: 0.1)')
    parser.add_argument('--device', type=str, default=None,
                        help='设备 (cuda/cpu)')
    parser.add_argument('--yield_weighted', action='store_true',
                        help='按产率加权条件损失（包含失败反应数据）')
    args = parser.parse_args()

    config_path = project_root / args.config
    with open(config_path) as f:
        config = yaml.safe_load(f)

    trainer = CVAEConditionTrainer(config, device=args.device)
    trainer.use_yield_weighting = args.yield_weighted
    if args.yield_weighted:
        print("Yield-weighted training enabled: failed reactions will suppress bad conditions")

    # 数据准备
    reaction_dim = trainer.setup_data()

    # 模型创建
    trainer.setup_model(reaction_dim)

    num_params = sum(p.numel() for p in trainer.model.parameters() if p.requires_grad)
    print(f"Model parameters: {num_params:,}")

    # 训练
    trainer.train(
        epochs=args.epochs,
        warmup_epochs=args.warmup_epochs,
        beta_max=args.beta_max,
    )


if __name__ == "__main__":
    main()
