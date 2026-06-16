"""
计算缺失的xTB特征

从训练数据中提取所有分子SMILES，计算那些在现有xTB CSV中没有的分子的xTB特征。
"""
import sys
import csv
import json
import subprocess
import tempfile
import os
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
if LOCAL_PACKAGES not in sys.path:
    sys.path.insert(0, LOCAL_PACKAGES)

import torch
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors
from tqdm import tqdm

project_root = Path(__file__).parent.parent


def compute_rdkit_descriptors(smiles: str):
    """计算RDKit描述符"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return {
        'num_heavy_atoms': mol.GetNumHeavyAtoms(),
        'molecular_weight': Descriptors.MolWt(mol),
        'num_rotatable_bonds': rdMolDescriptors.CalcNumRotatableBonds(mol),
        'tpsa': Descriptors.TPSA(mol),
        'logp': Descriptors.MolLogP(mol),
    }


def run_xtb_single(smiles: str, timeout: int = 120):
    """运行xTB计算单个分子"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {'smiles': smiles, 'status': 'failed', 'error': 'Invalid SMILES'}

    try:
        mol = Chem.AddHs(mol)
        result = AllChem.EmbedMolecule(mol, randomSeed=42, maxAttempts=100)
        if result == -1:
            # 尝试使用随机坐标
            AllChem.EmbedMolecule(mol, useRandomCoords=True, randomSeed=42)
        AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
    except Exception as e:
        return {'smiles': smiles, 'status': 'failed', 'error': f'3D generation failed: {str(e)}'}

    try:
        conf = mol.GetConformer()
    except Exception:
        return {'smiles': smiles, 'status': 'failed', 'error': 'No conformer'}

    with tempfile.TemporaryDirectory() as tmpdir:
        xyz_path = os.path.join(tmpdir, "mol.xyz")
        try:
            # 写入XYZ文件
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

                rdkit_desc = compute_rdkit_descriptors(smiles)
                if rdkit_desc is None:
                    return {'smiles': smiles, 'status': 'failed', 'error': 'RDKit failed'}

                return {
                    'smiles': smiles,
                    'status': 'success',
                    'error': '',
                    **rdkit_desc,
                    'total_energy_Eh': data.get('total energy', 0.0),
                    'homo_lumo_gap_eV': data.get('HOMO-LUMO gap/eV', 0.0),
                    'homo_eV': data.get('HOMO', 0.0),
                    'lumo_eV': data.get('LUMO', 0.0),
                    'dipole_total_Debye': data.get('dipole', 0.0),
                    'gsolv_Eh': data.get('gsolv', 0.0),
                }
            else:
                return {'smiles': smiles, 'status': 'failed', 'error': 'xTB output not found'}

        except subprocess.TimeoutExpired:
            return {'smiles': smiles, 'status': 'failed', 'error': 'Timeout'}
        except Exception as e:
            return {'smiles': smiles, 'status': 'failed', 'error': str(e)}


def process_batch(smiles_list, idx_start):
    """处理一批SMILES"""
    results = []
    for i, smi in enumerate(smiles_list):
        result = run_xtb_single(smi)
        result['idx'] = idx_start + i
        results.append(result)
    return results


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_data', type=str, default=str(project_root / 'data' / 'train.pt'))
    parser.add_argument('--existing_csv', type=str, default=str(project_root / 'data' / 'xtb_reaction_molecules.csv'))
    parser.add_argument('--output_csv', type=str, default=str(project_root / 'data' / 'xtb_reaction_molecules_extended.csv'))
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--batch_size', type=int, default=100)
    args = parser.parse_args()

    # 加载训练数据
    print(f"加载训练数据: {args.train_data}")
    train_data = torch.load(args.train_data)
    print(f"  样本数: {len(train_data)}")

    # 提取所有SMILES
    all_smiles = set()
    for sample in train_data:
        for smi in sample.get('reactant_smiles', []):
            if smi:
                all_smiles.add(smi)
        for smi in sample.get('product_smiles', []):
            if smi:
                all_smiles.add(smi)
        for smi in sample.get('solvent_smiles', []):
            if smi:
                all_smiles.add(smi)
        electrolyte = sample.get('electrolyte_smiles', '')
        if electrolyte:
            all_smiles.add(electrolyte)

    print(f"  唯一分子数: {len(all_smiles)}")

    # 加载现有xTB数据
    existing_smiles = set()
    existing_data = []
    if Path(args.existing_csv).exists():
        print(f"\n加载现有xTB数据: {args.existing_csv}")
        with open(args.existing_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_smiles.add(row['smiles'])
                existing_data.append(row)
        print(f"  已有xTB数据: {len(existing_smiles)}")

    # 找出缺失的SMILES
    missing_smiles = all_smiles - existing_smiles
    print(f"\n缺失的分子: {len(missing_smiles)}")

    if len(missing_smiles) == 0:
        print("没有缺失的分子，无需计算")
        return

    # 计算缺失的xTB特征
    print(f"\n计算缺失的xTB特征 (workers={args.workers})...")
    missing_list = list(missing_smiles)

    new_results = []
    success_count = 0
    fail_count = 0

    # 使用进度条
    with tqdm(total=len(missing_list), desc="Computing xTB") as pbar:
        # 由于xTB需要临时目录，使用顺序处理更稳定
        for i, smi in enumerate(missing_list):
            result = run_xtb_single(smi)
            result['idx'] = len(existing_data) + i
            new_results.append(result)

            if result['status'] == 'success':
                success_count += 1
            else:
                fail_count += 1

            pbar.update(1)
            pbar.set_postfix({'success': success_count, 'fail': fail_count})

    print(f"\n计算完成:")
    print(f"  成功: {success_count}")
    print(f"  失败: {fail_count}")

    # 合并数据并保存
    print(f"\n保存扩展的xTB数据: {args.output_csv}")

    fieldnames = [
        'idx', 'smiles', 'status', 'error',
        'num_heavy_atoms', 'molecular_weight', 'num_rotatable_bonds', 'tpsa', 'logp',
        'total_energy_Eh', 'homo_lumo_gap_eV', 'homo_eV', 'lumo_eV', 'dipole_total_Debye', 'gsolv_Eh'
    ]

    with open(args.output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # 写入现有数据
        for row in existing_data:
            writer.writerow({k: row.get(k, '') for k in fieldnames})

        # 写入新数据
        for result in new_results:
            writer.writerow({k: result.get(k, '') for k in fieldnames})

    total_success = len([r for r in existing_data if r.get('status') == 'success']) + success_count
    print(f"\n扩展后的xTB数据:")
    print(f"  总分子数: {len(existing_data) + len(new_results)}")
    print(f"  成功计算: {total_success}")


if __name__ == "__main__":
    main()
