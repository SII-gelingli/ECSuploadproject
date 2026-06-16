"""跑 test 集里还没跑过的反应; 合并到 _full 目录, 不动原 1000 跑过的部分.

Usage:
  ANTHROPIC_API_KEY=xxx python3 scripts/run_remaining_ablation.py \\
    --prior eval_results/llm_ablation_sonnet46_clean \\
    --out eval_results/llm_ablation_sonnet46_full \\
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

# Reuse process_one + everything from eval_llm_ablation.py
import importlib.util as _ilu
spec = _ilu.spec_from_file_location(
    'eval_llm_ablation', project_root / 'scripts' / 'eval_llm_ablation.py')
mod = _ilu.module_from_spec(spec); sys.modules['eval_llm_ablation'] = mod
spec.loader.exec_module(mod)
process_one = mod.process_one
canon_set = mod.canon_set

from rag.retriever import ReactionRetriever
from rag.mechanism_retriever import MechanismRetriever
from models.loader import ModelManager


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prior', required=True, help='dir containing existing raw_results.json')
    ap.add_argument('--out', required=True, help='dir for merged full results')
    ap.add_argument('--concurrency', type=int, default=6)
    ap.add_argument('--top_k_rxn', type=int, default=5)
    ap.add_argument('--model', default='claude-sonnet-4-6')
    args = ap.parse_args()

    prior_dir = Path(args.prior)
    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)

    # Load test data + exclude sets
    data_dir = project_root / 'data_audited_v3_clean'
    test = torch.load(data_dir / 'test.pt', weights_only=False)
    sm = json.load(open(data_dir / 'split_meta.json'))
    exclude_pids = set(sm['test_papers'])
    exclude_rxns = set()
    for r in test:
        exclude_rxns.add('.'.join(r['reactant_smiles']) + '>>' + '.'.join(r['product_smiles']))
    print(f'Test set: {len(test)}, exclude {len(exclude_pids)} pids, {len(exclude_rxns)} rxn smiles')

    # Restore qwen gold into test recs
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

    # Load prior results
    prior_raw = json.load(open(prior_dir / 'raw_results.json'))
    done_idx_to_rec = {}
    for r in prior_raw:
        if r and 'idx' in r and 'rxn' in r:
            done_idx_to_rec[r['idx']] = r
    print(f'Prior run: {len(prior_raw)} entries, {len(done_idx_to_rec)} valid (have idx + rxn)')

    # Compute remaining
    all_idx = set(range(len(test)))
    done_idx = set(done_idx_to_rec.keys())
    remaining = sorted(all_idx - done_idx)
    print(f'All: {len(all_idx)}, done: {len(done_idx)}, remaining: {len(remaining)}')

    if not remaining:
        print('Nothing to run. Just merging + writing final.')

    # Setup retrievers + client
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

    new_results = {}
    n = len(remaining); done = 0; new_failed = 0; t0 = time.time()
    if remaining:
        print(f'Running {n} remaining reactions with concurrency={args.concurrency}...')
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {
                ex.submit(process_one, idx, test[idx], rxn_retr, mech_retr,
                          exclude_pids, exclude_rxns, client, args.model, args.top_k_rxn): idx
                for idx in remaining
            }
            for fu in as_completed(futures):
                idx = futures[fu]
                try:
                    new_results[idx] = fu.result()
                except Exception as e:
                    new_failed += 1
                    new_results[idx] = {'idx': idx, 'error': f'{e}\n{traceback.format_exc()[:2000]}'}
                done += 1
                if done % 20 == 0 or done == n:
                    rate = done / max(time.time() - t0, 1e-3)
                    eta = (n - done) / rate
                    print(f'  {done}/{n} ({rate:.2f} rxn/s, eta {eta/60:.1f} min, new_failed={new_failed})', flush=True)

    # Build full ordered list by idx
    all_results = []
    for idx in sorted(all_idx):
        if idx in done_idx_to_rec:
            all_results.append(done_idx_to_rec[idx])
        elif idx in new_results:
            all_results.append(new_results[idx])
        else:
            all_results.append({'idx': idx, 'error': 'never_run'})

    # Truncate raw fields
    LIMIT = 10000
    for r in all_results:
        if r is None: continue
        for grp in ('A','B','C'):
            for key in (f'{grp}_pred_raw', f'{grp}_user_prompt'):
                t = r.get(key)
                if isinstance(t, str) and len(t) > LIMIT:
                    r[key] = t[:LIMIT] + '…[truncated]'

    out_raw = out_dir / 'raw_results.json'
    out_raw.write_text(json.dumps(all_results, indent=2, default=str))
    print(f'\n[OK] merged → {out_raw}  ({len(all_results)} entries)')

    still_failed = sum(1 for r in all_results if r is None or 'rxn' not in r)
    print(f'  Total: {len(all_results)}, still failed: {still_failed}')

    # Aggregate
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
    for r in all_results:
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

    n_valid = len(all_results) - still_failed
    agg = {
        'n_total': len(all_results), 'n_valid': n_valid,
        'parse_fail': parse_fail, 'valid': valid, 'sums': sums,
        'rates': {g: {k: sums[g][k] / max(n_valid, 1) for k in keys} for g in grps},
        'nonempty_total': nonempty_total, 'nonempty_hit': nonempty_hit,
        'nonempty_rate': {g: {f: nonempty_hit[g][f] / max(nonempty_total[f], 1) for f in list_fields} for g in grps},
    }
    (out_dir / 'aggregate.json').write_text(json.dumps(agg, indent=2))
    print(f'[OK] aggregate → {out_dir / "aggregate.json"}')

    print('\n=== Final summary (full test set) ===')
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
