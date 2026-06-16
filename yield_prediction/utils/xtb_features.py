"""
xTB量子化学描述符 + RDKit描述符模块

对于xTB量化特征（HOMO, LUMO等），优先从预计算CSV中查找；
查找失败时，如果xTB binary可用，则在线调用xTB计算；
对于RDKit描述符（MW, TPSA, LogP等），直接从SMILES计算（始终可用）。
"""
import csv
import os
import re
import subprocess
import tempfile
from typing import List, Dict, Optional
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors


# xTB量化特征列名（从CSV查找）
XTB_QC_COLS = [
    'total_energy_Eh',
    'homo_lumo_gap_eV',
    'homo_eV',
    'lumo_eV',
    'dipole_total_Debye',
    'gsolv_Eh',
]

# RDKit描述符（直接从SMILES计算）
RDKIT_DESC_NAMES = [
    'num_heavy_atoms',
    'molecular_weight',
    'num_rotatable_bonds',
    'tpsa',
    'logp',
]

# 每个分子的特征维度: 6 (xTB) + 5 (RDKit) = 11
SINGLE_MOL_FEAT_DIM = len(XTB_QC_COLS) + len(RDKIT_DESC_NAMES)  # 11

# 聚合后的反应特征维度: 反应物(11) + 产物(11) + 差异(11) + 溶剂(11) + 电解质(11) = 55
REACTION_XTB_FEAT_DIM = SINGLE_MOL_FEAT_DIM * 5  # 55


def compute_rdkit_descriptors(smiles: str) -> List[float]:
    """
    直接从SMILES计算RDKit描述符（始终可用，不依赖xTB）

    Returns:
        5维特征: [heavy_atoms, MW, rotatable_bonds, TPSA, LogP]
    """
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


# ── xTB 在线计算辅助函数 ──────────────────────────────────────

def _get_largest_fragment(smiles: str):
    """对于多片段SMILES（盐类），返回最大片段和总形式电荷。"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, 0
    frags = Chem.GetMolFrags(mol, asMols=True)
    if len(frags) == 1:
        return smiles, Chem.GetFormalCharge(mol)
    largest = max(frags, key=lambda m: m.GetNumHeavyAtoms())
    return Chem.MolToSmiles(largest), Chem.GetFormalCharge(largest)


def _smiles_to_xyz(smiles: str):
    """SMILES → RDKit 3D坐标 → XYZ字符串。返回 (xyz_str, charge) 或 (None, 0)。"""
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


def _parse_xtb_output(stdout: str, stderr: str = "") -> Optional[List[float]]:
    """
    解析xTB stdout，提取6维QC特征。

    返回 [total_energy, homo_lumo_gap, homo, lumo, dipole, gsolv] 或 None（解析失败）。
    """
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

    m = re.search(r"molecular dipole:.*?full:\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)",
                  text, re.DOTALL)
    if m:
        result["dipole_total_Debye"] = float(m.group(4))

    m = re.search(r"-> Gsolv\s+([-\d.]+)\s+Eh", text)
    if m:
        result["gsolv_Eh"] = float(m.group(1))

    # 需要全部6个特征都解析成功
    qc_features = []
    for col in XTB_QC_COLS:
        if col not in result:
            return None
        qc_features.append(result[col])

    return qc_features


class XTBFeatureLookup:
    """xTB描述符查找表 + RDKit描述符直接计算 + xTB在线计算"""

    def __init__(self, csv_path: str = None,
                 xtb_bin: str = None, xtb_data: str = None,
                 xtb_lib: str = None, timeout: int = 60):
        """
        Args:
            csv_path: xTB描述符CSV文件路径（可选，如果为None则只用RDKit + 在线计算）
            xtb_bin: xTB可执行文件路径（可选，用于在线计算CSV中缺失的分子）
            xtb_data: xTB数据目录（XTBPATH），默认None
            xtb_lib: xTB库目录（LD_LIBRARY_PATH），默认None
            timeout: xTB计算超时秒数，默认60
        """
        self.csv_path = csv_path
        self.xtb_lookup = {}  # SMILES → xTB QC features (6维)
        self._rdkit_cache = {}  # SMILES → RDKit descriptors (5维) 缓存
        self._xtb_failed = set()  # 在线计算失败过的SMILES，避免重复尝试

        # xTB在线计算配置
        self._xtb_bin = xtb_bin
        self._xtb_data = xtb_data
        self._xtb_lib = xtb_lib
        self._xtb_timeout = timeout
        self._xtb_available = None  # None = 未检测, True/False = 已检测

        if csv_path:
            self._load_csv()

        # 标准化参数
        self.mean = None
        self.std = None

    def _check_xtb_available(self) -> bool:
        """惰性检测xTB binary是否可用。"""
        if self._xtb_available is not None:
            return self._xtb_available

        if not self._xtb_bin or not os.path.isfile(self._xtb_bin):
            self._xtb_available = False
            if self._xtb_bin:
                print(f"  [xTB] binary不存在: {self._xtb_bin}，在线计算不可用")
            return False

        if not os.access(self._xtb_bin, os.X_OK):
            self._xtb_available = False
            print(f"  [xTB] binary不可执行: {self._xtb_bin}，在线计算不可用")
            return False

        self._xtb_available = True
        print(f"  [xTB] 在线计算已启用 (binary: {self._xtb_bin}, timeout: {self._xtb_timeout}s)")
        return True

    def _build_xtb_env(self) -> dict:
        """构建xTB运行环境变量。"""
        env = os.environ.copy()
        if self._xtb_data:
            env["XTBPATH"] = self._xtb_data
        if self._xtb_lib:
            env["LD_LIBRARY_PATH"] = self._xtb_lib + ":" + env.get("LD_LIBRARY_PATH", "")
        env["OMP_NUM_THREADS"] = "1"
        env["MKL_NUM_THREADS"] = "1"
        env["OMP_STACKSIZE"] = "1G"
        return env

    def _compute_xtb_single(self, smiles: str) -> Optional[List[float]]:
        """
        在线计算单个分子的xTB QC特征 (6维)。

        流程: SMILES → 最大片段 → RDKit 3D → XYZ → xTB GFN2-SP → 解析输出
        失败返回 None。
        """
        if not self._check_xtb_available():
            return None

        if smiles in self._xtb_failed:
            return None

        try:
            # 多片段取最大片段
            calc_smiles, _ = _get_largest_fragment(smiles)
            if calc_smiles is None:
                self._xtb_failed.add(smiles)
                return None

            # 跳过大分子
            calc_mol = Chem.MolFromSmiles(calc_smiles)
            if calc_mol is None:
                self._xtb_failed.add(smiles)
                return None
            n_atoms_with_h = Chem.AddHs(calc_mol).GetNumAtoms()
            if n_atoms_with_h > 300:
                self._xtb_failed.add(smiles)
                return None

            # 生成3D坐标
            xyz_str, charge = _smiles_to_xyz(calc_smiles)
            if xyz_str is None:
                self._xtb_failed.add(smiles)
                return None

            # 在临时目录中运行xTB
            with tempfile.TemporaryDirectory() as tmpdir:
                xyz_file = os.path.join(tmpdir, "mol.xyz")
                with open(xyz_file, "w") as f:
                    f.write(xyz_str)

                cmd = [
                    self._xtb_bin, xyz_file,
                    "--gfn", "2",
                    "--sp",
                    "--chrg", str(charge),
                    "--uhf", "0",
                    "--alpb", "water",
                ]

                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=self._xtb_timeout,
                    cwd=tmpdir,
                    env=self._build_xtb_env(),
                )

                qc_features = _parse_xtb_output(proc.stdout, proc.stderr)
                if qc_features is None:
                    self._xtb_failed.add(smiles)
                    return None

                return qc_features

        except subprocess.TimeoutExpired:
            print(f"  [xTB] 超时 ({self._xtb_timeout}s): {smiles[:80]}")
            self._xtb_failed.add(smiles)
            return None
        except Exception as e:
            print(f"  [xTB] 计算异常: {smiles[:80]} -> {e}")
            self._xtb_failed.add(smiles)
            return None

    def _load_csv(self):
        """加载xTB CSV中的量化特征"""
        print(f"加载xTB描述符: {self.csv_path}")
        success_count = 0
        fail_count = 0

        with open(self.csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                smiles = row.get('smiles', '')
                if not smiles:
                    continue

                if row.get('status') == 'success':
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
                        self.xtb_lookup[smiles] = qc_features
                        success_count += 1
                    else:
                        fail_count += 1
                else:
                    fail_count += 1

        print(f"  xTB量化特征加载: {success_count} 个分子")
        print(f"  加载失败/跳过: {fail_count} 个分子")

    def get_features(self, smiles: str) -> List[float]:
        """
        获取单个分子的完整特征 (11维)

        = xTB量化特征(6维) + RDKit描述符(5维)

        xTB量化特征：优先CSV查找 → 在线xTB计算 → 全零兜底
        RDKit描述符：直接从SMILES计算
        """
        # xTB量化特征 (6维)
        if smiles and smiles in self.xtb_lookup:
            qc_feat = self.xtb_lookup[smiles]
        elif smiles:
            # CSV中没有，尝试在线计算
            qc_feat = self._compute_xtb_single(smiles)
            if qc_feat is not None:
                # 缓存计算结果
                self.xtb_lookup[smiles] = qc_feat
            else:
                qc_feat = [0.0] * len(XTB_QC_COLS)
        else:
            qc_feat = [0.0] * len(XTB_QC_COLS)

        # RDKit描述符 (5维) — 从缓存或直接计算
        if smiles and smiles in self._rdkit_cache:
            rdkit_feat = self._rdkit_cache[smiles]
        elif smiles:
            rdkit_feat = compute_rdkit_descriptors(smiles)
            self._rdkit_cache[smiles] = rdkit_feat
        else:
            rdkit_feat = [0.0] * len(RDKIT_DESC_NAMES)

        return qc_feat + rdkit_feat

    def get_aggregated_features(self, smiles_list: List[str]) -> List[float]:
        """获取多个分子的聚合特征（均值）"""
        if not smiles_list:
            return [0.0] * SINGLE_MOL_FEAT_DIM

        all_feats = [self.get_features(smi) for smi in smiles_list]

        # 逐维求均值
        n = len(all_feats)
        result = [0.0] * SINGLE_MOL_FEAT_DIM
        for feat in all_feats:
            for i in range(SINGLE_MOL_FEAT_DIM):
                result[i] += feat[i]
        for i in range(SINGLE_MOL_FEAT_DIM):
            result[i] /= n

        return result

    def get_reaction_features(
        self,
        reactant_smiles: List[str],
        product_smiles: List[str],
        solvent_smiles: List[str],
        electrolyte_smiles: str
    ) -> List[float]:
        """
        获取完整反应的特征

        组合: [反应物均值(11), 产物均值(11), 差异(11), 溶剂均值(11), 电解质(11)]
        总计55维
        """
        reactant_feat = self.get_aggregated_features(reactant_smiles)
        product_feat = self.get_aggregated_features(product_smiles)

        # 差异特征
        diff_feat = [product_feat[i] - reactant_feat[i] for i in range(SINGLE_MOL_FEAT_DIM)]

        solvent_feat = self.get_aggregated_features(solvent_smiles)
        electrolyte_feat = self.get_features(electrolyte_smiles) if electrolyte_smiles else [0.0] * SINGLE_MOL_FEAT_DIM

        return reactant_feat + product_feat + diff_feat + solvent_feat + electrolyte_feat

    def compute_normalization(self, feature_arrays: List[List[float]]):
        """基于训练数据计算标准化参数"""
        if not feature_arrays:
            return

        n = len(feature_arrays)
        dim = len(feature_arrays[0])

        # 计算均值
        self.mean = [0.0] * dim
        for feat in feature_arrays:
            for i in range(dim):
                self.mean[i] += feat[i]
        for i in range(dim):
            self.mean[i] /= n

        # 计算标准差
        self.std = [0.0] * dim
        for feat in feature_arrays:
            for i in range(dim):
                self.std[i] += (feat[i] - self.mean[i]) ** 2
        for i in range(dim):
            self.std[i] = max((self.std[i] / n) ** 0.5, 1e-8)

        print(f"  xTB标准化参数已计算 (维度: {dim})")

    def normalize(self, features: List[float]) -> List[float]:
        """对特征做z-score标准化"""
        if self.mean is None or self.std is None:
            return features
        return [(features[i] - self.mean[i]) / self.std[i] for i in range(len(features))]

    def get_normalization_stats(self) -> Dict:
        """返回标准化参数"""
        return {
            'mean': self.mean,
            'std': self.std,
        }

    def set_normalization_stats(self, stats: Dict):
        """设置标准化参数"""
        self.mean = stats.get('mean')
        self.std = stats.get('std')

    def check_coverage(
        self,
        reactant_smiles_list: List[List[str]],
        product_smiles_list: List[List[str]]
    ) -> Dict:
        """检查xTB量化特征覆盖率"""
        all_smiles = set()
        for smi_list in reactant_smiles_list + product_smiles_list:
            for smi in smi_list:
                all_smiles.add(smi)

        found = sum(1 for s in all_smiles if s in self.xtb_lookup)
        total = len(all_smiles)

        return {
            'total_unique_molecules': total,
            'found_in_xtb': found,
            'xtb_coverage': found / total if total > 0 else 0.0,
            'rdkit_coverage': 1.0,  # RDKit描述符始终可计算
        }
