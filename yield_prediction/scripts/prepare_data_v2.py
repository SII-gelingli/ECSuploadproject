"""
数据预处理脚本 V2：改进的电极处理 + 去掉无用特征

改进点：
1. 使用规范化的电极分类（20类，覆盖率97%+）
2. 去掉 current_density 和 potential（数据太少）
3. 电极和电解池类型单独输出，用于 Embedding
"""
import sys
import json
import re
from pathlib import Path

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.graph_features import smiles_to_graph, smiles_list_to_graph, get_dummy_graph, ATOM_FEAT_DIM, BOND_FEAT_DIM
from utils.electrode_normalizer import electrode_to_id, NUM_ELECTRODE_TYPES, analyze_electrode_coverage


# 电解池类型映射
CELL_TYPE_MAP = {
    'undivided': 0,
    'divided': 1,
    'h-cell': 2,
    'h cell': 2,
    'flow': 3,
    'flow cell': 3,
}
NUM_CELL_TYPES = 5  # 0-3 + unknown(4)


def normalize_cell_type(cell_type: str) -> int:
    """规范化电解池类型"""
    if not cell_type or not str(cell_type).strip():
        return 4  # unknown
    cell_lower = str(cell_type).lower().strip()
    for key, idx in CELL_TYPE_MAP.items():
        if key in cell_lower:
            return idx
    return 4  # unknown


def parse_current(s: str) -> float:
    """解析电流值（mA）"""
    if not s:
        return 0.0
    try:
        s = str(s).lower().replace(' ', '')
        if 'ma' in s:
            nums = re.findall(r'[-\d.]+', s.replace('ma', ''))
            return float(nums[0]) if nums else 0.0
        elif 'a' in s:
            nums = re.findall(r'[-\d.]+', s.replace('a', ''))
            return float(nums[0]) * 1000 if nums else 0.0
        nums = re.findall(r'[-\d.]+', s)
        return float(nums[0]) if nums else 0.0
    except (ValueError, IndexError):
        return 0.0


def prepare_data_v2():
    """准备改进版数据"""
    data_dir = project_root / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    # 1. 加载原始数据
    print("=" * 60)
    print("加载原始反应数据...")
    print("=" * 60)

    yield_data_dir = Path("/inspire/hdd/global_user/gelingli-253114010248/alkene_reactions_by_yield")
    all_reactions = []
    for fname in yield_data_dir.glob("*.json"):
        with open(fname, 'r') as f:
            reactions = json.load(f)
            all_reactions.extend(reactions)

    print(f"总反应数: {len(all_reactions)}")

    # 2. 处理每个反应
    print("\n" + "=" * 60)
    print("处理反应数据...")
    print("=" * 60)

    processed_data = []
    skipped = 0
    all_anodes = []
    all_cathodes = []

    for rxn in tqdm(all_reactions, desc="处理反应"):
        try:
            # 提取SMILES
            reactant_smiles = [r.get('smiles', '') for r in rxn.get('reactants', []) if r.get('smiles')]
            product_smiles = [p.get('smiles', '') for p in rxn.get('products', []) if p.get('smiles')]
            solvent_smiles = [s.get('smiles', '') for s in rxn.get('solvents', []) if s.get('smiles')]

            echem = rxn.get('electrochemistry_params', {})
            electrolyte_smiles = echem.get('electrolyte', '') or ''

            if not reactant_smiles or not product_smiles:
                skipped += 1
                continue

            # 构建分子图
            reactant_graph = smiles_list_to_graph(reactant_smiles)
            product_graph = smiles_list_to_graph(product_smiles)
            solvent_graph = smiles_list_to_graph(solvent_smiles) if solvent_smiles else get_dummy_graph()

            if electrolyte_smiles:
                eg = smiles_to_graph(electrolyte_smiles)
                electrolyte_graph = eg if eg is not None else get_dummy_graph()
            else:
                electrolyte_graph = get_dummy_graph()

            # 电极处理（使用新的规范化）
            anode_raw = echem.get('anode', '')
            cathode_raw = echem.get('cathode', '')
            anode_id = electrode_to_id(anode_raw)
            cathode_id = electrode_to_id(cathode_raw)

            all_anodes.append(anode_raw)
            all_cathodes.append(cathode_raw)

            # 电流（唯一保留的连续特征）
            current = parse_current(echem.get('current', ''))

            # 电解池类型
            cell_type_id = normalize_cell_type(echem.get('cell_type', ''))

            # 产率
            yield_value = rxn.get('product_yield', 0)
            if isinstance(yield_value, str):
                nums = re.findall(r'[\d.]+', yield_value)
                yield_value = float(nums[0]) if nums else 0.0

            processed_data.append({
                'reactant_graph': reactant_graph,
                'product_graph': product_graph,
                'solvent_graph': solvent_graph,
                'electrolyte_graph': electrolyte_graph,
                # 分类特征（用于Embedding）
                'anode_id': anode_id,
                'cathode_id': cathode_id,
                'cell_type_id': cell_type_id,
                # 连续特征
                'current': current,
                'yield': float(yield_value),
            })

        except Exception as e:
            skipped += 1
            continue

    print(f"\n成功处理: {len(processed_data)} 个反应")
    print(f"跳过: {skipped} 个反应")

    # 3. 电极覆盖率统计
    print("\n" + "=" * 60)
    print("电极覆盖率统计")
    print("=" * 60)
    anode_stats = analyze_electrode_coverage(all_anodes)
    cathode_stats = analyze_electrode_coverage(all_cathodes)
    print(f"阳极覆盖率: {anode_stats['coverage']*100:.1f}%")
    print(f"阴极覆盖率: {cathode_stats['coverage']*100:.1f}%")

    # 4. 划分数据集
    print("\n" + "=" * 60)
    print("划分数据集...")
    print("=" * 60)
    train_data, temp_data = train_test_split(processed_data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

    print(f"  Train: {len(train_data)}")
    print(f"  Val:   {len(val_data)}")
    print(f"  Test:  {len(test_data)}")

    # 5. 计算电流标准化参数
    train_currents = [d['current'] for d in train_data]
    current_mean = sum(train_currents) / len(train_currents)
    current_std = (sum((c - current_mean) ** 2 for c in train_currents) / len(train_currents)) ** 0.5
    current_std = max(current_std, 1e-6)  # 避免除零

    print(f"\n电流统计: mean={current_mean:.2f}, std={current_std:.2f}")

    # 标准化电流
    for d in train_data + val_data + test_data:
        d['current_normalized'] = (d['current'] - current_mean) / current_std

    # 6. 保存
    print("\n" + "=" * 60)
    print("保存数据...")
    print("=" * 60)

    torch.save(train_data, data_dir / 'train_v2.pt')
    torch.save(val_data, data_dir / 'val_v2.pt')
    torch.save(test_data, data_dir / 'test_v2.pt')

    # 保存统计信息
    stats = {
        'total_reactions': len(processed_data),
        'train_size': len(train_data),
        'val_size': len(val_data),
        'test_size': len(test_data),
        'skipped': skipped,
        'atom_feat_dim': ATOM_FEAT_DIM,
        'bond_feat_dim': BOND_FEAT_DIM,
        'num_electrode_types': NUM_ELECTRODE_TYPES,
        'num_cell_types': NUM_CELL_TYPES,
        'current_mean': current_mean,
        'current_std': current_std,
        'anode_coverage': anode_stats['coverage'],
        'cathode_coverage': cathode_stats['coverage'],
        'anode_distribution': anode_stats['distribution'],
        'cathode_distribution': cathode_stats['distribution'],
    }

    with open(data_dir / 'stats_v2.json', 'w') as f:
        json.dump(stats, f, indent=2)

    print(f"\n数据已保存到 {data_dir}")
    print(f"  train_v2.pt: {len(train_data)} 样本")
    print(f"  val_v2.pt:   {len(val_data)} 样本")
    print(f"  test_v2.pt:  {len(test_data)} 样本")

    return stats


if __name__ == "__main__":
    prepare_data_v2()
