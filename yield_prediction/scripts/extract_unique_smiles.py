"""
提取反应数据集中所有唯一分子SMILES，用于xTB批量计算
"""
import sys
import json
from pathlib import Path

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

from rdkit import Chem, RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.data_processor import ReactionDataProcessor


def extract_unique_smiles():
    """提取所有唯一分子SMILES"""
    processor = ReactionDataProcessor(
        yield_data_dir="/inspire/hdd/global_user/gelingli-253114010248/alkene_reactions_by_yield",
        smiles_data_path="/inspire/hdd/global_user/gelingli-253114010248/extracted_smiles.json"
    )
    reactions = processor.load_yield_data()

    all_smiles = set()
    for rxn in reactions:
        for r in rxn.get('reactants', []):
            smi = r.get('smiles', '')
            if smi:
                all_smiles.add(smi)
        for p in rxn.get('products', []):
            smi = p.get('smiles', '')
            if smi:
                all_smiles.add(smi)
        for s in rxn.get('solvents', []):
            smi = s.get('smiles', '')
            if smi:
                all_smiles.add(smi)
        echem = rxn.get('electrochemistry_params', {})
        elec = echem.get('electrolyte', '')
        if elec:
            all_smiles.add(elec)
        for rg in rxn.get('reagents', []):
            smi = rg.get('smiles', '')
            if smi:
                all_smiles.add(smi)

    # 过滤掉RDKit无法解析的
    valid_smiles = []
    invalid = 0
    for smi in sorted(all_smiles):
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            valid_smiles.append(smi)
        else:
            invalid += 1

    # 检查已有xTB覆盖
    existing_xtb = set()
    xtb_csv = "/inspire/hdd/global_user/gelingli-253114010248/xtb_batch/xtb_descriptors_all.csv"
    import csv
    with open(xtb_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('status') == 'success':
                existing_xtb.add(row.get('smiles', ''))

    missing = [s for s in valid_smiles if s not in existing_xtb]
    already_have = [s for s in valid_smiles if s in existing_xtb]

    print(f"反应数据集唯一分子: {len(all_smiles)}")
    print(f"RDKit可解析: {len(valid_smiles)}")
    print(f"RDKit无法解析: {invalid}")
    print(f"已有xTB结果: {len(already_have)}")
    print(f"需要计算xTB: {len(missing)}")

    # 保存需要计算的分子列表
    output_path = project_root / 'data' / 'missing_xtb_smiles.txt'
    with open(output_path, 'w') as f:
        for smi in missing:
            f.write(smi + '\n')
    print(f"\n需要计算的分子已保存到: {output_path}")

    return missing


if __name__ == "__main__":
    extract_unique_smiles()
