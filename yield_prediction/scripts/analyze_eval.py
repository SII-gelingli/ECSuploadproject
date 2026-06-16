"""Post-hoc analysis on a saved eval_qwen_sft_voting.py output.

Adds:
  - Jaccard / F1 / precision / recall for SMILES-list fields (electrolytes/solvents/reagents/catalysts)
  - Per-field metrics split by gold-empty vs gold-non-empty
  - any-of-K recall = at least one gold item predicted in any of K samples
  - Top distribution diagnostics: what does the model predict vs what does the gold look like

No inference rerun — just reads detail entries from the JSON.
"""
import argparse
import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _silence_rdkit():
    try:
        from rdkit import RDLogger
        RDLogger.DisableLog('rdApp.*')
    except Exception:
        pass


_silence_rdkit()


def canonical(smi):
    try:
        from rdkit import Chem
        m = Chem.MolFromSmiles(smi)
        return Chem.MolToSmiles(m) if m else None
    except Exception:
        return None


def canon_set(lst):
    out = set()
    for s in lst or []:
        c = canonical(s)
        if c:
            out.add(c)
    return out


def set_metrics(pred: set, gold: set):
    """Return jaccard, precision, recall, f1 (0 if both empty -> all 1.0 for exact match consistency)."""
    if not pred and not gold:
        return 1.0, 1.0, 1.0, 1.0
    if not pred or not gold:
        return 0.0, 0.0, 0.0, 0.0
    inter = len(pred & gold)
    union = len(pred | gold)
    p = inter / len(pred)
    r = inter / len(gold)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    j = inter / union
    return j, p, r, f1


def best_over_K(pred_sets, gold: set, metric_idx: int):
    """Best (max) of jaccard/p/r/f1 over K predicted sets vs single gold."""
    return max(set_metrics(ps, gold)[metric_idx] for ps in pred_sets)


def union_over_K_recall(pred_sets, gold: set):
    """Recall computed on UNION of all K predictions — how much of gold did the model EVER predict."""
    if not gold:
        return 1.0 if not any(ps for ps in pred_sets) else 0.0
    union_pred = set().union(*pred_sets)
    return len(union_pred & gold) / len(gold)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--eval_json', default=str(Path(__file__).parent.parent / 'eval_results' / 'qwen3_14b_lora_v1_voted.json'))
    ap.add_argument('--out', default=None)
    args = ap.parse_args()

    d = json.load(open(args.eval_json))
    details = d['detail']
    K = d['K']
    n = len(details)
    print(f'Analyzing {n} samples (K={K})\n')

    SMI_FIELDS = ('electrolytes', 'solvents', 'reagents', 'catalysts')

    # Accumulate: per-field stats split by gold-empty vs gold-non-empty
    stats = {f: {
        'all':    defaultdict(float),  # sums over all n
        'empty':  defaultdict(float),  # sums when gold is empty
        'nonempty': defaultdict(float),
        'n_all': 0, 'n_empty': 0, 'n_nonempty': 0,
    } for f in SMI_FIELDS}

    # Distribution diagnostics: most-predicted vs most-gold per field
    pred_dist = {f: Counter() for f in SMI_FIELDS}  # union over K, dedup per sample
    gold_dist = {f: Counter() for f in SMI_FIELDS}

    for ent in details:
        gold_dict = ent['gold']
        preds = ent['preds']  # list of K dicts (or None)
        for f in SMI_FIELDS:
            gold_set = canon_set(gold_dict.get(f, []))
            pred_sets = [canon_set(p.get(f, []) if p else []) for p in preds]
            # voted = mode of pred_sets (frozenset for hashability)
            voted_set = Counter(frozenset(ps) for ps in pred_sets).most_common(1)[0][0]
            voted_set = set(voted_set)

            # Voted-vs-gold metrics
            j, p, r, f1 = set_metrics(voted_set, gold_set)
            # Best-of-K (oracle) metrics
            j_bk = best_over_K(pred_sets, gold_set, 0)
            f1_bk = best_over_K(pred_sets, gold_set, 3)
            # Union recall (model EVER predicted any gold item)
            ur = union_over_K_recall(pred_sets, gold_set)

            bucket = 'empty' if not gold_set else 'nonempty'
            for sub in ('all', bucket):
                stats[f][sub]['jaccard_voted'] += j
                stats[f][sub]['precision_voted'] += p
                stats[f][sub]['recall_voted'] += r
                stats[f][sub]['f1_voted'] += f1
                stats[f][sub]['jaccard_bestK'] += j_bk
                stats[f][sub]['f1_bestK'] += f1_bk
                stats[f][sub]['union_recall'] += ur
                stats[f][sub]['exact_match'] += (1.0 if voted_set == gold_set else 0.0)
            stats[f]['n_all'] += 1
            stats[f][f'n_{bucket}'] += 1

            # Distribution
            for s in gold_set:
                gold_dist[f][s] += 1
            seen_in_sample = set()
            for ps in pred_sets:
                for s in ps:
                    if s not in seen_in_sample:
                        seen_in_sample.add(s)
                        pred_dist[f][s] += 1

    # Print metrics tables
    HEADERS = ['exact_match', 'jaccard_voted', 'f1_voted', 'precision_voted', 'recall_voted', 'jaccard_bestK', 'f1_bestK', 'union_recall']
    for sub in ('all', 'nonempty', 'empty'):
        n_key = f'n_{sub}'
        any_field = next(iter(stats.values()))
        N = any_field[n_key]
        print(f'\n=== {sub.upper()} subset (n={N}) ===')
        print(f'{"field":14s}  ' + '  '.join(f'{h:>14s}' for h in HEADERS))
        for f in SMI_FIELDS:
            N_f = stats[f][n_key]
            if N_f == 0:
                continue
            vals = [stats[f][sub][h] / N_f * 100 for h in HEADERS]
            print(f'  {f:12s}  ' + '  '.join(f'{v:13.2f}%' for v in vals))

    # Distribution diagnostics
    print('\n\n=== TOP PREDICTIONS vs TOP GOLD ===')
    for f in SMI_FIELDS:
        print(f'\n--- {f} ---')
        print(f'{"":4s}{"GOLD top-10":<55s}  {"MODEL top-10 (union over K)":<55s}')
        gold_top = gold_dist[f].most_common(10)
        pred_top = pred_dist[f].most_common(10)
        for i in range(max(len(gold_top), len(pred_top))):
            g = f'{gold_top[i][1]:4d}  {gold_top[i][0][:48]}' if i < len(gold_top) else ''
            p = f'{pred_top[i][1]:4d}  {pred_top[i][0][:48]}' if i < len(pred_top) else ''
            print(f'    {g:<55s}  {p:<55s}')

    # Save
    if args.out:
        result = {
            'n': n, 'K': K,
            'subsets': {
                sub: {
                    f: {h: stats[f][sub][h] / max(stats[f][f'n_{sub}'], 1) for h in HEADERS}
                    for f in SMI_FIELDS
                }
                for sub in ('all', 'nonempty', 'empty')
            },
            'n_per_subset': {f: {sub: stats[f][f'n_{sub}'] for sub in ('all', 'nonempty', 'empty')} for f in SMI_FIELDS},
            'gold_top10': {f: gold_dist[f].most_common(10) for f in SMI_FIELDS},
            'pred_top10_unionK': {f: pred_dist[f].most_common(10) for f in SMI_FIELDS},
        }
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, 'w') as fout:
            json.dump(result, fout, indent=2, ensure_ascii=False)
        print(f'\nwrote {args.out}')


if __name__ == '__main__':
    main()
