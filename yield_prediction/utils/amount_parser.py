"""
解析 v2 schema 中各种用量字符串到 (float_value, mask) 形式。

mask = 1 表示成功解析出数值；mask = 0 表示缺失或无法解析。
全部解析都做了 trace/range 等鲁棒处理。
"""
import re
from typing import Optional, Tuple


def _to_float(s) -> Optional[float]:
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def _strip(s) -> str:
    return (str(s) if s is not None else '').strip().replace('\xa0', ' ')


def parse_equiv(amount_dict) -> Tuple[float, int]:
    """从 amount dict 解析 equiv（mol equivalents）。

    优先 amount.equiv；其次从 amount.raw 用正则提取 'N equiv'/'N eq.';
    支持 'cat.' 'catalytic' → 0.1；'trace' → 0.05；'excess' → 5.0。
    """
    if not isinstance(amount_dict, dict):
        return 0.0, 0
    e = amount_dict.get('equiv')
    if e:
        v = _to_float(e)
        if v is not None and 0 < v < 1000:
            return v, 1
        # 处理范围 "1.0-2.0"
        m = re.match(r'^([\d.]+)\s*[-~]\s*([\d.]+)$', str(e).strip())
        if m:
            a, b = _to_float(m.group(1)), _to_float(m.group(2))
            if a is not None and b is not None:
                return (a + b) / 2.0, 1
    mp = amount_dict.get('mol_percent')
    if mp is not None:
        v = _to_float(mp)
        if v is not None and 0 < v < 10000:
            return v / 100.0, 1  # 10 mol% = 0.1 equiv
    raw = _strip(amount_dict.get('raw'))
    if raw:
        low = raw.lower()
        if 'trace' in low:
            return 0.05, 1
        if 'cat' in low and 'catalyst' not in low and 'cation' not in low:
            return 0.1, 1
        if 'excess' in low:
            return 5.0, 1
        # 'N equiv' / 'N eq.' / 'N eq' / 'N equivalent'
        m = re.search(r'([\d.]+)\s*(?:equiv|eq\.?|equivalents?)\b', low)
        if m:
            v = _to_float(m.group(1))
            if v is not None and 0 < v < 1000:
                return v, 1
        # 'N mol%' / 'N%'
        m = re.search(r'([\d.]+)\s*mol\s*%', low)
        if m:
            v = _to_float(m.group(1))
            if v is not None and 0 < v < 10000:
                return v / 100.0, 1
    return 0.0, 0


def parse_concentration_M(amount_dict) -> Tuple[float, int]:
    """解析浓度到 mol/L。

    支持 '0.1 M', '100 mM', '0.1 mol/L', '0.02M'。
    """
    if not isinstance(amount_dict, dict):
        return 0.0, 0
    c = _strip(amount_dict.get('concentration'))
    if not c:
        c = _strip(amount_dict.get('raw'))
    if not c:
        return 0.0, 0
    low = c.lower().replace(' ', '')
    # mM 必须先检（因为它包含 M）
    m = re.search(r'([\d.]+)\s*mm(?:ol/l)?', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 100000:
            return v / 1000.0, 1
    # M / mol/L / mol·L⁻¹
    m = re.search(r'([\d.]+)\s*(?:m(?!l)|mol/?l|mol·?l)', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 30:
            return v, 1
    return 0.0, 0


def parse_current_mA(s) -> Tuple[float, int]:
    """解析电流到 mA。"""
    s = _strip(s)
    if not s:
        return 0.0, 0
    low = s.lower().replace(' ', '')
    # 'N mA' (mA must precede A check)
    m = re.search(r'([\d.]+)\s*ma\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 100000:
            return v, 1
    # 'N µA' / 'N uA' (microampere) → mA / 1000
    m = re.search(r'([\d.]+)\s*[uµ]a\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v / 1000.0, 1
    # 'N A' (ampere) → mA × 1000
    m = re.search(r'([\d.]+)\s*a\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 1000:
            return v * 1000.0, 1
    # 'I = N' 或纯数字
    m = re.search(r'i\s*=\s*([\d.]+)', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v, 1
    return 0.0, 0


def parse_current_density(s) -> Tuple[float, int]:
    """解析电流密度到 mA/cm²。"""
    s = _strip(s)
    if not s:
        return 0.0, 0
    low = s.lower().replace(' ', '').replace('²', '2')
    m = re.search(r'([\d.]+)\s*ma/cm2', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 10000:
            return v, 1
    m = re.search(r'([\d.]+)\s*ua/cm2', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v / 1000.0, 1
    m = re.search(r'([\d.]+)\s*a/cm2', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 100:
            return v * 1000.0, 1
    return 0.0, 0


def parse_potential_V(s) -> Tuple[float, int]:
    """解析电势到 V。

    去掉参比电极注释（vs Ag/AgCl 等），保留主数值，包括负号。
    """
    s = _strip(s)
    if not s:
        return 0.0, 0
    # 去掉 vs xxx 部分
    cleaned = re.split(r'\bvs\.?\b', s.lower())[0]
    cleaned = cleaned.replace(' ', '')
    # 匹配数值 + V
    m = re.search(r'(-?[\d.]+)\s*v\b', cleaned)
    if m:
        v = _to_float(m.group(1))
        if v is not None and -10 < v < 10:
            return v, 1
    # 仅 'E = N' 形式
    m = re.search(r'e\s*=\s*(-?[\d.]+)', cleaned)
    if m:
        v = _to_float(m.group(1))
        if v is not None and -10 < v < 10:
            return v, 1
    return 0.0, 0


def parse_temperature_C(s) -> Tuple[float, int]:
    """解析温度到 °C。

    rt/room temperature/RT → 25
    支持 '60 °C', '60°C', '60 C', '-10 to 0 °C' (取均值)
    """
    s = _strip(s)
    if not s:
        return 0.0, 0
    low = s.lower()
    if any(k in low for k in ('room temp', 'r.t.', ' rt ', 'rt,', 'rt ', 'ambient')):
        return 25.0, 1
    if low.strip() in ('rt', 'r.t', 'r.t.'):
        return 25.0, 1
    # 范围 '-10 to 0 °C' / '60-80 °C'
    m = re.search(r'(-?\d+(?:\.\d+)?)\s*(?:to|~|-)\s*(-?\d+(?:\.\d+)?)\s*°?\s*c\b', low)
    if m:
        a, b = _to_float(m.group(1)), _to_float(m.group(2))
        if a is not None and b is not None:
            t = (a + b) / 2.0
            if -100 < t < 500:
                return t, 1
    # 单值 '60 °C' / '60°C'
    m = re.search(r'(-?\d+(?:\.\d+)?)\s*°?\s*c\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and -100 < v < 500:
            return v, 1
    return 0.0, 0


def parse_time_h(s) -> Tuple[float, int]:
    """解析时间到小时。

    'N h' / 'N hours' / 'N min' / 'N s'
    """
    s = _strip(s)
    if not s:
        return 0.0, 0
    low = s.lower()
    # 范围 'N to M h'
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:to|~|-)\s*(\d+(?:\.\d+)?)\s*h(?:ours?|rs?)?\b', low)
    if m:
        a, b = _to_float(m.group(1)), _to_float(m.group(2))
        if a is not None and b is not None:
            return (a + b) / 2.0, 1
    # 'N h' / 'N hours'
    m = re.search(r'(\d+(?:\.\d+)?)\s*h(?:ours?|rs?)?\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 1000:
            return v, 1
    # 'N min'
    m = re.search(r'(\d+(?:\.\d+)?)\s*min\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 100000:
            return v / 60.0, 1
    # 'N s' / 'N sec'
    m = re.search(r'(\d+(?:\.\d+)?)\s*s(?:ec(?:onds?)?)?\b', low)
    if m:
        v = _to_float(m.group(1))
        if v is not None and 0 < v < 1000000:
            return v / 3600.0, 1
    # 'overnight' → 16 h
    if 'overnight' in low:
        return 16.0, 1
    return 0.0, 0


if __name__ == "__main__":
    # 自检
    print(parse_equiv({'equiv': '2.0', 'raw': '2.0 equiv'}))     # (2.0, 1)
    print(parse_equiv({'mol_percent': '5', 'raw': '5 mol%'}))    # (0.05, 1)
    print(parse_equiv({'raw': 'trace'}))                         # (0.05, 1)
    print(parse_equiv({'raw': 'cat. (5 mol%)'}))                 # (0.1, 1)
    print(parse_equiv({}))                                        # (0.0, 0)
    print(parse_concentration_M({'concentration': '0.02 M'}))    # (0.02, 1)
    print(parse_concentration_M({'concentration': '100 mM'}))    # (0.1, 1)
    print(parse_current_mA('12 mA'))                             # (12.0, 1)
    print(parse_current_mA('1.5 A'))                             # (1500.0, 1)
    print(parse_current_density('3 mA/cm²'))                     # (3.0, 1)
    print(parse_potential_V('1.5 V vs Ag/AgCl'))                 # (1.5, 1)
    print(parse_potential_V('-2.0 V'))                           # (-2.0, 1)
    print(parse_temperature_C('rt'))                             # (25.0, 1)
    print(parse_temperature_C('60 °C'))                          # (60.0, 1)
    print(parse_temperature_C('-10 to 0 °C'))                    # (-5.0, 1)
    print(parse_time_h('4 h'))                                   # (4.0, 1)
    print(parse_time_h('30 min'))                                # (0.5, 1)
    print(parse_time_h('overnight'))                             # (16.0, 1)
