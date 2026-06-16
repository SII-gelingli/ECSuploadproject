"""v3 分类器:针对 EC 烯烃双官能化数据,6 个 SMILES head + 3 个 EC head。

设计原则:
- 不允许 OTHER 桶,所有 SMILES 都归到化学有意义的类
- catalyst 单独导出 4 个正交 mechanism tag (mediator/photoredox/HAT/chiral)
- electrolyte 拆 cation + anion 双 head
- anode/cathode 简化为 ~10 个材料家族

公共 API:
    classify_reagent(smi)        -> str
    classify_catalyst(smi)       -> (str, set[str])    # (cls, mech_tags)
    classify_ligand(smi)         -> str
    classify_solvent(smi)        -> str
    classify_electrolyte(smi)    -> (str, str)         # (cation, anion)
    classify_additive(smi)       -> str
    classify_anode_from_id(id)   -> str                # 走老 electrode_to_id 反查
    classify_cathode_from_id(id) -> str
    classify_anode_text(text)    -> str                # 从原始字符串
    classify_cathode_text(text)  -> str
    classify_cell_type_text(text)-> str

每个分类的可能取值都列在 *_CLASSES 常量里;它们是 stable vocab (name 顺序固定)。
"""
from typing import Tuple, Set

try:
    from rdkit import Chem
    from rdkit import RDLogger
    RDLogger.DisableLog('rdApp.*')
    _RDKIT_OK = True
except ImportError:
    _RDKIT_OK = False


ALKALI = {'Li', 'Na', 'K', 'Cs', 'Rb'}
ALK_EARTH = {'Mg', 'Ca', 'Sr', 'Ba'}
TRANSITION = {
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd',
    'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
}
MAIN_GROUP_METAL = {'Al', 'Ga', 'In', 'Tl', 'Sn', 'Pb', 'Bi', 'Sb', 'Te'}
LANTHANIDE = {'Sc', 'Y', 'Yb', 'Eu', 'Sm', 'La', 'Ce', 'Nd', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Lu'}


# ============================================================================
# 类列表 (stable order — 训练 vocab 永远按此顺序)
# ============================================================================
REAGENT_CLASSES = [
    'ABSENT',
    'water', 'o2_oxidant', 'co2_reagent', 'hcl', 'hbr', 'hf', 'ammonia', 'alkane_simple_gas',
    'ferrocene_mediator', 'tempo_mediator', 'nhpi_mediator', 'aryl_iodide_mediator',
    'polyhalo_radical_transfer',
    'fluoride_anion', 'chloride_anion', 'bromide_anion', 'iodide_anion',
    'n_halo_imide', 'hypohalite', 'electrophilic_N_F',
    'hypervalent_iodine', 'metal_oxide_oxidant', 'peroxide',
    'azide_source', 'phthalimide_N_anion', 'nitrite_alkyl', 'diazonium', 'diazo_compound',
    'selenium_reagent', 'tellurium_reagent', 'disulfide',
    'sulfonyl_chloride', 'sulfonyl_azide', 'sulfonamide', 'sulfonic_acid', 'sulfinic_acid',
    'thiol', 'thiocyanate', 'cyanide',
    'imine', 'carbodiimide', 'amide',
    'alkali_carbonate', 'alkali_bicarbonate', 'alkali_phosphate', 'alkali_sulfate',
    'alkali_hydroxide', 'alkali_alkoxide', 'alkali_carboxylate', 'alkali_sulfonate',
    'alkali_sulfinate', 'alkali_formate', 'alkali_nitrate', 'alkali_BF4',
    'borohydride', 'alkali_other_salt',
    'alkaline_earth_halide', 'alkaline_earth_salt',
    'transition_metal_salt_reagent', 'main_group_metal_reagent',
    'hf_amine_complex', 'cf3_source', 'perfluoroalkyl_source',
    'carboxylic_acid', 'acid_anhydride', 'ester', 'aldehyde', 'ketone',
    'diboron', 'boronic_acid', 'boron_lewis_acid', 'borate_ester', 'tetraaryl_borate',
    'hydrosilane', 'silyl_electrophile', 'silane_other',
    'amidine_guanidine_base', 'pyridine', 'imidazole',
    'tertiary_amine', 'secondary_amine', 'primary_amine',
    'ammonium_salt', 'phosphine_neutral', 'phosphine_oxide',
    # 溶剂当反应物用 — 保留 solvent 语义
    'as_solvent_aromatic_hydrocarbon', 'as_solvent_polar_protic_alcohol',
    'as_solvent_alkane', 'as_solvent_polar_aprotic_amide',
    'as_solvent_polar_aprotic_sulfoxide', 'as_solvent_polar_aprotic_nitrile',
    'as_solvent_halogenated_aliphatic', 'as_solvent_cyclic_ether',
    'as_solvent_nitroalkane', 'as_solvent_ionic_liquid',
    # 化学语义兜底 (非 OTHER)
    'inorganic_simple', 'polycyclic_arene', 'aromatic_neutral',
    'aliphatic_neutral', 'alkene_coreagent', 'organic_neutral_misc',
    'unparseable_text',
]

CATALYST_CLASSES = [
    'ABSENT',
    # 跨 head 共享的 mediator 名(与 REAGENT_CLASSES 同名)
    'ferrocene_mediator', 'tempo_mediator', 'nhpi_mediator', 'aryl_iodide_mediator',
    'phthalimide_N_anion',
    'photoredox_organic', 'mediator_organic',
    'quinone_oxidant_cat', 'thianthrene_phenothiazine_cat', 'polycyclic_arene_cat',
    'silyl_lewis_acid_cat', 'brønsted_acid_cat', 'triarylamine_radical_cat',
    'Pd_complex', 'Ni_complex', 'Cu_complex', 'Co_complex', 'Mn_complex', 'Fe_complex',
    'Rh_complex', 'Ir_complex', 'Ru_complex', 'Pt_complex', 'Au_complex', 'Ag_complex',
    'Zn_complex', 'Mg_complex', 'Cd_complex', 'Cr_complex', 'V_complex', 'Ti_complex',
    'Hf_complex', 'Zr_complex', 'Mo_complex', 'W_complex', 'Re_complex', 'Os_complex',
    'lanthanide_complex', 'main_group_lewis_acid',
    'NHC_or_imidazole_organocat', 'amidine_guanidine_organocat',
    'tertiary_amine_organocat', 'pyridine_organocat', 'phosphine_organocat',
    'ammonium_PTC_organocat', 'ionic_organocat',
    'organic_neutral_cat',
    'unparseable_text',
]

CATALYST_TAGS = ['mediator', 'photoredox', 'HAT', 'chiral']

LIGAND_CLASSES = [
    'ABSENT',
    'bipyridine', 'phenanthroline', 'polypyridyl', 'pyridine_monodentate',
    'BOX_oxazoline', 'PyBOX',
    'phosphine_bidentate', 'phosphine_monodentate', 'ferrocenyl_phosphine',
    'NHC_carbene', 'salen_schiff', 'amine_bidentate_aliphatic',
    'chiral_diol_BINOL_TADDOL',
    'N_donor_other', 'P_donor_other', 'O_donor_other', 'carbon_donor_other',
    'unknown_placeholder', 'unparseable_text',
]

SOLVENT_CLASSES = [
    'ABSENT',
    'aqueous', 'hfip', 'tfe',
    'polar_aprotic_nitrile', 'polar_aprotic_amide', 'polar_aprotic_sulfoxide',
    'polar_protic_alcohol', 'polar_protic_acid',
    'halogenated_aliphatic', 'aromatic_fluorinated',
    'cyclic_ether', 'acyclic_ether', 'ester', 'ketone', 'carbonate_ester',
    'aromatic_hydrocarbon', 'alkane', 'nitroalkane',
    'acid_anhydride_solvent', 'amine_solvent', 'pyridine_solvent',
    'solvent_mixture', 'ionic_liquid',
    'inorganic_misc_solvent_field', 'other_polar_aprotic',
    'unparseable_text',
]

ELECTROLYTE_CATIONS = [
    'ABSENT',
    'NBu4', 'NEt4', 'NMe4', 'alkyl_ammonium', 'aryl_ammonium', 'BnNMe3',
    'imidazolium', 'pyridinium', 'aromatic_N_cation',
    'phosphonium',
    'Li', 'Na', 'K', 'Cs', 'Rb', 'Mg', 'Ca', 'NH4',
    'H', 'protonated_amine',
    'molecular_no_ion', 'unparseable_text',
]

ELECTROLYTE_ANIONS = [
    'ABSENT',
    'BF4', 'PF6', 'ClO4', 'NTf2', 'BArF20', 'borate_other',
    'F', 'Cl', 'Br', 'I',
    'OTf', 'OTs', 'carboxylate', 'formate', 'alkoxide',
    'NO3', 'SO4', 'sulfate_acid', 'OH', 'CO3', 'phosphate', 'SCN',
    'fluoride_complex', 'molecular_no_ion', 'unparseable_text',
]

ADDITIVE_CLASSES = list(REAGENT_CLASSES) + ['carbon_powder', 'polycyclic_arene_mediator']

ANODE_CATHODE_CLASSES = [
    'ABSENT',
    'carbon', 'platinum', 'nickel', 'stainless_steel',
    'sacrificial_magnesium', 'sacrificial_zinc', 'sacrificial_iron', 'sacrificial_aluminum',
    'copper', 'gold', 'silver', 'lead', 'titanium',
    'other_electrode',
]

CELL_CLASSES = ['undivided', 'divided', 'flow', 'ABSENT']


# ============================================================================
# RDKit 辅助
# ============================================================================
def _mol(smi: str):
    if not _RDKIT_OK or not smi:
        return None
    try:
        m = Chem.MolFromSmiles(smi, sanitize=True)
        if m is not None:
            return m
        m = Chem.MolFromSmiles(smi, sanitize=False)
        if m is not None:
            try:
                m.UpdatePropertyCache(strict=False)
            except Exception:
                pass
        return m
    except Exception:
        return None


_PAT_CACHE = {}
def _has(mol, smarts: str) -> bool:
    if mol is None:
        return False
    pat = _PAT_CACHE.get(smarts)
    if pat is None:
        pat = Chem.MolFromSmarts(smarts)
        _PAT_CACHE[smarts] = pat
    if pat is None:
        return False
    try:
        return mol.HasSubstructMatch(pat)
    except Exception:
        try:
            mol.UpdatePropertyCache(strict=False)
            return mol.HasSubstructMatch(pat)
        except Exception:
            return False


def _atoms(mol) -> set:
    if mol is None:
        return set()
    return {a.GetSymbol() for a in mol.GetAtoms()}


def _has_any_metal(mol) -> bool:
    return bool(_atoms(mol) & (ALKALI | ALK_EARTH | TRANSITION | MAIN_GROUP_METAL))


def _frags(smi: str):
    return smi.split('.')


# ============================================================================
# REAGENT
# ============================================================================
def classify_reagent(smi: str) -> str:
    if not smi or not str(smi).strip():
        return 'ABSENT'
    s = str(smi).strip()
    mol = _mol(s)

    # 1. EC 高频小分子(精确字串)
    if s in ('O=O', '[O][O]', 'O=[O]'):
        return 'o2_oxidant'
    if s in ('O=C=O', '[O]=C=[O]', 'O=C=[O]'):
        return 'co2_reagent'
    if s in ('O', '[OH2]', '[H]O[H]', '[18OH2]', '[H+].[OH-]', '[2H]O[2H]'):
        return 'water'
    if s in ('Cl', '[H]Cl'):
        return 'hcl'
    if s in ('Br', '[H]Br'):
        return 'hbr'
    if s in ('F', '[H]F'):
        return 'hf'
    if s in ('N', '[NH3]', '[H]N([H])[H]'):
        return 'ammonia'
    if s in ('[CH4]', 'C', 'CC', '[CH3]'):
        return 'alkane_simple_gas'

    # 2. 跨 head mediator
    if 'Fe' in s and ('[cH-]' in s or 'cH-]1cccc1' in s):
        return 'ferrocene_mediator'
    if mol is not None:
        if _has(mol, 'CC1(C)CCCC(C)(C)N1[O]') or _has(mol, '[N]([O])C(C)(C)CCCC([CH3])([CH3])'):
            return 'tempo_mediator'
        if _has(mol, 'O=C1N([OH,O])C(=O)c2ccccc21'):
            return 'nhpi_mediator'
        if _has(mol, 'O=C1[N-]C(=O)c2ccccc21'):
            return 'phthalimide_N_anion'
        if _has(mol, 'c[I;X1;H0]') and not _has(mol, '[I+3]') and not _has(mol, '[I+5]'):
            n_I = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == 'I')
            if mol.GetNumHeavyAtoms() <= 20 and n_I == 1:
                return 'aryl_iodide_mediator'

    # 3. 多卤代烷烃(自由基链转移)
    if mol is not None:
        if _has(mol, '[CX4]([Cl,Br])([Cl,Br])([Cl,Br,F])[CX4,Cl,Br,F]') or \
           _has(mol, '[CX4]([Cl,Br])([Cl,Br])[Cl,Br]'):
            return 'polyhalo_radical_transfer'
        if s in ('BrCCBr', 'ClCCCl', 'BrCBr', 'ClCBr'):
            return 'polyhalo_radical_transfer'

    # 4. 硒/碲/硫双化物
    if mol is not None:
        if _has(mol, '[Se][Se]'):
            return 'selenium_reagent'
        if _has(mol, '[Te][Te]'):
            return 'tellurium_reagent'
        if _has(mol, '[#6;!a][SD2][SD2][#6;!a]') or _has(mol, 'c[S][S]c'):
            return 'disulfide'

    # 5. N-F 亲电氟化
    if mol is not None and _has(mol, '[N;X3,X4][F]'):
        return 'electrophilic_N_F'

    # 6. 亚硝酸/重氮源
    if mol is not None:
        if _has(mol, '[#6][OX2]N=O') or _has(mol, '[#6][O][N]=[O]'):
            return 'nitrite_alkyl'
        if _has(mol, '[N+]#N'):
            return 'diazonium'
        if _has(mol, '[#6]=[N+]=[N-]') or _has(mol, '[#6]=N=N'):
            return 'diazo_compound'

    # 7. 叠氮
    if mol is not None and (_has(mol, '[N-]=[N+]=[N-]') or _has(mol, '[N]=[N+]=[N-]') or _has(mol, 'N=[N+]=N')):
        return 'azide_source'

    # 8. 卤化物离子
    if mol is not None:
        if _has(mol, '[F-]'):
            return 'fluoride_anion'
        if _has(mol, '[Cl-]'):
            return 'chloride_anion'
        if _has(mol, '[Br-]'):
            return 'bromide_anion'
        if _has(mol, '[I-]'):
            return 'iodide_anion'

    # 9. N-卤代琥珀酰亚胺 + 次卤酸
    if mol is not None:
        if _has(mol, 'O=C1CCC(=O)N1[Br,Cl,I,F]') or _has(mol, '[N;R]([Br,Cl,I,F])(C=O)C=O'):
            return 'n_halo_imide'
        if _has(mol, '[O-][Cl,Br,I,F;X1]') or _has(mol, 'O=[Cl,Br,I][O-]'):
            return 'hypohalite'

    # 10. 高价碘 / 高价金属氧化物
    if mol is not None:
        if _has(mol, '[I+3]') or _has(mol, '[I+5]') or _has(mol, '[I;X3]'):
            return 'hypervalent_iodine'
        if _has(mol, '[Mn]=[O]') or _has(mol, '[O]=[Mn]=[O]') or \
           _has(mol, '[Os]=[O]') or _has(mol, '[Ru]=[O]'):
            return 'metal_oxide_oxidant'

    # 11. 过氧化物
    if mol is not None and _has(mol, '[OX2][OX2]'):
        return 'peroxide'

    # 12. 碱金属盐(优先于 carboxylate / hydroxide 等)
    if mol is not None and len(_frags(s)) >= 2:
        syms = _atoms(mol)
        if syms & ALKALI:
            if _has(mol, '[O-]C(=O)[O-]') or _has(mol, '[OX1]=C([O-])[O-]'):
                return 'alkali_carbonate'
            if _has(mol, '[OH]C(=O)[O-]') or _has(mol, '[OH][CX3](=O)[O-]') or \
               _has(mol, '[O-]C(=O)O'):
                return 'alkali_bicarbonate'
            if _has(mol, '[O-]P(=O)([O-])[O-]') or _has(mol, '[OH]P(=O)([O-])[O-]') or \
               _has(mol, '[OH]P(=O)([OH])[O-]'):
                return 'alkali_phosphate'
            if _has(mol, '[O-]S(=O)(=O)[O-]') or _has(mol, '[OH]S(=O)(=O)[O-]'):
                return 'alkali_sulfate'
            if _has(mol, '[OH-]'):
                return 'alkali_hydroxide'
            if _has(mol, '[CX4][O-]'):
                return 'alkali_alkoxide'
            if _has(mol, '[CX3](=O)[O-]'):
                return 'alkali_carboxylate'
            if _has(mol, '[S;X4](=O)(=O)[O-]'):
                return 'alkali_sulfonate'
            if _has(mol, '[S;X3](=O)[O-]'):
                return 'alkali_sulfinate'
            if _has(mol, '[CX3H1](=O)[O-]'):
                return 'alkali_formate'
            if _has(mol, '[S-]C#N'):
                return 'thiocyanate'
            if _has(mol, '[C-]#N'):
                return 'cyanide'
            if _has(mol, '[O-][N+](=O)[O-]'):
                return 'alkali_nitrate'
            if _has(mol, '[BH4-]'):
                return 'borohydride'
            if _has(mol, 'F[B-](F)(F)F'):
                return 'alkali_BF4'
            return 'alkali_other_salt'

    # 13. 碱土 / 主族 / 过渡金属盐
    if mol is not None:
        syms = _atoms(mol)
        if syms & ALK_EARTH:
            if _has(mol, '[Cl-]') or _has(mol, '[Br-]') or _has(mol, '[I-]') or _has(mol, '[F-]'):
                return 'alkaline_earth_halide'
            return 'alkaline_earth_salt'
        if syms & TRANSITION:
            return 'transition_metal_salt_reagent'
        if syms & MAIN_GROUP_METAL:
            return 'main_group_metal_reagent'

    # 14. HF·胺复合物
    if 'F' in s and ('.F' in s or 'F.' in s):
        has_amine = any('N' in f and 'F' not in f for f in _frags(s))
        has_f_only = any(f == 'F' for f in _frags(s))
        if has_amine and has_f_only:
            return 'hf_amine_complex'

    # 15. CF3 / RfN(在 carboxylic_acid 之后 — 这里先检测,但 TFA 不在这归)
    if mol is not None and _has(mol, '[CX4](F)(F)F'):
        if _has(mol, '[CX3](=O)[OH]'):
            # 含 -COOH 的 (TFA),归到下面 carboxylic_acid
            pass
        elif _has(mol, '[CX4](F)(F)F[CX4](F)(F)F') or _has(mol, '[CX4](F)(F)F[CX4](F)(F)'):
            return 'perfluoroalkyl_source'
        else:
            return 'cf3_source'

    # 16. 含硫官能团
    if mol is not None:
        if _has(mol, '[S;X4](=O)(=O)Cl'):
            return 'sulfonyl_chloride'
        if _has(mol, '[S;X4](=O)(=O)N=[N+]=[N-]'):
            return 'sulfonyl_azide'
        if _has(mol, '[S;X4](=O)(=O)[NH,NH2]'):
            return 'sulfonamide'
        if _has(mol, '[S;X4](=O)(=O)[OH]'):
            return 'sulfonic_acid'
        if _has(mol, '[S;X3](=O)[OH]'):
            return 'sulfinic_acid'
        if _has(mol, '[#6;!a][SH]') or _has(mol, 'c[SH]'):
            return 'thiol'

    # 17. 含氧官能团
    if mol is not None:
        if _has(mol, '[CX3](=O)[OH]'):
            return 'carboxylic_acid'
        if _has(mol, '[CX3](=O)O[CX3](=O)'):
            return 'acid_anhydride'
        if _has(mol, '[CX3](=O)O[CX4,c]'):
            return 'ester'
        if _has(mol, '[CX3H1](=O)[#6]'):
            return 'aldehyde'
        if _has(mol, '[CX3](=O)([#6])[#6]'):
            return 'ketone'

    # 18. 硼 / 硅
    if mol is not None:
        if _has(mol, '[B][B]'):
            return 'diboron'
        if _has(mol, '[B]([OH])([OH])'):
            return 'boronic_acid'
        if _has(mol, 'B(F)(F)F') or _has(mol, '[B](F)(F)F'):
            return 'boron_lewis_acid'
        if _has(mol, '[B][O]') or _has(mol, '[B;X3]([O])'):
            return 'borate_ester'
        if _has(mol, '[B]([c,a])([c,a])([c,a])'):
            return 'tetraaryl_borate'
        if _has(mol, '[SiH]'):
            return 'hydrosilane'
        if _has(mol, '[Si][Cl,Br,I,O,N]'):
            return 'silyl_electrophile'
        if _has(mol, '[Si]'):
            return 'silane_other'

    # 19. 含氮碱(胍/脒) — 必须先于 imine
    if mol is not None:
        if _has(mol, '[#7;R]=[#6;R][#7;R]') or _has(mol, '[#7]C(=N)[#7]'):
            return 'amidine_guanidine_base'
        if _has(mol, '[#7]=[#6]=[#7]'):
            return 'carbodiimide'

    # 20. 酰胺 / 亚胺
    if mol is not None:
        if _has(mol, '[NX3][CX3](=O)[#6]'):
            return 'amide'
        if _has(mol, '[#6]=[#7]'):
            return 'imine'

    # 21. 其他含氮试剂
    if mol is not None:
        if _has(mol, 'c1ccncc1'):
            return 'pyridine'
        if _has(mol, 'c1cnc[nH]1') or _has(mol, 'c1[nH]cnc1'):
            return 'imidazole'
        if _has(mol, '[NX3;H0;!$(N=*);!$(NC=O);!$([N+])]'):
            return 'tertiary_amine'
        if _has(mol, '[NX3;H1;!$(N=*);!$(NC=O)]'):
            return 'secondary_amine'
        if _has(mol, '[NX3;H2;!$(N=*);!$(NC=O)]'):
            return 'primary_amine'

    # 22. PPh3 / 膦
    if mol is not None and _has(mol, '[P;X3]'):
        if _has(mol, '[P;X4](=O)') or _has(mol, '[P;X4]=O'):
            return 'phosphine_oxide'
        return 'phosphine_neutral'

    # 23. 四芳基硼酸盐
    if mol is not None and _has(mol, '[B-]'):
        return 'tetraaryl_borate'

    # 24. 季铵盐
    if mol is not None and _has(mol, '[N+;X4]'):
        return 'ammonium_salt'

    # 25. "溶剂当 reagent 用" — 走 solvent 分类
    if mol is not None:
        sol_cls = classify_solvent(s)
        if sol_cls not in ('ABSENT', 'other_polar_aprotic', 'inorganic_misc_solvent_field',
                           'solvent_mixture', 'unparseable_text', 'amine_solvent'):
            return f'as_solvent_{sol_cls}'

    # 26. 化学有意义的兜底
    if mol is None:
        return 'unparseable_text'
    syms = _atoms(mol)
    if not (syms & {'C'}):
        return 'inorganic_simple'
    if _has(mol, 'c1ccc2ccccc2c1') or _has(mol, 'c1ccc2c(c1)ccc1ccccc12'):
        return 'polycyclic_arene'
    if _has(mol, '[CX3]=[CX3]'):
        return 'alkene_coreagent'
    if _has(mol, 'c1ccccc1') or _has(mol, '[#6;a]'):
        return 'aromatic_neutral'
    if _has(mol, '[CX4]'):
        return 'aliphatic_neutral'
    return 'organic_neutral_misc'


# ============================================================================
# CATALYST
# ============================================================================
def classify_catalyst(smi: str) -> Tuple[str, Set[str]]:
    if not smi or not str(smi).strip():
        return 'ABSENT', set()
    s = str(smi).strip()
    mol = _mol(s)
    tags: Set[str] = set()

    if mol is not None:
        if 'Fe' in s and ('[cH-]' in s or 'cH-]1cccc1' in s):
            tags.add('mediator')
        if _has(mol, 'CC1(C)CCCC(C)(C)N1[O]') or _has(mol, '[N]([O])C(C)(C)CCCC([CH3])([CH3])'):
            tags.add('mediator'); tags.add('HAT')
        if _has(mol, 'O=C1N([OH,O])C(=O)c2ccccc21'):
            tags.add('mediator'); tags.add('HAT')
        if _has(mol, 'c[I;X1;H0]') and mol.GetNumHeavyAtoms() <= 20:
            tags.add('mediator')
        if 'N#C' in s and 'c1' in s and s.count('N2c3ccccc3c3ccccc32') >= 2:
            tags.add('photoredox')
        if _has(mol, '[n+;R1;X3](-c)(c)c'):
            tags.add('photoredox')
        if _has(mol, 'Brc1cc2c(cc1Br)C(=O)') and 'O2' in s:
            tags.add('photoredox')
        if 'Ir' in s and _has(mol, '[Ir]'):
            tags.add('photoredox')
        if 'Ru' in s and _has(mol, 'c1ccc(-c2ccccn2)nc1'):
            tags.add('photoredox')
        if 'W' in s and _has(mol, '[W]'):
            tags.add('photoredox'); tags.add('HAT')
        if '@' in s:
            tags.add('chiral')

    if mol is None:
        return 'unparseable_text', tags
    syms = _atoms(mol)

    # 跨 head 同名:ferrocene/TEMPO/NHPI/Tol-I 一律走专名
    if 'Fe' in s and ('[cH-]' in s or 'cH-]1cccc1' in s):
        return 'ferrocene_mediator', tags
    if _has(mol, 'CC1(C)CCCC(C)(C)N1[O]') or _has(mol, '[N]([O])C(C)(C)CCCC([CH3])([CH3])'):
        return 'tempo_mediator', tags
    if _has(mol, 'O=C1N([OH,O])C(=O)c2ccccc21'):
        return 'nhpi_mediator', tags
    if _has(mol, 'O=C1[N-]C(=O)c2ccccc21'):
        return 'phthalimide_N_anion', tags
    if _has(mol, 'c[I;X1;H0]') and mol.GetNumHeavyAtoms() <= 20:
        n_I = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == 'I')
        if n_I == 1 and not (syms & TRANSITION):
            return 'aryl_iodide_mediator', tags

    if 'photoredox' in tags and not (syms & TRANSITION):
        return 'photoredox_organic', tags
    if 'mediator' in tags and not (syms & TRANSITION):
        return 'mediator_organic', tags

    if _has(mol, 'O=C1C=CC(=O)C=C1') or _has(mol, 'O=C1[#6]=[#6]C(=O)[#6]=[#6]1') or \
       _has(mol, 'O=C1c2ccccc2C(=O)c2ccccc21'):
        tags.add('mediator')
        return 'quinone_oxidant_cat', tags
    if _has(mol, 'c1ccc2c(c1)Sc1ccccc1S2') or _has(mol, 'c1ccc2c(c1)Sc1ccccc1[N]2') or \
       _has(mol, 'c1ccc2c(c1)Sc1cc(O[CH3])ccc1N2'):
        tags.add('photoredox')
        return 'thianthrene_phenothiazine_cat', tags
    if _has(mol, 'c1ccc2c(c1)ccc1ccccc12') or _has(mol, 'c1ccc2ccccc2c1'):
        tags.add('mediator')
        return 'polycyclic_arene_cat', tags
    if _has(mol, '[Si]'):
        return 'silyl_lewis_acid_cat', tags
    if _has(mol, '[OH]C(F)(F)F') or _has(mol, 'OC(C(F)(F)F)C(F)(F)F') or \
       _has(mol, 'O=S(=O)(O)C(F)(F)F') or _has(mol, 'P(=O)(O[#6])(O[#6])O[#6]'):
        return 'brønsted_acid_cat', tags
    if _has(mol, '[N]([c,a])([c,a])[c,a]') and _has(mol, '[Br,I]') and \
       sum(1 for a in mol.GetAtoms() if a.GetSymbol() in ('Br', 'I')) >= 3:
        return 'triarylamine_radical_cat', tags

    for el in ['Pd', 'Ni', 'Cu', 'Co', 'Mn', 'Fe', 'Rh', 'Ir', 'Ru', 'Pt',
               'Au', 'Ag', 'Zn', 'Mg', 'Cd', 'Cr', 'V', 'Ti', 'Hf', 'Zr',
               'Mo', 'W', 'Re', 'Os']:
        if el in syms:
            return f'{el}_complex', tags
    if syms & LANTHANIDE:
        return 'lanthanide_complex', tags
    for el in ['B', 'Al', 'Ga', 'In', 'Sn', 'Pb', 'Bi', 'Sb']:
        if el in syms:
            return 'main_group_lewis_acid', tags

    if _has(mol, 'c1cnc[nH]1') or _has(mol, 'c1[nH]cnc1'):
        return 'NHC_or_imidazole_organocat', tags
    if _has(mol, '[#7;R]=[#6;R][#7;R]'):
        return 'amidine_guanidine_organocat', tags
    if _has(mol, '[N;R](C)(C)C[N;R]') or _has(mol, 'N12CCN(CC1)CC2'):
        return 'tertiary_amine_organocat', tags
    if _has(mol, 'c1ccncc1'):
        return 'pyridine_organocat', tags
    if _has(mol, '[P;X3]'):
        return 'phosphine_organocat', tags
    if _has(mol, '[N;X4+]'):
        return 'ammonium_PTC_organocat', tags
    if _has(mol, '[+,-]'):
        return 'ionic_organocat', tags
    return 'organic_neutral_cat', tags


# ============================================================================
# LIGAND
# ============================================================================
def classify_ligand(smi: str) -> str:
    if not smi or not str(smi).strip():
        return 'ABSENT'
    s = str(smi).strip()
    if s == '*':
        return 'unknown_placeholder'
    mol = _mol(s)
    if mol is None:
        return 'unparseable_text'

    if _has(mol, 'C1=[N+](c2ccccc2)C=CN1'):
        return 'NHC_carbene'
    pn = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == 'P')
    aromN = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == 'N' and a.GetIsAromatic())
    if 'Fe' in s and pn >= 1:
        return 'ferrocenyl_phosphine'
    if pn >= 2:
        return 'phosphine_bidentate'
    if pn == 1:
        return 'phosphine_monodentate'
    if _has(mol, 'c1cc([CX3]2=NCCO2)nc([CX3]3=NCCO3)c1'):
        return 'PyBOX'
    if _has(mol, 'C1=NC(*)CO1') or _has(mol, '[C]1=[N][C][C][O]1'):
        return 'BOX_oxazoline'
    if _has(mol, 'c1ccc(-c2ccccn2)nc1'):
        return 'bipyridine'
    if _has(mol, 'c1cnc2c(c1)ccc1cccnc12') or _has(mol, 'c1ccc2ccc3ccc(*)nc3c2n1'):
        return 'phenanthroline'
    if aromN >= 2 and _has(mol, 'n'):
        return 'polypyridyl'
    if _has(mol, 'C=Nc1ccccc1[OH]'):
        return 'salen_schiff'
    if _has(mol, '[NX3;H0]') and _has(mol, 'CN(C)CCN(C)C'):
        return 'amine_bidentate_aliphatic'
    if _has(mol, 'c1ccncc1'):
        return 'pyridine_monodentate'
    if '@' in s and _has(mol, 'c[OH]'):
        return 'chiral_diol_BINOL_TADDOL'
    syms = _atoms(mol)
    if 'P' in syms:
        return 'P_donor_other'
    if 'N' in syms:
        return 'N_donor_other'
    if 'O' in syms:
        return 'O_donor_other'
    return 'carbon_donor_other'


# ============================================================================
# SOLVENT
# ============================================================================
def classify_solvent(smi: str) -> str:
    if not smi or not str(smi).strip():
        return 'ABSENT'
    s = str(smi).strip()
    if '.' in s and not s.startswith('['):
        frag_list = _frags(s)
        if len(frag_list) >= 2:
            ok = True
            for f in frag_list:
                fm = _mol(f)
                if fm is None or _has_any_metal(fm):
                    ok = False
                    break
            if ok:
                return 'solvent_mixture'

    mol = _mol(s)
    if mol is None:
        return 'unparseable_text'

    if s in ('O', '[OH2]', '[H+].[OH-]', '[18OH2]', '[H]O[H]', '[2H]O[2H]'):
        return 'aqueous'

    if _has(mol, '[CX3](=O)O[CX3](=O)'):
        return 'acid_anhydride_solvent'

    if 'OC(C(F)(F)F)C(F)(F)F' in s or _has(mol, '[OH]C(C(F)(F)F)C(F)(F)F'):
        return 'hfip'
    if _has(mol, 'OCC(F)(F)F'):
        return 'tfe'
    if _has(mol, 'FC(F)(F)c1ccccc1') or _has(mol, 'C(F)(F)(F)c1ccccc1'):
        return 'aromatic_fluorinated'

    if _has(mol, '[Cl,Br,I][CX4]') or _has(mol, '[CX4][Cl,Br,I]'):
        return 'halogenated_aliphatic'

    if _has(mol, '[CX3](=O)[OH]'):
        return 'polar_protic_acid'

    if _has(mol, '[CX4][OH]') and not _has(mol, 'C(F)(F)F'):
        return 'polar_protic_alcohol'

    if _has(mol, '[CX2]#[NX1]'):
        return 'polar_aprotic_nitrile'

    if _has(mol, '[NX3][CX3](=O)'):
        return 'polar_aprotic_amide'

    if _has(mol, '[S;X3](=O)') or _has(mol, '[S;X4](=O)(=O)'):
        return 'polar_aprotic_sulfoxide'

    if _has(mol, '[CX4][N+](=O)[O-]') or _has(mol, '[CX4][N](=O)=O'):
        return 'nitroalkane'

    try:
        Chem.GetSSSR(mol)
        n_rings = mol.GetRingInfo().NumRings()
    except Exception:
        n_rings = 0
    if n_rings >= 1 and _has(mol, '[OX2;R]') and _has(mol, '[CX4;R]'):
        return 'cyclic_ether'

    if _has(mol, '[CX3](=O)O[CX4,c]'):
        return 'ester'
    if _has(mol, 'O=C(O[CX4])O[CX4]'):
        return 'carbonate_ester'
    if _has(mol, '[CX3](=O)([#6])[#6]'):
        return 'ketone'
    if _has(mol, '[CX4]O[CX4]'):
        return 'acyclic_ether'
    if _has(mol, 'c1ccccc1') and not _has(mol, '[OH]') and not _has(mol, 'C(=O)'):
        return 'aromatic_hydrocarbon'
    if _has(mol, '[CX4]') and not _has(mol, '[!#6;!#1]'):
        return 'alkane'
    if _has(mol, '[n+]') or _has(mol, '[P+]'):
        return 'ionic_liquid'
    if _has(mol, 'c1ccncc1'):
        return 'pyridine_solvent'
    if _has(mol, '[NX3;!$(N=*);!$(NC=O)]'):
        return 'amine_solvent'
    if _has_any_metal(mol):
        return 'inorganic_misc_solvent_field'
    return 'other_polar_aprotic'


# ============================================================================
# ELECTROLYTE — cation × anion
# ============================================================================
def classify_electrolyte(smi: str) -> Tuple[str, str]:
    if not smi or not str(smi).strip():
        return 'ABSENT', 'ABSENT'
    s = str(smi).strip()
    mol = _mol(s)
    if mol is None:
        return 'unparseable_text', 'unparseable_text'

    # cation
    cation = 'molecular_no_ion'
    if _has(mol, '[Li+]') or '[Li]' in s:
        cation = 'Li'
    elif _has(mol, '[Na+]') or '[Na]' in s:
        cation = 'Na'
    elif _has(mol, '[K+]') or '[K]' in s:
        cation = 'K'
    elif _has(mol, '[Cs+]'):
        cation = 'Cs'
    elif _has(mol, '[Rb+]'):
        cation = 'Rb'
    elif _has(mol, '[Mg+2]'):
        cation = 'Mg'
    elif _has(mol, '[Ca+2]'):
        cation = 'Ca'
    elif _has(mol, '[NH4+]'):
        cation = 'NH4'
    elif _has(mol, '[N+]([CH2][CH2][CH2][CH3])([CH2][CH2][CH2][CH3])([CH2][CH2][CH2][CH3])[CH2][CH2][CH2][CH3]'):
        cation = 'NBu4'
    elif _has(mol, '[N+]([CH2][CH3])([CH2][CH3])([CH2][CH3])[CH2][CH3]'):
        cation = 'NEt4'
    elif _has(mol, '[N+]([CH3])([CH3])([CH3])[CH3]'):
        cation = 'NMe4'
    elif _has(mol, '[N+;X4]'):
        if _has(mol, '[CH2]c1ccccc1') and _has(mol, '[N+](C)(C)C'):
            cation = 'BnNMe3'
        elif _has(mol, 'c[N+]'):
            cation = 'aryl_ammonium'
        else:
            cation = 'alkyl_ammonium'
    elif _has(mol, '[n+]'):
        if _has(mol, '[n+]1ccccc1'):
            cation = 'pyridinium'
        elif _has(mol, '[n+]1ccn(*)c1') or _has(mol, '[n+]1cnccc1') or _has(mol, '[n+]1cn(*)cc1'):
            cation = 'imidazolium'
        else:
            cation = 'aromatic_N_cation'
    elif _has(mol, '[P+;X4]'):
        cation = 'phosphonium'
    elif _has(mol, '[H+]'):
        cation = 'H'

    # anion
    anion = 'molecular_no_ion'
    if _has(mol, 'F[B-](F)(F)F'):
        anion = 'BF4'
    elif _has(mol, 'F[P-](F)(F)(F)(F)F') or _has(mol, '[P-](F)(F)(F)(F)(F)F'):
        anion = 'PF6'
    elif _has(mol, '[O-][Cl+3]([O-])([O-])[O-]') or _has(mol, '[O-]Cl(=O)(=O)=O'):
        anion = 'ClO4'
    elif _has(mol, 'O=S(=O)(C(F)(F)F)[N-]S(=O)(=O)C(F)(F)F'):
        anion = 'NTf2'
    elif _has(mol, '[F-]'):
        anion = 'F'
    elif _has(mol, '[Cl-]'):
        anion = 'Cl'
    elif _has(mol, '[Br-]'):
        anion = 'Br'
    elif _has(mol, '[I-]'):
        anion = 'I'
    elif _has(mol, 'O=S(=O)([O-])C(F)(F)F') or _has(mol, '[O-]S(=O)(=O)C(F)(F)F'):
        anion = 'OTf'
    elif _has(mol, 'Cc1ccc(S(=O)(=O)[O-])cc1'):
        anion = 'OTs'
    elif _has(mol, '[CX3](=O)[O-]'):
        anion = 'carboxylate'
    elif _has(mol, '[O-][N+](=O)[O-]') or _has(mol, '[O-][N+]([O-])=O'):
        anion = 'NO3'
    elif _has(mol, '[O-]S(=O)(=O)[O-]') or _has(mol, 'OS(=O)(=O)[O-]'):
        anion = 'SO4'
    elif _has(mol, 'O=S(=O)(O)O') or _has(mol, 'O=S(=O)([OH])[OH]'):
        anion = 'sulfate_acid'
    elif _has(mol, '[OH-]'):
        anion = 'OH'
    elif _has(mol, '[CX4][O-]'):
        anion = 'alkoxide'
    elif _has(mol, '[O-]C(=O)[O-]'):
        anion = 'CO3'
    elif _has(mol, '[O-]P(=O)([O-])[O-]') or _has(mol, '[O-]P(=O)([O-])O') or _has(mol, '[O-]P(=O)(O)O'):
        anion = 'phosphate'
    elif _has(mol, '[S-]C#N'):
        anion = 'SCN'
    elif _has(mol, '[O-][CX3]=O') or _has(mol, '[O-]C=O'):
        anion = 'formate'
    elif _has(mol, '[B-](c1c(F)c(F)c(F)c(F)c1F)'):
        anion = 'BArF20'
    elif _has(mol, '[B-]'):
        anion = 'borate_other'

    if cation == 'molecular_no_ion' and anion == 'molecular_no_ion':
        if _has(mol, '[CX3](=O)[OH]'):
            return 'H', 'carboxylate'
        if _has(mol, 'O=S(=O)(O)C(F)(F)F'):
            return 'H', 'OTf'
        if _has(mol, 'O=S(=O)([OH])[OH]'):
            return 'H', 'sulfate_acid'
        if 'F' in s and 'N' in s:
            return 'protonated_amine', 'fluoride_complex'

    return cation, anion


# ============================================================================
# ADDITIVE (复用 reagent + 特殊情况)
# ============================================================================
def classify_additive(smi: str) -> str:
    if not smi or not str(smi).strip():
        return 'ABSENT'
    s = str(smi).strip()
    if s in ('[C]', '[c]'):
        return 'carbon_powder'
    mol = _mol(s)
    if mol is not None:
        if _has(mol, 'c1ccc2ccccc2c1') or _has(mol, 'c1ccc2c(c1)ccc1ccccc12'):
            return 'polycyclic_arene_mediator'
    return classify_reagent(s)


# ============================================================================
# ELECTRODE: 23 → 14 类
# 接受老的 electrode_to_id 整数,或原始字符串
# ============================================================================
_ELECTRODE_ID_TO_V3 = {
    0: 'carbon',                  # graphite
    1: 'platinum',                # platinum
    2: 'carbon',                  # carbon
    3: 'carbon',                  # carbon_felt
    4: 'carbon',                  # graphite_felt
    5: 'carbon',                  # glassy_carbon
    6: 'nickel',                  # nickel
    7: 'stainless_steel',         # stainless_steel
    8: 'sacrificial_magnesium',   # magnesium
    9: 'sacrificial_zinc',        # zinc
    10: 'sacrificial_iron',       # iron
    11: 'sacrificial_aluminum',   # aluminum
    12: 'copper',                 # copper
    13: 'gold',                   # gold
    14: 'silver',                 # silver
    15: 'lead',                   # lead
    16: 'titanium',               # titanium
    17: 'carbon',                 # bdd
    18: 'other_electrode',        # palladium
    19: 'other_electrode',        # niobium
    20: 'other_electrode',        # mercury
    21: 'carbon',                 # pencil_graphite
    22: 'ABSENT',                 # unknown
}

def classify_anode_from_id(idx: int) -> str:
    return _ELECTRODE_ID_TO_V3.get(int(idx), 'ABSENT')

def classify_cathode_from_id(idx: int) -> str:
    return _ELECTRODE_ID_TO_V3.get(int(idx), 'ABSENT')


def classify_electrode_text(text: str) -> str:
    if not text or not str(text).strip():
        return 'ABSENT'
    t = str(text).strip().lower()
    carbon_kw = ['graphite', 'carbon', 'rvc', 'vitreous', 'glassy', 'cetech', 'bdd',
                 'boron-doped', 'boron doped', 'diamond', 'gf', 'gc', 'ccloth', 'pencil']
    if any(k in t for k in carbon_kw) or t in {'c', 'gf', 'gc', 'cc', 'rvc', 'bdd'}:
        return 'carbon'
    if any(k in t for k in ['platinum', 'pt']):
        return 'platinum'
    if 'nickel' in t or 'nifoam' in t or 'nimesh' in t or t in {'ni', 'ni(+)', 'ni(-)'}:
        return 'nickel'
    if 'stainless' in t or 'steel' in t or t == 'ss':
        return 'stainless_steel'
    if 'magnesium' in t or t == 'mg' or 'mg ' in t or 'mg(' in t or '(mg' in t or 'mg+' in t or 'mg-' in t:
        return 'sacrificial_magnesium'
    if 'zinc' in t or t == 'zn' or 'zn ' in t or 'zn(' in t or '(zn' in t:
        return 'sacrificial_zinc'
    if 'iron' in t or t == 'fe' or 'fe ' in t or 'fe(' in t or '(fe' in t:
        return 'sacrificial_iron'
    if 'aluminum' in t or 'aluminium' in t or t == 'al' or 'al ' in t or 'al(' in t:
        return 'sacrificial_aluminum'
    if 'copper' in t or t == 'cu':
        return 'copper'
    if 'silver' in t or t == 'ag':
        return 'silver'
    if 'gold' in t or t == 'au':
        return 'gold'
    if 'lead' in t or t == 'pb':
        return 'lead'
    if 'titanium' in t or t == 'ti':
        return 'titanium'
    if 'tin' in t or t == 'sn':
        return 'other_electrode'
    return 'other_electrode'


classify_anode_text = classify_electrode_text
classify_cathode_text = classify_electrode_text


_CELL_KEYWORDS_UNDIVIDED = ('undivid', 'indivis', 'in cell', 'integrated', 'beaker',
                            'electrasyn', 'three-necked', 'c(+)-c(-)', 'c (+)/c (-)')
_CELL_KEYWORDS_DIVIDED = ('divided', 'membrane', 'nafion', 'h-type', 'compartment',
                          'separated', 'separation', 'cce', 'h type')

def classify_cell_type_text(text: str) -> str:
    if not text or not str(text).strip():
        return 'ABSENT'
    t = str(text).strip().lower()
    if 'flow' in t or 'single-pass' in t or 'continuous' in t:
        return 'flow'
    if any(k in t for k in _CELL_KEYWORDS_UNDIVIDED):
        return 'undivided'
    if any(k in t for k in _CELL_KEYWORDS_DIVIDED):
        return 'divided'
    return 'undivided'


# ============================================================================
# Name → integer id 映射(stable vocab)
# ============================================================================
REAGENT_NAME2ID = {n: i for i, n in enumerate(REAGENT_CLASSES)}
CATALYST_NAME2ID = {n: i for i, n in enumerate(CATALYST_CLASSES)}
LIGAND_NAME2ID = {n: i for i, n in enumerate(LIGAND_CLASSES)}
SOLVENT_NAME2ID = {n: i for i, n in enumerate(SOLVENT_CLASSES)}
CATION_NAME2ID = {n: i for i, n in enumerate(ELECTROLYTE_CATIONS)}
ANION_NAME2ID = {n: i for i, n in enumerate(ELECTROLYTE_ANIONS)}
ADDITIVE_NAME2ID = {n: i for i, n in enumerate(ADDITIVE_CLASSES)}
ELECTRODE_NAME2ID = {n: i for i, n in enumerate(ANODE_CATHODE_CLASSES)}
CELL_NAME2ID = {n: i for i, n in enumerate(CELL_CLASSES)}
TAG_NAME2BIT = {t: 1 << i for i, t in enumerate(CATALYST_TAGS)}


def reagent_id(smi: str) -> int:
    return REAGENT_NAME2ID[classify_reagent(smi)]

def catalyst_id_and_tags(smi: str) -> Tuple[int, int]:
    cls, tags = classify_catalyst(smi)
    cls_id = CATALYST_NAME2ID[cls]
    tag_bits = 0
    for t in tags:
        tag_bits |= TAG_NAME2BIT.get(t, 0)
    return cls_id, tag_bits

def ligand_id(smi: str) -> int:
    return LIGAND_NAME2ID[classify_ligand(smi)]

def solvent_id(smi: str) -> int:
    return SOLVENT_NAME2ID[classify_solvent(smi)]

def electrolyte_ids(smi: str) -> Tuple[int, int]:
    c, a = classify_electrolyte(smi)
    return CATION_NAME2ID.get(c, CATION_NAME2ID['molecular_no_ion']), \
           ANION_NAME2ID.get(a, ANION_NAME2ID['molecular_no_ion'])

def additive_id(smi: str) -> int:
    return ADDITIVE_NAME2ID[classify_additive(smi)]

def electrode_id_from_old(idx: int) -> int:
    return ELECTRODE_NAME2ID[classify_anode_from_id(idx)]

def cell_id(text: str) -> int:
    return CELL_NAME2ID[classify_cell_type_text(text)]


N_REAGENT_CLASSES = len(REAGENT_CLASSES)
N_CATALYST_CLASSES = len(CATALYST_CLASSES)
N_LIGAND_CLASSES = len(LIGAND_CLASSES)
N_SOLVENT_CLASSES = len(SOLVENT_CLASSES)
N_CATION_CLASSES = len(ELECTROLYTE_CATIONS)
N_ANION_CLASSES = len(ELECTROLYTE_ANIONS)
N_ADDITIVE_CLASSES = len(ADDITIVE_CLASSES)
N_ELECTRODE_CLASSES = len(ANODE_CATHODE_CLASSES)
N_CELL_CLASSES = len(CELL_CLASSES)
N_CATALYST_TAGS = len(CATALYST_TAGS)
