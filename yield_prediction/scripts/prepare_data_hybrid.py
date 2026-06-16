"""
Hybrid GNN 数据准备脚本

为每个反应准备:
1. 分子图数据 (reactant, product, solvent, electrolyte)
2. xTB量子化学特征 (每个分子11维)
3. 电极/电解池分类特征
4. 电流连续特征
5. 产率标签

xTB特征来源:
1. 优先从预计算CSV查找
2. 找不到时使用xTB实时计算
"""
import sys
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from collections import defaultdict
import subprocess
import tempfile
import os

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
import numpy as np
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.graph_features import smiles_to_graph, smiles_list_to_graph, get_dummy_graph, ATOM_FEAT_DIM, BOND_FEAT_DIM


# ============================================================
# xTB 特征计算
# ============================================================

XTB_QC_COLS = [
    'total_energy_Eh',
    'homo_lumo_gap_eV',
    'homo_eV',
    'lumo_eV',
    'dipole_total_Debye',
    'gsolv_Eh',
]

RDKIT_DESC_NAMES = [
    'num_heavy_atoms',
    'molecular_weight',
    'num_rotatable_bonds',
    'tpsa',
    'logp',
]

XTB_FEAT_DIM = len(XTB_QC_COLS) + len(RDKIT_DESC_NAMES)  # 11


def compute_rdkit_descriptors(smiles: str) -> List[float]:
    """计算RDKit描述符 (5维)"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return [0.0] * len(RDKIT_DESC_NAMES)

    return [
        float(mol.GetNumHeavyAtoms()),
        Descriptors.MolWt(mol),
        float(rdMolDescriptors.CalcNumRotatableBonds(mol)),
        Descriptors.TPSA(mol),
        Descriptors.MolLogP(mol),
    ]


def run_xtb_calculation(smiles: str, timeout: int = 60) -> Optional[Dict[str, float]]:
    """
    运行xTB计算获取量子化学描述符

    Returns:
        dict with keys: total_energy_Eh, homo_lumo_gap_eV, homo_eV, lumo_eV, dipole_total_Debye, gsolv_Eh
        如果计算失败返回None
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    try:
        from rdkit.Chem import AllChem
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, randomSeed=42)
        AllChem.MMFFOptimizeMolecule(mol)
    except Exception:
        return None

    with tempfile.TemporaryDirectory() as tmpdir:
        xyz_path = os.path.join(tmpdir, "mol.xyz")
        try:
            # 写入XYZ文件
            conf = mol.GetConformer()
            atoms = mol.GetAtoms()
            with open(xyz_path, 'w') as f:
                f.write(f"{mol.GetNumAtoms()}\n")
                f.write(f"SMILES: {smiles}\n")
                for atom in atoms:
                    pos = conf.GetAtomPosition(atom.GetIdx())
                    f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")

            # 运行xTB
            result = subprocess.run(
                ['xtb', xyz_path, '--gfn', '2', '--alpb', 'water', '--json'],
                cwd=tmpdir,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            # 解析结果
            json_path = os.path.join(tmpdir, 'xtbout.json')
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    data = json.load(f)

                return {
                    'total_energy_Eh': data.get('total energy', 0.0),
                    'homo_lumo_gap_eV': data.get('HOMO-LUMO gap/eV', 0.0),
                    'homo_eV': data.get('HOMO', 0.0),
                    'lumo_eV': data.get('LUMO', 0.0),
                    'dipole_total_Debye': data.get('dipole', 0.0),
                    'gsolv_Eh': data.get('gsolv', 0.0),
                }
        except (subprocess.TimeoutExpired, Exception):
            pass

    return None


class XTBFeatureCache:
    """xTB特征缓存管理器"""

    def __init__(self, csv_path: Optional[str] = None):
        self.cache = {}  # smiles -> [11维特征]
        self._xtb_lookup = {}  # 预计算的xTB量化特征

        if csv_path and Path(csv_path).exists():
            self._load_csv(csv_path)

    def _load_csv(self, csv_path: str):
        """加载预计算的xTB特征"""
        import csv
        print(f"加载xTB预计算特征: {csv_path}")
        count = 0
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                smiles = row.get('smiles', '')
                if not smiles or row.get('status') != 'success':
                    continue

                qc_features = []
                valid = True
                for col in XTB_QC_COLS:
                    val = row.get(col, '')
                    if val == '' or val is None:
                        valid = False
                        break
                    try:
                        qc_features.append(float(val))
                    except (ValueError, TypeError):
                        valid = False
                        break

                if valid and len(qc_features) == len(XTB_QC_COLS):
                    self._xtb_lookup[smiles] = qc_features
                    count += 1

        print(f"  加载了 {count} 个分子的xTB特征")

    def get_features(self, smiles: str, compute_if_missing: bool = True) -> List[float]:
        """
        获取分子的完整特征 (11维)

        Args:
            smiles: SMILES字符串
            compute_if_missing: 如果缺失是否实时计算xTB
        """
        if not smiles:
            return [0.0] * XTB_FEAT_DIM

        if smiles in self.cache:
            return self.cache[smiles]

        # xTB量化特征 (6维)
        if smiles in self._xtb_lookup:
            qc_feat = self._xtb_lookup[smiles]
        elif compute_if_missing:
            xtb_result = run_xtb_calculation(smiles)
            if xtb_result:
                qc_feat = [xtb_result[col] for col in XTB_QC_COLS]
                self._xtb_lookup[smiles] = qc_feat  # 缓存
            else:
                qc_feat = [0.0] * len(XTB_QC_COLS)
        else:
            qc_feat = [0.0] * len(XTB_QC_COLS)

        # RDKit描述符 (5维)
        rdkit_feat = compute_rdkit_descriptors(smiles)

        features = qc_feat + rdkit_feat
        self.cache[smiles] = features
        return features

    def get_aggregated_features(self, smiles_list: List[str], compute_if_missing: bool = True) -> List[float]:
        """获取多个分子的聚合特征（均值）"""
        if not smiles_list:
            return [0.0] * XTB_FEAT_DIM

        all_feats = [self.get_features(smi, compute_if_missing) for smi in smiles_list]

        # 均值聚合
        result = [0.0] * XTB_FEAT_DIM
        for feat in all_feats:
            for i in range(XTB_FEAT_DIM):
                result[i] += feat[i]
        for i in range(XTB_FEAT_DIM):
            result[i] /= len(all_feats)

        return result

    def save_cache(self, path: str):
        """保存缓存到文件"""
        with open(path, 'w') as f:
            json.dump({'cache': self.cache, 'xtb_lookup': self._xtb_lookup}, f)
        print(f"xTB缓存已保存: {path}")

    def load_cache(self, path: str):
        """从文件加载缓存"""
        if Path(path).exists():
            with open(path, 'r') as f:
                data = json.load(f)
            self.cache = data.get('cache', {})
            self._xtb_lookup.update(data.get('xtb_lookup', {}))
            print(f"xTB缓存已加载: {len(self.cache)} 条目")


# ============================================================
# 电极映射
# ============================================================

ELECTRODE_MAPPING = {
    'carbon': 0, 'graphite': 1, 'platinum': 2, 'glassy carbon': 3,
    'rvc': 4, 'nickel': 5, 'stainless steel': 6, 'copper': 7,
    'zinc': 8, 'lead': 9, 'gold': 10, 'silver': 11, 'iron': 12,
    'magnesium': 13, 'aluminum': 14, 'boron-doped diamond': 15,
    'niobium': 16, 'titanium': 17, 'unknown': 18,
}

CELL_TYPE_MAPPING = {
    'undivided': 0, 'divided': 1, 'flow': 2, 'sealed': 3,
    'other': 4, 'unknown': 5,
}


def load_vocab_reverse(vocab_path: str) -> Dict[str, Dict[int, str]]:
    """加载vocab.json并创建反向映射 (index -> smiles)"""
    if not Path(vocab_path).exists():
        return {}

    with open(vocab_path, 'r') as f:
        vocab = json.load(f)

    reverse_vocab = {}
    for category, smiles_to_idx in vocab.items():
        reverse_vocab[category] = {idx: smiles for smiles, idx in smiles_to_idx.items()}

    return reverse_vocab


def normalize_electrode(name) -> int:
    """规范化电极名称并返回ID"""
    # 如果已经是整数，直接返回（限制范围）
    if isinstance(name, int):
        return min(name, len(ELECTRODE_MAPPING) - 1)
    if not name:
        return ELECTRODE_MAPPING['unknown']
    name_lower = str(name).lower().strip()
    for key, idx in ELECTRODE_MAPPING.items():
        if key in name_lower or name_lower in key:
            return idx
    return ELECTRODE_MAPPING['unknown']


def normalize_cell_type(name) -> int:
    """规范化电解池类型并返回ID"""
    # 如果已经是整数，直接返回（限制范围）
    if isinstance(name, int):
        return min(name, len(CELL_TYPE_MAPPING) - 1)
    if not name:
        return CELL_TYPE_MAPPING['unknown']
    name_lower = str(name).lower().strip()
    for key, idx in CELL_TYPE_MAPPING.items():
        if key in name_lower:
            return idx
    return CELL_TYPE_MAPPING['unknown']


# ============================================================
# 数据处理
# ============================================================

def process_reaction(
    sample: Dict,
    xtb_cache: XTBFeatureCache,
    current_mean: float,
    current_std: float,
    compute_xtb: bool = True,
    vocab_reverse: Dict[str, Dict[int, str]] = None,
) -> Optional[Dict]:
    """
    处理单个反应样本

    Returns:
        字典包含所有特征，如果处理失败返回None
    """
    # 1. 分子图
    reactant_smiles = sample.get('reactant_smiles', [])
    product_smiles = sample.get('product_smiles', [])

    if not reactant_smiles or not product_smiles:
        return None

    reactant_graph = smiles_list_to_graph(reactant_smiles)
    product_graph = smiles_list_to_graph(product_smiles)

    # 溶剂和电解质 - 从vocab反向查找SMILES
    solvent_smiles = sample.get('solvent_smiles', [])
    electrolyte_smiles = sample.get('electrolyte_smiles', '')

    # 如果没有SMILES但有label，从vocab反向查找
    if not solvent_smiles and vocab_reverse:
        solvent_label = sample.get('solvent_label')
        if solvent_label and 'solvent' in vocab_reverse:
            smi = vocab_reverse['solvent'].get(solvent_label, '')
            if smi:
                solvent_smiles = [smi]

    if not electrolyte_smiles and vocab_reverse:
        electrolyte_label = sample.get('electrolyte_label')
        if electrolyte_label and 'electrolyte' in vocab_reverse:
            electrolyte_smiles = vocab_reverse['electrolyte'].get(electrolyte_label, '')

    solvent_graph = smiles_list_to_graph(solvent_smiles) if solvent_smiles else get_dummy_graph()
    electrolyte_graph = smiles_to_graph(electrolyte_smiles) if electrolyte_smiles else get_dummy_graph()
    if electrolyte_graph is None:
        electrolyte_graph = get_dummy_graph()

    # 2. xTB特征
    reactant_xtb = xtb_cache.get_aggregated_features(reactant_smiles, compute_xtb)
    product_xtb = xtb_cache.get_aggregated_features(product_smiles, compute_xtb)
    solvent_xtb = xtb_cache.get_aggregated_features(solvent_smiles, compute_xtb) if solvent_smiles else [0.0] * XTB_FEAT_DIM
    electrolyte_xtb = xtb_cache.get_features(electrolyte_smiles, compute_xtb) if electrolyte_smiles else [0.0] * XTB_FEAT_DIM

    # 3. 分类特征
    anode = sample.get('anode', 'unknown')
    cathode = sample.get('cathode', 'unknown')
    cell_type = sample.get('cell_type', 'unknown')

    anode_id = normalize_electrode(anode)
    cathode_id = normalize_electrode(cathode)
    cell_type_id = normalize_cell_type(cell_type)

    # 4. 电流 (标准化)
    current = sample.get('current', 0.0)
    if current is None:
        current = 0.0
    current_normalized = (current - current_mean) / (current_std + 1e-8)

    # 5. 产率
    yield_value = sample.get('yield', 0.0)
    if yield_value is None or yield_value < 0 or yield_value > 100:
        return None

    return {
        'reactant_graph': reactant_graph,
        'product_graph': product_graph,
        'solvent_graph': solvent_graph,
        'electrolyte_graph': electrolyte_graph,
        'reactant_xtb': torch.tensor(reactant_xtb, dtype=torch.float32),
        'product_xtb': torch.tensor(product_xtb, dtype=torch.float32),
        'solvent_xtb': torch.tensor(solvent_xtb, dtype=torch.float32),
        'electrolyte_xtb': torch.tensor(electrolyte_xtb, dtype=torch.float32),
        'anode_id': anode_id,
        'cathode_id': cathode_id,
        'cell_type_id': cell_type_id,
        'current_normalized': current_normalized,
        'yield': yield_value,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default=str(project_root / 'data' / 'train.pt'),
                        help='输入数据文件路径')
    parser.add_argument('--output_dir', type=str, default=str(project_root / 'data'),
                        help='输出目录')
    parser.add_argument('--xtb_csv', type=str, default=str(project_root / 'data' / 'xtb_reaction_molecules.csv'),
                        help='预计算xTB特征CSV')
    parser.add_argument('--xtb_cache', type=str, default=None,
                        help='xTB缓存文件路径')
    parser.add_argument('--compute_xtb', action='store_true',
                        help='实时计算缺失的xTB特征')
    parser.add_argument('--train_ratio', type=float, default=0.8)
    parser.add_argument('--val_ratio', type=float, default=0.1)
    parser.add_argument('--vocab', type=str, default=str(project_root / 'checkpoints' / 'condition_model' / 'vocab.json'),
                        help='vocab.json路径，用于反向查找SMILES')
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载原始数据
    print(f"\n加载数据: {args.input}")
    raw_data = torch.load(args.input, weights_only=False)
    print(f"  样本数: {len(raw_data)}")

    # 初始化xTB缓存
    xtb_cache = XTBFeatureCache(args.xtb_csv if Path(args.xtb_csv).exists() else None)
    if args.xtb_cache and Path(args.xtb_cache).exists():
        xtb_cache.load_cache(args.xtb_cache)

    # 加载vocab反向映射
    vocab_reverse = load_vocab_reverse(args.vocab) if Path(args.vocab).exists() else {}
    if vocab_reverse:
        print(f"  加载vocab: solvent={len(vocab_reverse.get('solvent', {}))} 种, "
              f"electrolyte={len(vocab_reverse.get('electrolyte', {}))} 种")

    # 计算电流统计
    currents = [s.get('current', 0.0) or 0.0 for s in raw_data]
    current_mean = np.mean(currents)
    current_std = np.std(currents)
    print(f"  电流均值: {current_mean:.4f}, 标准差: {current_std:.4f}")

    # 处理数据
    print("\n处理反应数据...")
    processed = []
    for sample in tqdm(raw_data, desc="Processing"):
        result = process_reaction(
            sample, xtb_cache, current_mean, current_std,
            compute_xtb=args.compute_xtb,
            vocab_reverse=vocab_reverse,
        )
        if result is not None:
            processed.append(result)

    print(f"  有效样本: {len(processed)} / {len(raw_data)}")

    # 划分数据集
    np.random.seed(42)
    indices = np.random.permutation(len(processed))

    n_train = int(len(processed) * args.train_ratio)
    n_val = int(len(processed) * args.val_ratio)

    train_indices = indices[:n_train]
    val_indices = indices[n_train:n_train + n_val]
    test_indices = indices[n_train + n_val:]

    train_data = [processed[i] for i in train_indices]
    val_data = [processed[i] for i in val_indices]
    test_data = [processed[i] for i in test_indices]

    print(f"\n数据集划分:")
    print(f"  Train: {len(train_data)}")
    print(f"  Val:   {len(val_data)}")
    print(f"  Test:  {len(test_data)}")

    # 保存数据
    torch.save(train_data, output_dir / 'train_hybrid.pt')
    torch.save(val_data, output_dir / 'val_hybrid.pt')
    torch.save(test_data, output_dir / 'test_hybrid.pt')

    # 保存统计信息
    stats = {
        'atom_feat_dim': ATOM_FEAT_DIM,
        'bond_feat_dim': BOND_FEAT_DIM,
        'xtb_feat_dim': XTB_FEAT_DIM,
        'num_electrode_types': len(ELECTRODE_MAPPING),
        'num_cell_types': len(CELL_TYPE_MAPPING),
        'current_mean': current_mean,
        'current_std': current_std,
        'n_train': len(train_data),
        'n_val': len(val_data),
        'n_test': len(test_data),
    }

    with open(output_dir / 'stats_hybrid.json', 'w') as f:
        json.dump(stats, f, indent=2)

    # 保存xTB缓存
    if args.xtb_cache:
        xtb_cache.save_cache(args.xtb_cache)
    else:
        xtb_cache.save_cache(str(output_dir / 'xtb_cache.json'))

    print(f"\n数据已保存到: {output_dir}")
    print(f"  train_hybrid.pt, val_hybrid.pt, test_hybrid.pt")
    print(f"  stats_hybrid.json")


if __name__ == "__main__":
    main()
