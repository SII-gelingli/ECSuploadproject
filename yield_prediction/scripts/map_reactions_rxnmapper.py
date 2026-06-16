"""用 rxnmapper (IBM transformer mapper) 给全 24K 反应做 atom mapping + 模板提取.

需要在 /inspire/hdd/global_user/gelingli-253114010248/rxnmapper_venv 环境里跑.
"""
import sys, json, time, os
from pathlib import Path
from collections import defaultdict, Counter

# Disable proxies (they cause connection issues for HF model fetch)
for var in ['https_proxy', 'HTTPS_PROXY', 'HTTP_PROXY', 'http_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(var, None)

from rxnmapper import RXNMapper
from rdchiral.template_extractor import extract_from_reaction

RAW = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')
OUT_DIR = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/data/reaction_templates')
OUT_DIR.mkdir(parents=True, exist_ok=True)

BATCH_SIZE = 32   # GPU batch size for rxnmapper


def parse_y(x):
    if x is None: return None
    if isinstance(x, (int, float)): return float(x)
    if isinstance(x, str):
        import re
        m = re.search(r'(\d+(?:\.\d+)?)', x); return float(m.group(1)) if m else None
    if isinstance(x, dict): return parse_y(x.get('value'))
    return None


def safe_smiles_list(field):
    out = []
    if isinstance(field, list):
        for x in field:
            if isinstance(x, dict) and x.get('smiles'):
                out.append(x['smiles'])
            elif isinstance(x, str) and x:
                out.append(x)
    return out


def main():
    print(f'Loading from {RAW}...')
    rxns = []
    for jf in RAW.rglob('*.json'):
        try: d = json.load(open(jf))
        except: continue
        src = d.get('source') or {}
        paper_id = (src.get('doi') or jf.stem) if isinstance(src, dict) else jf.stem
        for r in d.get('reactions') or []:
            rs = safe_smiles_list(r.get('reactants'))
            ps = safe_smiles_list(r.get('products'))
            if not rs or not ps: continue
            rxn_smi = '.'.join(rs) + '>>' + '.'.join(ps)
            yld = None
            for p in r.get('products') or []:
                if isinstance(p, dict):
                    y = parse_y(p.get('yield'))
                    if y is not None: yld = y; break
            cond = r.get('conditions') or {}
            cond_sig = {
                'anode': cond.get('anode'), 'cathode': cond.get('cathode'),
                'cell_type': cond.get('cell_type'),
                'electrolytes': safe_smiles_list(r.get('electrolytes')),
                'solvents': safe_smiles_list(r.get('solvents')),
                'reagents': safe_smiles_list(r.get('reagents')),
                'catalysts': safe_smiles_list(r.get('catalysts')),
                'ligands': safe_smiles_list(r.get('ligands')),
                'additives': safe_smiles_list(r.get('additives')),
            }
            rxns.append({'rxn': rxn_smi, 'rs': rs, 'ps': ps,
                          'paper_id': paper_id, 'yield': yld, 'cond': cond_sig,
                          'paper_file': str(jf.relative_to(RAW))})
    print(f'  {len(rxns)} reactions loaded')

    print('Loading RXNMapper on GPU...')
    mapper = RXNMapper()  # auto picks GPU
    print('  ready')

    out_records = []
    template_counter = Counter()
    n_map_fail = 0; n_tmpl_ok = 0; n_tmpl_fail = 0
    t0 = time.time()
    for batch_start in range(0, len(rxns), BATCH_SIZE):
        batch = rxns[batch_start:batch_start+BATCH_SIZE]
        rxn_smis = [r['rxn'] for r in batch]
        try:
            results = mapper.get_attention_guided_atom_maps(rxn_smis)
        except Exception:
            # try one-by-one fallback for this batch
            results = []
            for s in rxn_smis:
                try:
                    results.append(mapper.get_attention_guided_atom_maps([s])[0])
                except Exception:
                    results.append({'mapped_rxn': None, 'confidence': 0.0})

        for r, res in zip(batch, results):
            mapped = res.get('mapped_rxn')
            conf = res.get('confidence', 0.0)
            tmpl = None
            if mapped is None:
                n_map_fail += 1
            else:
                try:
                    mrs, mps = mapped.split('>>', 1)
                    if ' |' in mps: mps = mps.split(' |')[0]
                    if ' |' in mrs: mrs = mrs.split(' |')[0]
                    t = extract_from_reaction({'_id': batch_start, 'reactants': mrs, 'products': mps})
                    if t and 'reaction_smarts' in t:
                        tmpl = t['reaction_smarts']
                        template_counter[tmpl] += 1
                        n_tmpl_ok += 1
                    else:
                        n_tmpl_fail += 1
                except Exception:
                    n_tmpl_fail += 1

            rec = dict(r)
            rec['mapped'] = mapped
            rec['confidence'] = float(conf) if conf else 0.0
            rec['template'] = tmpl
            out_records.append(rec)

        done = len(out_records)
        if done % (BATCH_SIZE * 10) == 0 or done == len(rxns):
            rate = done / max(time.time() - t0, 1e-3)
            eta = (len(rxns) - done) / rate
            print(f'  {done}/{len(rxns)}  ({rate:.1f} rxn/s, eta {eta/60:.1f} min, '
                  f'map_fail={n_map_fail}, tmpl_fail={n_tmpl_fail}, unique_templates={len(template_counter)})',
                  flush=True)

    print(f'\n[OK] mapping done')
    print(f'  total: {len(out_records)}, map_fail: {n_map_fail}, tmpl_ok: {n_tmpl_ok}, tmpl_fail: {n_tmpl_fail}')
    print(f'  unique templates: {len(template_counter)}')

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / 'reactions_mapped_rxnmapper.json').write_text(
        json.dumps(out_records, indent=1, default=str))
    (OUT_DIR / 'template_freq_rxnmapper.json').write_text(
        json.dumps(dict(template_counter.most_common()), indent=2))

    print(f'\n=== Top 15 templates ===')
    for t, c in template_counter.most_common(15):
        print(f'  [{c:>4d}]  {t[:120]}')

    print(f'\n=== Cluster size distribution ===')
    sizes = sorted(template_counter.values(), reverse=True)
    for label, lo, hi in [('singletons (1)', 1, 1), ('2-5', 2, 5), ('6-10', 6, 10),
                          ('11-50', 11, 50), ('51-100', 51, 100), ('>100', 101, 999999)]:
        n = sum(1 for s in sizes if lo <= s <= hi)
        cov = sum(s for s in sizes if lo <= s <= hi)
        print(f'  {label:15s}: {n:4d} templates, {cov:5d} reactions covered')


if __name__ == '__main__':
    main()
