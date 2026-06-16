"""仅重跑上次 ablation 失败的 worker(并发竞态导致), 与成功部分合并。

Usage:
  ANTHROPIC_API_KEY=xxx python3 scripts/retry_failed_ablation.py \\
    --src eval_results/llm_ablation_sonnet46_clean \\
    --concurrency 6 --model claude-sonnet-4-6
"""
import os, sys, json, time, random, argparse, traceback
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

for _p in (
    '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent',
):
    if _p not in sys.path: sys.path.insert(0, _p)

import torch
import anthropic

project_root = Path(__file__).parent.parent

# Reuse process_one + helpers from eval_llm_ablation.py
import importlib.util as _ilu
spec = _ilu.spec_from_file_location(
    'eval_llm_ablation', project_root / 'scripts' / 'eval_llm_ablation.py')
mod = _ilu.module_from_spec(spec); sys.modules['eval_llm_ablation'] = mod
spec.loader.exec_module(mod)
process_one = mod.process_one

from rag.retriever import ReactionRetriever
from rag.mechanism_retriever import MechanismRetriever
from models.loader import ModelManager


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, help='dir containing raw_results.json from prior run')
    ap.add_argument('--concurrency', type=int, default=6)
    ap.add_argument('--top_k_rxn', type=int, default=5)
    ap.add_argument('--model', default='claude-sonnet-4-6')
    args = ap.parse_args()

    src_dir = Path(args.src)
    raw_path = src_dir / 'raw_results.json'
    print(f'Loading {raw_path}')
    results = json.load(open(raw_path))
    n_total = len(results)

    # Identify failed positions
    failed_positions = [pos for pos, r in enumerate(results) if r is None or 'rxn' not in r]
    print(f'Total: {n_total}, failed (no rxn key): {len(failed_positions)}')
    if not failed_positions:
        print('Nothing to retry.')
        return

    # Need test set + exclude sets to recompute
    data_dir = project_root / 'data_audited_v3_clean'
    test = torch.load(data_dir / 'test.pt', weights_only=False)
    sm = json.load(open(data_dir / 'split_meta.json'))
    exclude_pids = set(sm['test_papers'])
    exclude_rxns = set()
    for r in test:
        exclude_rxns.add('.'.join(r['reactant_smiles']) + '>>' + '.'.join(r['product_smiles']))

    # Restore qwen gold (same as main eval)
    qwen_test = []
    with open(data_dir.parent / 'data_qwen_sft_v3' / 'test.jsonl') as f:
        for line in f:
            r = json.loads(line)
            assistant = None
            for m in r['messages']:
                if m['role'] == 'assistant':
                    try: assistant = json.loads(m['content'])
                    except: assistant = None
                    break
            qwen_test.append(assistant or {})
    for i, rec in enumerate(test):
        g = qwen_test[i]
        rec['anode'] = g.get('anode', '')
        rec['cathode'] = g.get('cathode', '')
        rec['cell_type'] = g.get('cell_type', '')
        rec['electrolyte_smiles_list'] = g.get('electrolytes', []) or []
        rec['solvent_smiles_list'] = g.get('solvents', []) or []
        rec['reagent_smiles_list'] = g.get('reagents', []) or []
        rec['catalyst_smiles_list'] = g.get('catalysts', []) or []
        rec['ligand_smiles_list'] = g.get('ligands', []) or []
        rec['additive_smiles_list'] = g.get('additives', []) or []

    # Failed positions hold raw[pos] = {'idx': ..., 'error': ...}
    # we need the original idx for each failed position
    failed_idx_pairs = []
    for pos in failed_positions:
        r = results[pos]
        if r is None:
            print(f'  WARN pos={pos} has None entry, skip')
            continue
        failed_idx_pairs.append((pos, r['idx']))
    print(f'Re-running {len(failed_idx_pairs)} reactions with concurrency={args.concurrency}')

    print('Loading retrievers + ModelManager...')
    rxn_retr = ReactionRetriever('data/faiss_index_paper.bin', 'data/reaction_db_paper.pkl')
    mech_retr = MechanismRetriever('data/mechanism_kb')
    mm = ModelManager()
    process_one.mol_extractor = mm.mol_extractor

    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    base_url = os.environ.get('ANTHROPIC_BASE_URL') or None
    if not api_key:
        raise RuntimeError('Set ANTHROPIC_API_KEY env var')
    client = anthropic.Anthropic(api_key=api_key, base_url=base_url)

    n = len(failed_idx_pairs)
    done = 0; new_failed = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {
            ex.submit(process_one, idx, test[idx], rxn_retr, mech_retr,
                      exclude_pids, exclude_rxns, client, args.model, args.top_k_rxn): (pos, idx)
            for pos, idx in failed_idx_pairs
        }
        for fu in as_completed(futures):
            pos, idx = futures[fu]
            try:
                results[pos] = fu.result()
            except Exception as e:
                new_failed += 1
                results[pos] = {'idx': idx, 'error': f'{e}\n{traceback.format_exc()[:2000]}'}
            done += 1
            if done % 20 == 0 or done == n:
                rate = done / max(time.time() - t0, 1e-3)
                eta = (n - done) / rate
                print(f'  retry {done}/{n}  ({rate:.2f} rxn/s, eta {eta/60:.1f} min, new_failed={new_failed})', flush=True)

    # Truncate raw fields
    LIMIT = 10000
    for r in results:
        if r is None: continue
        for grp in ('A','B','C'):
            for key in (f'{grp}_pred_raw', f'{grp}_user_prompt'):
                t = r.get(key)
                if isinstance(t, str) and len(t) > LIMIT:
                    r[key] = t[:LIMIT] + '…[truncated]'

    raw_path.write_text(json.dumps(results, indent=2, default=str))
    print(f'\n[OK] merged + saved → {raw_path}')

    still_failed = sum(1 for r in results if r is None or 'rxn' not in r)
    print(f'Total {n_total}, still failed: {still_failed} (was {len(failed_positions)})')

    # Re-compute aggregate
    from eval_llm_ablation import canon_set
    keys = ['anode','cathode','cell_type',
            'electrolytes_first','electrolytes_exact_set',
            'solvents_first','solvents_exact_set',
            'reagents_first','reagents_exact_set',
            'catalysts_first','catalysts_exact_set']
    grps = ['A','B','C']
    sums = {g: {k: 0 for k in keys} for g in grps}
    parse_fail = {g: 0 for g in grps}; valid = {g: 0 for g in grps}
    nonempty_total = {f: 0 for f in ('electrolytes','solvents','reagents','catalysts')}
    nonempty_hit = {g: {f: 0 for f in nonempty_total} for g in grps}
    list_fields = list(nonempty_total)
    for r in results:
        if r is None or 'rxn' not in r: continue
        g_gold = r.get('gold') or {}
        for f in list_fields:
            if canon_set(g_gold.get(f, []) or []): nonempty_total[f] += 1
        for g in grps:
            mt = r.get(f'{g}_metrics')
            if not mt:
                parse_fail[g] += 1; continue
            valid[g] += 1
            for k in keys:
                if mt.get(k): sums[g][k] += 1
            pred = r.get(f'{g}_pred') or {}
            for f in list_fields:
                gs = canon_set(g_gold.get(f, []) or [])
                ps = canon_set(pred.get(f, []) or [])
                if gs and gs == ps: nonempty_hit[g][f] += 1

    agg = {
        'n_total': n_total,
        'n_valid': n_total - still_failed,
        'parse_fail': parse_fail, 'valid': valid, 'sums': sums,
        'rates': {g: {k: sums[g][k] / max(n_total - still_failed, 1) for k in keys} for g in grps},
        'nonempty_total': nonempty_total, 'nonempty_hit': nonempty_hit,
        'nonempty_rate': {g: {f: nonempty_hit[g][f] / max(nonempty_total[f], 1) for f in list_fields} for g in grps},
    }
    agg_path = src_dir / 'aggregate.json'
    agg_path.write_text(json.dumps(agg, indent=2))
    print(f'[OK] re-aggregated → {agg_path}')

    print('\n=== Final summary (after retry) ===')
    print(f'{"field":30s}  {"A pure":>10s}  {"B +rxn":>10s}  {"C +rxn+mech":>12s}')
    for k in keys:
        a, b, c = (agg['rates']['A'][k]*100, agg['rates']['B'][k]*100, agg['rates']['C'][k]*100)
        print(f'{k:30s}  {a:>9.2f}%  {b:>9.2f}%  {c:>11.2f}%')
    print()
    for f in list_fields:
        nt = nonempty_total[f]
        a, b, c = (nonempty_hit['A'][f], nonempty_hit['B'][f], nonempty_hit['C'][f])
        print(f'{f+" (GT非空 set✓)":30s}  {a:>4d}/{nt}={a/max(nt,1)*100:>5.1f}%  '
              f'{b:>4d}/{nt}={b/max(nt,1)*100:>5.1f}%  '
              f'{c:>4d}/{nt}={c/max(nt,1)*100:>5.1f}%')


if __name__ == '__main__':
    main()
