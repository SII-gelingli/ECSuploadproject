"""Template-aware re-evaluation of LLM ablation on the 1713 subset with same-sig train precedents."""
import sys, json
from pathlib import Path
from collections import defaultdict
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
    sig_winners = json.load(open(OUT_DIR / 'rc_sig_winners.json'))
    rec_sigs = json.load(open(OUT_DIR / 'records_with_rc_sig.json'))
    llm_raw = json.load(open(ABLATION_RAW))
    print(f'  sig_winners: {len(sig_winners)} clusters')
    print(f'  raw records w/ sig: {len(rec_sigs)}')
    print(f'  llm_raw: {len(llm_raw)}')

    # Build rxn_smiles → sig_key (test side only, looking at first occurrence)
    rxn2sig = {}
    for r in rec_sigs:
        if r.get('in_test') and r.get('rc_sig_key'):
            # If multiple test rows share the same rxn smiles (which they often do
            # because dataset duplicates), all share the same sig — keep first seen
            rxn2sig.setdefault(r['rxn'], r['rc_sig_key'])
    print(f'  unique test rxn smiles with sig: {len(rxn2sig)}')

    # For each LLM raw record, look up its sig
    list_fields = ('electrolytes','solvents','reagents','catalysts')
    # Auto-detect groups from raw records
    GROUPS = []
    for r in llm_raw:
        if r and 'rxn' in r:
            for g in 'ABCDEF':
                if f'{g}_pred' in r and g not in GROUPS:
                    GROUPS.append(g)
            if GROUPS: break
    if not GROUPS: GROUPS = ['A','B','C']
    print(f'  groups detected: {GROUPS}')
    eligible_records = []  # records whose sig is in train winners
    no_sig_in_train = 0; no_sig_at_all = 0
    for r in llm_raw:
        if not r or 'rxn' not in r: continue
        sig_key = rxn2sig.get(r['rxn'])
        if not sig_key:
            no_sig_at_all += 1
            continue
        if sig_key not in sig_winners:
            no_sig_in_train += 1
            continue
        eligible_records.append((r, sig_key))

    print(f'\n=== Records used for template-aware evaluation ===')
    print(f'  total LLM raw: {len(llm_raw)}')
    print(f'  no sig (can\'t parse mapped or no winners in train): {no_sig_at_all}')
    print(f'  sig found but not in train winners: {no_sig_in_train}')
    print(f'  eligible (sig in train winners): {len(eligible_records)}')

    # Evaluate: for each eligible reaction, did LLM's pred match any winning variant?
    def hit_in_winners(pred_set, winning_variants):
        """winning_variants is list of sorted SMILES tuples representing winning condition variants.
           pred_set is canon_set output. Return True if pred_set == any variant (as a set).
        """
        if not pred_set:
            return False
        ps = frozenset(pred_set)
        for v in winning_variants:
            if frozenset(v) == ps:
                return True
        return False

    def hit_any_overlap(pred_set, winning_variants):
        """Looser: pred_set has at least one SMILES in common with any winning variant."""
        if not pred_set: return False
        all_winners_union = set()
        for v in winning_variants:
            all_winners_union |= set(v)
        return bool(set(pred_set) & all_winners_union)

    results = {g: {} for g in GROUPS}
    for grp in GROUPS:
        for f in list_fields:
            results[grp][f] = {
                'eligible': 0,  # eligibility (sig has winners + GT is nonempty)
                'exact_winner': 0,  # pred exactly matches some winning variant
                'overlap_winner': 0,  # pred overlaps with winning variants
                'exact_gt': 0,  # pred exactly matches GT (original metric, for comparison)
            }

    # Also track: are eligible reactions ones whose GT condition is itself a winning variant?
    # (This is a sanity check — if GT yield > 50%, GT should be in winners; but not all GT have yield>50)
    gt_is_winner_count = {f: 0 for f in list_fields}
    eligible_per_field = {f: 0 for f in list_fields}

    for r, sig_key in eligible_records:
        win_dict = sig_winners[sig_key]
        gold = r.get('gold') or {}
        for f in list_fields:
            winners = win_dict.get(f, [])
            if not winners: continue
            gold_set = canon_set(gold.get(f, []) or [])
            if not gold_set: continue
            eligible_per_field[f] += 1
            # check if gold is in winners (sanity)
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

    # Print results
    print(f'\n=== Template-aware evaluation (eligible reactions only) ===')
    for f in list_fields:
        elig = eligible_per_field[f]
        gt_in = gt_is_winner_count[f]
        print(f'\n{f}: eligible={elig}, GT is itself a winner: {gt_in} ({gt_in/max(elig,1)*100:.1f}%)')
        print(f'{"  ":4s}{"":12s} {"hit ∈ winners":>15s}   {"hit overlap":>13s}   {"hit exact GT":>14s}')
        for grp in GROUPS:
            r = results[grp][f]
            print(f'  {grp}      {"":12s} {r["exact_winner"]:>4d} ({r["exact_winner"]/max(r["eligible"],1)*100:5.1f}%)  '
                  f'  {r["overlap_winner"]:>4d} ({r["overlap_winner"]/max(r["eligible"],1)*100:5.1f}%)  '
                  f'   {r["exact_gt"]:>4d} ({r["exact_gt"]/max(r["eligible"],1)*100:5.1f}%)')

    # Build comparison table
    print(f'\n\n=== Summary table: 3 metrics × 4 fields × {len(GROUPS)} groups ===')
    col_hdr = '  '.join(f'{g:>8s}' for g in GROUPS)
    print(f'{"field":15s} {"metric":>20s}  {col_hdr}')
    for f in list_fields:
        for metric, metric_key in [('hit ∈ winners', 'exact_winner'),
                                     ('overlap', 'overlap_winner'),
                                     ('exact GT (old)', 'exact_gt')]:
            vals = [results[g][f][metric_key] / max(results[g][f]['eligible'], 1) * 100 for g in GROUPS]
            cells = '  '.join(f'{v:>7.1f}%' for v in vals)
            print(f'{f:15s} {metric:>20s}  {cells}')

    # Save raw
    out = {
        'n_llm_raw': len(llm_raw),
        'n_eligible_records': len(eligible_records),
        'n_no_sig_in_train': no_sig_in_train,
        'n_no_sig_at_all': no_sig_at_all,
        'per_field': {
            f: {
                'eligible_with_gt': eligible_per_field[f],
                'gt_is_winner_count': gt_is_winner_count[f],
                **{g: results[g][f] for g in GROUPS}
            } for f in list_fields
        },
    }
    out_path = OUT_DIR / f'template_aware_eval__{_OUT_TAG}.json'
    out_path.write_text(json.dumps(out, indent=2))
    print(f'\nSaved to {out_path}')


if __name__ == '__main__':
    main()
