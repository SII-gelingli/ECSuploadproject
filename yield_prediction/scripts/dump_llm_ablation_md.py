"""把 LLM ablation 的 raw_results.json 输出成 per-reaction markdown (A/B/C/GT 并排)."""
import sys, json, re
from pathlib import Path

for _p in (
    '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent',
):
    if _p not in sys.path: sys.path.insert(0, _p)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Reuse the eval_qwen_sft canon_set / compare via importlib trick
import importlib.util as _ilu
def _load(name, p):
    spec = _ilu.spec_from_file_location(name, str(p))
    m = _ilu.module_from_spec(spec); sys.modules[name] = m
    spec.loader.exec_module(m); return m
_en = _load('utils.electrode_normalizer', project_root / 'utils' / 'electrode_normalizer.py')
_eqs = _load('_eval_qwen_sft_mod', project_root / 'scripts' / 'eval_qwen_sft.py')
canon_set = _eqs.canon_set

import argparse as _ap
_argp = _ap.ArgumentParser()
_argp.add_argument('--src', default='llm_ablation_sonnet46_clean')
_args, _ = _argp.parse_known_args()
RAW = project_root.parent / 'eval_results' / _args.src / 'raw_results.json'
OUT_DIR = project_root.parent / 'eval_results' / _args.src / 'per_reaction_md'
OUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_SRC = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')


def build_paper_lookup():
    print(f'Building paper lookup from {RAW_SRC}...')
    lookup = {}
    for jf in RAW_SRC.rglob('*.json'):
        try: d = json.load(open(jf))
        except: continue
        for ri, r in enumerate(d.get('reactions', [])):
            rs = r.get('reactants', []); ps = r.get('products', [])
            if isinstance(rs, list) and rs and isinstance(rs[0], dict):
                rs = [x.get('smiles') for x in rs if isinstance(x, dict) and x.get('smiles')]
            if isinstance(ps, list) and ps and isinstance(ps[0], dict):
                ps = [x.get('smiles') for x in ps if isinstance(x, dict) and x.get('smiles')]
            if not rs or not ps: continue
            key = '.'.join(rs) + '>>' + '.'.join(ps)
            yld_raw = r.get('yield')
            yld_v = None
            if isinstance(yld_raw, dict): yld_v = yld_raw.get('value')
            elif isinstance(yld_raw, (int, float)): yld_v = yld_raw
            elif isinstance(yld_raw, str):
                m = re.search(r'(\d+(?:\.\d+)?)', yld_raw)
                if m: yld_v = float(m.group(1))
            lookup.setdefault(key, []).append((str(jf.relative_to(RAW_SRC)), ri, yld_v))
    print(f'  {len(lookup)} unique reactions in raw')
    return lookup


def fmt_list(x):
    if not x: return '_(empty)_'
    if isinstance(x, str): return f'`{x}`'
    return ' + '.join(f'`{s}`' for s in x)


def fmt_str(x):
    if x is None or x == '': return '_(empty)_'
    return f'`{x}`'


def hit_mark(b): return '✓' if b else '✗'


def field_status_set(gold_list, pred_list):
    g_set = canon_set(gold_list or [])
    p_set = canon_set(pred_list or [])
    if not g_set and not p_set: return '∅(both empty)'
    exact = (g_set == p_set)
    any_ok = bool(g_set & p_set)
    return f'set {hit_mark(exact)} / any {hit_mark(any_ok)}'


def field_status_single(gold, pred):
    """For anode/cathode/cell_type — qwen-eval compare() result is the canonical truth"""
    return hit_mark(pred and str(pred).lower() == str(gold or '').lower())


def render(r, paper_info):
    rxn = r['rxn']
    yld = r.get('yield_gt')
    yld_s = f' yield={yld}%' if yld is not None else ''
    lines = [f'### Reaction #{r["idx"]+1}{yld_s}', '']
    if paper_info:
        p, ri = paper_info
        prel = f'reactions_by_journal_alkene_ec_audited/{p}'
        lines.append(f'**Source paper**: [`{p}`]({prel}) (反应 idx 在该 JSON 内 = #{ri})')
    else:
        lines.append('**Source paper**: _(not found)_')
    lines += ['', '```', rxn[:300] + ('…' if len(rxn) > 300 else ''), '```', '']

    # Retrieval context summary
    lines.append('**Retrieval**: '
                 f'rxn_matches={r.get("n_rxn_matches", 0)}, '
                 f'mech_seed_found={r.get("mech_seed_found")}, '
                 f'mech_seed_excluded={r.get("mech_seed_excluded")}, '
                 f'mech_matches={r.get("mech_n_matches", 0)}')
    lines.append('')

    gold = r.get('gold') or {}
    pA = r.get('A_pred') or {}
    pB = r.get('B_pred') or {}
    pC = r.get('C_pred') or {}

    # 表头
    lines.append('| 字段 | GT | A (pure) | B (+rxn) | C (+rxn+mech) |')
    lines.append('|------|----|----------|----------|---------------|')

    # 单字段(anode/cathode/cell_type)— 复用 compare 结果
    mA = r.get('A_metrics') or {}
    mB = r.get('B_metrics') or {}
    mC = r.get('C_metrics') or {}
    for k in ('anode', 'cathode', 'cell_type'):
        gv = fmt_str(gold.get(k))
        aA = fmt_str(pA.get(k))
        aB = fmt_str(pB.get(k))
        aC = fmt_str(pC.get(k))
        sA = hit_mark(mA.get(k, False))
        sB = hit_mark(mB.get(k, False))
        sC = hit_mark(mC.get(k, False))
        lines.append(f'| {k} | {gv} | {aA} {sA} | {aB} {sB} | {aC} {sC} |')

    # 多元素字段 — 显示 set 命中
    for k in ('electrolytes', 'solvents', 'reagents', 'catalysts', 'ligands', 'additives'):
        gv = fmt_list(gold.get(k, []))
        aA = fmt_list(pA.get(k, []))
        aB = fmt_list(pB.get(k, []))
        aC = fmt_list(pC.get(k, []))
        sA = field_status_set(gold.get(k, []), pA.get(k, []))
        sB = field_status_set(gold.get(k, []), pB.get(k, []))
        sC = field_status_set(gold.get(k, []), pC.get(k, []))
        lines.append(f'| {k} | {gv} | {aA}<br>**{sA}** | {aB}<br>**{sB}** | {aC}<br>**{sC}** |')

    lines += ['', '---', '']
    return '\n'.join(lines)


def main():
    print(f'Loading {RAW}')
    results = json.load(open(RAW))
    print(f'  {len(results)} reactions')

    paper_lookup = build_paper_lookup()

    # Count + filter out failed records (those without 'rxn' key, e.g. process_one crashed)
    n_failed = sum(1 for r in results if r is None or 'rxn' not in r)
    print(f'  failed worker count (will skip): {n_failed} / {len(results)}')

    # Resolve papers
    paper_resolved = []
    for r in results:
        if r is None or 'rxn' not in r:
            paper_resolved.append(None); continue
        matches = paper_lookup.get(r['rxn'], [])
        if not matches:
            paper_resolved.append(None); continue
        yld = r.get('yield_gt')
        if yld is not None and len(matches) > 1:
            best = min(matches, key=lambda x: abs((x[2] or -999) - yld))
            paper_resolved.append((best[0], best[1]))
        else:
            paper_resolved.append((matches[0][0], matches[0][1]))

    # Compute per-reaction interesting flags
    def overall_score(r, grp):
        """Sum of all field hits as a quick score for sorting."""
        if r is None: return 0
        mt = r.get(f'{grp}_metrics') or {}
        s = sum(1 for v in mt.values() if v is True)
        gold = r.get('gold') or {}
        pred = r.get(f'{grp}_pred') or {}
        for k in ('electrolytes', 'solvents', 'reagents', 'catalysts'):
            g_set = canon_set(gold.get(k, []) or [])
            p_set = canon_set(pred.get(k, []) or [])
            if g_set and g_set == p_set: s += 1  # GT 非空 exact set
        return s

    flags = {}
    for r in results:
        if r is None or 'rxn' not in r: continue
        sa, sb, sc = (overall_score(r, g) for g in 'ABC')
        flags[r['idx']] = {'A': sa, 'B': sb, 'C': sc,
                          'mech_helped': sc > sb,
                          'mech_hurt': sc < sb,
                          'rxn_helped': sb > sa,
                          'all_failed': sa == sb == sc == 0}

    # Split into parts (250 / file)
    PER = 200
    n_parts = (len(results) + PER - 1) // PER
    part_files = []
    for p in range(n_parts):
        lo, hi = p * PER, min((p+1)*PER, len(results))
        fname = f'part_{p+1:02d}.md'
        path = OUT_DIR / fname
        part_files.append((fname, lo+1, hi))
        with open(path, 'w') as f:
            f.write(f'# LLM Ablation part {p+1} — reactions {lo+1}-{hi}\n\n')
            f.write('[← back to INDEX](INDEX.md)\n\n')
            for r, pi in zip(results[lo:hi], paper_resolved[lo:hi]):
                if r is None or 'rxn' not in r:
                    continue
                f.write(render(r, pi))
        print(f'  wrote {fname} ({hi-lo} reactions)')

    # Write INDEX
    agg_path = OUT_DIR.parent / 'aggregate.json'
    agg = json.load(open(agg_path)) if agg_path.exists() else None

    with open(OUT_DIR / 'INDEX.md', 'w') as f:
        f.write('# LLM Ablation — Pure vs +Reaction DB vs +Mechanism\n\n')
        f.write(f'**模型**: Claude Sonnet 4.6 (`claude-sonnet-4-6`)\n')
        f.write(f'**样本**: subsample {len(results)} of 2947 test (paper-level 零泄漏 split, seed=42)\n')
        f.write(f'**反应库**: 24,564 反应 / 2617 paper (`reactions_by_journal_alkene_ec_audited/`)\n')
        f.write(f'**机理库**: ~534 paper 机理 JSON (`mechanism_extracts/`)\n')
        f.write(f'**Retrieval**: top-5 相似反应 + top-3 机理 paper, **paper-level 排除 test set 的 118 paper**\n')
        f.write(f'**评测**: 复用 `scripts/eval_qwen_sft.compare()`,canonical SMILES 匹配\n\n')

        if agg:
            f.write('## 三组准确率\n\n')
            f.write('### 整库 exact_set (含 GT=空)\n\n')
            f.write('| 字段 | A pure | B +rxn | C +rxn+mech | B-A | C-B |\n')
            f.write('|------|--------|--------|-------------|-----|-----|\n')
            keys_to_show = ['anode','cathode','cell_type',
                            'electrolytes_exact_set','solvents_exact_set',
                            'reagents_exact_set','catalysts_exact_set']
            for k in keys_to_show:
                a = agg['rates']['A'][k]*100
                b = agg['rates']['B'][k]*100
                c = agg['rates']['C'][k]*100
                f.write(f'| {k} | {a:.1f}% | {b:.1f}% | {c:.1f}% | {b-a:+.1f} | {c-b:+.1f} |\n')

            f.write('\n### GT 非空 + set✓ 真本事(排除 ABSENT 白送)\n\n')
            f.write('| 字段 | GT 非空 | A pure | B +rxn | C +rxn+mech |\n')
            f.write('|------|---------|--------|--------|-------------|\n')
            for fld in ('electrolytes','solvents','reagents','catalysts'):
                nt = agg['nonempty_total'][fld]
                a = agg['nonempty_hit']['A'][fld]
                b = agg['nonempty_hit']['B'][fld]
                c = agg['nonempty_hit']['C'][fld]
                f.write(f'| {fld} | {nt} | {a} ({a/max(nt,1)*100:.1f}%) | '
                        f'{b} ({b/max(nt,1)*100:.1f}%) | {c} ({c/max(nt,1)*100:.1f}%) |\n')

        # Highlights
        f.write('\n## Highlights\n\n')
        mech_helped = sorted([(k, v) for k, v in flags.items() if v['mech_helped']],
                             key=lambda x: -(x[1]['C'] - x[1]['B']))
        mech_hurt = sorted([(k, v) for k, v in flags.items() if v['mech_hurt']],
                           key=lambda x: -(x[1]['B'] - x[1]['C']))
        rxn_helped = sorted([(k, v) for k, v in flags.items() if v['rxn_helped']],
                            key=lambda x: -(x[1]['B'] - x[1]['A']))
        all_failed = [k for k, v in flags.items() if v['all_failed']]

        f.write(f'- **机理帮了 (C > B)**: {len(mech_helped)} 反应\n')
        f.write(f'- **机理害了 (C < B)**: {len(mech_hurt)} 反应\n')
        f.write(f'- **反应库帮了 (B > A)**: {len(rxn_helped)} 反应\n')
        f.write(f'- **三组全错 (A=B=C=0)**: {len(all_failed)} 反应\n\n')

        f.write('### Top 10 机理增益最大的反应\n\n')
        f.write('| reaction # | A score | B score | C score | C-B gain |\n|---|---|---|---|---|\n')
        for k, v in mech_helped[:10]:
            f.write(f'| #{k+1} | {v["A"]} | {v["B"]} | {v["C"]} | +{v["C"]-v["B"]} |\n')

        f.write('\n### Top 10 反应库增益最大的反应\n\n')
        f.write('| reaction # | A score | B score | C score | B-A gain |\n|---|---|---|---|---|\n')
        for k, v in rxn_helped[:10]:
            f.write(f'| #{k+1} | {v["A"]} | {v["B"]} | {v["C"]} | +{v["B"]-v["A"]} |\n')

        f.write('\n## 分文件\n\n')
        for fname, lo, hi in part_files:
            f.write(f'- [Part {fname.split("_")[1].split(".")[0]}: reactions #{lo}-#{hi}]({fname})\n')

        f.write('\n## 字段说明\n\n')
        f.write('- **GT**: paper 真值(`data_audited_v3_clean/test.pt`,canonical SMILES)\n')
        f.write('- **A / B / C**: Claude Sonnet 4.6 在 3 种 prompt 下的输出\n')
        f.write('  - A = 只有反应 SMILES + system prompt\n')
        f.write('  - B = A + top-5 相似反应(reaction_db_paper.pkl,**paper-level 排除 test**)\n')
        f.write('  - C = B + top-3 机理 paper 摘要(mechanism_kb,同样排除 test)\n')
        f.write('- **`set ✓` / `set ✗`**: pred 集合与 GT 集合完全相等(对应千问 `_exact_set`)\n')
        f.write('- **`any ✓`**: pred 与 GT 至少 1 个 SMILES 重合(宽松参考)\n')
        f.write('- **Retrieval 行**:本次反应实际拿到的 retrieval 上下文统计\n')

    print(f'\n[OK] wrote {OUT_DIR}/INDEX.md + {len(part_files)} parts')


if __name__ == '__main__':
    main()
