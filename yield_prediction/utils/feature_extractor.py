"""
分子特征提取模块：将SMILES转换为模型可用的特征
支持xTB量子化学描述符整合
"""
import numpy as np
from typing import List, Dict, Optional, Tuple
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors
from rdkit import DataStructs
import torch

# 导入xTB特征模块
try:
    from .xtb_features import XTBFeatureLookup, REACTION_XTB_FEAT_DIM
    XTB_AVAILABLE = True
except ImportError:
    XTB_AVAILABLE = False
    REACTION_XTB_FEAT_DIM = 55


class MolecularFeatureExtractor:
    """分子特征提取器"""

    def __init__(self, fingerprint_size: int = 2048, fingerprint_radius: int = 2):
        self.fp_size = fingerprint_size
        self.fp_radius = fingerprint_radius

    def smiles_to_mol(self, smiles: str) -> Optional[Chem.Mol]:
        """将SMILES转换为分子对象"""
        try:
            mol = Chem.MolFromSmiles(smiles)
            return mol
        except:
            return None

    def get_morgan_fingerprint(self, smiles: str) -> np.ndarray:
        """获取Morgan指纹 (ECFP)"""
        mol = self.smiles_to_mol(smiles)
        if mol is None:
            return np.zeros(self.fp_size)

        fp = AllChem.GetMorganFingerprintAsBitVect(
            mol, self.fp_radius, nBits=self.fp_size
        )
        arr = np.zeros(self.fp_size)
        DataStructs.ConvertToNumpyArray(fp, arr)
        return arr

    def get_rdkit_fingerprint(self, smiles: str) -> np.ndarray:
        """获取RDKit指纹"""
        mol = self.smiles_to_mol(smiles)
        if mol is None:
            return np.zeros(self.fp_size)

        fp = Chem.RDKFingerprint(mol, fpSize=self.fp_size)
        arr = np.zeros(self.fp_size)
        DataStructs.ConvertToNumpyArray(fp, arr)
        return arr

    def get_molecular_descriptors(self, smiles: str) -> np.ndarray:
        """获取分子描述符"""
        mol = self.smiles_to_mol(smiles)
        if mol is None:
            return np.zeros(10)

        descriptors = [
            Descriptors.MolWt(mol),  # 分子量
            Descriptors.MolLogP(mol),  # LogP
            Descriptors.TPSA(mol),  # 拓扑极性表面积
            Descriptors.NumHDonors(mol),  # 氢键供体数
            Descriptors.NumHAcceptors(mol),  # 氢键受体数
            Descriptors.NumRotatableBonds(mol),  # 可旋转键数
            Descriptors.NumAromaticRings(mol),  # 芳香环数
            rdMolDescriptors.CalcNumRings(mol),  # 环数
            Descriptors.FractionCSP3(mol),  # sp3碳比例
            Descriptors.HeavyAtomCount(mol),  # 重原子数
        ]

        return np.array(descriptors, dtype=np.float32)

    def encode_reaction(self, reactants: List[str], products: List[str]) -> np.ndarray:
        """编码整个反应（反应物-产物差异指纹）"""
        # 合并所有反应物指纹
        reactant_fp = np.zeros(self.fp_size)
        for smiles in reactants:
            fp = self.get_morgan_fingerprint(smiles)
            reactant_fp = np.maximum(reactant_fp, fp)  # 使用OR合并

        # 合并所有产物指纹
        product_fp = np.zeros(self.fp_size)
        for smiles in products:
            fp = self.get_morgan_fingerprint(smiles)
            product_fp = np.maximum(product_fp, fp)

        # 反应指纹 = [反应物FP, 产物FP, 差异FP]
        diff_fp = np.abs(product_fp - reactant_fp)
        reaction_fp = np.concatenate([reactant_fp, product_fp, diff_fp])

        return reaction_fp

    def encode_molecules(self, smiles_list: List[str]) -> np.ndarray:
        """编码分子列表（取最大值合并）"""
        if not smiles_list:
            return np.zeros(self.fp_size)

        combined_fp = np.zeros(self.fp_size)
        for smiles in smiles_list:
            fp = self.get_morgan_fingerprint(smiles)
            combined_fp = np.maximum(combined_fp, fp)

        return combined_fp


class ConditionEncoder:
    """反应条件编码器"""

    def __init__(self, vocab: Dict = None):
        self.vocab = vocab or {}
        self.solvent_to_idx = {}
        self.electrolyte_to_idx = {}
        self._build_vocab()

    def _build_vocab(self):
        """构建条件词汇表"""
        if 'solvents' in self.vocab:
            self.solvent_to_idx = {s: i for i, s in enumerate(self.vocab['solvents'])}
        if 'electrolytes' in self.vocab:
            self.electrolyte_to_idx = {e: i for i, e in enumerate(self.vocab['electrolytes'])}

    def encode_electrochemistry(self, echem_params: Dict) -> np.ndarray:
        """编码电化学参数"""
        features = [
            echem_params.get('anode', 14),  # 阳极材料编码
            echem_params.get('cathode', 14),  # 阴极材料编码
            echem_params.get('current', 0.0),  # 电流
            echem_params.get('current_density', 0.0),  # 电流密度
            echem_params.get('potential', 0.0),  # 电势
            echem_params.get('cell_type', 4),  # 电解池类型
        ]
        return np.array(features, dtype=np.float32)

    def encode_solvents(self, solvents: List[str], mol_extractor: MolecularFeatureExtractor) -> np.ndarray:
        """编码溶剂（使用分子指纹）"""
        return mol_extractor.encode_molecules(solvents)

    def encode_electrolyte(self, electrolyte: str, mol_extractor: MolecularFeatureExtractor) -> np.ndarray:
        """编码电解质（使用分子指纹）"""
        if not electrolyte:
            return np.zeros(mol_extractor.fp_size)
        return mol_extractor.get_morgan_fingerprint(electrolyte)


class ReactionFeaturizer:
    """反应特征化器：整合所有特征（含xTB量子化学描述符）"""

    def __init__(self, fp_size: int = 2048, fp_radius: int = 2,
                 xtb_csv_path: str = None, use_xtb: bool = False):
        self.mol_extractor = MolecularFeatureExtractor(fp_size, fp_radius)
        self.cond_encoder = ConditionEncoder()
        self.fp_size = fp_size
        self.use_xtb = use_xtb and XTB_AVAILABLE

        # 初始化xTB特征查找表
        self.xtb_lookup = None
        if self.use_xtb and xtb_csv_path:
            self.xtb_lookup = XTBFeatureLookup(xtb_csv_path)
            print(f"xTB特征已加载，共 {len(self.xtb_lookup.xtb_lookup)} 个分子")

    def featurize(self, reaction: Dict) -> Tuple[np.ndarray, float]:
        """将反应转换为特征向量"""
        # 获取SMILES列表
        reactant_smiles = reaction.get('reactants', [])
        product_smiles = reaction.get('products', [])
        solvent_smiles = reaction.get('solvents', [])
        echem = reaction.get('electrochemistry', {})
        electrolyte_smiles = echem.get('electrolyte', '')

        # 1. 反应物/产物指纹
        reaction_fp = self.mol_extractor.encode_reaction(
            reactant_smiles, product_smiles
        )  # 3 * fp_size

        # 2. 溶剂指纹
        solvent_fp = self.mol_extractor.encode_molecules(solvent_smiles)  # fp_size

        # 3. 电化学参数
        echem_features = self.cond_encoder.encode_electrochemistry(echem)  # 6

        # 4. 电解质指纹
        electrolyte_fp = self.cond_encoder.encode_electrolyte(
            electrolyte_smiles, self.mol_extractor
        )  # fp_size

        # 合并指纹特征
        features = np.concatenate([
            reaction_fp,  # 3 * 2048 = 6144
            solvent_fp,  # 2048
            electrolyte_fp,  # 2048
            echem_features  # 6
        ])

        # 5. xTB量子化学特征（可选）
        if self.use_xtb and self.xtb_lookup:
            xtb_features = self.xtb_lookup.get_reaction_features(
                reactant_smiles, product_smiles, solvent_smiles, electrolyte_smiles
            )
            features = np.concatenate([features, np.array(xtb_features, dtype=np.float32)])

        yield_value = reaction.get('yield', 0.0)

        return features.astype(np.float32), float(yield_value)

    def get_feature_dim(self) -> int:
        """获取特征维度"""
        base_dim = 5 * self.fp_size + 6  # 10246
        if self.use_xtb:
            return base_dim + REACTION_XTB_FEAT_DIM  # 10246 + 55 = 10301
        return base_dim


class ReactionDataset(torch.utils.data.Dataset):
    """PyTorch数据集（支持xTB特征归一化）"""

    def __init__(self, reactions: List[Dict], featurizer: ReactionFeaturizer,
                 normalize_xtb: bool = True, xtb_stats: dict = None):
        self.reactions = reactions
        self.featurizer = featurizer
        self.features = []
        self.labels = []
        self.normalize_xtb = normalize_xtb and featurizer.use_xtb
        self.xtb_stats = xtb_stats  # {'mean': ..., 'std': ...}
        self._preprocess()

    def _preprocess(self):
        """预处理所有数据"""
        from tqdm import tqdm
        for rxn in tqdm(self.reactions, desc="Featurizing reactions"):
            try:
                feat, label = self.featurizer.featurize(rxn)
                self.features.append(feat)
                self.labels.append(label / 100.0)  # 归一化到0-1
            except Exception as e:
                continue

        # xTB特征归一化
        if self.normalize_xtb and len(self.features) > 0:
            self._normalize_xtb_features()

    def _normalize_xtb_features(self):
        """对xTB特征进行z-score归一化"""
        base_dim = 5 * self.featurizer.fp_size + 6  # 10246
        features_array = np.array(self.features)

        if self.xtb_stats is None:
            # 计算xTB特征的统计量
            xtb_feats = features_array[:, base_dim:]
            self.xtb_stats = {
                'mean': np.mean(xtb_feats, axis=0),
                'std': np.std(xtb_feats, axis=0) + 1e-8
            }

        # 应用归一化
        mean = self.xtb_stats['mean']
        std = self.xtb_stats['std']
        for i in range(len(self.features)):
            self.features[i][base_dim:] = (self.features[i][base_dim:] - mean) / std

    def get_xtb_stats(self):
        """返回xTB归一化统计量"""
        return self.xtb_stats

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return (
            torch.tensor(self.features[idx], dtype=torch.float32),
            torch.tensor(self.labels[idx], dtype=torch.float32)
        )


class XtbOnlyDataset(torch.utils.data.Dataset):
    """仅使用xTB特征的数据集（产率预测）

    特征: xTB(55D) + 电化学参数(6D) = 61D
    """

    def __init__(self, reactions: List, xtb_csv_path: str,
                 xtb_stats: dict = None):
        from .xtb_features import XTBFeatureLookup
        self.xtb_lookup = XTBFeatureLookup(xtb_csv_path)
        self.cond_encoder = ConditionEncoder()
        self.xtb_stats = xtb_stats
        self.features = []
        self.labels = []
        self._preprocess(reactions)

    def _preprocess(self, reactions):
        from tqdm import tqdm
        all_xtb = []

        for rxn in tqdm(reactions, desc="Extracting xTB-only features"):
            try:
                reactant_smiles = rxn.get('reactants', [])
                product_smiles = rxn.get('products', [])
                solvent_smiles = rxn.get('solvents', [])
                echem = rxn.get('electrochemistry', {})
                electrolyte_smiles = echem.get('electrolyte', '')

                # xTB特征 (55D)
                xtb_feat = np.array(self.xtb_lookup.get_reaction_features(
                    reactant_smiles, product_smiles, solvent_smiles, electrolyte_smiles
                ), dtype=np.float32)

                # 电化学参数 (6D)
                echem_feat = self.cond_encoder.encode_electrochemistry(echem)

                all_xtb.append(xtb_feat)
                self.features.append(np.concatenate([xtb_feat, echem_feat]))
                self.labels.append(rxn.get('yield', 0.0) / 100.0)
            except Exception:
                continue

        # 归一化xTB部分 (前55维)
        if len(all_xtb) > 0:
            xtb_array = np.array(all_xtb)
            if self.xtb_stats is None:
                self.xtb_stats = {
                    'mean': np.mean(xtb_array, axis=0),
                    'std': np.std(xtb_array, axis=0) + 1e-8
                }
            mean, std = self.xtb_stats['mean'], self.xtb_stats['std']
            for i in range(len(self.features)):
                self.features[i][:55] = (self.features[i][:55] - mean) / std

    def get_xtb_stats(self):
        return self.xtb_stats

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return (
            torch.tensor(self.features[idx], dtype=torch.float32),
            torch.tensor(self.labels[idx], dtype=torch.float32)
        )


class CompactReactionFeaturizer:
    """紧凑特征提取器：PCA压缩指纹 + 溶剂/电解质词汇表索引"""

    def __init__(self, fp_size: int = 2048, fp_radius: int = 2,
                 xtb_csv_path: str = None, use_xtb: bool = False,
                 solvent_vocab: dict = None, electrolyte_vocab: dict = None):
        self.mol_extractor = MolecularFeatureExtractor(fp_size, fp_radius)
        self.cond_encoder = ConditionEncoder()
        self.fp_size = fp_size
        self.use_xtb = use_xtb and XTB_AVAILABLE
        self.solvent_vocab = solvent_vocab or {}
        self.electrolyte_vocab = electrolyte_vocab or {}

        self.xtb_lookup = None
        if self.use_xtb and xtb_csv_path:
            self.xtb_lookup = XTBFeatureLookup(xtb_csv_path)
            print(f"xTB特征已加载，共 {len(self.xtb_lookup.xtb_lookup)} 个分子")

    def extract_raw(self, reaction: dict) -> dict:
        """提取原始分离特征（PCA前）"""
        reactant_smiles = reaction.get('reactants', [])
        product_smiles = reaction.get('products', [])
        solvent_smiles = reaction.get('solvents', [])
        echem = reaction.get('electrochemistry', {})
        electrolyte_smiles = echem.get('electrolyte', '')

        # 反应指纹（用于PCA）
        reaction_fp = self.mol_extractor.encode_reaction(
            reactant_smiles, product_smiles
        )  # 3 * fp_size

        # 溶剂词汇表索引
        if solvent_smiles:
            solvent_idx = self.solvent_vocab.get(solvent_smiles[0], 0)
        else:
            solvent_idx = 0

        # 电解质词汇表索引
        electrolyte_idx = self.electrolyte_vocab.get(electrolyte_smiles, 0)

        # 电化学参数
        echem_features = self.cond_encoder.encode_electrochemistry(echem)  # 6D

        # xTB特征
        xtb_features = None
        if self.use_xtb and self.xtb_lookup:
            xtb_features = np.array(self.xtb_lookup.get_reaction_features(
                reactant_smiles, product_smiles, solvent_smiles, electrolyte_smiles
            ), dtype=np.float32)

        yield_value = reaction.get('yield', 0.0)

        return {
            'reaction_fp': reaction_fp.astype(np.float32),  # 6144D
            'solvent_idx': solvent_idx,
            'electrolyte_idx': electrolyte_idx,
            'echem': echem_features.astype(np.float32),  # 6D
            'xtb': xtb_features,  # 55D or None
            'yield': float(yield_value),
        }


class CompactReactionDataset(torch.utils.data.Dataset):
    """紧凑特征数据集：PCA压缩指纹 + 溶剂/电解质索引"""

    def __init__(self, reactions: List, featurizer: CompactReactionFeaturizer,
                 pca_reducer=None, xtb_stats: dict = None):
        self.featurizer = featurizer
        self.pca_reducer = pca_reducer
        self.xtb_stats = xtb_stats

        self.reaction_fps = []
        self.solvent_idxs = []
        self.electrolyte_idxs = []
        self.echem_feats = []
        self.xtb_feats = []
        self.labels = []

        self._preprocess(reactions)

    def _preprocess(self, reactions):
        from tqdm import tqdm
        raw_fps = []

        for rxn in tqdm(reactions, desc="Extracting features"):
            try:
                raw = self.featurizer.extract_raw(rxn)
                raw_fps.append(raw['reaction_fp'])
                self.solvent_idxs.append(raw['solvent_idx'])
                self.electrolyte_idxs.append(raw['electrolyte_idx'])
                self.echem_feats.append(raw['echem'])
                self.xtb_feats.append(raw['xtb'])
                self.labels.append(raw['yield'] / 100.0)
            except Exception:
                continue

        # PCA降维
        raw_fp_array = np.array(raw_fps)
        if self.pca_reducer is not None:
            if not self.pca_reducer.is_fitted:
                self.reaction_fps = self.pca_reducer.fit_transform(raw_fp_array)
            else:
                self.reaction_fps = self.pca_reducer.transform(raw_fp_array)
        else:
            self.reaction_fps = raw_fp_array

        # xTB归一化
        if self.xtb_feats[0] is not None:
            xtb_array = np.array(self.xtb_feats)
            if self.xtb_stats is None:
                self.xtb_stats = {
                    'mean': np.mean(xtb_array, axis=0),
                    'std': np.std(xtb_array, axis=0) + 1e-8
                }
            mean, std = self.xtb_stats['mean'], self.xtb_stats['std']
            xtb_array = (xtb_array - mean) / std
            self.xtb_feats = [xtb_array[i] for i in range(len(xtb_array))]

    def get_xtb_stats(self):
        return self.xtb_stats

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        # 拼接连续特征: pca_fp + echem + xtb
        parts = [self.reaction_fps[idx], self.echem_feats[idx]]
        if self.xtb_feats[idx] is not None:
            parts.append(self.xtb_feats[idx])
        continuous = np.concatenate(parts)

        return {
            'continuous': torch.tensor(continuous, dtype=torch.float32),
            'solvent_idx': torch.tensor(self.solvent_idxs[idx], dtype=torch.long),
            'electrolyte_idx': torch.tensor(self.electrolyte_idxs[idx], dtype=torch.long),
            'label': torch.tensor(self.labels[idx], dtype=torch.float32),
        }

    def get_continuous_dim(self):
        """连续特征维度 = pca_dim + 6(echem) + 55(xtb, optional)"""
        dim = self.reaction_fps.shape[1] + 6
        if self.xtb_feats[0] is not None:
            dim += len(self.xtb_feats[0])
        return dim


if __name__ == "__main__":
    # 测试特征提取
    extractor = MolecularFeatureExtractor()

    test_smiles = "C=C(c1ccccc1)C(C)(O)c1ccccc1"
    fp = extractor.get_morgan_fingerprint(test_smiles)
    print(f"Fingerprint shape: {fp.shape}")
    print(f"Non-zero elements: {np.sum(fp > 0)}")

    desc = extractor.get_molecular_descriptors(test_smiles)
    print(f"Descriptors: {desc}")
