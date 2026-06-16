"""RDKit 官能团计数特征。

每个分子计 22 个 FG 数，反应汇总成 22*3 = 66 维 (reactant_agg + product_agg + diff)。
"""
from typing import List
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem


# 22 个常见有机/电化学反应相关官能团 (SMARTS)
FG_PATTERNS = [
    ('hydroxyl',     '[OX2H]'),                                    # -OH (alcohols + phenols)
    ('amine_NH',     '[NX3;H2,H1;!$(NC=O);!$(N=*);!$([N+])]'),    # primary/secondary amine (excl. amide/imine)
    ('amine_3',      '[NX3;H0;!$(NC=O);!$(N=*);!$([N+])]'),       # tertiary amine
    ('amide',        '[NX3][CX3]=[OX1]'),                          # -C(=O)N-
    ('carboxyl',     '[CX3](=O)[OX2H1]'),                          # -COOH
    ('ester',        '[#6][CX3](=O)[OX2H0][#6]'),                  # -COOR
    ('ketone',       '[#6][CX3](=O)[#6]'),                         # R-CO-R (excl. aldehyde)
    ('aldehyde',     '[CX3H1](=O)[#6]'),                           # -CHO
    ('ether',        '[OD2]([#6])[#6]'),                           # R-O-R
    ('cyano',        '[CX2]#[NX1]'),                               # -CN
    ('nitro',        '[NX3](=O)=O'),                               # -NO2
    ('sulfonyl',     '[SX4](=O)(=O)'),                             # -SO2-
    ('sulfide',      '[#16X2]'),                                   # R-S-R
    ('phosphonate',  '[PX4]'),                                     # P(=O)(OR)2 / phosphine oxide
    ('halogen_F',    '[#9]'),                                      # -F
    ('halogen_Cl',   '[#17]'),                                     # -Cl
    ('halogen_Br',   '[#35]'),                                     # -Br
    ('halogen_I',    '[#53]'),                                     # -I
    ('alkene',       '[CX3]=[CX3;!$(C=O);!$(C=N)]'),               # C=C (non-aromatic)
    ('alkyne',       '[CX2]#[CX2]'),                               # C≡C
    ('aromatic_ring', 'a1aaaaa1'),                                 # 6-membered aromatic
    ('cf3',          '[CX4](F)(F)F'),                              # -CF3
]

NUM_FG = len(FG_PATTERNS)
# 总维度: 22 (反应物聚合) + 22 (产物聚合) + 22 (差异) + 2 (heavy atoms ratio, ring count diff) = 68
SINGLE_FG_DIM = NUM_FG + 2  # 每分子 22 FG + 2 extra: HA count, ring count
REACTION_FG_DIM = SINGLE_FG_DIM * 3  # 反应物 + 产物 + 差异


# 预编译 SMARTS
_FG_MOLS = [(name, Chem.MolFromSmarts(smarts)) for name, smarts in FG_PATTERNS]


def count_fg_for_mol(smiles: str) -> np.ndarray:
    """单个分子的 FG 计数, 返回 SINGLE_FG_DIM 维向量。失败返回全 0。"""
    if not smiles:
        return np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return np.zeros(SINGLE_FG_DIM, dtype=np.float32)

    vec = np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    for i, (_, pat) in enumerate(_FG_MOLS):
        if pat is not None:
            vec[i] = float(len(mol.GetSubstructMatches(pat)))
    # 额外: heavy atoms, ring count
    vec[NUM_FG] = float(mol.GetNumHeavyAtoms())
    vec[NUM_FG + 1] = float(Chem.rdMolDescriptors.CalcNumRings(mol))
    return vec


def reaction_fg_features(reactant_smiles: List[str],
                          product_smiles: List[str]) -> np.ndarray:
    """对一条反应聚合 (反应物均值 + 产物均值 + 差异), 返回 REACTION_FG_DIM 维。"""
    if reactant_smiles:
        r_vecs = [count_fg_for_mol(s) for s in reactant_smiles if s]
        r_agg = np.mean(r_vecs, axis=0) if r_vecs else np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    else:
        r_agg = np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    if product_smiles:
        p_vecs = [count_fg_for_mol(s) for s in product_smiles if s]
        p_agg = np.mean(p_vecs, axis=0) if p_vecs else np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    else:
        p_agg = np.zeros(SINGLE_FG_DIM, dtype=np.float32)
    diff = p_agg - r_agg
    return np.concatenate([r_agg, p_agg, diff]).astype(np.float32)


if __name__ == "__main__":
    # 测试
    print(f"NUM_FG={NUM_FG}, SINGLE_FG_DIM={SINGLE_FG_DIM}, REACTION_FG_DIM={REACTION_FG_DIM}")
    tests = [
        ('C=Cc1ccccc1', 'styrene'),
        ('CC(=O)O', 'acetic acid'),
        ('C(F)(F)(F)c1ccccc1', 'trifluorotoluene'),
        ('NCCO', 'ethanolamine'),
    ]
    for smi, name in tests:
        vec = count_fg_for_mol(smi)
        nonzero = [(FG_PATTERNS[i][0], vec[i]) for i in range(NUM_FG) if vec[i] > 0]
        print(f"\n{name} ({smi}): heavy={vec[NUM_FG]}, rings={vec[NUM_FG+1]}")
        for n, v in nonzero:
            print(f"  {n}: {v}")
