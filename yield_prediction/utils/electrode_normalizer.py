"""
电极材料规范化模块

将各种电极名称写法归一化为标准类别
"""
import re
from typing import Optional, Dict, Tuple


# 电极材料规范化映射
ELECTRODE_PATTERNS = {
    # 石墨类
    'graphite': [
        r'graphite', r'gf\b', r'isostatic graphite',
    ],
    # 铂类
    'platinum': [
        r'platinum', r'\bpt\b', r'pt\s',
    ],
    # 碳类（非石墨）
    'carbon': [
        r'carbon(?!\s*felt)', r'\bc\b',  # carbon 但不是 carbon felt
    ],
    # 碳毡
    'carbon_felt': [
        r'carbon\s*felt', r'carbon\s*cloth', r'carbon\s*fiber',
    ],
    # 石墨毡
    'graphite_felt': [
        r'graphite\s*felt', r'graphite\s*cloth',
    ],
    # 玻碳/RVC
    'glassy_carbon': [
        r'glassy\s*carbon', r'vitreous\s*carbon', r'\brvc\b',
        r'reticulated\s*vitreous', r'gc\b',
    ],
    # 镍类
    'nickel': [
        r'nickel', r'\bni\b', r'ni\s',
    ],
    # 不锈钢
    'stainless_steel': [
        r'stainless', r'steel',
    ],
    # 镁类
    'magnesium': [
        r'magnesium', r'\bmg\b', r'mg\s',
    ],
    # 锌类
    'zinc': [
        r'zinc', r'\bzn\b', r'zn\s',
    ],
    # 铁类
    'iron': [
        r'iron', r'\bfe\b', r'fe\s',
    ],
    # 铝类
    'aluminum': [
        r'aluminum', r'aluminium', r'\bal\b',
    ],
    # 铜类
    'copper': [
        r'copper', r'\bcu\b',
    ],
    # 金类
    'gold': [
        r'gold', r'\bau\b',
    ],
    # 银类
    'silver': [
        r'silver', r'\bag\b',
    ],
    # 铅类
    'lead': [
        r'lead', r'\bpb\b',
    ],
    # 钛类
    'titanium': [
        r'titanium', r'\bti\b',
    ],
    # 硼掺杂金刚石
    'bdd': [
        r'boron.?doped', r'\bbdd\b', r'diamond',
    ],
    # 钯类
    'palladium': [
        r'palladium', r'\bpd\b',
    ],
    # 铌类
    'niobium': [
        r'niobium', r'\bnb\b',
    ],
    # 汞类
    'mercury': [
        r'mercury', r'\bhg\b',
    ],
    # 铅笔石墨
    'pencil_graphite': [
        r'pencil', r'\bpge\b',
    ],
}


# 标准电极类别到ID的映射
ELECTRODE_TO_ID = {
    'graphite': 0,
    'platinum': 1,
    'carbon': 2,
    'carbon_felt': 3,
    'graphite_felt': 4,
    'glassy_carbon': 5,
    'nickel': 6,
    'stainless_steel': 7,
    'magnesium': 8,
    'zinc': 9,
    'iron': 10,
    'aluminum': 11,
    'copper': 12,
    'gold': 13,
    'silver': 14,
    'lead': 15,
    'titanium': 16,
    'bdd': 17,
    'palladium': 18,
    'niobium': 19,
    'mercury': 20,
    'pencil_graphite': 21,
    'unknown': 22,  # 未知/缺失
}

ID_TO_ELECTRODE = {v: k for k, v in ELECTRODE_TO_ID.items()}
NUM_ELECTRODE_TYPES = len(ELECTRODE_TO_ID)


def normalize_electrode(name: Optional[str]) -> str:
    """
    将电极名称规范化为标准类别

    Args:
        name: 原始电极名称，如 "graphite rod", "Pt plate"

    Returns:
        标准类别名，如 "graphite", "platinum"
    """
    if not name or not str(name).strip() or str(name).strip().lower() in ('null', 'none', 'unspecified'):
        return 'unknown'

    name_lower = str(name).lower().strip()

    # 常见拼写错误修正
    # 使用负向回顾断言，避免把已正确的词重复修正 (如 'glassy carbon' → 'glassy ccarbon')
    name_lower = name_lower.replace('platinium', 'platinum').replace('platium', 'platinum')
    name_lower = re.sub(r'(?<!c)arbon', 'carbon', name_lower)       # "arbon" 修成 "carbon"
    name_lower = re.sub(r'(?<!g)raphite', 'graphite', name_lower)   # "raphite" 修成 "graphite"
    name_lower = re.sub(r'(?<!p)latinum', 'platinum', name_lower)   # "latinum" 修成 "platinum"
    name_lower = re.sub(r'(?<!s)tainless', 'stainless', name_lower) # "tainless" 修成 "stainless"
    name_lower = name_lower.replace('crabon', 'carbon').replace('gaphite', 'graphite')

    # 按优先级匹配（更具体的模式优先，避免 "glassy carbon" 误判为 carbon）
    # 优先级: 毡类 > 玻碳类 > 石墨类 > BDD > 一般类
    PRIORITY = [
        'carbon_felt', 'graphite_felt',           # 毡/布类
        'glassy_carbon',                          # 玻碳/RVC（必须在 carbon 之前）
        'pencil_graphite',                        # 铅笔石墨（必须在 graphite 之前）
        'bdd',                                    # BDD（含 diamond/boron-doped 等独特词）
        'graphite', 'carbon',                     # 常见碳基
        'platinum', 'nickel', 'stainless_steel',  # 主流金属
        'magnesium', 'zinc', 'iron', 'aluminum',
        'copper', 'gold', 'silver', 'lead',
        'titanium', 'palladium', 'niobium', 'mercury',
    ]
    for electrode_type in PRIORITY:
        patterns = ELECTRODE_PATTERNS.get(electrode_type, [])
        for pattern in patterns:
            if re.search(pattern, name_lower):
                return electrode_type

    return 'unknown'


def electrode_to_id(name: Optional[str]) -> int:
    """将电极名称转换为ID"""
    normalized = normalize_electrode(name)
    return ELECTRODE_TO_ID.get(normalized, ELECTRODE_TO_ID['unknown'])


def id_to_electrode(idx: int) -> str:
    """将ID转换为电极类别名"""
    return ID_TO_ELECTRODE.get(idx, 'unknown')


def analyze_electrode_coverage(electrode_names: list) -> Dict:
    """
    分析电极名称的覆盖情况

    Returns:
        统计信息字典
    """
    from collections import Counter

    normalized = [normalize_electrode(name) for name in electrode_names]
    counter = Counter(normalized)

    total = len(electrode_names)
    unknown_count = counter.get('unknown', 0)

    return {
        'total': total,
        'unknown_count': unknown_count,
        'unknown_ratio': unknown_count / total if total > 0 else 0,
        'coverage': 1 - unknown_count / total if total > 0 else 0,
        'distribution': dict(counter.most_common()),
    }


if __name__ == "__main__":
    # 测试
    test_names = [
        "graphite rod", "graphite", "graphite felt", "graphite plate",
        "platinum plate", "platinum", "pt", "Pt plate", "platinum electrode",
        "carbon felt", "carbon rod", "carbon cloth", "carbon",
        "reticulated vitreous carbon", "rvc", "glassy carbon",
        "nickel plate", "nickel", "Ni foam",
        "stainless steel", "stainless-steel",
        "mg plate", "magnesium",
        "zinc plate", "Zn",
        "iron", "Fe",
        "boron-doped diamond", "BDD",
        "", None, "unknown material xyz",
    ]

    print("电极规范化测试:")
    print("=" * 60)
    for name in test_names:
        normalized = normalize_electrode(name)
        idx = electrode_to_id(name)
        print(f"  '{name}' -> '{normalized}' (ID: {idx})")

    print(f"\n总电极类别数: {NUM_ELECTRODE_TYPES}")
