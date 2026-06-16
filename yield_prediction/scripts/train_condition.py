"""
训练脚本：条件推荐模型训练
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
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import MolecularFeatureExtractor
from models.condition_recommender import ConditionRecommender, DualTowerConditionRecommender, CompactConditionRecommender
from utils.pca_reducer import FingerprintPCAReducer
from utils.electrode_normalizer import electrode_to_id, NUM_ELECTRODE_TYPES


class ConditionDataset(Dataset):
    """条件推荐数据集（支持xTB特征和PCA降维）"""

    def __init__(self, reactions: list, mol_extractor: MolecularFeatureExtractor,
                 electrolyte_vocab: dict, solvent_vocab: dict, reagent_vocab: dict,
                 catalyst_vocab: dict = None,
                 xtb_lookup=None, xtb_stats=None,
                 pca_reducer=None, xtb_only: bool = False):
        self.reactions = reactions
        self.mol_extractor = mol_extractor
        self.electrolyte_vocab = electrolyte_vocab
        self.solvent_vocab = solvent_vocab
        self.reagent_vocab = reagent_vocab
        self.catalyst_vocab = catalyst_vocab or {}
        self.xtb_lookup = xtb_lookup
        self.xtb_stats = xtb_stats
        self.pca_reducer = pca_reducer
        self.xtb_only = xtb_only

        self.data = []
        self._prepare_data()

    def _prepare_data(self):
        """准备数据"""
        import numpy as np
        raw_fps = []  # 收集原始指纹用于PCA

        for rxn in tqdm(self.reactions, desc="Preparing condition data"):
            try:
                # 提取反应指纹（xtb_only模式跳过）
                reaction_fp = []
                if not self.xtb_only:
                    reactant_fp = self.mol_extractor.encode_molecules(
                        [r.get('smiles', '') for r in rxn.get('reactants', [])]
                    )
                    product_fp = self.mol_extractor.encode_molecules(
                        [p.get('smiles', '') for p in rxn.get('products', [])]
                    )
                    reactant_t = torch.tensor(reactant_fp, dtype=torch.float32)
                    product_t = torch.tensor(product_fp, dtype=torch.float32)
                    diff_t = torch.abs(product_t - reactant_t)
                    reaction_fp = torch.cat([reactant_t, product_t, diff_t]).tolist()

                # 提取条件标签
                echem = rxn.get('electrochemistry_params', {})

                anode_label = self._encode_electrode(echem.get('anode', ''))
                cathode_label = self._encode_electrode(echem.get('cathode', ''))
                cell_type_label = self._encode_cell_type(echem.get('cell_type', ''))
                electrolyte_label = self.electrolyte_vocab.get(echem.get('electrolyte', ''), 0)

                solvents = rxn.get('solvents', [])
                solvent_label = self.solvent_vocab.get(solvents[0].get('smiles', ''), 0) if solvents else 0

                reagents = rxn.get('reagents', [])
                reagent_label = self.reagent_vocab.get(reagents[0].get('smiles', ''), 0) if reagents else 0

                catalysts = rxn.get('catalysts', [])
                catalyst_label = self.catalyst_vocab.get(catalysts[0].get('smiles', ''), 0) if catalysts else 0

                # xTB特征（可选） - 只用反应物+产物+差异(33维)
                xtb_feat = []
                if self.xtb_lookup is not None:
                    reactant_smiles = [r.get('smiles', '') for r in rxn.get('reactants', [])]
                    product_smiles = [p.get('smiles', '') for p in rxn.get('products', [])]
                    r_feat = self.xtb_lookup.get_aggregated_features(reactant_smiles)
                    p_feat = self.xtb_lookup.get_aggregated_features(product_smiles)
                    diff_feat = [p_feat[i] - r_feat[i] for i in range(len(r_feat))]
                    xtb_feat = r_feat + p_feat + diff_feat
                    if self.xtb_stats is not None:
                        xtb_feat = np.array(xtb_feat)
                        xtb_feat = (xtb_feat - self.xtb_stats['mean']) / self.xtb_stats['std']
                        xtb_feat = xtb_feat.tolist()

                raw_fps.append(reaction_fp)
                self.data.append({
                    'reaction_fp': reaction_fp,
                    'xtb_feat': xtb_feat,
                    'anode': anode_label,
                    'cathode': cathode_label,
                    'cell_type': cell_type_label,
                    'electrolyte': electrolyte_label,
                    'solvent': solvent_label,
                    'reagent': reagent_label,
                    'catalyst': catalyst_label,
                    'yield_value': float(rxn.get('yield_value', rxn.get('product_yield', 50.0) or 50.0))
                })

            except Exception:
                continue

        # PCA降维（可选，xtb_only模式不需要）
        if self.pca_reducer is not None and not self.xtb_only and len(raw_fps) > 0:
            fp_array = np.array(raw_fps, dtype=np.float32)
            if not self.pca_reducer.is_fitted:
                reduced = self.pca_reducer.fit_transform(fp_array)
            else:
                reduced = self.pca_reducer.transform(fp_array)
            for i in range(len(self.data)):
                self.data[i]['reaction_fp'] = reduced[i].tolist()

    def _encode_electrode(self, electrode):
        """编码电极 — 使用electrode_normalizer统一归一化"""
        return electrode_to_id(electrode)

    # 电解池类别数 = 6 (0~4 + 5=Unknown)
    NUM_CELL_TYPE_CLASSES = 6

    def _encode_cell_type(self, cell_type):
        """编码电解池类型 — 基于关键词匹配（大小写不敏感）。

        类别编号:
            0  undivided  (undivided/beaker-type/ElectraSyn/三颈瓶 等)
            1  divided    (divided/H-cell/two-compartment/diaphragm 等)
            2  flow       (flow electrolytic/Vapourtec 等)
            3  sealed     (sealed 等)
            4  other      (electrochemical/electrolysis cell/其他明确类型)
            5  Unknown/empty
        """
        if cell_type is None or cell_type.strip() == '':
            return 5

        ct = cell_type.lower().strip()

        # 去掉前导/尾随引号和括号
        ct = ct.strip('"\'()')

        # divided 相关（在 undivided 之前，因 "undivided" 包含 "divided"）
        if 'undivi' in ct or 'undvi' in ct or 'udivi' in ct or 'unndiv' in ct or 'undiv' in ct:
            return 0
        if 'beaker' in ct or 'electrasyn' in ct or 'three-neck' in ct or 'bottle' in ct or 'flask' in ct or 'schlenk' in ct:
            return 0

        # divided / H-cell
        if 'h-cell' in ct or 'h-type' in ct or 'h cell' in ct or 'diaphragm' in ct or 'ptfe divided' in ct or 'two-compartment' in ct or 'purged two' in ct or 'compartment' in ct:
            return 1
        if 'divided' in ct or 'devided' in ct or 'separation' in ct or 'ex-cell' in ct:
            return 1

        # flow
        if 'flow' in ct or 'vapourtec' in ct:
            return 2

        # sealed
        if 'sealed' in ct:
            return 3

        # other recognizable types
        if 'electrochem' in ct or 'electrolysis' in ct or 'electrolytic' in ct or 'reactor' in ct:
            return 4

        # Unknown
        return 5

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        features = item['reaction_fp']
        if item.get('xtb_feat'):
            features = features + item['xtb_feat']
        return {
            'reaction_fp': torch.tensor(features, dtype=torch.float32),
            'anode': torch.tensor(item['anode'], dtype=torch.long),
            'cathode': torch.tensor(item['cathode'], dtype=torch.long),
            'cell_type': torch.tensor(item['cell_type'], dtype=torch.long),
            'electrolyte': torch.tensor(item['electrolyte'], dtype=torch.long),
            'solvent': torch.tensor(item['solvent'], dtype=torch.long),
            'reagent': torch.tensor(item['reagent'], dtype=torch.long),
            'catalyst': torch.tensor(item['catalyst'], dtype=torch.long),
            'yield_weight': torch.tensor(item['yield_value'] / 100.0, dtype=torch.float32)
        }

    def compute_xtb_stats(self):
        """计算xTB特征的归一化统计量"""
        if not self.data or not self.data[0].get('xtb_feat'):
            return None
        import numpy as np
        xtb_feats = np.array([d['xtb_feat'] for d in self.data if d.get('xtb_feat')])
        return {
            'mean': np.mean(xtb_feats, axis=0),
            'std': np.std(xtb_feats, axis=0) + 1e-8
        }


class ConditionTrainer:
    """条件推荐模型训练器"""

    def __init__(self, config: dict, device: str = None):
        self.config = config
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.use_yield_weighting = False  # 是否按产率加权损失
        print(f"Using device: {self.device}")

        self.output_dir = Path(config['output']['model_dir']) / 'condition_model'
        self.output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.writer = SummaryWriter(Path(config['output']['log_dir']) / f'condition_{timestamp}')

    def build_vocabulary(self, reactions: list):
        """构建电解质、溶剂、试剂和催化剂词汇表"""
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
        """准备数据"""
        print("Loading data for condition recommendation...")

        processor = ReactionDataProcessor(
            yield_data_dir=self.config['data']['yield_data_dir'],
            smiles_data_path=self.config['data']['smiles_data_path']
        )

        # yield 加权模式：加载失败反应一起训练（权重由 yield 决定）
        if self.use_yield_weighting:
            reactions = processor.load_combined_data(include_failed=True)
        else:
            reactions = processor.load_yield_data()

        # 构建词汇表（仅基于有产率的反应，不让失败反应影响词表）
        vocab_reactions = [r for r in reactions if r.get('yield_value', 0) > 0]
        self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab, self.catalyst_vocab = self.build_vocabulary(vocab_reactions)
        print(f"Electrolyte vocab size: {len(self.electrolyte_vocab)}")
        print(f"Solvent vocab size: {len(self.solvent_vocab)}")
        print(f"Reagent vocab size: {len(self.reagent_vocab)}")
        print(f"Catalyst vocab size: {len(self.catalyst_vocab)}")

        # 保存词汇表
        vocab = {
            'electrolyte': self.electrolyte_vocab,
            'solvent': self.solvent_vocab,
            'reagent': self.reagent_vocab,
            'catalyst': self.catalyst_vocab
        }
        with open(self.output_dir / 'vocab.json', 'w') as f:
            json.dump(vocab, f, indent=2)

        # 分割数据
        from sklearn.model_selection import train_test_split
        train_rxn, temp_rxn = train_test_split(reactions, test_size=0.2, random_state=42)
        val_rxn, test_rxn = train_test_split(temp_rxn, test_size=0.5, random_state=42)

        # 创建数据集
        fp_size = self.config['model']['mol_encoder']['fingerprint_size']
        self.mol_extractor = MolecularFeatureExtractor(fp_size)

        # xTB特征（可选）
        xtb_lookup = None
        xtb_config = self.config.get('xtb', {})
        if xtb_config.get('use_xtb', False):
            from utils.xtb_features import XTBFeatureLookup
            xtb_lookup = XTBFeatureLookup(xtb_config.get('csv_path'))
            print(f"xTB特征已加载，共 {len(xtb_lookup.xtb_lookup)} 个分子")

        # PCA降维器（compact模式）
        pca_reducer = self.pca_reducer if hasattr(self, 'pca_reducer') else None
        xtb_only = getattr(self, 'xtb_only', False)

        # 训练集先计算xTB统计量（训练集fit PCA）
        train_dataset = ConditionDataset(train_rxn, self.mol_extractor,
                                         self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
                                         catalyst_vocab=self.catalyst_vocab,
                                         xtb_lookup=xtb_lookup,
                                         pca_reducer=pca_reducer,
                                         xtb_only=xtb_only)
        xtb_stats = train_dataset.compute_xtb_stats()

        # 验证/测试集使用训练集统计量归一化（PCA已fitted，只transform）
        val_dataset = ConditionDataset(val_rxn, self.mol_extractor,
                                       self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
                                       catalyst_vocab=self.catalyst_vocab,
                                       xtb_lookup=xtb_lookup, xtb_stats=xtb_stats,
                                       pca_reducer=pca_reducer,
                                       xtb_only=xtb_only)
        test_dataset = ConditionDataset(test_rxn, self.mol_extractor,
                                        self.electrolyte_vocab, self.solvent_vocab, self.reagent_vocab,
                                        catalyst_vocab=self.catalyst_vocab,
                                        xtb_lookup=xtb_lookup, xtb_stats=xtb_stats,
                                        pca_reducer=pca_reducer,
                                        xtb_only=xtb_only)

        batch_size = self.config['training']['batch_size']
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        self.val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

        print(f"Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")

        # 特征维度
        if xtb_only:
            reaction_dim = 33  # 仅xTB: 反应物(11) + 产物(11) + 差异(11)
        elif pca_reducer is not None:
            reaction_dim = pca_reducer.n_components  # PCA降维后维度
            if xtb_config.get('use_xtb', False):
                reaction_dim += 33
        else:
            reaction_dim = fp_size * 3
            if xtb_config.get('use_xtb', False):
                reaction_dim += 33
        print(f"特征总维度: {reaction_dim}")
        return reaction_dim

    def setup_model(self, reaction_dim: int, model_type: str = 'default',
                    fp_dim: int = 6144, xtb_dim: int = 33):
        """创建模型"""
        num_classes = dict(
            num_anode_materials=NUM_ELECTRODE_TYPES,
            num_cathode_materials=NUM_ELECTRODE_TYPES,
            num_cell_types=6,
            num_electrolytes=len(self.electrolyte_vocab) + 1,
            num_solvents=len(self.solvent_vocab) + 1,
            num_reagents=len(self.reagent_vocab) + 1,
            num_catalysts=len(self.catalyst_vocab) + 1,
        )

        if model_type in ('compact', 'xtb_only'):
            print(f"使用Compact模型: input_dim={reaction_dim}")
            self.model = CompactConditionRecommender(
                input_dim=reaction_dim, hidden_dim=256, dropout=0.2, **num_classes
            ).to(self.device)
        elif model_type == 'dual_tower':
            print(f"使用双塔模型: fp_dim={fp_dim}, xtb_dim={xtb_dim}")
            self.model = DualTowerConditionRecommender(
                fp_dim=fp_dim, xtb_dim=xtb_dim, dropout=0.2, **num_classes
            ).to(self.device)
        else:
            self.model = ConditionRecommender(
                reaction_dim=reaction_dim, hidden_dim=256, dropout=0.2, **num_classes
            ).to(self.device)

        self.optimizer = optim.AdamW(
            self.model.parameters(),
            lr=self.config['training']['learning_rate'],
            weight_decay=self.config['training']['weight_decay']
        )

        self.ce_loss = nn.CrossEntropyLoss(
            reduction='none' if self.use_yield_weighting else 'mean'
        )

    def train_epoch(self, epoch: int):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0.0

        for batch in tqdm(self.train_loader, desc=f"Epoch {epoch}"):
            reaction_fp = batch['reaction_fp'].to(self.device)
            anode = batch['anode'].to(self.device)
            cathode = batch['cathode'].to(self.device)
            cell_type = batch['cell_type'].to(self.device)
            electrolyte = batch['electrolyte'].to(self.device)
            solvent = batch['solvent'].to(self.device)
            reagent = batch['reagent'].to(self.device)
            catalyst = batch['catalyst'].to(self.device)

            self.optimizer.zero_grad()
            predictions = self.model(reaction_fp)

            if self.use_yield_weighting:
                # 按产率加权：per-sample loss × yield_weight
                # 失败反应 (yield=0) → weight≈0.05，高产率 → weight≈1.0
                yield_weight = batch['yield_weight'].to(self.device).clamp(min=0.05)
                loss_per_sample = (
                    self.ce_loss(predictions['anode_logits'], anode)
                    + self.ce_loss(predictions['cathode_logits'], cathode)
                    + self.ce_loss(predictions['cell_type_logits'], cell_type)
                    + self.ce_loss(predictions['electrolyte_logits'], electrolyte)
                    + self.ce_loss(predictions['solvent_logits'], solvent)
                    + self.ce_loss(predictions['reagent_logits'], reagent)
                    + self.ce_loss(predictions['catalyst_logits'], catalyst)
                )
                loss = (loss_per_sample * yield_weight).mean()
            else:
                # 标准模式：等权重 mean CE
                loss = (
                    self.ce_loss(predictions['anode_logits'], anode)
                    + self.ce_loss(predictions['cathode_logits'], cathode)
                    + self.ce_loss(predictions['cell_type_logits'], cell_type)
                    + self.ce_loss(predictions['electrolyte_logits'], electrolyte)
                    + self.ce_loss(predictions['solvent_logits'], solvent)
                    + self.ce_loss(predictions['reagent_logits'], reagent)
                    + self.ce_loss(predictions['catalyst_logits'], catalyst)
                )

            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(self.train_loader)

    TOP_KS = [1, 3, 5, 10]
    CONDITION_KEYS = ['anode', 'cathode', 'cell_type', 'electrolyte', 'solvent', 'reagent', 'catalyst']

    def validate(self):
        """验证：计算 top-1/3/5/10 准确率"""
        self.model.eval()
        # correct[key][k] = 命中次数
        correct = {
            key: {k: 0 for k in self.TOP_KS}
            for key in self.CONDITION_KEYS
        }
        total = 0

        with torch.no_grad():
            for batch in self.val_loader:
                reaction_fp = batch['reaction_fp'].to(self.device)
                predictions = self.model(reaction_fp)

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

        # accuracy[key] = {1: ..., 3: ..., 5: ..., 10: ...}
        accuracy = {
            key: {k: correct[key][k] / total for k in self.TOP_KS}
            for key in self.CONDITION_KEYS
        }
        return accuracy

    def train(self):
        """完整训练"""
        print("\nStarting condition model training...")

        best_acc = 0
        epochs = self.config['training']['epochs']

        for epoch in range(1, epochs + 1):
            train_loss = self.train_epoch(epoch)
            val_acc = self.validate()

            # top-1 平均准确率用于选最佳模型
            avg_top1 = sum(val_acc[k][1] for k in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)

            # 打印 top-1
            print(f"Epoch {epoch}: Loss={train_loss:.4f}, "
                  f"Anode={val_acc['anode'][1]:.3f}, "
                  f"Cathode={val_acc['cathode'][1]:.3f}, "
                  f"Cell={val_acc['cell_type'][1]:.3f}, "
                  f"Elec={val_acc['electrolyte'][1]:.3f}, "
                  f"Solv={val_acc['solvent'][1]:.3f}, "
                  f"Reag={val_acc['reagent'][1]:.3f}, "
                  f"Cata={val_acc['catalyst'][1]:.3f}")

            # 打印 top-k 汇总
            for k in self.TOP_KS:
                avg_k = sum(val_acc[key][k] for key in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)
                details = " | ".join(f"{key}={val_acc[key][k]:.3f}" for key in self.CONDITION_KEYS)
                print(f"  Top-{k:<2d} Avg={avg_k:.3f}  ({details})")

            self.writer.add_scalar('Loss/train', train_loss, epoch)
            for key in self.CONDITION_KEYS:
                for k in self.TOP_KS:
                    self.writer.add_scalar(f'Accuracy_top{k}/{key}', val_acc[key][k], epoch)
            for k in self.TOP_KS:
                avg_k = sum(val_acc[key][k] for key in self.CONDITION_KEYS) / len(self.CONDITION_KEYS)
                self.writer.add_scalar(f'Accuracy_top{k}/avg', avg_k, epoch)

            if avg_top1 > best_acc:
                best_acc = avg_top1
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'accuracy': val_acc
                }, self.output_dir / 'best_condition_model.pt')

        self.writer.close()
        print(f"Training complete. Best avg top-1 accuracy: {best_acc:.4f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='configs/config.yaml')
    parser.add_argument('--model', type=str, default='default',
                        help='Model type: default, dual_tower, or compact')
    parser.add_argument('--yield_weighted', action='store_true',
                        help='Weight condition loss by reaction yield (include failed reactions)')
    args = parser.parse_args()

    config_path = project_root / args.config
    with open(config_path) as f:
        config = yaml.safe_load(f)

    trainer = ConditionTrainer(config)
    trainer.use_yield_weighting = args.yield_weighted
    if args.yield_weighted:
        print("Yield-weighted training enabled: failed reactions will suppress bad conditions")

    # compact模式需要PCA降维器, xtb_only模式跳过指纹
    if args.model == 'compact':
        trainer.pca_reducer = FingerprintPCAReducer(n_components=128)
    elif args.model == 'xtb_only':
        trainer.xtb_only = True

    reaction_dim = trainer.setup_data()

    xtb_config = config.get('xtb', {})
    fp_dim = config['model']['mol_encoder']['fingerprint_size'] * 3  # 6144
    xtb_dim = 33 if xtb_config.get('use_xtb', False) else 0
    trainer.setup_model(reaction_dim, model_type=args.model,
                        fp_dim=fp_dim, xtb_dim=xtb_dim)

    num_params = sum(p.numel() for p in trainer.model.parameters() if p.requires_grad)
    print(f"Model parameters: {num_params:,}")

    trainer.train()


if __name__ == "__main__":
    main()
