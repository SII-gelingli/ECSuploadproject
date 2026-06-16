"""Build mechanism retrieval KB.

输入:
- 535 个 mechanism JSON (data/mechanism_extracts/<Journal>/<doi>.json)
- ~2617 个 raw reaction JSON (reactions_by_journal_alkene_ec_audited/<Journal>/<file>.json)

输出 (写到 data/mechanism_kb/):
- index.json          每篇 paper 的机理记录 (doi → record)
- rxn2doi.json        reaction_smiles → [doi, ...]  (从 raw reaction 取 source.doi)
- tfidf_vectorizer.pkl   sklearn TfidfVectorizer fit 在所有 paper 的机理文本上
- text_vectors.npz    每篇 paper 的 TF-IDF 向量 (用于文本相似度)
- doi_order.json      paper 顺序列表, 和 text_vectors 行号对应
"""
import sys, json, re, pickle
from pathlib import Path
from collections import defaultdict

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

PROJECT_ROOT = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2')
MECH_DIR = PROJECT_ROOT / 'condition_agent/data/mechanism_extracts'
RAW_DIR = PROJECT_ROOT / 'reactions_by_journal_alkene_ec_audited'
OUT_DIR = PROJECT_ROOT / 'condition_agent/data/mechanism_kb'


SUFFIX_STRIP = re.compile(r'(_sup_?\d*|_supl_?\d*|_si_?\d*|_esi_?\d*|_sm_?\d*)$', re.I)


def base_doi(doi: str) -> str:
    """去掉 _sup_1 / _si_2 等附件后缀, 拿主文 DOI"""
    if not doi: return ''
    return SUFFIX_STRIP.sub('', doi)


def build_mechanism_index():
    """扫 mechanism_extracts 建 {doi: record}, 同时记录 base_doi → [all variants]"""
    records = {}
    base_map = defaultdict(list)
    for jf in MECH_DIR.rglob('*.json'):
        try:
            d = json.load(open(jf))
        except Exception:
            continue
        doi = d.get('doi', '').strip()
        if not doi: continue
        # 跳过 review 综述
        if d.get('is_review'): continue
        records[doi] = {
            'doi': doi,
            'journal': d.get('journal', ''),
            'rxn_class_summary': d.get('rxn_class_summary') or '',
            'mechanism_family': d.get('mechanism_family') or [],
            'electrochemical_role': d.get('electrochemical_role') or '',
            'electron_flow': d.get('electron_flow') or '',
            'rate_determining_step': d.get('rate_determining_step') or '',
            'key_intermediates': d.get('key_intermediates') or [],
            'probe_reagents': d.get('probe_reagents') or [],
            'evidence_types_used': d.get('evidence_types_used') or [],
            'evidence_strength': d.get('evidence_strength') or '',
            'notes': d.get('notes') or '',
        }
        base_map[base_doi(doi)].append(doi)
    print(f'Mechanism index: {len(records)} non-review papers '
          f'({len(base_map)} unique base DOIs)')
    return records, dict(base_map)


def build_rxn2doi():
    """扫 raw reaction JSON 建 {reaction_smiles: [doi, ...]}"""
    rxn2doi = defaultdict(set)
    n_files = 0
    n_no_doi = 0
    for jf in RAW_DIR.rglob('*.json'):
        try:
            d = json.load(open(jf))
        except Exception:
            continue
        n_files += 1
        src = d.get('source', {})
        doi = src.get('doi') if isinstance(src, dict) else None
        if not doi:
            n_no_doi += 1
            continue
        for r in d.get('reactions', []):
            rs = r.get('reactants', []); ps = r.get('products', [])
            if isinstance(rs, list) and rs and isinstance(rs[0], dict):
                rs = [x.get('smiles') for x in rs if isinstance(x, dict) and x.get('smiles')]
            if isinstance(ps, list) and ps and isinstance(ps[0], dict):
                ps = [x.get('smiles') for x in ps if isinstance(x, dict) and x.get('smiles')]
            if not rs or not ps: continue
            key = '.'.join(rs) + '>>' + '.'.join(ps)
            rxn2doi[key].add(doi)
    print(f'rxn2doi: {n_files} files scanned, {n_no_doi} without DOI; '
          f'{len(rxn2doi)} unique reaction SMILES')
    return {k: sorted(v) for k, v in rxn2doi.items()}


def make_text_blob(record: dict) -> str:
    """把一篇 paper 的机理字段拼成一段文本, 给 TF-IDF 用"""
    parts = [
        record.get('rxn_class_summary', ''),
        record.get('electrochemical_role', ''),
        record.get('electron_flow', ''),
        record.get('rate_determining_step', ''),
        record.get('notes', ''),
    ]
    # key intermediates 名字也加进来 (中间体 motif 是机理特征)
    for ki in record.get('key_intermediates') or []:
        if isinstance(ki, dict):
            parts.append(ki.get('name', '') or '')
    # 把 family 名字拼进文本, 让其也参与 TF-IDF (家族名也是好的文本特征)
    parts.extend(record.get('mechanism_family') or [])
    parts.extend(record.get('evidence_types_used') or [])
    return ' '.join(p for p in parts if p).strip()


def build_tfidf(records: dict):
    """fit TF-IDF + 计算每篇 paper 的向量"""
    doi_order = list(records.keys())
    docs = [make_text_blob(records[d]) for d in doi_order]
    # 同时用 1-gram 和 2-gram. min_df=2 去掉只出现一次的怪词. stop words 用英文.
    vec = TfidfVectorizer(
        max_features=15000,
        ngram_range=(1, 2),
        min_df=2, max_df=0.9,
        stop_words='english',
        lowercase=True,
    )
    X = vec.fit_transform(docs)
    print(f'TF-IDF: {X.shape[0]} docs × {X.shape[1]} features '
          f'(avg doc length {np.mean([len(d.split()) for d in docs]):.0f} tokens)')
    return doi_order, vec, X


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print('=== Step 1: parse mechanism extracts ===')
    records, base_map = build_mechanism_index()

    print('\n=== Step 2: build reaction → DOI lookup ===')
    rxn2doi = build_rxn2doi()

    # 估一下耦合率: 多少 raw reaction 能找到至少 1 篇 mechanism paper
    mech_dois = set(records.keys())
    mech_base = set(base_map.keys())
    n_hit, n_hit_base = 0, 0
    for rxn, dois in rxn2doi.items():
        if any(d in mech_dois for d in dois):
            n_hit += 1
        elif any(base_doi(d) in mech_base for d in dois):
            n_hit_base += 1
    pct1 = n_hit / max(len(rxn2doi), 1) * 100
    pct2 = (n_hit + n_hit_base) / max(len(rxn2doi), 1) * 100
    print(f'\nCoverage:')
    print(f'  reactions with direct DOI mechanism: {n_hit}/{len(rxn2doi)} ({pct1:.1f}%)')
    print(f'  +reactions with base-DOI fallback:   +{n_hit_base} ({pct2:.1f}% total)')

    print('\n=== Step 3: build TF-IDF text vectors ===')
    doi_order, vectorizer, X = build_tfidf(records)

    # === 写文件 ===
    (OUT_DIR / 'index.json').write_text(
        json.dumps(records, ensure_ascii=False, indent=2)
    )
    (OUT_DIR / 'rxn2doi.json').write_text(
        json.dumps(rxn2doi, ensure_ascii=False)
    )
    (OUT_DIR / 'base_map.json').write_text(
        json.dumps(base_map, ensure_ascii=False, indent=2)
    )
    (OUT_DIR / 'doi_order.json').write_text(
        json.dumps(doi_order, ensure_ascii=False)
    )
    with open(OUT_DIR / 'tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    # 用 npz 保存稀疏矩阵 (csr)
    from scipy.sparse import save_npz
    save_npz(OUT_DIR / 'text_vectors.npz', X)

    print(f'\n✓ Wrote KB to {OUT_DIR}')
    for p in sorted(OUT_DIR.iterdir()):
        sz = p.stat().st_size
        print(f'  {p.name}  ({sz/1024:.1f} KB)')


if __name__ == '__main__':
    main()
