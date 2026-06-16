"""
数据预处理脚本：将原始数据处理并保存到data目录
"""
import sys
import json
from pathlib import Path
from collections import Counter

import torch
import numpy

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

from tqdm import tqdm
from sklearn.model_selection import train_test_split

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor
from utils.feature_extractor import MolecularFeatureExtractor
from utils.electrode_normalizer import electrode_to_id, NUM_ELECTRODE_TYPES


def prepare_and_save_data():
    """准备数据并保存"""
    data_dir = project_root / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    print("Loading raw data...")
    processor = ReactionDataProcessor(
        yield_data_dir="/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/data/alkene_reactions_by_yield",
        smiles_data_path="/inspire/hdd/global_user/gelingli-253114010248/extracted_smiles.json"
    )
    reactions = processor.load_combined_data(include_failed=True)

    # 构建词汇表（完全涵盖所有种类）
    print("Building vocabularies...")
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

    # 按频率排序，index 0 保留给 UNK，全部纳入词汇表
    vocab = {
        'electrolyte': {e: i + 1 for i, (e, _) in enumerate(electrolytes.most_common())},
        'solvent': {s: i + 1 for i, (s, _) in enumerate(solvents.most_common())},
        'reagent': {r: i + 1 for i, (r, _) in enumerate(reagents.most_common())},
        'catalyst': {c: i + 1 for i, (c, _) in enumerate(catalysts.most_common())}
    }

    with open(data_dir / 'vocab.json', 'w') as f:
        json.dump(vocab, f, indent=2)
    print(f"Saved vocab: electrolyte={len(vocab['electrolyte'])}, solvent={len(vocab['solvent'])}, "
          f"reagent={len(vocab['reagent'])}, catalyst={len(vocab['catalyst'])}")

    # 特征提取
    print("Extracting features...")
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    processed_data = []
    for rxn in tqdm(reactions, desc="Processing"):
        try:
            # 反应指纹
            reactant_smiles = [r.get('smiles', '') for r in rxn.get('reactants', [])]
            product_smiles = [p.get('smiles', '') for p in rxn.get('products', [])]

            reactant_fp = mol_extractor.encode_molecules(reactant_smiles)
            product_fp = mol_extractor.encode_molecules(product_smiles)

            reactant_t = torch.tensor(reactant_fp, dtype=torch.float32)
            product_t = torch.tensor(product_fp, dtype=torch.float32)
            diff_t = torch.abs(product_t - reactant_t)

            # 溶剂/电解质指纹
            solvent_smiles = [s.get('smiles', '') for s in rxn.get('solvents', [])]
            solvent_fp = mol_extractor.encode_molecules(solvent_smiles)

            echem = rxn.get('electrochemistry_params', {})
            electrolyte_smiles = echem.get('electrolyte', '')
            electrolyte_fp = mol_extractor.get_morgan_fingerprint(electrolyte_smiles) if electrolyte_smiles else [0] * 2048

            # 条件标签（使用electrode_normalizer进行归一化）
            def encode_cell(c):
                cells = {'undivided': 0, 'divided': 1, 'h-cell': 2, 'flow': 3, '': 4}
                if c is None:
                    return 4
                return cells.get(c.lower().strip(), 4)

            anode = electrode_to_id(echem.get('anode', ''))
            cathode = electrode_to_id(echem.get('cathode', ''))
            cell_type = encode_cell(echem.get('cell_type', ''))
            electrolyte_label = vocab['electrolyte'].get(electrolyte_smiles, 0)

            solvent_label = 0
            if solvent_smiles:
                solvent_label = vocab['solvent'].get(solvent_smiles[0], 0)

            reagent_label = 0
            reagents_list = rxn.get('reagents', [])
            if reagents_list:
                reagent_label = vocab['reagent'].get(reagents_list[0].get('smiles', ''), 0)

            catalyst_label = 0
            catalysts_list = rxn.get('catalysts', [])
            if catalysts_list:
                catalyst_label = vocab['catalyst'].get(catalysts_list[0].get('smiles', ''), 0)

            yield_value = rxn.get('yield_value', 0)

            processed_data.append({
                'reactant_fp': reactant_t.tolist(),
                'product_fp': product_t.tolist(),
                'diff_fp': diff_t.tolist(),
                'solvent_fp': list(solvent_fp),
                'electrolyte_fp': list(electrolyte_fp),
                'anode': anode,
                'cathode': cathode,
                'cell_type': cell_type,
                'electrolyte_label': electrolyte_label,
                'solvent_label': solvent_label,
                'reagent_label': reagent_label,
                'catalyst_label': catalyst_label,
                'yield': yield_value,
                'reactant_smiles': reactant_smiles,
                'product_smiles': product_smiles
            })
        except Exception as e:
            continue

    print(f"Processed {len(processed_data)} reactions")

    # 划分数据集
    train_data, temp_data = train_test_split(processed_data, test_size=0.2, random_state=42)
    val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

    # 保存
    torch.save(train_data, data_dir / 'train.pt')
    torch.save(val_data, data_dir / 'val.pt')
    torch.save(test_data, data_dir / 'test.pt')

    print(f"Saved: train={len(train_data)}, val={len(val_data)}, test={len(test_data)}")
    print(f"Data saved to {data_dir}")

    # 统计信息
    stats = {
        'total_reactions': len(processed_data),
        'train_size': len(train_data),
        'val_size': len(val_data),
        'test_size': len(test_data),
        'feature_dims': {
            'reaction_fp': 2048 * 3,
            'solvent_fp': 2048,
            'electrolyte_fp': 2048,
            'total': 2048 * 5 + 6
        },
        'num_classes': {
            'anode': NUM_ELECTRODE_TYPES,
            'cathode': NUM_ELECTRODE_TYPES,
            'cell_type': 5,
            'electrolyte': len(vocab['electrolyte']) + 1,
            'solvent': len(vocab['solvent']) + 1,
            'reagent': len(vocab['reagent']) + 1,
            'catalyst': len(vocab['catalyst']) + 1
        }
    }
    with open(data_dir / 'stats.json', 'w') as f:
        json.dump(stats, f, indent=2)

    return stats


if __name__ == "__main__":
    prepare_and_save_data()
