"""Radius-1 reaction clustering via rdchiral template extraction.
Uses canonical SMARTS string as cluster key. Compare to radius-0 results."""
import sys, json, time
from pathlib import Path
from collections import Counter, defaultdict
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')

from rdchiral.template_extractor import extract_from_reaction
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

DATA = Path('data/reaction_templates/reactions_mapped_rxnmapper.json')
SPLIT = Path('eval_results/template_analysis/_split_papers.json')
OUT_DIR = Path('eval_results/template_analysis')


def extract_template(mapped_rxn):
    """Return canonical SMARTS (radius-1) or None on failure."""
    if not mapped_rxn or '>>' not in mapped_rxn:
        return None
    try:
        rs, ps = mapped_rxn.split('>>', 1)
        out = extract_from_reaction({'reactants': rs, 'products': ps, '_id': 0})
        return out.get('reaction_smarts')
    except Exception:
        return None


def main():
    print(f'Loading mapped reactions from {DATA}...')
    records = json.load(open(DATA))
    print(f'  {len(records)} records')

    split = json.load(open(SPLIT))
    test_papers = set(split.get('test_papers') or [])
    print(f'  test papers: {len(test_papers)}')

    print('\nExtracting radius-1 templates via rdchiral...')
    t0 = time.time()
    sig_ok = 0; sig_fail = 0
    for i, r in enumerate(records):
        tpl = extract_template(r.get('mapped'))
        r['r1_template'] = tpl
        r['in_test'] = r.get('paper_id') in test_papers
        if tpl: sig_ok += 1
        else: sig_fail += 1
        if (i+1) % 2000 == 0:
            dt = time.time() - t0
            print(f'  {i+1}/{len(records)} ({(i+1)/dt:.0f} rxn/s, eta {(len(records)-i-1)/(i/dt):.0f}s)', flush=True)
    print(f'  total: ok={sig_ok}, fail={sig_fail}, {(time.time()-t0):.1f}s')

    # Build clusters
    print('\nBuilding clusters...')
    cluster_to_recs = defaultdict(list)
    for r in records:
        if r.get('r1_template'):
            cluster_to_recs[r['r1_template']].append(r)
    print(f'  unique templates: {len(cluster_to_recs)}')

    # Size distribution
    sizes = sorted([len(v) for v in cluster_to_recs.values()], reverse=True)
    print(f'  top 10 sizes: {sizes[:10]}')
    print(f'  median: {sizes[len(sizes)//2]}, mean: {sum(sizes)/len(sizes):.2f}')
    bands = [(1, 1), (2, 5), (6, 10), (11, 50), (51, 100), (101, 1e9)]
    print(f'  size distribution:')
    for lo, hi in bands:
        in_band = [s for s in sizes if lo <= s <= hi]
        print(f'    {lo}..{hi}: {len(in_band)} clusters, {sum(in_band)} rxns ({sum(in_band)/len(records)*100:.1f}%)')

    # Train/test coverage
    train_cluster_sigs = set()
    test_cluster_sigs = set()
    train_total = test_total = 0
    train_with_sig = test_with_sig = 0
    for r in records:
        if r.get('in_test'):
            test_total += 1
            if r.get('r1_template'):
                test_with_sig += 1
                test_cluster_sigs.add(r['r1_template'])
        else:
            train_total += 1
            if r.get('r1_template'):
                train_with_sig += 1
                train_cluster_sigs.add(r['r1_template'])
    print(f'\n  Train: {train_with_sig}/{train_total} ({train_with_sig/train_total*100:.1f}%) with sig; {len(train_cluster_sigs)} unique sigs')
    print(f'  Test:  {test_with_sig}/{test_total} ({test_with_sig/test_total*100:.1f}%) with sig; {len(test_cluster_sigs)} unique sigs')
    shared = test_cluster_sigs & train_cluster_sigs
    test_with_shared = sum(1 for r in records if r.get('in_test') and r.get('r1_template') in shared)
    print(f'  shared sigs: {len(shared)} ({len(shared)/len(test_cluster_sigs)*100:.1f}% of test sigs)')
    print(f'  test rxns with shared sig: {test_with_shared} ({test_with_shared/test_total*100:.1f}% of test)')

    # Aggregate winning conditions per cluster (yield > 50% on train side)
    print('\nAggregating winning conditions (yield > 50% on train)...')
    def canon_set(items):
        if not items: return frozenset()
        return frozenset(sorted(items))
    cluster_winners = defaultdict(lambda: defaultdict(set))
    for r in records:
        tpl = r.get('r1_template')
        if not tpl or r.get('in_test'): continue
        try:
            y = float(r.get('yield', 0) or 0)
        except (ValueError, TypeError):
            continue
        if y < 50: continue
        cond = r.get('cond') or {}
        for f in ('electrolytes', 'solvents', 'reagents', 'catalysts'):
            vals = cond.get(f) or []
            if vals:
                cluster_winners[tpl][f].add(canon_set(vals))
    cluster_winners_serializable = {
        tpl: {f: [sorted(s) for s in sorted(vset)] for f, vset in v.items()}
        for tpl, v in cluster_winners.items()
    }
    print(f'  clusters with >=1 winning condition: {len(cluster_winners)}')

    # Save outputs
    out1 = OUT_DIR / 'r1_template_winners.json'
    out2 = OUT_DIR / 'records_with_r1_template.json'
    out3 = OUT_DIR / 'r1_cluster_stats.json'
    json.dump(cluster_winners_serializable, open(out1, 'w'))

    light_records = [
        {
            'rxn': r['rxn'],
            'paper_id': r.get('paper_id'),
            'yield': r.get('yield'),
            'r1_template': r.get('r1_template'),
            'in_test': r.get('in_test'),
        } for r in records
    ]
    json.dump(light_records, open(out2, 'w'))

    stats = {
        'total_records': len(records),
        'sig_ok': sig_ok, 'sig_fail': sig_fail,
        'unique_clusters': len(cluster_to_recs),
        'train_total': train_total, 'train_with_sig': train_with_sig, 'train_unique_sigs': len(train_cluster_sigs),
        'test_total': test_total, 'test_with_sig': test_with_sig, 'test_unique_sigs': len(test_cluster_sigs),
        'shared_sigs': len(shared),
        'test_with_shared': test_with_shared,
        'winners_clusters': len(cluster_winners),
    }
    json.dump(stats, open(out3, 'w'), indent=2)
    print(f'\nSaved:')
    print(f'  {out1}  ({len(cluster_winners)} clusters with winners)')
    print(f'  {out2}  ({len(records)} records with r1_template)')
    print(f'  {out3}  (summary stats)')


if __name__ == '__main__':
    main()
