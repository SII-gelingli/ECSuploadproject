"""
新数据准备脚本：处理 reactions_by_journal_alkene_ec_audited (schema v2)
并以"最新文献"作为测试集进行 paper-level 切分。

- 测试集 = 所有 year >= 2025 的论文（约 3080 条反应，不会跨论文泄漏）
- 训练/验证 = 其余论文，按 paper_id 90/10 划分
- 输出到 yield_prediction/data_audited/
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

import torch
import numpy as np
from tqdm import tqdm

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.feature_extractor import MolecularFeatureExtractor
from utils.electrode_normalizer import electrode_to_id, NUM_ELECTRODE_TYPES


AUDITED_ROOT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited")
OUT_DIR = project_root / "data_audited"


# ---------- 1. 年份提取 ----------

def extract_year(fp_name, doi, src):
    """从 source / DOI / 文件名提取发表年份。失败返回 None。"""
    if isinstance(src, dict):
        y = src.get('year')
        if y:
            try:
                yi = int(str(y)[:4])
                if 1990 <= yi <= 2026:
                    return yi, 'source.year'
            except Exception:
                pass
        cite = src.get('citation') or ''
        m = re.search(r'\b(19|20)(\d{2})\b', cite)
        if m:
            yi = int(m.group(1) + m.group(2))
            if 1990 <= yi <= 2026:
                return yi, 'citation'
    m = re.match(r'^(\d{4})_', fp_name)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'filename_prefix'
    m = re.search(r'_((?:19|20)\d{2})-\d{2}-\d{2}', fp_name)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'patent_date'
    m = re.search(r'(?:WO|US|EP)((?:19|20)\d{2})\d+', fp_name)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'patent_number'
    pool = ((doi or '') + ' ' + fp_name).lower()
    m = re.search(r'10\.1021[_/][a-z.]+\.([0-9])([abc])', pool)
    if m:
        base = {'a': 2000, 'b': 2010, 'c': 2020}[m.group(2)]
        return base + int(m.group(1)), 'acs_doi'
    m = re.search(r'10\.1002[_/][a-z.]+\.(?:e)?(20\d{2})\d{4,6}', pool)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'wiley_doi'
    m = re.search(r'10\.1039[_/]([bcd])(\d)[a-z]+', pool)
    if m:
        base = {'b': 2000, 'c': 2010, 'd': 2020}[m.group(1)]
        yi = base + int(m.group(2))
        if 1990 <= yi <= 2026:
            return yi, 'rsc_doi'
    m = re.search(r'10\.1038[_/]s\d+-0?(\d{2})-', pool)
    if m:
        yy = int(m.group(1))
        yi = 2000 + yy if yy <= 26 else 1900 + yy
        if 1990 <= yi <= 2026:
            return yi, 'nature_doi'
    m = re.search(r's-(00\d{2})-', pool)
    if m:
        yi = 1980 + int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'thieme_doi'
    m = re.search(r'10\.1016[_/]j\.[a-z]+\.(20\d{2})\.', pool)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'elsevier_doi'
    m = re.search(r'10\.1016[_/]s\d{4}-\d{4}\((\d{2})\)', pool)
    if m:
        yy = int(m.group(1))
        yi = 2000 + yy if yy <= 26 else 1900 + yy
        if 1990 <= yi <= 2026:
            return yi, 'elsevier_s_doi'
    m = re.search(r'10\.1007[_/]s\d+-0?(\d{2})-', pool)
    if m:
        yy = int(m.group(1))
        yi = 2000 + yy if yy <= 26 else 1900 + yy
        if 1990 <= yi <= 2026:
            return yi, 'springer_doi'
    m = re.search(r'10\.3390[_/]molecules(\d{2})', pool)
    if m:
        yi = 1995 + int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'mdpi_molecules'
    m = re.search(r'10\.3390[_/]catalysts(\d{2})', pool)
    if m:
        yi = 2010 + int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'mdpi_catalysts'
    m = re.search(r'ccschem\.\d{3}\.(20\d{2})\d+', pool)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'ccschem_doi'
    m = re.search(r'(?:^|[^a-z0-9])a-(\d{4})-\d{4}', pool)
    if m:
        prefix = int(m.group(1)[:2])
        if prefix <= 26:
            return 2000 + prefix, 'thieme_new_doi'
    m = re.search(r'(?:^|[^a-z])(?:ja|ol|jo|ic|or|sc|cm|nl|mp)(\d)([abc])\d{4,5}', pool)
    if m:
        base = {'a': 2000, 'b': 2010, 'c': 2020}[m.group(2)]
        return base + int(m.group(1)), 'acs_legacy'
    after = pool.split('/', 1)[-1] if '/' in pool else pool
    m = re.search(r'(?<!\d)(20[0-2]\d)(?!\d)', after)
    if m:
        yi = int(m.group(1))
        if 1990 <= yi <= 2026:
            return yi, 'doi_year_substr'
    return None, None


# cutoff patterns after which we should strip in _CAS_no_citation filenames
_NOCITE_CUTOFF = re.compile(
    r'(?:_\d+_table|_table|-entry.*|_scope.*|_rxn\d*|_figure.*|_scheme.*|_supp.*).*$',
    re.I,
)


def _extract_embedded_doi(fp_name: str):
    """从 _CAS_no_citation 类文件名中抽出嵌入式 DOI.

    文件名格式举例:
      'no-citation-extracted-reaction_00098_SI_10.1002_anie.201912119_19_table_0_3_rxn0.json'
        → '10.1002_anie.201912119'
      'no-citation-article-10.1021_jacs.0c11214_2_scope_0-entry22-rxn1.json'
        → '10.1021_jacs.0c11214'
    返回 None 表示无法识别.
    """
    if not fp_name: return None
    s = re.sub(r'\.json$', '', fp_name).lower()
    m = re.search(r'(10\.\d{4,5}_\S+)', s)
    if not m: return None
    s = m.group(1)
    s = _NOCITE_CUTOFF.sub('', s)
    # 剥末尾 _XX (1-3 位 table/scope 数字), 但保留 DOI 内部连字符数字段
    s = re.sub(r'_\d{1,3}$', '', s)
    return s if s.startswith('10.') else None


def paper_id(doi, fp_name):
    """生成 paper-level ID：去除 SI 标记、page/table 后缀，使同一篇论文的多张表合并。

    优先级:
      1) source.doi 字段非空 → 用 DOI (剥 SI 后缀)
      2) 文件名里嵌了 DOI (_CAS_no_citation/ 目录) → 用嵌入式 DOI
      3) 兜底: 用 filename stem

    注意: 单纯靠 (doi, fp_name) 无法识别"同一篇 paper 既有 DOI 文件又有无 DOI 文件"
    的双身份场景 (Wiley 系 EurJOC / Angew / AdvSynthCatal / ChemSusChem 等).
    要消除该泄漏请用 canonical_paper_id(doi, fp_name, alias_table), 配合
    build_paper_alias_table() 一起用.
    """
    if doi:
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_supplementary.*|_si1|si_1)$', '', doi.lower())
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_si1|si_1)', '', pid)
        return pid
    # 文件名嵌入式 DOI (_CAS_no_citation 这种)
    embedded = _extract_embedded_doi(fp_name)
    if embedded:
        return embedded
    base = re.sub(r'\.json$', '', fp_name)
    base = re.sub(r'_p\d+_t\d+.*$', '', base)
    base = re.sub(r'(_sup_?\d*|_si_?\d*|_supl_?\d*|_si1|si_1)', '', base)
    return base.lower()


# ── 双身份 paper 合并: 从 article number token 反查 canonical pid ──

def _article_number_token(s: str):
    """从 DOI 或 filename 抽取 publisher-issued article number, 用于跨身份匹配.

    返回标准化的"末尾数字串", 不含期刊前缀:
      '10.1002_anie.202425634' -> '202425634'
      '10.1002_anie.202425634_sup_1' -> '202425634'
      '2025_angewandte_chemie_int_ed_2025_64_9_e202425634' -> '202425634'
      'EurJOC/10.1002_ejoc.202400351_p2_t0.json' -> '202400351'
      'Synlett/10.1055_s-0041-1738439.json' -> '00411738439'  (s-XXXX-XXXXXXX)
    """
    if not s: return None
    s = s.lower()
    s = re.sub(r'\.json$', '', s)
    # 剥掉 _sup_, _si_, _supplementary_, _p#_t# 等后缀
    s = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_supplementary.*|_si1|si_1).*$', '', s)
    s = re.sub(r'_p\d+_t\d+.*$', '', s)
    # Wiley publisher prefixes: ejoc/anie/ange/chem/adsc/cssc/slct/asia/ajoc/cctc/ardp 等
    m = re.search(
        r'(?:^|[\._/])(?:e|ejoc\.|anie\.|ange\.|chem\.|adsc\.|cssc\.|slct\.|asia\.|ajoc\.|cctc\.|ardp\.)(20\d{7})(?:$|[^\d])',
        s,
    )
    if m: return m.group(1)
    # Wiley legacy 6-7 digit (rare, 安全网)
    m = re.search(r'(?:^|[\._/])e(20\d{6})(?:$|[^\d])', s)
    if m: return m.group(1)
    # Thieme Synlett: s-0041-1738439
    m = re.search(r's\-?(\d{4})\-(\d{6,})', s)
    if m: return m.group(1) + m.group(2)
    # ACS legacy + new: acs.orglett.4c04041 (年份编码在第二段)
    m = re.search(r'acs\.\w+\.(\d{1,2}[a-z]\d{4,5})', s)
    if m: return m.group(1)
    return None


# Wiley DOI 期刊后缀 → article token 反查时构造的 canonical DOI 前缀
_WILEY_JOURNAL_TO_DOI_PREFIX = {
    'eurjoc': '10.1002_ejoc.',
    'angew': '10.1002_anie.',
    'chemistry': '10.1002_chem.',
    'advsynthcatal': '10.1002_adsc.',
    'chemsuschem': '10.1002_cssc.',
    'chemasianj': '10.1002_asia.',
    'asianjoc': '10.1002_ajoc.',
    'slct': '10.1002_slct.',
    'chemcatchem': '10.1002_cctc.',
    'chemistryselect': '10.1002_slct.',
}


def build_paper_alias_table(raw_dir):
    """扫一遍 raw_dir, 返回 {old_pid: canonical_pid} 用于合并双身份 paper.

    规则:
      - 对每个文件计算 (journal, article_number_token) 元组
      - 若同一元组下既有 DOI 一侧文件又有无 DOI 文件, 把无 DOI 一侧的 old_pid
        映射到 DOI 一侧的 pid (= canonical)
      - 若同一元组下只有无 DOI 文件, 但 article_token 能识别期刊, 则
        构造 canonical DOI-style pid 作为合并键

    返回 dict 可以传给 canonical_paper_id().
    """
    from collections import defaultdict
    import json as _json
    from pathlib import Path as _Path

    raw_dir = _Path(raw_dir)
    by_key = defaultdict(list)
    for fp in raw_dir.rglob('*.json'):
        try:
            with open(fp) as f: d = _json.load(f)
        except Exception:
            continue
        src = d.get('source') or {}
        if not isinstance(src, dict): src = {}
        doi = src.get('doi', '') or ''
        journal = (src.get('journal', '') or '').lower()
        tok = _article_number_token(doi) if doi else _article_number_token(fp.name)
        if not tok: continue
        old_pid = paper_id(doi, fp.name)
        by_key[(journal, tok)].append((doi, fp.name, old_pid))

    alias = {}
    for (journal, tok), entries in by_key.items():
        doi_entries = [e for e in entries if e[0]]
        if doi_entries:
            # 已有 DOI 文件: 用其 pid 作 canonical
            canonical = doi_entries[0][2]
        elif journal in _WILEY_JOURNAL_TO_DOI_PREFIX:
            # 无 DOI 但可构造 canonical
            canonical = _WILEY_JOURNAL_TO_DOI_PREFIX[journal] + tok
        else:
            # 只有无 DOI 文件且期刊不可识别: 不合并
            continue
        for doi, fname, old_pid in entries:
            if old_pid != canonical:
                alias[old_pid] = canonical
    return alias


def canonical_paper_id(doi, fp_name, alias_table=None):
    """paper_id() 的增强版本, 用 alias_table 合并跨身份 paper."""
    pid = paper_id(doi, fp_name)
    if alias_table:
        return alias_table.get(pid, pid)
    return pid


# ---------- 2. 反应解析 ----------

def parse_yield_string(s):
    """解析产率字符串为 float。无法解析返回 None。"""
    if not s:
        return None
    val = str(s).strip().lower().replace('％', '%').replace(' ', '')
    if val in ('', '-', 'n.d.', 'nd', 'n.d', 'n.r.', 'nr', 'n.r'):
        return None
    if val in ('trace', 'traces'):
        return 0.5
    if val.startswith('<') or val.startswith('＜'):
        try:
            num = float(val.lstrip('<＜').rstrip('%'))
            return num / 2.0
        except (ValueError, TypeError):
            return None
    if '-' in val[1:] and '%' in val:
        try:
            parts = val.rstrip('%').split('-')
            return (float(parts[0]) + float(parts[1])) / 2.0
        except (ValueError, TypeError, IndexError):
            return None
    try:
        return float(val.rstrip('%'))
    except (ValueError, TypeError):
        return None


def convert_v2_reaction(rxn):
    """将 v2 schema 单个反应转成训练管线期望的 dict 格式。

    返回 None 表示数据不可用（缺反应物/产物/产率）。
    """
    reactants = [r for r in (rxn.get('reactants') or []) if isinstance(r, dict)]
    products = [p for p in (rxn.get('products') or []) if isinstance(p, dict)]
    if not reactants or not products:
        return None
    r_smiles = [r.get('smiles') for r in reactants if r.get('smiles')]
    p_smiles = [p.get('smiles') for p in products if p.get('smiles')]
    if not r_smiles or not p_smiles:
        return None

    # 选取首个能解析的产物产率
    yield_val = None
    for p in products:
        yv = parse_yield_string(p.get('yield'))
        if yv is not None:
            yield_val = yv
            break
    if yield_val is None:
        return None
    yield_val = max(0.0, min(100.0, yield_val))

    # 抽取电化学参数（v2 嵌套在 conditions.electrochemistry）
    conditions = rxn.get('conditions') or {}
    ec = (conditions.get('electrochemistry') or {}) if isinstance(conditions, dict) else {}

    # 电解质：v2 有顶层 electrolytes 列表，优先取第一个 SMILES，否则用 ec.electrolyte 字符串（虽然多半不是 SMILES）
    electrolyte_smiles = ''
    elist = rxn.get('electrolytes') or []
    for e in elist:
        sm = e.get('smiles') if isinstance(e, dict) else None
        if sm:
            electrolyte_smiles = sm
            break

    def smiles_list(key):
        return [
            {'smiles': item.get('smiles')}
            for item in (rxn.get(key) or [])
            if isinstance(item, dict) and item.get('smiles')
        ]
    out = {
        'reactants': [{'smiles': s} for s in r_smiles],
        'products': [{'smiles': s} for s in p_smiles],
        'solvents': smiles_list('solvents'),
        'reagents': smiles_list('reagents'),
        'catalysts': smiles_list('catalysts'),
        'additives': smiles_list('additives'),
        'electrochemistry_params': {
            'anode': ec.get('anode') or '',
            'cathode': ec.get('cathode') or '',
            'cell_type': ec.get('cell_type') or '',
            'electrolyte': electrolyte_smiles,
            'current': ec.get('current') or '',
            'current_density': ec.get('current_density') or '',
            'potential': ec.get('potential') or '',
        },
        'reaction_smiles': rxn.get('reaction_smiles', ''),
        'yield_value': yield_val,
        'product_yield': str(yield_val),
    }
    return out


# ---------- 3. 词表与编码 ----------

def encode_cell_type(cell_type):
    if cell_type is None or str(cell_type).strip() == '':
        return 5
    ct = str(cell_type).lower().strip().strip('"\'()')
    if any(k in ct for k in ('undivi', 'undvi', 'udivi', 'unndiv', 'undiv')):
        return 0
    if any(k in ct for k in ('beaker', 'electrasyn', 'three-neck', 'bottle', 'flask', 'schlenk')):
        return 0
    if any(k in ct for k in ('h-cell', 'h-type', 'h cell', 'diaphragm', 'two-compartment', 'compartment')):
        return 1
    if 'divided' in ct or 'devided' in ct or 'separation' in ct or 'ex-cell' in ct:
        return 1
    if 'flow' in ct or 'vapourtec' in ct:
        return 2
    if 'sealed' in ct:
        return 3
    if 'electrochem' in ct or 'electrolysis' in ct or 'electrolytic' in ct or 'reactor' in ct:
        return 4
    return 5


NUM_CELL_TYPE_CLASSES = 6


def build_vocab(reactions):
    electrolytes = Counter()
    solvents = Counter()
    reagents = Counter()
    catalysts = Counter()
    for rxn in reactions:
        ec = rxn.get('electrochemistry_params', {})
        e = ec.get('electrolyte', '')
        if e:
            electrolytes[e] += 1
        for s in rxn.get('solvents', []):
            sm = s.get('smiles', '')
            if sm:
                solvents[sm] += 1
        for r in rxn.get('reagents', []):
            sm = r.get('smiles', '')
            if sm:
                reagents[sm] += 1
        for c in rxn.get('catalysts', []):
            sm = c.get('smiles', '')
            if sm:
                catalysts[sm] += 1
    return {
        'electrolyte': {e: i + 1 for i, (e, _) in enumerate(electrolytes.most_common())},
        'solvent': {s: i + 1 for i, (s, _) in enumerate(solvents.most_common())},
        'reagent': {r: i + 1 for i, (r, _) in enumerate(reagents.most_common())},
        'catalyst': {c: i + 1 for i, (c, _) in enumerate(catalysts.most_common())},
    }


def featurize(rxn, mol_extractor, vocab):
    r_smiles = [r.get('smiles', '') for r in rxn.get('reactants', [])]
    p_smiles = [p.get('smiles', '') for p in rxn.get('products', [])]
    reactant_fp = mol_extractor.encode_molecules(r_smiles)
    product_fp = mol_extractor.encode_molecules(p_smiles)
    reactant_t = torch.tensor(reactant_fp, dtype=torch.float32)
    product_t = torch.tensor(product_fp, dtype=torch.float32)
    diff_t = torch.abs(product_t - reactant_t)

    solvent_smiles = [s.get('smiles', '') for s in rxn.get('solvents', [])]
    solvent_fp = mol_extractor.encode_molecules(solvent_smiles)

    ec = rxn.get('electrochemistry_params', {})
    electrolyte_smiles = ec.get('electrolyte', '')
    electrolyte_fp = (
        mol_extractor.get_morgan_fingerprint(electrolyte_smiles).tolist()
        if electrolyte_smiles
        else [0] * 2048
    )

    anode = electrode_to_id(ec.get('anode', ''))
    cathode = electrode_to_id(ec.get('cathode', ''))
    cell_type = encode_cell_type(ec.get('cell_type', ''))
    electrolyte_label = vocab['electrolyte'].get(electrolyte_smiles, 0)

    solvent_label = 0
    if solvent_smiles:
        solvent_label = vocab['solvent'].get(solvent_smiles[0], 0)

    reagent_label = 0
    reagents_list = rxn.get('reagents', [])
    if reagents_list:
        reagent_label = vocab['reagent'].get(reagents_list[0].get('smiles', ''), 0)

    catalyst_label = 0
    catalysts_list = rxn.get('catalysts', [])
    if catalysts_list:
        catalyst_label = vocab['catalyst'].get(catalysts_list[0].get('smiles', ''), 0)

    return {
        'reactant_fp': reactant_t.tolist(),
        'product_fp': product_t.tolist(),
        'diff_fp': diff_t.tolist(),
        'solvent_fp': list(solvent_fp),
        'electrolyte_fp': list(electrolyte_fp),
        'anode': anode,
        'cathode': cathode,
        'cell_type': cell_type,
        'electrolyte_label': electrolyte_label,
        'solvent_label': solvent_label,
        'reagent_label': reagent_label,
        'catalyst_label': catalyst_label,
        'yield': rxn.get('yield_value', 0.0),
        'reactant_smiles': r_smiles,
        'product_smiles': p_smiles,
    }


# ---------- 4. 主流程 ----------

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(AUDITED_ROOT.rglob('*.json'))
    print(f"Found {len(files)} JSON files under {AUDITED_ROOT}")

    # Step 1: 解析+分组 paper -> reactions (含 year)
    papers = defaultdict(lambda: {'year': None, 'reactions': []})
    year_kind_counter = Counter()
    skip_stats = Counter()
    for fp in tqdm(files, desc="Loading v2 audited JSONs"):
        try:
            with open(fp) as f:
                d = json.load(f)
        except Exception:
            skip_stats['load_fail'] += 1
            continue
        src = d.get('source') or {}
        doi = src.get('doi') or ''
        y, kind = extract_year(fp.name, doi, src if isinstance(src, dict) else {})
        if kind:
            year_kind_counter[kind] += 1
        pid = paper_id(doi, fp.name)
        p = papers[pid]
        if y is not None and (p['year'] is None or y > p['year']):
            p['year'] = y
        for rxn in d.get('reactions', []):
            conv = convert_v2_reaction(rxn)
            if conv is None:
                skip_stats['unconvertible'] += 1
                continue
            p['reactions'].append(conv)

    print(f"\nUnique papers: {len(papers)}")
    print(f"Total reactions kept: {sum(len(p['reactions']) for p in papers.values())}")
    print(f"Skip stats: {dict(skip_stats)}")
    print(f"Year extraction sources (top 8):")
    for k, c in year_kind_counter.most_common(8):
        print(f"  {k}: {c}")

    # Step 2: paper-level 切分（test = year >= 2025）
    TEST_YEAR_THRESHOLD = 2025
    test_papers = []
    rest_papers = []
    no_year_papers = []
    for pid, p in papers.items():
        if p['year'] is None:
            no_year_papers.append((pid, p))
        elif p['year'] >= TEST_YEAR_THRESHOLD:
            test_papers.append((pid, p))
        else:
            rest_papers.append((pid, p))
    # no-year papers default to training
    rest_papers.extend(no_year_papers)

    # 训练/验证再按 paper-level 9:1
    random.seed(42)
    random.shuffle(rest_papers)
    n_val = max(1, len(rest_papers) // 10)
    val_papers = rest_papers[:n_val]
    train_papers = rest_papers[n_val:]

    def flatten(plist):
        out = []
        for _, p in plist:
            out.extend(p['reactions'])
        return out

    train_rxns = flatten(train_papers)
    val_rxns = flatten(val_papers)
    test_rxns = flatten(test_papers)
    print(f"\nPaper-level split:")
    print(f"  train: {len(train_papers)} papers, {len(train_rxns)} reactions")
    print(f"  val:   {len(val_papers)} papers, {len(val_rxns)} reactions")
    print(f"  test:  {len(test_papers)} papers, {len(test_rxns)} reactions  (year >= {TEST_YEAR_THRESHOLD})")

    # Step 3: 词表用全部数据构建（包括 val/test）
    # 词表是"可推荐条件池"，不是特征——推理时希望能从所有已知条件里选。
    # 模型对训练未见过的条件预测能力差，但至少它在候选集中。
    all_rxns = train_rxns + val_rxns + test_rxns
    vocab = build_vocab(all_rxns)
    print(f"\nVocab sizes (built from train+val+test):")
    for k, v in vocab.items():
        print(f"  {k}: {len(v)}")
    with open(OUT_DIR / 'vocab.json', 'w') as f:
        json.dump(vocab, f, indent=2)

    # Step 4: 特征提取并保存
    mol_extractor = MolecularFeatureExtractor(fingerprint_size=2048)

    def process(rxns, name):
        out = []
        for rxn in tqdm(rxns, desc=f"Featurize {name}"):
            try:
                out.append(featurize(rxn, mol_extractor, vocab))
            except Exception:
                continue
        return out

    train_data = process(train_rxns, 'train')
    val_data = process(val_rxns, 'val')
    test_data = process(test_rxns, 'test')

    torch.save(train_data, OUT_DIR / 'train.pt')
    torch.save(val_data, OUT_DIR / 'val.pt')
    torch.save(test_data, OUT_DIR / 'test.pt')

    stats = {
        'source_root': str(AUDITED_ROOT),
        'test_year_threshold': TEST_YEAR_THRESHOLD,
        'total_papers': len(papers),
        'paper_split': {
            'train': len(train_papers),
            'val': len(val_papers),
            'test': len(test_papers),
        },
        'reaction_split': {
            'train': len(train_data),
            'val': len(val_data),
            'test': len(test_data),
        },
        'feature_dims': {
            'reaction_fp': 2048 * 3,
            'solvent_fp': 2048,
            'electrolyte_fp': 2048,
            'total': 2048 * 5 + 6,
        },
        'num_classes': {
            'anode': NUM_ELECTRODE_TYPES,
            'cathode': NUM_ELECTRODE_TYPES,
            'cell_type': NUM_CELL_TYPE_CLASSES,
            'electrolyte': len(vocab['electrolyte']) + 1,
            'solvent': len(vocab['solvent']) + 1,
            'reagent': len(vocab['reagent']) + 1,
            'catalyst': len(vocab['catalyst']) + 1,
        },
    }
    with open(OUT_DIR / 'stats.json', 'w') as f:
        json.dump(stats, f, indent=2)

    # 同时记录 paper-level 切分元数据，便于复现
    split_meta = {
        'test_year_threshold': TEST_YEAR_THRESHOLD,
        'test_papers': sorted([pid for pid, _ in test_papers]),
        'val_papers': sorted([pid for pid, _ in val_papers]),
    }
    with open(OUT_DIR / 'split_meta.json', 'w') as f:
        json.dump(split_meta, f, indent=2)

    print(f"\nSaved to {OUT_DIR}")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
