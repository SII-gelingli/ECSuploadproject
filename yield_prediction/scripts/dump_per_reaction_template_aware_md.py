"""Per-reaction template-aware MD: rxn + GT + winning pool + A/B/C pred + match status."""
import sys, json, argparse
from pathlib import Path
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')

import importlib.util as _ilu
spec = _ilu.spec_from_file_location('utils.electrode_normalizer',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/utils/electrode_normalizer.py')
m = _ilu.module_from_spec(spec); sys.modules['utils.electrode_normalizer'] = m; spec.loader.exec_module(m)
spec = _ilu.spec_from_file_location('_eqs',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/scripts/eval_qwen_sft.py')
m = _ilu.module_from_spec(spec); sys.modules['_eqs'] = m; spec.loader.exec_module(m)
canon_set = m.canon_set


def fmt_list(x):
    if not x: return '_(empty)_'
    if isinstance(x, str): return f'`{x}`'
    return ' + '.join(f'`{s}`' for s in (x[:6] if len(x) > 6 else x)) + (' …' if len(x) > 6 else '')


def fmt_winning_pool(winners, n=5):
    """Format the winning conditions pool for a field. Show up to n variants."""
    if not winners: return '_(no winners)_'
    variants = winners[:n]
    lines = []
    for i, v in enumerate(variants):
        lines.append(f'  {i+1}. {fmt_list(v)}')
    if len(winners) > n:
        lines.append(f'  …({len(winners)-n} more variants)')
    return '<br>'.join(lines)


def hit_mark(b): return '✓' if b else '✗'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, help='subdir under eval_results/ (LLM ablation output dir)')
    ap.add_argument('--tag', required=True, help='short label, used in title and out dir name')
    args = ap.parse_args()

    src_dir = Path(f'eval_results/{args.src}')
    raw = json.load(open(src_dir / 'raw_results.json'))
    sig_winners = json.load(open('eval_results/template_analysis/rc_sig_winners.json'))
    rec_sigs = json.load(open('eval_results/template_analysis/records_with_rc_sig.json'))

    # Build rxn → sig_key (test side first)
    rxn2sig = {}
    for r in rec_sigs:
        if r.get('in_test') and r.get('rc_sig_key'):
            rxn2sig.setdefault(r['rxn'], r['rc_sig_key'])

    out_dir = src_dir / 'per_reaction_template_aware_md'
    out_dir.mkdir(exist_ok=True)

    # Build per-reaction info
    list_fields = ('electrolytes','solvents','reagents','catalysts')
    items = []
    for r in raw:
        if not r or 'rxn' not in r: continue
        sig_key = rxn2sig.get(r['rxn'])
        winners = sig_winners.get(sig_key) if sig_key else None
        items.append({'rec': r, 'sig_key': sig_key, 'winners': winners})

    # Statistics
    total = len(items)
    eligible = sum(1 for it in items if it['winners'])
    print(f'Total LLM raw: {total}, eligible (sig in train winners): {eligible}')

    # Group by part files (200/file)
    PART = 200
    n_parts = (total + PART - 1) // PART
    part_files = []

    for p in range(n_parts):
        lo = p * PART; hi = min(lo + PART, total)
        fname = f'part_{p+1:02d}.md'
        path = out_dir / fname
        part_files.append((fname, lo+1, hi))
        with open(path, 'w') as f:
            f.write(f'# {args.tag} — Per-reaction template-aware view part {p+1} (rxns #{lo+1}-#{hi})\n\n')
            f.write('[← INDEX](INDEX.md)\n\n')
            for i, it in enumerate(items[lo:hi], start=lo+1):
                r = it['rec']
                winners = it['winners']
                gold = r.get('gold') or {}
                rxn = r.get('rxn', '')
                yld = r.get('yield_gt')
                yld_s = f' yield={yld}%' if yld is not None else ''
                f.write(f'### Reaction #{i}{yld_s}\n\n')
                f.write(f'```\n{rxn[:280] + ("…" if len(rxn) > 280 else "")}\n```\n\n')
                if winners is None:
                    f.write(f'⚠️ **No same-signature precedent in train** (novel-chemistry reaction → template-aware metric not applicable)\n\n')
                else:
                    f.write(f'**Template cluster**: {winners.get("n_train_rxns", "?")} train rxns, '
                            f'{winners.get("n_high_yield", "?")} yield>50% (winning examples)\n\n')

                # Table: per-field GT / winning pool / A/B/C pred / match status
                f.write('| Field | GT | Winning Pool (train, top 5 variants) | A pure | B +rxn | C +rxn+mech |\n')
                f.write('|-------|----|-------------------------------------|--------|--------|-------------|\n')
                for fld in list_fields:
                    gold_set = canon_set(gold.get(fld, []) or [])
                    pool = (winners or {}).get(fld, []) if winners else []
                    pool_frozensets = [frozenset(v) for v in pool]
                    gt_in_pool = bool(gold_set) and frozenset(gold_set) in pool_frozensets
                    gt_disp = fmt_list(gold.get(fld, []) or [])
                    if gt_in_pool: gt_disp += ' 🏆'
                    pool_disp = fmt_winning_pool(pool) if pool else '_(no winners)_'

                    cells = []
                    for grp in 'ABC':
                        pred_set = canon_set((r.get(f'{grp}_pred') or {}).get(fld, []) or [])
                        pred_disp = fmt_list((r.get(f'{grp}_pred') or {}).get(fld, []) or []) if pred_set else '_(empty)_'
                        # 3 marks: hit in winners, overlap, exact GT
                        if winners and pool_frozensets and pred_set:
                            hit_w = frozenset(pred_set) in pool_frozensets
                            union = set()
                            for v in pool: union |= set(v)
                            ov = bool(pred_set & union)
                        else:
                            hit_w = False; ov = False
                        exact = bool(gold_set) and frozenset(pred_set) == frozenset(gold_set)
                        marks = []
                        marks.append(f'set:{hit_mark(hit_w)}' if winners else 'set:-')
                        marks.append(f'overlap:{hit_mark(ov)}' if winners else 'overlap:-')
                        marks.append(f'GT:{hit_mark(exact)}')
                        cells.append(f'{pred_disp}<br>**{" / ".join(marks)}**')
                    f.write(f'| {fld} | {gt_disp} | {pool_disp} | {cells[0]} | {cells[1]} | {cells[2]} |\n')
                f.write('\n---\n\n')
        print(f'  wrote {fname} ({hi-lo} reactions)')

    # INDEX
    with open(out_dir / 'INDEX.md', 'w') as f:
        f.write(f'# {args.tag} — Per-reaction template-aware comparison\n\n')
        f.write(f'**Source**: `eval_results/{args.src}/raw_results.json` ({total} LLM rows)\n')
        f.write(f'**Eligible** (sig has train winners): **{eligible}** ({eligible/total*100:.1f}%)\n')
        f.write(f'**Methodology**: see `../../template_analysis/WINNING_CONDITIONS_METHODOLOGY.md`\n\n')

        f.write('## Field markers per cell\n\n')
        f.write('Each LLM pred cell has 3 status marks:\n\n')
        f.write('- **`set:✓`** = LLM pred matches ANY winning variant in pool (= template-aware hit, **main fair metric**)\n')
        f.write('- **`overlap:✓`** = LLM pred shares ≥1 SMILES with the union of all winners (looser)\n')
        f.write('- **`GT:✓`** = LLM pred exactly equals the GT set (strict / old metric)\n\n')
        f.write('GT 旁 🏆 表示该 GT 本身就在 winning pool 里(yield>50% 已知有效)\n\n')

        f.write('## Files\n\n')
        for fname, lo, hi in part_files:
            f.write(f'- [Part {fname[5:7]}: reactions #{lo}-#{hi}]({fname})\n')

    print(f'\n[OK] wrote {out_dir}/INDEX.md + {len(part_files)} parts')


if __name__ == '__main__':
    main()
