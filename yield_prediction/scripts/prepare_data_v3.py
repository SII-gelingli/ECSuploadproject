"""
prepare_data_v3.py — 2-step 条件预测专用数据准备

相对 v2 的改进：
1. 8 个种类 head，全部带显式 ABSENT 类（index 0）
2. 电解质优先用 electrolytes 字段 SMILES，否则用 ec.electrolyte 字符串经
   electrolyte_name_map 归一化到 SMILES（覆盖率 81% → ~95%）
3. 长尾裁剪：electrolyte ≥3 次保留、catalyst/reagent ≥3 次保留、ligand/additive ≥5 次保留，
   其余进 OTHER（index 1），降低 CE 损失被稀有类稀释
4. 用量解析：调用 amount_parser 解析 7 个数值字段 + mask
5. 测试集 = 年份 ≥2025 的论文（沿用 prepare_data_audited 的 paper-level 切分）
6. 输出 data_audited_v3/{train,val,test}.pt + vocab.json + amount_stats.json + split_meta.json
"""
import sys
import json
import re
import random
from pathlib import Path
from collections import Counter, defaultdict

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np
import torch
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.feature_extractor import MolecularFeatureExtractor
from utils.electrode_normalizer import electrode_to_id, NUM_ELECTRODE_TYPES
from utils.amount_parser import (
    parse_equiv, parse_concentration_M, parse_current_mA,
    parse_current_density, parse_potential_V, parse_temperature_C, parse_time_h,
)
from utils.electrolyte_name_map import name_to_smiles
from scripts.prepare_data_audited import (
    extract_year, paper_id, parse_yield_string,
    canonical_paper_id, build_paper_alias_table,
)

AUDITED_ROOT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited")
OUT_DIR = project_root / "data_audited_v3"
TEST_YEAR_THRESHOLD = 2025

# 8 个种类 head 的最小出现次数（决定是否进 vocab，否则归 OTHER）
# 当前策略 B: 全量保留 (≥1) — 配合 hier+Set 架构, class signal 缩小搜索空间
# 让稀有 SMILES 也能被预测出来 (化学身份不丢)
MIN_FREQ = {
    'solvent': 1,
    'electrolyte': 1,
    'catalyst': 1,
    'reagent': 1,
    'ligand': 1,
    'additive': 1,
}

# 每个 head 的特殊 index
IDX_ABSENT = 0     # 表示 "不需要这种条件"
IDX_OTHER = 1      # 表示 "罕见 SMILES，未进 vocab"
# 真实 SMILES 从 index 2 开始

CELL_TYPE_CLASSES = ['undivided', 'divided', 'flow', 'ABSENT']  # 4 类


# 应当被归到 ABSENT 的"方法/技术"描述（非真实 cell_type）
_METHOD_KEYWORDS = (
    'cce',                          # constant current electrolysis (方法)
    'integrated cell reaction',     # 方法/抽象描述
    'in cell',                      # 模糊术语
    'separation cell reaction',     # 含糊
)
# 仅仅是电极描述（不含 cell 几何信息），也归 ABSENT
_ELECTRODE_ONLY_PATTERNS = (
    'c(+)/c(-)', 'c (+)/c (-)', '(+)c/(-)c', 'pt(+)/pt(-)',
)


def encode_cell_type(cell_type) -> int:
    """编码 cell_type 到 0-3（4 类: undivided/divided/flow/ABSENT）。

    清洗规则: CCE / Integrated Cell Reaction / "in cell" 等"方法/含糊"描述 → ABSENT (而非 other)
    """
    if cell_type is None or str(cell_type).strip() == '':
        return 3  # ABSENT
    ct = str(cell_type).lower().strip().strip('"\'()')
    if ct in ('null', 'none', 'unspecified', ''):
        return 3
    # 清洗: 方法描述、仅电极描述 → ABSENT
    if any(k == ct or k in ct.split() for k in _METHOD_KEYWORDS):
        return 3
    if any(p in ct for p in _ELECTRODE_ONLY_PATTERNS):
        return 3
    # flow（含 flow undivided 也归 flow，因为流动比 undivided 更具体）
    if 'flow' in ct or 'vapourtec' in ct:
        return 2
    # **关键: undivided 必须先于 divided 检查 (字符串 "undivided" 包含 "divided")**
    if any(k in ct for k in ('undivi', 'undvi', 'udivi', 'unndiv', 'undiv',
                              'indivisi', 'indivisible',  # typo
                              'beaker', 'electrasyn', 'three-neck', 'bottle',
                              'flask', 'schlenk', 'ika')):
        return 0
    # sealed → 当作 undivided
    if 'sealed' in ct:
        return 0
    # divided / H-cell / two-compartment / membrane / nafion / 隔板/隔膜
    if any(k in ct for k in ('h-cell', 'h-type', 'h cell', 'h type', 'diaphragm',
                              'two-compartment', 'two compartment', 'compartment',
                              'divided', 'devided', 'separation cell', 'separating',
                              'separator', 'ex-cell', 'nafion', 'membrane')):
        return 1
    # 其他无法识别 → ABSENT
    return 3


# 同样地，anode/cathode 用 electrode_to_id（22 个具体 + index 22 = unknown）
# 我们这里把 index 22 重命名为 ABSENT（语义一致：没记录电极信息 ≈ 缺失）
def encode_electrode(name) -> int:
    return electrode_to_id(name)  # 已经返回 22 = unknown 当输入为空


_canonical_cache = {}


def canonicalize_smiles(smi: str) -> str:
    """RDKit canonical 化 SMILES。失败保留原文。带缓存。"""
    if not smi:
        return ''
    if smi in _canonical_cache:
        return _canonical_cache[smi]
    try:
        from rdkit import Chem
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            _canonical_cache[smi] = smi
            return smi
        canon = Chem.MolToSmiles(mol, canonical=True)
        _canonical_cache[smi] = canon
        return canon
    except Exception:
        _canonical_cache[smi] = smi
        return smi


def get_first_smiles(items) -> str:
    """从 catalysts/reagents/etc. list 取第一个有 SMILES 的条目, 自动 canonical 化。"""
    for it in (items or []):
        if isinstance(it, dict):
            sm = it.get('smiles')
            if sm:
                return canonicalize_smiles(sm)
    return ''


def get_first_amount_dict(items) -> dict:
    """从 list 取第一个 amount dict（与 get_first_smiles 配对）。"""
    for it in (items or []):
        if isinstance(it, dict) and it.get('smiles'):
            return it.get('amount') or {}
    return {}


def get_electrolyte_smiles(rxn) -> str:
    """优先 electrolytes 字段；否则用 ec.electrolyte 字符串经 name_map 归一化。两路径都做 canonical。"""
    elist = rxn.get('electrolytes') or []
    sm = get_first_smiles(elist)
    if sm:
        return sm
    ec = (rxn.get('conditions') or {}).get('electrochemistry') or {}
    name = ec.get('electrolyte')
    if name:
        sm2 = name_to_smiles(name)
        if sm2:
            sm2 = canonicalize_smiles(sm2)
        if sm2:
            return sm2
    return ''


def get_electrolyte_amount(rxn) -> dict:
    elist = rxn.get('electrolytes') or []
    for it in elist:
        if isinstance(it, dict) and it.get('amount'):
            return it.get('amount') or {}
    return {}


def convert_reaction(rxn):
    """把 v2 reaction dict 转成 v3 内部格式（含 8 个种类 SMILES + 7 个用量）。"""
    reactants = [r for r in (rxn.get('reactants') or []) if isinstance(r, dict) and r.get('smiles')]
    products = [p for p in (rxn.get('products') or []) if isinstance(p, dict) and p.get('smiles')]
    if not reactants or not products:
        return None

    # 取首个能解析的产率
    yield_val = None
    for p in products:
        yv = parse_yield_string(p.get('yield'))
        if yv is not None:
            yield_val = yv
            break

    conditions = rxn.get('conditions') or {}
    ec = (conditions.get('electrochemistry') or {}) if isinstance(conditions, dict) else {}

    # 8 个种类 SMILES（空字符串将被映射为 ABSENT 类）
    anode_name = ec.get('anode') or ''
    cathode_name = ec.get('cathode') or ''
    cell_type_name = ec.get('cell_type') or ''
    solvent_sm = get_first_smiles(rxn.get('solvents'))
    electrolyte_sm = get_electrolyte_smiles(rxn)
    catalyst_sm = get_first_smiles(rxn.get('catalysts'))
    reagent_sm = get_first_smiles(rxn.get('reagents'))
    ligand_sm = get_first_smiles(rxn.get('ligands'))
    additive_sm = get_first_smiles(rxn.get('additives'))

    # 10 个用量数值 + mask
    # 分物质解析 equiv: catalyst / reagent / ligand / additive 各自一个 head
    cat_eq, m_cat_eq = parse_equiv(get_first_amount_dict(rxn.get('catalysts')))
    reag_eq, m_reag_eq = parse_equiv(get_first_amount_dict(rxn.get('reagents')))
    lig_eq, m_lig_eq = parse_equiv(get_first_amount_dict(rxn.get('ligands')))
    add_eq, m_add_eq = parse_equiv(get_first_amount_dict(rxn.get('additives')))
    elec_amount = get_electrolyte_amount(rxn)
    elec_conc, m_elec_c = parse_concentration_M(elec_amount)
    current_mA, m_cur = parse_current_mA(ec.get('current'))
    current_den, m_den = parse_current_density(ec.get('current_density'))
    potential, m_pot = parse_potential_V(ec.get('potential'))
    temperature, m_temp = parse_temperature_C(conditions.get('temperature') if isinstance(conditions, dict) else None)
    time_h, m_time = parse_time_h(conditions.get('time') if isinstance(conditions, dict) else None)

    return {
        'reactant_smiles': [r['smiles'] for r in reactants],
        'product_smiles': [p['smiles'] for p in products],
        'yield_value': yield_val if yield_val is not None else 0.0,
        'has_yield': 1 if yield_val is not None else 0,
        # 种类 raw 数据（编码留到后面 vocab 建好后做）
        'anode_name': anode_name,
        'cathode_name': cathode_name,
        'cell_type_name': cell_type_name,
        'solvent_sm': solvent_sm,
        'electrolyte_sm': electrolyte_sm,
        'catalyst_sm': catalyst_sm,
        'reagent_sm': reagent_sm,
        'ligand_sm': ligand_sm,
        'additive_sm': additive_sm,
        # 用量数值
        'amount': {
            'catalyst_equiv': cat_eq,       'mask_catalyst_equiv': m_cat_eq,
            'reagent_equiv': reag_eq,       'mask_reagent_equiv': m_reag_eq,
            'ligand_equiv': lig_eq,         'mask_ligand_equiv': m_lig_eq,
            'additive_equiv': add_eq,       'mask_additive_equiv': m_add_eq,
            'electrolyte_M': elec_conc,     'mask_electrolyte_M': m_elec_c,
            'current_mA': current_mA,       'mask_current_mA': m_cur,
            'current_density': current_den, 'mask_current_density': m_den,
            'potential_V': potential,       'mask_potential_V': m_pot,
            'temperature_C': temperature,   'mask_temperature_C': m_temp,
            'time_h': time_h,               'mask_time_h': m_time,
        },
    }


def build_smiles_vocab(items, min_freq, max_size=None):
    """构造 SMILES → index 映射；index 0=ABSENT, 1=OTHER, 实类从 2 开始。"""
    cnt = Counter(items)
    pairs = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    vocab = {'__ABSENT__': IDX_ABSENT, '__OTHER__': IDX_OTHER}
    next_idx = 2
    for sm, c in pairs:
        if not sm:
            continue
        if c < min_freq:
            continue
        if max_size is not None and next_idx >= max_size + 2:
            break
        vocab[sm] = next_idx
        next_idx += 1
    return vocab


def lookup(vocab, sm):
    if not sm:
        return IDX_ABSENT
    return vocab.get(sm, IDX_OTHER)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(AUDITED_ROOT.rglob('*.json'))
    print(f"Found {len(files)} v2 JSON files")

    # Step 0: 构建 alias 表合并 "DOI 文件 + no-DOI 文件" 同篇 paper (双身份泄漏修复)
    print("Building paper alias table for cross-identity dedup...")
    alias_table = build_paper_alias_table(AUDITED_ROOT)
    print(f"  {len(alias_table)} aliases (no-DOI pid → canonical DOI pid)")

    # Step 1: 加载 + 分组到 paper (用 canonical_paper_id 避免双身份)
    papers = defaultdict(lambda: {'year': None, 'reactions': []})
    skip = Counter()
    for fp in tqdm(files, desc="Loading"):
        try:
            with open(fp) as f:
                d = json.load(f)
        except Exception:
            skip['load_fail'] += 1
            continue
        src = d.get('source') or {}
        doi = src.get('doi') or ''
        y, _ = extract_year(fp.name, doi, src if isinstance(src, dict) else {})
        pid = canonical_paper_id(doi, fp.name, alias_table)
        p = papers[pid]
        if y is not None and (p['year'] is None or y > p['year']):
            p['year'] = y
        for rxn in d.get('reactions', []):
            conv = convert_reaction(rxn)
            if conv is None:
                skip['unconvertible'] += 1
                continue
            p['reactions'].append(conv)

    print(f"Total papers: {len(papers)}, kept reactions: {sum(len(p['reactions']) for p in papers.values())}")
    print(f"Skip: {dict(skip)}")

    # Step 2: paper-level 切分（test=2025+ 新生成, 不再复用 v2 split — v2 split 基于
    # 老 paper_id 规则, 与 canonical_paper_id 不兼容. 双身份 paper 修复后必须重新切分）
    rest, no_year, test = [], [], []
    for pid, p in papers.items():
        if p['year'] is None:
            no_year.append((pid, p))
        elif p['year'] >= TEST_YEAR_THRESHOLD:
            test.append((pid, p))
        else:
            rest.append((pid, p))
    test_papers = test
    rest.extend(no_year)
    random.seed(42)
    random.shuffle(rest)
    n_val = max(1, len(rest) // 10)
    val_papers = rest[:n_val]
    train_papers = rest[n_val:]
    print(f"Fresh split (canonical paper_id): train={len(train_papers)}, val={len(val_papers)}, test={len(test_papers)}")

    def flatten(plist):
        return [r for _, p in plist for r in p['reactions']]

    def _rxn_smi_key(r):
        """反应 SMILES 唯一键 (用于跨 split 去重)."""
        rs = r.get('reactant_smiles', []) or []
        ps = r.get('product_smiles', []) or []
        return '.'.join(rs) + '>>' + '.'.join(ps)

    # 反应级 dedup: 不同 paper 报告同一反应时, 优先级 test > val > train.
    # 从 train 中剔除所有与 val/test 同 SMILES 的反应, 防止反应级泄漏.
    test_keys = set()
    for _, p in test_papers:
        for r in p['reactions']: test_keys.add(_rxn_smi_key(r))
    val_keys = set()
    for _, p in val_papers:
        for r in p['reactions']: val_keys.add(_rxn_smi_key(r))
    holdout_keys = test_keys | val_keys

    n_removed_train = 0
    for pid, p in train_papers:
        keep = []
        for r in p['reactions']:
            if _rxn_smi_key(r) in holdout_keys:
                n_removed_train += 1
                continue
            keep.append(r)
        p['reactions'] = keep
    # val 中与 test 同 SMILES 的, 也从 val 剔除 (test 优先)
    n_removed_val = 0
    for pid, p in val_papers:
        keep = []
        for r in p['reactions']:
            if _rxn_smi_key(r) in test_keys:
                n_removed_val += 1
                continue
            keep.append(r)
        p['reactions'] = keep
    print(f"Reaction-level dedup (priority test > val > train):")
    print(f"  removed {n_removed_train} train reactions overlapping val/test")
    print(f"  removed {n_removed_val} val reactions overlapping test")

    train_rxns = flatten(train_papers)
    val_rxns = flatten(val_papers)
    test_rxns = flatten(test_papers)
    print(f"Reactions: train={len(train_rxns)}, val={len(val_rxns)}, test={len(test_rxns)}")

    # Step 3: 构造 vocab — 用全部数据（推理时希望覆盖所有已知条件）
    all_rxns = train_rxns + val_rxns + test_rxns
    vocab = {
        'solvent': build_smiles_vocab([r['solvent_sm'] for r in all_rxns], MIN_FREQ['solvent']),
        'electrolyte': build_smiles_vocab([r['electrolyte_sm'] for r in all_rxns], MIN_FREQ['electrolyte']),
        'catalyst': build_smiles_vocab([r['catalyst_sm'] for r in all_rxns], MIN_FREQ['catalyst']),
        'reagent': build_smiles_vocab([r['reagent_sm'] for r in all_rxns], MIN_FREQ['reagent']),
        'ligand': build_smiles_vocab([r['ligand_sm'] for r in all_rxns], MIN_FREQ['ligand']),
        'additive': build_smiles_vocab([r['additive_sm'] for r in all_rxns], MIN_FREQ['additive']),
    }
    print("\nVocab sizes (含 ABSENT + OTHER):")
    for k, v in vocab.items():
        print(f"  {k}: {len(v)}")

    with open(OUT_DIR / 'vocab.json', 'w') as f:
        json.dump(vocab, f, indent=2)

    # Step 4: featurize + 编码标签
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    HEADS_SMILES = ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']
    AMOUNT_FIELDS = ['catalyst_equiv', 'reagent_equiv', 'ligand_equiv', 'additive_equiv',
                     'electrolyte_M', 'current_mA', 'current_density',
                     'potential_V', 'temperature_C', 'time_h']

    def featurize(rxns, name):
        out = []
        for rxn in tqdm(rxns, desc=f"Featurize {name}"):
            try:
                r_fp = mol_extractor.encode_molecules(rxn['reactant_smiles'])
                p_fp = mol_extractor.encode_molecules(rxn['product_smiles'])
                diff_fp = np.abs(p_fp - r_fp)
                labels = {
                    'anode': encode_electrode(rxn['anode_name']),
                    'cathode': encode_electrode(rxn['cathode_name']),
                    'cell_type': encode_cell_type(rxn['cell_type_name']),
                }
                for h in HEADS_SMILES:
                    labels[h] = lookup(vocab[h], rxn[f'{h}_sm'])

                amount_values = np.array(
                    [rxn['amount'][f] for f in AMOUNT_FIELDS], dtype=np.float32
                )
                amount_mask = np.array(
                    [rxn['amount'][f'mask_{f}'] for f in AMOUNT_FIELDS], dtype=np.float32
                )

                out.append({
                    'reactant_fp': r_fp.astype(np.float32),
                    'product_fp': p_fp.astype(np.float32),
                    'diff_fp': diff_fp.astype(np.float32),
                    'labels': labels,
                    'amount_values': amount_values,
                    'amount_mask': amount_mask,
                    'yield': float(rxn['yield_value']),
                    'has_yield': int(rxn['has_yield']),
                    'reactant_smiles': rxn['reactant_smiles'],
                    'product_smiles': rxn['product_smiles'],
                })
            except Exception as e:
                continue
        return out

    train_data = featurize(train_rxns, 'train')
    val_data = featurize(val_rxns, 'val')
    test_data = featurize(test_rxns, 'test')

    torch.save(train_data, OUT_DIR / 'train.pt')
    torch.save(val_data, OUT_DIR / 'val.pt')
    torch.save(test_data, OUT_DIR / 'test.pt')

    # Step 5: 计算用量统计（用 train 集上 mask=1 的样本）
    amount_stats = {}
    for i, field in enumerate(AMOUNT_FIELDS):
        vals = np.array([d['amount_values'][i] for d in train_data if d['amount_mask'][i] > 0])
        LOG_FIELDS = ('catalyst_equiv', 'reagent_equiv', 'ligand_equiv', 'additive_equiv',
                       'electrolyte_M', 'current_mA', 'current_density', 'time_h')
        if field in LOG_FIELDS:
            offset = 0.01 if field in ('electrolyte_M',) else 0.1
            t = np.log(vals + offset)
            transform = 'log'
        elif field == 'temperature_C':
            t = (vals - 25) / 30.0
            transform = 'temperature'
            offset = None
        else:  # potential_V
            t = vals
            transform = 'identity'
            offset = None
        if len(t) > 0:
            amount_stats[field] = {
                'n': int(len(vals)),
                'raw_mean': float(np.mean(vals)),
                'raw_std': float(np.std(vals)),
                'raw_min': float(np.min(vals)),
                'raw_max': float(np.max(vals)),
                'transform': transform,
                'offset': offset,
                'norm_mean': float(np.mean(t)),
                'norm_std': float(np.std(t) + 1e-8),
            }
        else:
            amount_stats[field] = {'n': 0, 'transform': transform, 'offset': offset,
                                   'norm_mean': 0.0, 'norm_std': 1.0}

    with open(OUT_DIR / 'amount_stats.json', 'w') as f:
        json.dump(amount_stats, f, indent=2)

    # 统计 ABSENT 占比（验证 logic）
    print("\n=== ABSENT 占比检查 ===")
    print(f"{'head':<14}{'train':>12}{'val':>12}{'test':>12}")
    HEAD_ABSENT_IDX = {'anode': 22, 'cathode': 22, 'cell_type': 5,
                       'solvent': 0, 'electrolyte': 0, 'catalyst': 0,
                       'reagent': 0, 'ligand': 0, 'additive': 0}
    for h, idx in HEAD_ABSENT_IDX.items():
        counts = []
        for name, data in [('train', train_data), ('val', val_data), ('test', test_data)]:
            n = len(data)
            absent = sum(1 for d in data if d['labels'][h] == idx)
            counts.append(f"{absent/n*100:5.1f}% ({absent}/{n})")
        print(f"  {h:<14}{counts[0]:>12}{counts[1]:>12}{counts[2]:>12}")

    # 用量字段 mask 占比
    print("\n=== 用量字段可用率 ===")
    print(f"{'field':<20}{'train':>12}{'val':>12}{'test':>12}")
    for i, f in enumerate(AMOUNT_FIELDS):
        counts = []
        for name, data in [('train', train_data), ('val', val_data), ('test', test_data)]:
            n = len(data)
            valid = sum(1 for d in data if d['amount_mask'][i] > 0)
            counts.append(f"{valid/n*100:5.1f}% ({valid}/{n})")
        print(f"  {f:<20}{counts[0]:>12}{counts[1]:>12}{counts[2]:>12}")

    stats = {
        'source_root': str(AUDITED_ROOT),
        'test_year_threshold': TEST_YEAR_THRESHOLD,
        'reaction_split': {
            'train': len(train_data),
            'val': len(val_data),
            'test': len(test_data),
        },
        'feature_dim': 6144,
        'num_classes': {
            'anode': NUM_ELECTRODE_TYPES,
            'cathode': NUM_ELECTRODE_TYPES,
            'cell_type': len(CELL_TYPE_CLASSES),
            **{h: len(vocab[h]) for h in HEADS_SMILES},
        },
        'absent_index': {
            'anode': 22, 'cathode': 22, 'cell_type': 5,
            **{h: 0 for h in HEADS_SMILES},
        },
        'amount_fields': AMOUNT_FIELDS,
    }
    with open(OUT_DIR / 'stats.json', 'w') as f:
        json.dump(stats, f, indent=2)

    split_meta = {
        'test_year_threshold': TEST_YEAR_THRESHOLD,
        'test_papers': sorted([pid for pid, _ in test_papers]),
        'val_papers': sorted([pid for pid, _ in val_papers]),
    }
    with open(OUT_DIR / 'split_meta.json', 'w') as f:
        json.dump(split_meta, f, indent=2)

    print(f"\nSaved everything to {OUT_DIR}")


if __name__ == "__main__":
    main()
