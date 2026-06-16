#!/usr/bin/env python3
"""
为反应数据集中缺失的分子运行xTB批量计算

复用已有的xTB环境: /inspire/hdd/global_user/gelingli-253114010248/xtb_install/xtb-dist/
"""
import argparse
import csv
import os
import re
import subprocess
import tempfile
from multiprocessing import Pool, cpu_count
from pathlib import Path

from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors

RDLogger.logger().setLevel(RDLogger.ERROR)

# xTB路径
BASE_DIR = "/inspire/hdd/global_user/gelingli-253114010248"
XTB_BIN = os.path.join(BASE_DIR, "xtb_install/xtb-dist/bin/xtb")
XTB_PATH = os.path.join(BASE_DIR, "xtb_install/xtb-dist/share/xtb")
XTB_LIB = os.path.join(BASE_DIR, "xtb_install/xtb-dist/lib")

# xTB环境变量
XTB_ENV = os.environ.copy()
XTB_ENV["XTBPATH"] = XTB_PATH
XTB_ENV["LD_LIBRARY_PATH"] = XTB_LIB + ":" + XTB_ENV.get("LD_LIBRARY_PATH", "")
XTB_ENV["OMP_NUM_THREADS"] = "1"
XTB_ENV["MKL_NUM_THREADS"] = "1"
XTB_ENV["OMP_STACKSIZE"] = "1G"

# 输入输出
SMILES_FILE = os.path.join(BASE_DIR, "WDproject2/yield_prediction/data/missing_xtb_smiles.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "WDproject2/yield_prediction/data/xtb_reaction_molecules.csv")

# CSV列名
FIELDNAMES = [
    "idx", "smiles", "status", "error",
    "num_heavy_atoms", "molecular_weight", "num_rotatable_bonds", "tpsa", "logp",
    "total_energy_Eh", "homo_lumo_gap_eV", "homo_eV", "lumo_eV",
    "dipole_total_Debye", "gsolv_Eh",
]


def get_largest_fragment(smiles):
    """对于多片段SMILES（盐类），返回最大片段"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, 0
    frags = Chem.GetMolFrags(mol, asMols=True)
    if len(frags) == 1:
        charge = Chem.GetFormalCharge(mol)
        return smiles, charge
    largest = max(frags, key=lambda m: m.GetNumHeavyAtoms())
    charge = Chem.GetFormalCharge(largest)
    return Chem.MolToSmiles(largest), charge


def smiles_to_xyz(smiles):
    """SMILES → 3D XYZ"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, 0
    charge = Chem.GetFormalCharge(mol)
    mol = Chem.AddHs(mol)

    params = AllChem.ETKDGv3()
    params.maxIterations = 500
    params.randomSeed = 42
    status = AllChem.EmbedMolecule(mol, params)
    if status == -1:
        params.useRandomCoords = True
        status = AllChem.EmbedMolecule(mol, params)
        if status == -1:
            return None, 0

    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
    except Exception:
        pass

    conf = mol.GetConformer()
    n_atoms = mol.GetNumAtoms()
    lines = [str(n_atoms), smiles]
    for i in range(n_atoms):
        pos = conf.GetAtomPosition(i)
        symbol = mol.GetAtomWithIdx(i).GetSymbol()
        lines.append(f"{symbol:2s} {pos.x:15.8f} {pos.y:15.8f} {pos.z:15.8f}")
    return "\n".join(lines) + "\n", charge


def parse_xtb_output(stdout, stderr=""):
    """解析xTB输出"""
    text = stdout + "\n" + stderr
    result = {}

    m = re.search(r"TOTAL ENERGY\s+([-\d.]+)\s+Eh", text)
    if m:
        result["total_energy_Eh"] = float(m.group(1))

    m = re.search(r"HOMO-LUMO GAP\s+([-\d.]+)\s+eV", text)
    if m:
        result["homo_lumo_gap_eV"] = float(m.group(1))

    m = re.search(r"([-\d.]+)\s+\(HOMO\)", text)
    if m:
        result["homo_eV"] = float(m.group(1))

    m = re.search(r"([-\d.]+)\s+\(LUMO\)", text)
    if m:
        result["lumo_eV"] = float(m.group(1))

    m = re.search(r"molecular dipole:.*?full:\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)", text, re.DOTALL)
    if m:
        result["dipole_total_Debye"] = float(m.group(4))

    m = re.search(r"-> Gsolv\s+([-\d.]+)\s+Eh", text)
    if m:
        result["gsolv_Eh"] = float(m.group(1))

    return result


def calc_xtb_single(args):
    """计算单个分子的xTB描述符"""
    idx, smiles = args

    result = {"idx": idx, "smiles": smiles, "status": "failed"}

    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            result["error"] = "RDKit parse failed"
            return result

        result["num_heavy_atoms"] = mol.GetNumHeavyAtoms()
        result["molecular_weight"] = round(Descriptors.MolWt(mol), 2)
        result["num_rotatable_bonds"] = rdMolDescriptors.CalcNumRotatableBonds(mol)
        result["tpsa"] = round(Descriptors.TPSA(mol), 2)
        result["logp"] = round(Descriptors.MolLogP(mol), 2)

        # 多片段处理
        calc_smiles, _ = get_largest_fragment(smiles)
        if calc_smiles is None:
            result["error"] = "Fragment extraction failed"
            return result

        calc_mol = Chem.MolFromSmiles(calc_smiles)
        if calc_mol is None:
            result["error"] = "Fragment parse failed"
            return result
        calc_mol_h = Chem.AddHs(calc_mol)
        n_total_atoms = calc_mol_h.GetNumAtoms()
        if n_total_atoms > 300:
            result["error"] = f"Too large ({n_total_atoms} atoms)"
            return result

        xyz_result = smiles_to_xyz(calc_smiles)
        if xyz_result is None or xyz_result[0] is None:
            result["error"] = "3D generation failed"
            return result
        xyz, frag_charge = xyz_result

        with tempfile.TemporaryDirectory() as tmpdir:
            xyz_file = os.path.join(tmpdir, "mol.xyz")
            with open(xyz_file, "w") as f:
                f.write(xyz)

            cmd = [
                XTB_BIN, xyz_file,
                "--gfn", "2",
                "--sp",
                "--chrg", str(frag_charge),
                "--uhf", "0",
                "--alpb", "water",
            ]

            proc = subprocess.run(
                cmd,
                capture_output=True, text=True,
                timeout=120, cwd=tmpdir, env=XTB_ENV,
            )

            if proc.returncode != 0:
                result["error"] = f"xTB failed (rc={proc.returncode})"
                xtb_desc = parse_xtb_output(proc.stdout, proc.stderr)
                if xtb_desc:
                    result.update(xtb_desc)
                return result

            xtb_desc = parse_xtb_output(proc.stdout)
            result.update(xtb_desc)
            result["status"] = "success"

    except subprocess.TimeoutExpired:
        result["error"] = "xTB timeout (120s)"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description='Run xTB for reaction molecules')
    parser.add_argument("--workers", type=int, default=min(16, cpu_count()),
                        help="Number of parallel workers")
    parser.add_argument("--smiles-file", type=str, default=SMILES_FILE)
    parser.add_argument("--output", type=str, default=OUTPUT_FILE)
    args = parser.parse_args()

    # 加载分子列表
    with open(args.smiles_file) as f:
        all_smiles = [line.strip() for line in f if line.strip()]

    print(f"需要计算的分子: {len(all_smiles)}")
    print(f"并行进程数: {args.workers}")
    print(f"输出文件: {args.output}")

    tasks = [(i, smi) for i, smi in enumerate(all_smiles)]
    success_count = 0
    fail_count = 0

    with open(args.output, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()

        with Pool(args.workers) as pool:
            for i, result in enumerate(pool.imap_unordered(calc_xtb_single, tasks, chunksize=10)):
                writer.writerow(result)
                if result["status"] == "success":
                    success_count += 1
                else:
                    fail_count += 1

                if (i + 1) % 200 == 0:
                    csvfile.flush()
                    total = success_count + fail_count
                    print(f"  [{total}/{len(all_smiles)}] "
                          f"success={success_count} fail={fail_count} "
                          f"({success_count/total*100:.1f}%)")

    print(f"\n完成! success={success_count}, fail={fail_count}")
    print(f"成功率: {success_count/(success_count+fail_count)*100:.1f}%")
    print(f"输出: {args.output}")


if __name__ == "__main__":
    main()
