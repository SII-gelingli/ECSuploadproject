"""细粒度电极分类: 材料 × 形状 ~ 50 类.

层次:
  1. 材料 (~15 大类, 同 V3 anode_material)
  2. 形状/类型 (rod / plate / felt / cloth / mesh / wire / foil / generic)
  3. 特殊: BDD / Pencil / RVC / Glassy Carbon 单列 (技术上是材料层级)

规则: 关键词扫描 (优先级从特殊到一般).
"""
import re


# 特殊材料/类型 (优先级最高, 它们本身就是独特电极类型)
SPECIAL = [
    ('boron_doped_diamond', [r'\bbdd\b', r'boron[- ]?doped[- ]?diamond']),
    ('pencil_graphite',     [r'pencil', r'pgl(?!\w)', r'^pg\b']),
    ('reticulated_vitreous_carbon', [r'\brvc\b', r'reticulated[- ]?vitreous[- ]?carbon']),
    ('glassy_carbon',       [r'glassy[- ]?carbon', r'\bgc\b(?! [a-z])', r'vitreous[- ]?carbon(?!.*reticulat)']),
    ('graphene_felt',       [r'graphene[- ]?felt']),
    ('graphene_oxide',      [r'graphene[- ]?oxide', r'\bgo\b']),
    ('mmo',                 [r'\bmmo\b', r'mixed[- ]?metal[- ]?oxide']),
    ('aluminum_oxide',      [r'al2o3', r'aluminum[- ]?oxide']),
]

# 通用形状关键词 (用于材料后的子类)
FORM_KEYWORDS = [
    ('rod',       [r'\brod\b', r'cylinder', r'\bbar\b', r'stick']),
    ('plate',     [r'\bplate\b', r'\bsheet\b']),
    ('felt',      [r'\bfelt\b', r'\bgf\b']),
    ('cloth',     [r'\bcloth\b', r'\bfabric\b']),
    ('mesh',      [r'\bmesh\b', r'screen', r'\bnet\b']),
    ('foil',      [r'\bfoil\b']),
    ('wire',      [r'\bwire\b', r'\bfilament']),
    ('foam',      [r'\bfoam\b']),
    ('paper',     [r'\bpaper\b']),
    ('powder',    [r'\bpowder\b', r'\bblack\b']),  # 如 "Pt black"
    ('brush',     [r'\bbrush\b']),
    ('disk',      [r'\bdisk\b', r'\bdisc\b']),
]

# 材料关键词 (按优先级排, 先 match graphite 再 carbon — 否则 'graphite' 被 'carbon' 吃掉)
MATERIAL_KEYWORDS = [
    ('graphite',           [r'\bgraphite\b', r'\bgraph\b']),
    ('carbon',             [r'\bcarbon\b', r'(?<![a-z])c(?![a-z])', r'\bc anode\b', r'\bc cathode\b', r'\bc \(']),
    ('platinum',           [r'\bplatinum\b', r'(?<![a-z])pt(?![a-z])']),
    ('palladium',          [r'\bpalladium\b', r'\bpd(?![a-z])']),
    ('nickel',             [r'\bnickel\b', r'(?<![a-z])ni(?![a-z])']),
    ('stainless_steel',    [r'stainless[- ]?steel', r'\bss\b', r'\b316l\b', r'\b304\b']),
    ('copper',             [r'\bcopper\b', r'(?<![a-z])cu(?![a-z])']),
    ('iron',               [r'\biron\b', r'(?<![a-z])fe(?![a-z])']),
    ('zinc',               [r'\bzinc\b', r'(?<![a-z])zn(?![a-z])']),
    ('magnesium',          [r'magnesium', r'(?<![a-z])mg(?![a-z])']),
    ('aluminum',           [r'aluminum', r'aluminium', r'(?<![a-z])al(?![a-z])']),
    ('lead',               [r'\blead\b', r'(?<![a-z])pb(?![a-z])']),
    ('tin',                [r'\btin\b', r'(?<![a-z])sn(?![a-z])']),
    ('titanium',           [r'titanium', r'\bti(?![a-z])']),
    ('silver',             [r'\bsilver\b', r'(?<![a-z])ag(?![a-z])']),
    ('gold',               [r'\bgold\b', r'(?<![a-z])au(?![a-z])']),
    ('cobalt',             [r'\bcobalt\b', r'(?<![a-z])co(?![a-z])']),
    ('mercury',            [r'mercury', r'(?<![a-z])hg(?![a-z])']),
    ('niobium',            [r'niobium', r'\bnb(?![a-z])']),
]


def classify_electrode_fine(raw: str) -> str:
    """Return finely-grained electrode class string (e.g. 'graphite_felt', 'platinum_plate', 'RVC')."""
    if not raw or not raw.strip():
        return 'ABSENT'
    t = raw.strip().lower()
    # 去掉 charge / size 标记
    t = re.sub(r'\([+-±]\)', ' ', t)
    t = re.sub(r'\d+\s*(mm|cm|×|x)', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()

    # 优先级 1: 特殊单类电极
    for cls, patterns in SPECIAL:
        for p in patterns:
            if re.search(p, t):
                return cls

    # 优先级 2: 材料 + 形状组合
    matched_material = None
    for mat, pats in MATERIAL_KEYWORDS:
        for p in pats:
            if re.search(p, t):
                matched_material = mat
                break
        if matched_material: break
    if matched_material is None:
        return 'unknown_electrode'

    # 找形状关键词
    for form, pats in FORM_KEYWORDS:
        for p in pats:
            if re.search(p, t):
                return f'{matched_material}_{form}'
    # 没找到形状 → 用 _generic
    return f'{matched_material}_generic'


# 把所有可能的输出类放到一个固定 vocab (用于 model output dim)
def build_fine_electrode_vocab() -> list:
    """生成所有 (材料 × 形状) + 特殊类 + ABSENT/unknown 的完整 vocab."""
    vocab = ['ABSENT', 'unknown_electrode']
    # special 类
    for cls, _ in SPECIAL:
        vocab.append(cls)
    # 材料 × 形状
    for mat, _ in MATERIAL_KEYWORDS:
        for form, _ in FORM_KEYWORDS:
            vocab.append(f'{mat}_{form}')
        vocab.append(f'{mat}_generic')
    return vocab


FINE_ELECTRODE_VOCAB = build_fine_electrode_vocab()
FINE_ELECTRODE_NAME2ID = {n: i for i, n in enumerate(FINE_ELECTRODE_VOCAB)}
NUM_FINE_ELECTRODE_CLASSES = len(FINE_ELECTRODE_VOCAB)


if __name__ == '__main__':
    print(f'Fine electrode vocab size: {NUM_FINE_ELECTRODE_CLASSES}')
    print()
    # 测试一些样本
    tests = [
        'graphite', 'graphite rod', 'graphite felt', 'graphite plate',
        'carbon', 'carbon rod', 'carbon felt', 'carbon cloth', 'carbon plate',
        'C(+)', 'C', 'C anode', 'Pt', 'platinum plate', 'platinum wire', 'Pt(+)',
        'RVC', 'RVC anode', 'reticulated vitreous carbon',
        'glassy carbon', 'GC', 'pencil', 'BDD',
        'Mg', 'Mg plate', 'Mg rod',
        'stainless steel', 'SS', 'Ni foam', 'Pd plate',
        'graphite SK-50', 'carbon cloth anode (15 mm × 15 mm × 0.36 mm)',
    ]
    for t in tests:
        print(f'  {t:<50} → {classify_electrode_fine(t)}')
