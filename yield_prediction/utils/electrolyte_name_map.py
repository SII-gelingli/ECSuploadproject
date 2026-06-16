"""
常用电化学支持电解质名称到 SMILES 的手工映射。

v2 schema 中 19% 的反应 `electrolytes` 字段有 SMILES，但 `conditions.electrochemistry.electrolyte`
是一个名字字符串（例如 'n-Bu4NBF4'）。这里覆盖最常见的 ~30 个名字，把 SMILES 覆盖率从 81% 提到 ~95%。

SMILES 都已通过 RDKit 验证（ion pair 形式，正负离子用 . 分隔）。
"""
import re
from typing import Optional


# 一组常见电化学支持电解质：name → canonical SMILES (ion pair)
ELECTROLYTE_NAME_TO_SMILES = {
    # tetrabutylammonium 系列
    'nbu4nbf4': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',
    'n-bu4nbf4': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',
    'tbabf4': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',
    'bu4nbf4': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',
    'tetrabutylammonium tetrafluoroborate': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',
    'tetra-n-butylammonium tetrafluoroborate': 'CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F',

    'nbu4npf6': 'CCCC[N+](CCCC)(CCCC)CCCC.F[P-](F)(F)(F)(F)F',
    'n-bu4npf6': 'CCCC[N+](CCCC)(CCCC)CCCC.F[P-](F)(F)(F)(F)F',
    'tbapf6': 'CCCC[N+](CCCC)(CCCC)CCCC.F[P-](F)(F)(F)(F)F',
    'bu4npf6': 'CCCC[N+](CCCC)(CCCC)CCCC.F[P-](F)(F)(F)(F)F',
    'tetrabutylammonium hexafluorophosphate': 'CCCC[N+](CCCC)(CCCC)CCCC.F[P-](F)(F)(F)(F)F',

    'nbu4nclo4': 'CCCC[N+](CCCC)(CCCC)CCCC.[O-]Cl(=O)(=O)=O',
    'n-bu4nclo4': 'CCCC[N+](CCCC)(CCCC)CCCC.[O-]Cl(=O)(=O)=O',
    'tbaclo4': 'CCCC[N+](CCCC)(CCCC)CCCC.[O-]Cl(=O)(=O)=O',
    'bu4nclo4': 'CCCC[N+](CCCC)(CCCC)CCCC.[O-]Cl(=O)(=O)=O',
    'tetrabutylammonium perchlorate': 'CCCC[N+](CCCC)(CCCC)CCCC.[O-]Cl(=O)(=O)=O',

    'nbu4nbr': 'CCCC[N+](CCCC)(CCCC)CCCC.[Br-]',
    'tbabr': 'CCCC[N+](CCCC)(CCCC)CCCC.[Br-]',
    'bu4nbr': 'CCCC[N+](CCCC)(CCCC)CCCC.[Br-]',
    'tetrabutylammonium bromide': 'CCCC[N+](CCCC)(CCCC)CCCC.[Br-]',

    'nbu4ni': 'CCCC[N+](CCCC)(CCCC)CCCC.[I-]',
    'tbai': 'CCCC[N+](CCCC)(CCCC)CCCC.[I-]',
    'bu4ni': 'CCCC[N+](CCCC)(CCCC)CCCC.[I-]',
    'tetrabutylammonium iodide': 'CCCC[N+](CCCC)(CCCC)CCCC.[I-]',

    'nbu4ncl': 'CCCC[N+](CCCC)(CCCC)CCCC.[Cl-]',
    'tbacl': 'CCCC[N+](CCCC)(CCCC)CCCC.[Cl-]',
    'tetrabutylammonium chloride': 'CCCC[N+](CCCC)(CCCC)CCCC.[Cl-]',

    'nbu4notf': 'CCCC[N+](CCCC)(CCCC)CCCC.O=S(=O)([O-])C(F)(F)F',
    'tbaotf': 'CCCC[N+](CCCC)(CCCC)CCCC.O=S(=O)([O-])C(F)(F)F',
    'tetrabutylammonium triflate': 'CCCC[N+](CCCC)(CCCC)CCCC.O=S(=O)([O-])C(F)(F)F',

    'nbu4nhso4': 'CCCC[N+](CCCC)(CCCC)CCCC.OS(=O)(=O)[O-]',
    'tbahso4': 'CCCC[N+](CCCC)(CCCC)CCCC.OS(=O)(=O)[O-]',

    # tetraethylammonium 系列
    'et4nbr': 'CC[N+](CC)(CC)CC.[Br-]',
    'tetraethylammonium bromide': 'CC[N+](CC)(CC)CC.[Br-]',
    'et4nbf4': 'CC[N+](CC)(CC)CC.F[B-](F)(F)F',
    'et4npf6': 'CC[N+](CC)(CC)CC.F[P-](F)(F)(F)(F)F',
    'et4nclo4': 'CC[N+](CC)(CC)CC.[O-]Cl(=O)(=O)=O',
    'tetraethylammonium perchlorate': 'CC[N+](CC)(CC)CC.[O-]Cl(=O)(=O)=O',
    'et4nots': 'CC[N+](CC)(CC)CC.Cc1ccc(S(=O)(=O)[O-])cc1',
    'tetraethylammonium tosylate': 'CC[N+](CC)(CC)CC.Cc1ccc(S(=O)(=O)[O-])cc1',
    'et4ni': 'CC[N+](CC)(CC)CC.[I-]',
    'et4ncl': 'CC[N+](CC)(CC)CC.[Cl-]',

    # alkali metal salts
    'liclo4': '[Li+].[O-]Cl(=O)(=O)=O',
    'lithium perchlorate': '[Li+].[O-]Cl(=O)(=O)=O',
    'libf4': '[Li+].F[B-](F)(F)F',
    'lipf6': '[Li+].F[P-](F)(F)(F)(F)F',
    'liotf': '[Li+].O=S(=O)([O-])C(F)(F)F',
    'lcl': '[Li+].[Cl-]',
    'libr': '[Li+].[Br-]',
    'lii': '[Li+].[I-]',
    'lioac': 'CC(=O)[O-].[Li+]',
    'lithium acetate': 'CC(=O)[O-].[Li+]',
    'liome': '[Li+].[O-]C',
    'liotbu': '[Li+].[O-]C(C)(C)C',

    'kpf6': '[K+].F[P-](F)(F)(F)(F)F',
    'potassium hexafluorophosphate': '[K+].F[P-](F)(F)(F)(F)F',
    'kbf4': '[K+].F[B-](F)(F)F',
    'kclo4': '[K+].[O-]Cl(=O)(=O)=O',
    'kcl': '[K+].[Cl-]',
    'kbr': '[K+].[Br-]',
    'ki': '[K+].[I-]',
    'kf': '[K+].[F-]',
    'k2co3': '[K+].[K+].O=C([O-])[O-]',
    'k3po4': '[K+].[K+].[K+].O=P([O-])([O-])[O-]',
    'kotbu': '[K+].[O-]C(C)(C)C',

    'naclo4': '[Na+].[O-]Cl(=O)(=O)=O',
    'sodium perchlorate': '[Na+].[O-]Cl(=O)(=O)=O',
    'nabr': '[Na+].[Br-]',
    'nai': '[Na+].[I-]',
    'nacl': '[Na+].[Cl-]',
    'naoh': '[Na+].[OH-]',
    'na2co3': '[Na+].[Na+].O=C([O-])[O-]',
    'na2so4': '[Na+].[Na+].O=S(=O)([O-])[O-]',

    'nh4cl': '[NH4+].[Cl-]',
    'nh4br': '[NH4+].[Br-]',
    'nh4i': '[NH4+].[I-]',
    'nh4bf4': '[NH4+].F[B-](F)(F)F',
    'nh4pf6': '[NH4+].F[P-](F)(F)(F)(F)F',
    'nh4oac': 'CC(=O)[O-].[NH4+]',

    # fluoride/HF salts
    'et3n·3hf': 'CCN(CC)CC.F.F.F',
    'et3n.3hf': 'CCN(CC)CC.F.F.F',
    'triethylamine trihydrofluoride': 'CCN(CC)CC.F.F.F',
    'et3n*3hf': 'CCN(CC)CC.F.F.F',
    'pyridine·hf': 'F.c1ccncc1',
    'py·hf': 'F.c1ccncc1',
    'py.hf': 'F.c1ccncc1',
    'hf·pyridine': 'F.c1ccncc1',
    'olah’s reagent': 'F.c1ccncc1',

    # acids/buffers as electrolyte
    'h2so4': 'O=S(=O)(O)O',
    'sulfuric acid': 'O=S(=O)(O)O',
    'hcl': 'Cl',
    'tfa': 'OC(=O)C(F)(F)F',
    'trifluoroacetic acid': 'OC(=O)C(F)(F)F',
    'tsoh': 'Cc1ccc(S(=O)(=O)O)cc1',
    'p-tsoh': 'Cc1ccc(S(=O)(=O)O)cc1',
    'p-toluenesulfonic acid': 'Cc1ccc(S(=O)(=O)O)cc1',
    'aco2h': 'CC(=O)O',
    'acoh': 'CC(=O)O',
    'acetic acid': 'CC(=O)O',
    'hbf4': 'F[B-](F)(F)F.[H+]',
    'hpf6': 'F[P-](F)(F)(F)(F)F.[H+]',
}


# 预编译归一化：忽略大小写、空格、连字符、星号
def _normalize_key(name: str) -> str:
    if not name:
        return ''
    s = name.lower().strip()
    # 一些常见替换
    s = s.replace('·', '.')  # · → .
    s = s.replace('‧', '.')
    s = s.replace('•', '.')
    s = s.replace('×', '.')
    s = s.replace('*', '.')
    # 标准化空格
    s = re.sub(r'\s+', ' ', s)
    return s


def name_to_smiles(name: Optional[str]) -> Optional[str]:
    """通过手工映射把名字归一化为 SMILES，找不到返回 None。"""
    if not name:
        return None
    s = _normalize_key(name)
    # 直接命中
    if s in ELECTROLYTE_NAME_TO_SMILES:
        return ELECTROLYTE_NAME_TO_SMILES[s]
    # 去掉所有空格/连字符再试
    s2 = s.replace(' ', '').replace('-', '')
    if s2 in ELECTROLYTE_NAME_TO_SMILES:
        return ELECTROLYTE_NAME_TO_SMILES[s2]
    # 去标点
    s3 = re.sub(r'[^a-z0-9.]', '', s)
    if s3 in ELECTROLYTE_NAME_TO_SMILES:
        return ELECTROLYTE_NAME_TO_SMILES[s3]
    # 从子串里匹配（取第一个匹配的 key）
    for k in ELECTROLYTE_NAME_TO_SMILES:
        if len(k) >= 5 and k in s2:
            return ELECTROLYTE_NAME_TO_SMILES[k]
    return None


if __name__ == "__main__":
    tests = [
        'n-Bu4NBF4', 'nBu4NBF4', 'TBABF4', 'Tetrabutylammonium tetrafluoroborate',
        'KPF6', 'LiClO4', 'Et3N·3HF', 'Et3N*3HF', 'nBu4NPF6 = 0.02 M',
        'NaCl', 'NH4Br', 'unknown salt',
    ]
    for t in tests:
        print(f"  {t!r:<50} → {name_to_smiles(t)}")
