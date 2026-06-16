"""基于 SMARTS 规则的 reagent SMILES → 化学类别 分类器。

电化学烯烃二官能团反应里最常见的 reagent 类（25 个 + ABSENT + OTHER）:

按优先级匹配（更具体的类先匹配）, 一个 SMILES 只归一个类。
"""
from typing import List, Tuple
from rdkit import Chem


# (class_name, SMARTS pattern)
# 顺序很重要：先匹配更具体的，再匹配更宽泛的
REAGENT_CLASS_PATTERNS: List[Tuple[str, str]] = [
    # 三氟甲基化/全氟烷基化试剂
    ('cf3_source',         '[CX4](F)(F)F'),                            # CF3 carbon
    ('rfn_source',         '[CX4](F)(F)C(F)(F)'),                      # CnF2n+1 chain
    # 二氟甲基/单氟试剂
    ('hf_source',          'F.N'),                                      # Et3N·3HF 等 — 多片段含 F + N
    ('fluoride_anion',     '[F-]'),                                    # KF, CsF
    # 卤素源
    ('chloride_anion',     '[Cl-]'),
    ('bromide_anion',      '[Br-]'),
    ('iodide_anion',       '[I-]'),
    ('nbs_nis',            '[N+]1(=O)C(=O)CC[N+]1=O'),                # N-Halo-succinimide
    ('hypohalite',         '[O-]Cl'),                                  # NaClO etc
    # 叠氮源
    ('azide_source',       '[N-]=[N+]=[N-]'),                          # azide anion
    ('tms_azide',          '[Si]C[N-]=[N+]=[N-]'),                     # TMS-N3 (rare matching)
    # 氰化/异氰
    ('cyanide_anion',      '[C-]#N'),
    ('isocyanide',         '[N+]#[C-]'),
    # 含硫试剂
    ('thiocyanate',        '[S-]C#N'),                                 # SCN-
    ('sulfinate',          'S(=O)[O-]'),                               # sulfinic acid salt
    ('sulfonyl_chloride',  'S(=O)(=O)Cl'),                            # RSO2Cl
    ('sulfonyl_azide',     'S(=O)(=O)N=[N+]=[N-]'),                   # RSO2N3
    ('sulfonamide',        'S(=O)(=O)N'),                              # RSO2NHR'
    ('sulfonic_acid',      'S(=O)(=O)O'),                              # RSO3H (匹配后留意覆盖)
    ('thiol',              '[#6;!a][SH]'),                             # R-SH
    ('disulfide',          '[#6;!a]SS[#6;!a]'),                        # R-S-S-R'
    # 含氮试剂
    ('tertiary_amine',     '[NX3;!$(NC=O);H0]'),                       # R3N
    ('secondary_amine',    '[NX3;!$(NC=O);H1]'),                       # R2NH
    ('primary_amine',      '[NX3;!$(NC=O);H2]'),                       # RNH2
    ('amide',              '[NX3][CX3](=O)'),                          # carboxamide
    ('pyridine',           'c1ccncc1'),                                # 吡啶环
    ('imidazole',          'c1cnc[nH]1'),                              # 咪唑
    ('nitro',              '[NX3](=O)=O'),                             # -NO2
    # 含氧试剂
    ('carboxylic_acid',    '[CX3](=O)[OX2H]'),                         # RCOOH
    ('carboxylate',        '[CX3](=O)[O-]'),                           # RCOO-
    ('alcohol',            '[CX4][OH]'),                               # R-OH (sp3)
    ('phenol',             'c[OH]'),                                   # ArOH
    ('aldehyde',           '[CX3H1](=O)[#6]'),                         # RCHO
    ('ketone',             '[CX3](=O)([#6])[#6]'),                     # R-CO-R'
    ('peroxide',           '[OX2][OX2]'),                              # R-O-O-R
    ('hypervalent_iodine', '[I+5]'),                                   # Togni etc
    # 碱
    ('alkali_carbonate',   '[Li,Na,K,Cs].O=C([O-])[O-]'),             # M2CO3
    ('alkali_bicarbonate', '[Li,Na,K,Cs].O=C([O-])O'),                # MHCO3
    ('alkali_phosphate',   '[Li,Na,K,Cs].O=P([O-])([O-])[O-]'),       # M3PO4
    ('hydroxide',          '[Li,Na,K,Cs].[OH-]'),                     # MOH
    # 硼/硅
    ('boronic_acid',       '[BX3]([OX2H])'),                          # RB(OH)2
    ('borate',             '[BX4]'),                                  # R3B-
    ('silane',             '[SiX4]([#6])([#6])'),                     # R3Si-X
    # 重氮
    ('diazo',              '[#6]=[N+]=[N-]'),                         # R-N2+
    # 水/质子
    ('water',              '[OX2H2]'),                                # H2O
]

CLASS_NAMES = [c for c, _ in REAGENT_CLASS_PATTERNS]
# 编号: 0 = ABSENT/empty, 1 = OTHER, 2+ = SMARTS classes
N_CLASSES = len(CLASS_NAMES) + 2  # +ABSENT +OTHER

# 预编译
_PATTERNS = [(name, Chem.MolFromSmarts(smarts)) for name, smarts in REAGENT_CLASS_PATTERNS]


def classify_reagent(smiles: str) -> int:
    """SMILES → class index (0=ABSENT, 1=OTHER, 2.. = 具体类)。失败/空返回 0=ABSENT。"""
    if not smiles:
        return 0  # ABSENT
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return 1  # OTHER (无法解析)
    for i, (_, pat) in enumerate(_PATTERNS):
        if pat is None:
            continue
        if mol.HasSubstructMatch(pat):
            return i + 2  # idx 0=ABSENT, 1=OTHER, 2+ = class
    return 1  # OTHER


def get_class_name(idx: int) -> str:
    if idx == 0: return 'ABSENT'
    if idx == 1: return 'OTHER'
    if 2 <= idx < N_CLASSES:
        return CLASS_NAMES[idx - 2]
    return 'INVALID'


if __name__ == "__main__":
    tests = [
        ('', 0),                                  # ABSENT
        ('O=S(=O)([O-])C(F)(F)F.[Na+]', 'cf3_source'),  # CF3SO2Na
        ('[N-]=[N+]=[N-].[Na+]', 'azide_source'),       # NaN3
        ('CCN(CC)CC.F.F.F', 'hf_source'),               # Et3N·3HF
        ('CC(=O)O', 'carboxylic_acid'),                 # AcOH
        ('O=C([O-])[O-].[K+].[K+]', 'alkali_carbonate'),# K2CO3
        ('Cl', 'chloride_anion'),                       # HCl/Cl-
        ('[Cu]', 'OTHER'),                              # 不在分类里
        ('c1ccncc1', 'pyridine'),                       # pyridine
        ('CC(=O)C', 'ketone'),                          # acetone
        ('CCCCNCC', 'secondary_amine'),                 # R2NH
        ('OCCO', 'alcohol'),                            # ethylene glycol
    ]
    print(f"Total classes (含 ABSENT/OTHER): {N_CLASSES}")
    print(f"\n测试:")
    for smi, expected in tests:
        idx = classify_reagent(smi)
        name = get_class_name(idx)
        ok = '✓' if (name == expected or idx == expected) else '✗'
        print(f"  {smi[:40]:<40} -> {name} {ok}")
