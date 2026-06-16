"""
GNN数据预处理脚本：将原始反应数据转换为分子图 + xTB特征，保存到data目录
"""
import sys
import json
from pathlib import Path

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
from tqdm import tqdm
from sklearn.model_selection import train_test_split

# 抑制RDKit的解析警告
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.graph_features import smiles_to_graph, smiles_list_to_graph, get_dummy_graph, ATOM_FEAT_DIM, BOND_FEAT_DIM
from utils.xtb_features import XTBFeatureLookup, REACTION_XTB_FEAT_DIM
from utils.feature_extractor import MolecularFeatureExtractor


def prepare_gnn_data():
    """准备GNN训练数据"""
    data_dir = project_root / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    # 1. 加载原始反应数据
    print("=" * 60)
    print("加载原始反应数据...")
    print("=" * 60)
    processor = ReactionDataProcessor(
        yield_data_dir="/inspire/hdd/global_user/gelingli-253114010248/alkene_reactions_by_yield",
        smiles_data_path="/inspire/hdd/global_user/gelingli-253114010248/extracted_smiles.json"
    )
    reactions = processor.load_yield_data()

    # 2. 加载xTB描述符
    print("\n" + "=" * 60)
    print("加载xTB描述符...")
    print("=" * 60)
    xtb_lookup = XTBFeatureLookup(
        csv_path="/inspire/hdd/global_user/gelingli-253114010248/xtb_batch/xtb_descriptors_all.csv"
    )

    # 3. 电极编码映射
    electrode_map = {
        'carbon': 0, 'graphite': 1, 'platinum': 2, 'platinum plate': 2,
        'carbon rod': 0, 'glassy carbon': 3, 'rvc': 4, 'nickel': 5,
        'stainless steel': 6, 'copper': 7, 'zinc': 8, 'lead': 9,
        'gold': 10, 'silver': 11, 'iron': 12, 'magnesium': 13, '': 14
    }
    cell_map = {'undivided': 0, 'divided': 1, 'h-cell': 2, 'flow': 3, '': 4}

    def encode_electrode(e):
        if e is None:
            return 14
        return electrode_map.get(e.lower().strip(), 14)

    def encode_cell(c):
        if c is None:
            return 4
        return cell_map.get(c.lower().strip(), 4)

    def parse_numeric(s, factor=1.0):
        """从字符串中提取数值"""
        if not s:
            return 0.0
        try:
            import re
            s = s.lower().replace(' ', '')
            if 'ma' in s:
                return float(s.replace('ma', '')) * factor
            elif 'a' in s and 'ma' not in s:
                return float(s.replace('a', '')) * 1000 * factor
            nums = re.findall(r'[-\d.]+', s)
            if nums:
                return float(nums[0])
            return 0.0
        except (ValueError, AttributeError):
            return 0.0

    # 4. 指纹提取器（供hybrid模型使用）
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    # 5. 处理每个反应
    print("\n" + "=" * 60)
    print("处理反应数据为图格式...")
    print("=" * 60)

    processed_data = []
    skipped = 0
    all_reactant_smiles = []
    all_product_smiles = []

    for rxn in tqdm(reactions, desc="处理反应"):
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

            # xTB特征
            xtb_features = xtb_lookup.get_reaction_features(
                reactant_smiles=reactant_smiles,
                product_smiles=product_smiles,
                solvent_smiles=solvent_smiles,
                electrolyte_smiles=electrolyte_smiles,
            )

            # 电化学条件
            anode = encode_electrode(echem.get('anode', ''))
            cathode = encode_electrode(echem.get('cathode', ''))
            current = parse_numeric(echem.get('current', ''))
            current_density = parse_numeric(echem.get('current_density', ''))
            potential = parse_numeric(echem.get('potential', ''))
            cell_type = encode_cell(echem.get('cell_type', ''))

            echem_features = [
                float(anode), float(cathode), current, current_density, potential, float(cell_type)
            ]

            yield_value = rxn.get('yield_value', 0)

            # 反应指纹（供hybrid模型使用）
            reaction_fp = mol_extractor.encode_reaction(reactant_smiles, product_smiles)

            processed_data.append({
                'reactant_graph': reactant_graph,
                'product_graph': product_graph,
                'solvent_graph': solvent_graph,
                'electrolyte_graph': electrolyte_graph,
                'xtb_features': torch.tensor(xtb_features, dtype=torch.float32),
                'echem_features': torch.tensor(echem_features, dtype=torch.float32),
                'reaction_fp': torch.tensor(reaction_fp, dtype=torch.float32),
                'yield': float(yield_value),
            })

            all_reactant_smiles.append(reactant_smiles)
            all_product_smiles.append(product_smiles)

        except Exception as e:
            skipped += 1
            continue

    print(f"\n成功处理: {len(processed_data)} 个反应")
    print(f"跳过: {skipped} 个反应")

    # 5. 检查xTB覆盖率
    print("\n" + "=" * 60)
    print("xTB特征覆盖率检查...")
    print("=" * 60)
    coverage = xtb_lookup.check_coverage(all_reactant_smiles, all_product_smiles)
    print(f"  唯一分子数: {coverage['total_unique_molecules']}")
    print(f"  xTB量化覆盖: {coverage['found_in_xtb']}")
    print(f"  xTB覆盖率: {coverage['xtb_coverage']:.2%}")
    print(f"  RDKit描述符: 100% (直接从SMILES计算)")

    # 6. 划分数据集
    print("\n" + "=" * 60)
    print("划分数据集...")
    print("=" * 60)
    train_data, temp_data = train_test_split(processed_data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

    print(f"  Train: {len(train_data)}")
    print(f"  Val:   {len(val_data)}")
    print(f"  Test:  {len(test_data)}")

    # 7. 计算xTB标准化参数（基于训练集）
    print("\n计算xTB特征标准化参数...")
    train_xtb_feats = [d['xtb_features'].tolist() for d in train_data]
    xtb_lookup.compute_normalization(train_xtb_feats)

    # 标准化所有数据的xTB特征
    for d in train_data + val_data + test_data:
        normalized = xtb_lookup.normalize(d['xtb_features'].tolist())
        d['xtb_features'] = torch.tensor(normalized, dtype=torch.float32)

    # 8. 保存
    print("\n" + "=" * 60)
    print("保存数据...")
    print("=" * 60)
    torch.save(train_data, data_dir / 'train_gnn.pt')
    torch.save(val_data, data_dir / 'val_gnn.pt')
    torch.save(test_data, data_dir / 'test_gnn.pt')

    # 保存统计信息
    stats = {
        'total_reactions': len(processed_data),
        'train_size': len(train_data),
        'val_size': len(val_data),
        'test_size': len(test_data),
        'skipped': skipped,
        'atom_feat_dim': ATOM_FEAT_DIM,
        'bond_feat_dim': BOND_FEAT_DIM,
        'xtb_feat_dim': REACTION_XTB_FEAT_DIM,
        'echem_feat_dim': 6,
        'xtb_coverage': coverage,
        'xtb_normalization': xtb_lookup.get_normalization_stats(),
    }

    with open(data_dir / 'gnn_stats.json', 'w') as f:
        json.dump(stats, f, indent=2, default=lambda x: x.tolist() if hasattr(x, 'tolist') else str(x))

    print(f"\n数据已保存到 {data_dir}")
    print(f"  train_gnn.pt: {len(train_data)} 样本")
    print(f"  val_gnn.pt:   {len(val_data)} 样本")
    print(f"  test_gnn.pt:  {len(test_data)} 样本")
    print(f"  gnn_stats.json: 统计信息")

    return stats


if __name__ == "__main__":
    prepare_gnn_data()
