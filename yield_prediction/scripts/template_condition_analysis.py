"""按 template cluster 聚合 winning conditions, 并做 sanity check + LLM ablation 重评."""
import sys, json
from pathlib import Path
from collections import defaultdict, Counter
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent')

import importlib.util as _ilu
spec = _ilu.spec_from_file_location('utils.electrode_normalizer',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/utils/electrode_normalizer.py')
m = _ilu.module_from_spec(spec); sys.modules['utils.electrode_normalizer'] = m; spec.loader.exec_module(m)
spec = _ilu.spec_from_file_location('_eqs',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction/scripts/eval_qwen_sft.py')
m = _ilu.module_from_spec(spec); sys.modules['_eqs'] = m; spec.loader.exec_module(m)
canon_set = m.canon_set

DATA_DIR = Path('data/reaction_templates')
OUT_DIR = Path('eval_results/template_analysis')
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1) Load mapped data
print('Loading rxnmapper mapped reactions...')
records = json.load(open(DATA_DIR / 'reactions_mapped_rxnmapper.json'))
print(f'  {len(records)} records')

# Index by template
template2rxns = defaultdict(list)
for r in records:
    t = r.get('template')
    if t:
        template2rxns[t].append(r)
print(f'  unique templates: {len(template2rxns)}')

# 2) Identify TEST paper ids — we need to know which records are train/test
print('\nLoading test set + split_meta...')
import torch
test = torch.load('yield_prediction/data_audited_v3_clean/test.pt', weights_only=False)
sm = json.load(open('yield_prediction/data_audited_v3_clean/split_meta.json'))
test_pids = set(sm['test_papers'])
test_rxn_smis = set()
for r in test:
    test_rxn_smis.add('.'.join(r['reactant_smiles']) + '>>' + '.'.join(r['product_smiles']))
print(f'  test paper_ids: {len(test_pids)}, test rxn smiles: {len(test_rxn_smis)}')

# Split records into train vs test based on paper_id
import re
SUFFIX = re.compile(r'(_sup_?\d*|_supl_?\d*|_si_?\d*|_esi_?\d*|_sm_?\d*)$', re.I)
def base_pid(d):
    if not d: return ''
    return SUFFIX.sub('', d).lower()

train_records = []
test_records = []
for r in records:
    bpid = base_pid(r.get('paper_id', ''))
    if bpid in test_pids or r.get('rxn') in test_rxn_smis:
        test_records.append(r)
    else:
        train_records.append(r)
print(f'  train records: {len(train_records)}, test records: {len(test_records)}')

# 3) Aggregate winning conditions per template (using train side only)
def cond_signature(r):
    """Return a canonical tuple representing the condition set."""
    c = r.get('cond', {})
    return (
        (c.get('anode') or '').lower(),
        (c.get('cathode') or '').lower(),
        (c.get('cell_type') or '').lower(),
        tuple(sorted(canon_set(c.get('electrolytes', []) or []))),
        tuple(sorted(canon_set(c.get('solvents', []) or []))),
        tuple(sorted(canon_set(c.get('reagents', []) or []))),
        tuple(sorted(canon_set(c.get('catalysts', []) or []))),
    )

# template -> per-component winning conditions (yield > 50)
template_train = defaultdict(list)  # template -> [train record list]
for r in train_records:
    t = r.get('template')
    if t:
        template_train[t].append(r)

print(f'  train-side templates: {len(template_train)}')

template_winners = {}  # template -> dict of field -> set of winning SMILES sets (yield>50)
for t, rs in template_train.items():
    high_yield = [r for r in rs if r.get('yield') is not None and r['yield'] > 50]
    if not high_yield: continue
    field_winners = {f: set() for f in ('electrolytes','solvents','reagents','catalysts','anode','cathode','cell_type')}
    for r in high_yield:
        c = r.get('cond', {})
        for f in ('electrolytes','solvents','reagents','catalysts'):
            cs = canon_set(c.get(f, []) or [])
            if cs:
                field_winners[f].add(frozenset(cs))
        for f in ('anode','cathode','cell_type'):
            v = c.get(f)
            if v: field_winners[f].add(str(v).lower())
    # convert frozensets to sorted tuples for JSON
    template_winners[t] = {
        f: [sorted(list(s)) if isinstance(s, frozenset) else s for s in field_winners[f]]
        for f in field_winners
    }

print(f'  templates with at least one yield>50% train rxn: {len(template_winners)}')

# 4) Sanity check: print top 15 templates with their reaction examples + dominant conditions
print(f'\n=== Top 15 rxnmapper templates (sanity check) ===')
top15 = sorted(template_train.items(), key=lambda x: -len(x[1]))[:15]
top15_info = []
for i, (t, rs) in enumerate(top15):
    high = [r for r in rs if r.get('yield') is not None and r['yield'] > 50]
    print(f'\n[#{i+1}] template (truncated):')
    print(f'   {t[:130]}')
    print(f'   train_n: {len(rs)}, yield>50%: {len(high)}')
    # Show 2 example reactions
    for j, r in enumerate(rs[:2]):
        print(f'   ex{j+1}: {r["rxn"][:120]}  (yield={r["yield"]})')
    # Show dominant winning conditions
    winners = template_winners.get(t, {})
    for f in ('anode','cathode','cell_type','electrolytes','solvents','catalysts'):
        vals = winners.get(f, [])
        n_unique = len(vals) if isinstance(vals, (list, set)) else 0
        if vals:
            samples = [str(v)[:40] for v in (list(vals) if isinstance(vals, (set, list)) else [])][:3]
            print(f'   {f}: {n_unique} winning variants. e.g. {samples}')
    top15_info.append({'template': t, 'train_n': len(rs), 'high_yield_n': len(high),
                        'example_rxns': [(r['rxn'], r.get('yield')) for r in rs[:3]],
                        'winners': winners})

# Save outputs
print(f'\nSaving outputs...')
(OUT_DIR / 'template_winners.json').write_text(json.dumps({
    t: w for t, w in template_winners.items()
}, indent=1, default=str))
(OUT_DIR / 'top15_inspect.json').write_text(json.dumps(top15_info, indent=2, default=str))
print(f'  saved {OUT_DIR}/template_winners.json + top15_inspect.json')

# 5) For each test reaction, find its template + check if test_records have matching template in train
print(f'\n=== Test reaction template coverage ===')
test_template_match = 0
test_template_missing = 0
test_winners_avail = 0
for r in test_records:
    t = r.get('template')
    if not t:
        test_template_missing += 1
        continue
    if t in template_train:
        test_template_match += 1
        if t in template_winners:
            test_winners_avail += 1
    else:
        # template only in test side (no train precedent) — singleton or test-only cluster
        test_template_missing += 1

print(f'  test records: {len(test_records)}')
print(f'  test records with template matched in train: {test_template_match} ({test_template_match/len(test_records)*100:.1f}%)')
print(f'  test records with winners available (>=1 yield>50% train rxn): {test_winners_avail}')
print(f'  test records without template precedent: {test_template_missing}')

# 6) Save train/test split as JSON for later LLM eval re-scoring
(OUT_DIR / 'train_test_split.json').write_text(json.dumps({
    'n_train_records': len(train_records),
    'n_test_records': len(test_records),
    'test_winners_avail': test_winners_avail,
    'test_template_match': test_template_match,
    'test_template_missing': test_template_missing,
}, indent=2))

print(f'\nDone. Use template_winners.json for downstream eval.')
