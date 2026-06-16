"""
xTB增强数据准备脚本

在原始指纹数据基础上添加xTB量子化学特征
目标：利用xTB特征提升MLP性能
"""
import sys
import json
from pathlib import Path
from typing import List, Dict

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


# xTB特征列名
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


def load_xtb_features(csv_path: str) -> Dict[str, List[float]]:
    """加载预计算的xTB特征"""
    import csv
    xtb_lookup = {}

    if not Path(csv_path).exists():
        print(f"警告: xTB CSV不存在: {csv_path}")
        return xtb_lookup

    print(f"加载xTB特征: {csv_path}")
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

            if valid:
                xtb_lookup[smiles] = qc_features

    print(f"  加载了 {len(xtb_lookup)} 个分子的xTB特征")
    return xtb_lookup


def load_vocab_reverse(vocab_path: str) -> Dict[str, Dict[int, str]]:
    """加载vocab.json并创建反向映射"""
    if not Path(vocab_path).exists():
        return {}

    with open(vocab_path, 'r') as f:
        vocab = json.load(f)

    reverse_vocab = {}
    for category, smiles_to_idx in vocab.items():
        reverse_vocab[category] = {idx: smiles for smiles, idx in smiles_to_idx.items()}

    return reverse_vocab


def get_molecular_xtb_features(
    smiles_list: List[str],
    xtb_lookup: Dict[str, List[float]]
) -> List[float]:
    """
    获取分子列表的聚合xTB+RDKit特征 (11维)
    """
    if not smiles_list:
        return [0.0] * 11

    all_features = []
    for smiles in smiles_list:
        if not smiles:
            continue

        # xTB特征 (6维)
        if smiles in xtb_lookup:
            qc_feat = xtb_lookup[smiles]
        else:
            qc_feat = [0.0] * 6

        # RDKit描述符 (5维)
        rdkit_feat = compute_rdkit_descriptors(smiles)

        all_features.append(qc_feat + rdkit_feat)

    if not all_features:
        return [0.0] * 11

    # 均值聚合
    result = [0.0] * 11
    for feat in all_features:
        for i in range(11):
            result[i] += feat[i]
    for i in range(11):
        result[i] /= len(all_features)

    return result


def prepare_xtb_enhanced_data(
    raw_data: List[Dict],
    xtb_lookup: Dict[str, List[float]],
    vocab_reverse: Dict[str, Dict[int, str]],
) -> List[Dict]:
    """
    为原始数据添加xTB特征

    每个样本添加:
    - reactant_xtb: 11维
    - product_xtb: 11维
    - solvent_xtb: 11维
    - electrolyte_xtb: 11维
    - reaction_xtb_diff: 11维 (product - reactant的差异)

    总共添加55维xTB特征
    """
    enhanced_data = []

    for sample in tqdm(raw_data, desc="添加xTB特征"):
        # 获取SMILES
        reactant_smiles = sample.get('reactant_smiles', [])
        product_smiles = sample.get('product_smiles', [])

        # 从vocab反向查找溶剂和电解质SMILES
        solvent_smiles = []
        electrolyte_smiles = []

        if 'solvent' in vocab_reverse:
            solvent_label = sample.get('solvent_label')
            if solvent_label is not None:
                smi = vocab_reverse['solvent'].get(solvent_label, '')
                if smi:
                    solvent_smiles = [smi]

        if 'electrolyte' in vocab_reverse:
            electrolyte_label = sample.get('electrolyte_label')
            if electrolyte_label is not None:
                smi = vocab_reverse['electrolyte'].get(electrolyte_label, '')
                if smi:
                    electrolyte_smiles = [smi]

        # 计算xTB特征
        reactant_xtb = get_molecular_xtb_features(reactant_smiles, xtb_lookup)
        product_xtb = get_molecular_xtb_features(product_smiles, xtb_lookup)
        solvent_xtb = get_molecular_xtb_features(solvent_smiles, xtb_lookup)
        electrolyte_xtb = get_molecular_xtb_features(electrolyte_smiles, xtb_lookup)

        # 计算反应差异特征
        reaction_diff_xtb = [product_xtb[i] - reactant_xtb[i] for i in range(11)]

        # 复制原始样本并添加xTB特征
        enhanced_sample = sample.copy()
        enhanced_sample['reactant_xtb'] = reactant_xtb
        enhanced_sample['product_xtb'] = product_xtb
        enhanced_sample['solvent_xtb'] = solvent_xtb
        enhanced_sample['electrolyte_xtb'] = electrolyte_xtb
        enhanced_sample['reaction_diff_xtb'] = reaction_diff_xtb

        enhanced_data.append(enhanced_sample)

    return enhanced_data


def normalize_xtb_features(data: List[Dict], feature_keys: List[str]) -> Dict[str, Dict]:
    """计算并应用xTB特征标准化"""
    # 收集所有特征值
    all_values = {key: [] for key in feature_keys}

    for sample in data:
        for key in feature_keys:
            all_values[key].extend(sample.get(key, [0.0] * 11))

    # 计算统计量
    stats = {}
    for key in feature_keys:
        values = np.array(all_values[key])
        stats[key] = {
            'mean': np.mean(values).tolist() if len(values) > 0 else 0.0,
            'std': np.std(values).tolist() if len(values) > 0 else 1.0,
        }

    return stats


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default=str(project_root / 'data'))
    parser.add_argument('--xtb_csv', type=str, default=str(project_root / 'data' / 'xtb_reaction_molecules.csv'))
    parser.add_argument('--vocab', type=str, default=str(project_root / 'checkpoints' / 'condition_model' / 'vocab.json'))
    args = parser.parse_args()

    data_dir = Path(args.data_dir)

    # 加载xTB特征
    xtb_lookup = load_xtb_features(args.xtb_csv)

    # 加载vocab反向映射
    vocab_reverse = load_vocab_reverse(args.vocab)
    if vocab_reverse:
        print(f"加载vocab: solvent={len(vocab_reverse.get('solvent', {}))} 种, "
              f"electrolyte={len(vocab_reverse.get('electrolyte', {}))} 种")

    # 处理三个数据集
    for split in ['train', 'val', 'test']:
        input_path = data_dir / f'{split}.pt'
        output_path = data_dir / f'{split}_xtb.pt'

        print(f"\n处理 {split} 数据集...")
        raw_data = torch.load(input_path, weights_only=False)
        print(f"  原始样本数: {len(raw_data)}")

        enhanced_data = prepare_xtb_enhanced_data(raw_data, xtb_lookup, vocab_reverse)

        torch.save(enhanced_data, output_path)
        print(f"  保存到: {output_path}")

    # 计算并保存统计信息
    print("\n计算xTB特征统计...")
    train_data = torch.load(data_dir / 'train_xtb.pt', weights_only=False)

    xtb_keys = ['reactant_xtb', 'product_xtb', 'solvent_xtb', 'electrolyte_xtb', 'reaction_diff_xtb']
    stats = normalize_xtb_features(train_data, xtb_keys)

    # 总体统计
    stats['info'] = {
        'fp_dim': 10246,  # 5*2048 + 6
        'xtb_dim': 55,    # 5*11
        'total_dim': 10301,
        'n_train': len(train_data),
    }

    with open(data_dir / 'stats_xtb.json', 'w') as f:
        json.dump(stats, f, indent=2)

    print(f"\n统计信息已保存到: {data_dir / 'stats_xtb.json'}")
    print("完成！")


if __name__ == "__main__":
    main()
