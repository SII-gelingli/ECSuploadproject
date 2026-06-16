"""用 Indigo 给全 24K 反应做 atom-atom mapping, 然后用 rdchiral 提取模板."""
import sys, json, time
from pathlib import Path
from collections import defaultdict, Counter

for _p in ('/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',):
    if _p not in sys.path: sys.path.insert(0, _p)

from indigo import Indigo
from rdchiral.template_extractor import extract_from_reaction

RAW = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')
OUT_DIR = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/data/reaction_templates')
OUT_DIR.mkdir(parents=True, exist_ok=True)

ind = Indigo()
ind.setOption('ignore-stereochemistry-errors', True)
ind.setOption('treat-x-as-pseudoatom', True)


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
    # 1) Load all reactions
    print(f'Loading reactions from {RAW}...')
    rxns = []  # (rxn_smiles_unmapped, paper_id, yield, conditions)
    n_paper = 0; n_rxn = 0
    for jf in RAW.rglob('*.json'):
        try: d = json.load(open(jf))
        except: continue
        n_paper += 1
        src = d.get('source') or {}
        paper_id = (src.get('doi') or jf.stem) if isinstance(src, dict) else jf.stem
        for r in d.get('reactions') or []:
            rs = safe_smiles_list(r.get('reactants'))
            ps = safe_smiles_list(r.get('products'))
            if not rs or not ps: continue
            n_rxn += 1
            rxn_smi = '.'.join(rs) + '>>' + '.'.join(ps)
            yld = None
            for p in r.get('products') or []:
                if isinstance(p, dict):
                    y = parse_y(p.get('yield'))
                    if y is not None: yld = y; break
            cond = r.get('conditions') or {}
            cond_sig = {
                'anode': cond.get('anode'),
                'cathode': cond.get('cathode'),
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
    print(f'  {n_paper} papers, {n_rxn} reactions, {len(rxns)} valid')

    # 2) Map with Indigo + extract templates with rdchiral
    print(f'\nMapping + template extraction...')
    out_records = []
    n_map_fail = 0; n_tmpl_fail = 0; n_tmpl_ok = 0
    t0 = time.time()
    template_counter = Counter()  # template_smarts -> count
    for i, r in enumerate(rxns):
        # Indigo mapping
        mapped = None
        try:
            rxn = ind.loadReaction(r['rxn'])
            rxn.automap('discard')
            mapped = rxn.smiles()
        except Exception:
            n_map_fail += 1

        # rdchiral template extraction
        tmpl = None
        if mapped:
            try:
                # split mapped reaction smiles
                mrs, mps = mapped.split('>>', 1)
                # strip |...| extra info if present
                if ' |' in mps: mps = mps.split(' |')[0]
                if ' |' in mrs: mrs = mrs.split(' |')[0]
                t = extract_from_reaction({'_id': i, 'reactants': mrs, 'products': mps})
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
        rec['template'] = tmpl
        out_records.append(rec)

        if (i+1) % 1000 == 0:
            rate = (i+1) / (time.time() - t0)
            eta = (len(rxns) - i - 1) / rate
            print(f'  {i+1}/{len(rxns)}  ({rate:.1f} rxn/s, eta {eta/60:.1f} min, '
                  f'map_fail={n_map_fail}, tmpl_fail={n_tmpl_fail}, unique_templates={len(template_counter)})',
                  flush=True)

    print(f'\n[OK] mapping done')
    print(f'  total rxns: {len(out_records)}')
    print(f'  Indigo map fail: {n_map_fail}')
    print(f'  Template extract OK: {n_tmpl_ok}')
    print(f'  Template extract fail: {n_tmpl_fail}')
    print(f'  Unique templates: {len(template_counter)}')

    # Save raw mapped + template records
    out_path = OUT_DIR / 'reactions_mapped_v1.json'
    out_path.write_text(json.dumps(out_records, indent=1, default=str))
    print(f'  saved {out_path}  ({out_path.stat().st_size/1e6:.1f} MB)')

    # Save template histogram
    tmpl_dist = OUT_DIR / 'template_freq.json'
    tmpl_dist.write_text(json.dumps(dict(template_counter.most_common()), indent=2))
    print(f'  saved template freq: {tmpl_dist}')

    # Print top 15 templates
    print(f'\n=== Top 15 most frequent templates ===')
    for t, c in template_counter.most_common(15):
        print(f'  [{c:>4d}]  {t[:120]}')

    # Cluster size distribution
    print(f'\n=== Template cluster size distribution ===')
    sizes = sorted(template_counter.values(), reverse=True)
    print(f'  singletons (1 rxn): {sum(1 for s in sizes if s == 1)}')
    print(f'  2-5 rxns:           {sum(1 for s in sizes if 2 <= s <= 5)}')
    print(f'  6-10 rxns:          {sum(1 for s in sizes if 6 <= s <= 10)}')
    print(f'  11-50 rxns:         {sum(1 for s in sizes if 11 <= s <= 50)}')
    print(f'  51-100 rxns:        {sum(1 for s in sizes if 51 <= s <= 100)}')
    print(f'  >100 rxns:          {sum(1 for s in sizes if s > 100)}')


if __name__ == '__main__':
    main()
