"""Radius-1 template-aware re-evaluation of LLM ablation.
Same logic as eval_llm_template_aware.py but uses r1_template_winners.json."""
import sys, json
from pathlib import Path
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent')

# Reuse canon_set
import importlib.util as _ilu
spec = _ilu.spec_from_file_location('utils.electrode_normalizer',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/utils/electrode_normalizer.py')
m = _ilu.module_from_spec(spec); sys.modules['utils.electrode_normalizer'] = m; spec.loader.exec_module(m)
spec = _ilu.spec_from_file_location('_eqs',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/scripts/eval_qwen_sft.py')
m = _ilu.module_from_spec(spec); sys.modules['_eqs'] = m; spec.loader.exec_module(m)
canon_set = m.canon_set

import argparse as _ap
_argp = _ap.ArgumentParser()
_argp.add_argument('--src', default='llm_ablation_sonnet46_full',
                   help='subdir under eval_results/ containing raw_results.json')
_argp.add_argument('--tag', default=None,
                   help='label for output file (defaults to src)')
_args, _ = _argp.parse_known_args()

OUT_DIR = Path('eval_results/template_analysis')
ABLATION_RAW = Path(f'eval_results/{_args.src}/raw_results.json')
_OUT_TAG = _args.tag or _args.src


def main():
    print('Loading inputs...')
    cluster_winners = json.load(open(OUT_DIR / 'r1_template_winners.json'))
    rec_r1 = json.load(open(OUT_DIR / 'records_with_r1_template.json'))
    llm_raw = json.load(open(ABLATION_RAW))
    print(f'  cluster_winners: {len(cluster_winners)} clusters')
    print(f'  raw records w/ r1: {len(rec_r1)}')
    print(f'  llm_raw: {len(llm_raw)}')

    rxn2tpl = {}
    for r in rec_r1:
        if r.get('in_test') and r.get('r1_template'):
            rxn2tpl.setdefault(r['rxn'], r['r1_template'])
    print(f'  unique test rxn smiles with r1: {len(rxn2tpl)}')

    list_fields = ('electrolytes','solvents','reagents','catalysts')
    GROUPS = []
    for r in llm_raw:
        if r and 'rxn' in r:
            for g in 'ABCDEF':
                if f'{g}_pred' in r and g not in GROUPS:
                    GROUPS.append(g)
            if GROUPS: break
    if not GROUPS: GROUPS = ['A','B','C']
    print(f'  groups: {GROUPS}')

    eligible_records = []
    no_tpl_in_train = 0; no_tpl_at_all = 0
    for r in llm_raw:
        if not r or 'rxn' not in r: continue
        tpl = rxn2tpl.get(r['rxn'])
        if not tpl:
            no_tpl_at_all += 1; continue
        if tpl not in cluster_winners:
            no_tpl_in_train += 1; continue
        eligible_records.append((r, tpl))

    print(f'\n=== Records used for radius-1 template-aware evaluation ===')
    print(f'  total LLM raw: {len(llm_raw)}')
    print(f'  no template (mapping/extract fail): {no_tpl_at_all}')
    print(f'  template found but not in train winners: {no_tpl_in_train}')
    print(f'  eligible (r1 template in train winners): {len(eligible_records)}')

    def hit_in_winners(pred_set, winning_variants):
        if not pred_set: return False
        ps = frozenset(pred_set)
        return any(frozenset(v) == ps for v in winning_variants)

    def hit_any_overlap(pred_set, winning_variants):
        if not pred_set: return False
        u = set()
        for v in winning_variants: u |= set(v)
        return bool(set(pred_set) & u)

    results = {g: {} for g in GROUPS}
    for grp in GROUPS:
        for f in list_fields:
            results[grp][f] = {'eligible':0, 'exact_winner':0, 'overlap_winner':0, 'exact_gt':0}

    gt_is_winner_count = {f: 0 for f in list_fields}
    eligible_per_field = {f: 0 for f in list_fields}

    for r, tpl in eligible_records:
        win_dict = cluster_winners[tpl]
        gold = r.get('gold') or {}
        for f in list_fields:
            winners = win_dict.get(f, [])
            if not winners: continue
            gold_set = canon_set(gold.get(f, []) or [])
            if not gold_set: continue
            eligible_per_field[f] += 1
            if frozenset(gold_set) in [frozenset(v) for v in winners]:
                gt_is_winner_count[f] += 1
            for grp in GROUPS:
                pred_set = canon_set((r.get(f'{grp}_pred') or {}).get(f, []) or [])
                results[grp][f]['eligible'] += 1
                if hit_in_winners(pred_set, winners):
                    results[grp][f]['exact_winner'] += 1
                if hit_any_overlap(pred_set, winners):
                    results[grp][f]['overlap_winner'] += 1
                if frozenset(pred_set) == frozenset(gold_set):
                    results[grp][f]['exact_gt'] += 1

    print(f'\n=== Radius-1 template-aware results ===')
    for f in list_fields:
        elig = eligible_per_field[f]
        gt_in = gt_is_winner_count[f]
        print(f'\n{f}: eligible={elig}, GT in winners: {gt_in} ({gt_in/max(elig,1)*100:.1f}%)')
        print(f'{"  ":4s}{"":12s} {"hit ∈ winners":>15s}   {"hit overlap":>13s}   {"hit exact GT":>14s}')
        for grp in GROUPS:
            r = results[grp][f]
            print(f'  {grp}      {"":12s} {r["exact_winner"]:>4d} ({r["exact_winner"]/max(r["eligible"],1)*100:5.1f}%)  '
                  f'  {r["overlap_winner"]:>4d} ({r["overlap_winner"]/max(r["eligible"],1)*100:5.1f}%)  '
                  f'   {r["exact_gt"]:>4d} ({r["exact_gt"]/max(r["eligible"],1)*100:5.1f}%)')

    print(f'\n=== Summary: r1 metrics × {len(GROUPS)} groups ===')
    col_hdr = '  '.join(f'{g:>8s}' for g in GROUPS)
    print(f'{"field":15s} {"metric":>20s}  {col_hdr}')
    for f in list_fields:
        for metric, key in [('hit ∈ winners', 'exact_winner'),
                             ('overlap', 'overlap_winner'),
                             ('exact GT', 'exact_gt')]:
            vals = [results[g][f][key] / max(results[g][f]['eligible'], 1) * 100 for g in GROUPS]
            cells = '  '.join(f'{v:>7.1f}%' for v in vals)
            print(f'{f:15s} {metric:>20s}  {cells}')

    out = {
        'n_llm_raw': len(llm_raw),
        'n_eligible_records': len(eligible_records),
        'n_no_tpl_in_train': no_tpl_in_train,
        'n_no_tpl_at_all': no_tpl_at_all,
        'per_field': {
            f: {
                'eligible_with_gt': eligible_per_field[f],
                'gt_is_winner_count': gt_is_winner_count[f],
                **{g: results[g][f] for g in GROUPS}
            } for f in list_fields
        },
    }
    out_path = OUT_DIR / f'r1_template_aware_eval__{_OUT_TAG}.json'
    out_path.write_text(json.dumps(out, indent=2))
    print(f'\nSaved to {out_path}')


if __name__ == '__main__':
    main()
