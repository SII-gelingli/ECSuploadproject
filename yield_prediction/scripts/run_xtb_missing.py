"""并行计算 data_audited_v3 里缺失的 xTB 描述符，merge 进 xtb_cache.json。

xtb binary: /inspire/hdd/global_user/gelingli-253114010248/xtb_install/xtb-dist/bin/xtb
特征维度: 6 (xTB QC) + 5 (RDKit) = 11
"""
import sys
import os
import re
import json
import csv
import subprocess
import tempfile
import time
from pathlib import Path
from multiprocessing import Pool

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors
from tqdm import tqdm

# ---- xTB 配置 ----
XTB_ROOT = "/inspire/hdd/global_user/gelingli-253114010248/xtb_install/xtb-dist"
XTB_BIN = f"{XTB_ROOT}/bin/xtb"
XTB_PATH = f"{XTB_ROOT}/share/xtb"
XTB_LIB = f"{XTB_ROOT}/lib"
XTB_ENV = os.environ.copy()
XTB_ENV["XTBPATH"] = XTB_PATH
XTB_ENV["LD_LIBRARY_PATH"] = XTB_LIB + ":" + XTB_ENV.get("LD_LIBRARY_PATH", "")
XTB_ENV["OMP_NUM_THREADS"] = "1"
XTB_ENV["MKL_NUM_THREADS"] = "1"
XTB_ENV["OMP_STACKSIZE"] = "1G"

XTB_QC_COLS = ['total_energy_Eh', 'homo_lumo_gap_eV', 'homo_eV',
               'lumo_eV', 'dipole_total_Debye', 'gsolv_Eh']

project_root = Path(__file__).parent.parent
CACHE_PATH = project_root / 'data' / 'xtb_cache.json'
DATA_DIR = project_root / 'data_audited_v3'


def compute_rdkit(smiles: str):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return [0.0]*5
    return [
        float(mol.GetNumHeavyAtoms()),
        float(Descriptors.MolWt(mol)),
        float(rdMolDescriptors.CalcNumRotatableBonds(mol)),
        float(Descriptors.TPSA(mol)),
        float(Descriptors.MolLogP(mol)),
    ]


def smiles_to_xyz(smiles: str):
    """SMILES -> 3D 优化 -> XYZ 字符串 + 形式电荷。失败返回 None。"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, 0
    # 多片段取最大片段
    frags = Chem.GetMolFrags(mol, asMols=True)
    if len(frags) > 1:
        mol = max(frags, key=lambda m: m.GetNumHeavyAtoms())
    charge = Chem.GetFormalCharge(mol)
    try:
        mol = Chem.AddHs(mol)
        params = AllChem.ETKDGv3()
        params.randomSeed = 42
        ret = AllChem.EmbedMolecule(mol, params)
        if ret == -1:
            # 再试一次 with random coord
            params.useRandomCoords = True
            ret = AllChem.EmbedMolecule(mol, params)
            if ret == -1:
                return None, charge
        try:
            AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
        except Exception:
            pass
        xyz = Chem.MolToXYZBlock(mol)
        return xyz, charge
    except Exception:
        return None, charge


def parse_xtb_results(json_path: str, stdout: str):
    """从 xtbout.json + stdout 解析 6 维 QC 特征。

    返回 [total_energy_Eh, homo_lumo_gap_eV, homo_eV, lumo_eV,
          dipole_total_Debye, gsolv_Eh]
    """
    total_energy = 0.0
    gap_eV = 0.0
    if os.path.exists(json_path):
        try:
            d = json.load(open(json_path))
            total_energy = float(d.get('total energy', 0.0))
            gap_eV = float(d.get('HOMO-LUMO gap / eV', d.get('HOMO-LUMO gap/eV', 0.0)))
        except Exception:
            pass

    homo_eV = 0.0
    lumo_eV = 0.0
    m = re.search(r'([-\d.]+)\s*\(HOMO\)', stdout)
    if m: homo_eV = float(m.group(1))
    m = re.search(r'([-\d.]+)\s*\(LUMO\)', stdout)
    if m: lumo_eV = float(m.group(1))

    dipole_D = 0.0
    # "molecular dipole:" 段后面 "full:" 行最后一个数 = total Debye
    m = re.search(r'molecular dipole:[\s\S]*?full:[\s\d.+-]*?([-\d.]+)\s*$', stdout, re.MULTILINE)
    if m:
        dipole_D = float(m.group(1))
    else:
        # fallback: 找 "q+dip:" or "q only:" 末尾的 tot debye
        m = re.search(r'q only:[\s\d.+-]*?([-\d.]+)\s+([-\d.]+)\s*$', stdout, re.MULTILINE)

    gsolv_Eh = 0.0
    m = re.search(r'->\s*Gsolv\s+([-\d.]+)\s*Eh', stdout)
    if m: gsolv_Eh = float(m.group(1))

    return [total_energy, gap_eV, homo_eV, lumo_eV, dipole_D, gsolv_Eh]


def run_xtb_single(smiles: str, timeout: int = 60):
    """计算单个 SMILES 的 11 维特征。返回 None 表示完全失败。"""
    xyz, charge = smiles_to_xyz(smiles)
    rdkit_feat = compute_rdkit(smiles)
    if xyz is None:
        # 3D 失败：返回 [0]*6 + rdkit
        return {'smiles': smiles, 'status': 'rdkit_only',
                'features': [0.0]*6 + rdkit_feat}

    with tempfile.TemporaryDirectory() as tmpdir:
        xyz_path = os.path.join(tmpdir, 'mol.xyz')
        with open(xyz_path, 'w') as f:
            f.write(xyz)
        # 调用 xtb (gfn2, alpb water, json output)
        try:
            res = subprocess.run(
                [XTB_BIN, xyz_path, '--gfn', '2', '--alpb', 'water', '--json',
                 '--charge', str(charge)],
                cwd=tmpdir, env=XTB_ENV, timeout=timeout,
                capture_output=True, text=True,
            )
        except subprocess.TimeoutExpired:
            return {'smiles': smiles, 'status': 'timeout',
                    'features': [0.0]*6 + rdkit_feat}
        except Exception as e:
            return {'smiles': smiles, 'status': f'error:{e}',
                    'features': [0.0]*6 + rdkit_feat}

        qc = parse_xtb_results(os.path.join(tmpdir, 'xtbout.json'), res.stdout or '')
        if qc is None or res.returncode != 0:
            return {'smiles': smiles, 'status': 'xtb_failed',
                    'features': [0.0]*6 + rdkit_feat}
        return {'smiles': smiles, 'status': 'success',
                'features': qc + rdkit_feat}


def collect_missing_smiles():
    """收集 train/val/test 里所有反应物+产物+条件物质的 SMILES, 找出 cache 没有的。"""
    cache = {}
    if CACHE_PATH.exists():
        try:
            obj = json.load(open(CACHE_PATH))
            cache = obj.get('cache', {}) if isinstance(obj, dict) and 'cache' in obj else obj
        except Exception:
            cache = {}
    print(f"已有 xtb_cache 条目: {len(cache)}")

    all_smi = set()
    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in recs:
            for smi in r.get('reactant_smiles', []) + r.get('product_smiles', []):
                if smi: all_smi.add(smi)
    print(f"data_audited_v3 里所有反应分子: {len(all_smi)}")

    missing = sorted(all_smi - set(cache.keys()))
    print(f"缺失需要计算的: {len(missing)}")
    return cache, missing


def main(num_workers: int = 32):
    cache, missing = collect_missing_smiles()
    if not missing:
        print("无缺失，直接退出。")
        return

    print(f"\n开始用 {num_workers} 进程并行计算 xTB ...")
    start = time.time()
    success = 0
    rdkit_only = 0
    failed = 0
    with Pool(num_workers) as pool:
        for i, res in enumerate(tqdm(
            pool.imap_unordered(run_xtb_single, missing, chunksize=4),
            total=len(missing), desc="xTB calc",
        )):
            cache[res['smiles']] = res['features']
            if res['status'] == 'success':
                success += 1
            elif res['status'] == 'rdkit_only':
                rdkit_only += 1
            else:
                failed += 1
            if (i + 1) % 500 == 0:
                # 中途保存 cache
                json.dump({'cache': cache}, open(CACHE_PATH, 'w'))

    elapsed = time.time() - start
    print(f"\n完成: success={success}, rdkit_only={rdkit_only}, failed={failed}")
    print(f"用时 {elapsed:.1f}s ({elapsed/len(missing)*1000:.1f} ms/分子, 实际 wall-clock 速度受并行影响)")
    # 最后保存
    json.dump({'cache': cache}, open(CACHE_PATH, 'w'))
    print(f"Saved {CACHE_PATH}, 总计 {len(cache)} 条")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=32)
    args = parser.parse_args()
    main(num_workers=args.workers)
