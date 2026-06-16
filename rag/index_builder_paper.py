"""Build a paper-aware reaction retrieval index from reactions_by_journal_alkene_ec_audited/.

输出:
  data/reaction_db_paper.pkl  : list[dict] — 每个反应一个 dict, 含 canonical paper_id
  data/faiss_index_paper.bin  : FAISS IndexFlatIP (L2-normalized 6144D 向量)

每个记录字段:
  - reaction_smiles, reactants, products, yield (float|None)
  - anode, cathode, cell_type, electrolyte, solvents, reagents, catalysts, ligands, additives
  - paper_id (canonical), paper_file, journal, citation

Usage:
  python3 rag/index_builder_paper.py [--raw RAW_DIR] [--out_db PATH] [--out_index PATH]
"""
import sys, json, argparse, pickle
from pathlib import Path
from collections import defaultdict

for _p in ('/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models.loader import ModelManager
from utils.smiles_utils import compute_reaction_fingerprint


# ── inline minimal paper_id / alias logic (copied from yield_prediction/scripts/prepare_data_audited.py)
import re
from collections import defaultdict as _dd

_NOCITE_CUTOFF = re.compile(
    r'(?:_\d+_table|_table|-entry.*|_scope.*|_rxn\d*|_figure.*|_scheme.*|_supp.*).*$', re.I)

_WILEY_JOURNAL_TO_DOI_PREFIX = {
    'eurjoc': '10.1002_ejoc.', 'angew': '10.1002_anie.', 'chemistry': '10.1002_chem.',
    'advsynthcatal': '10.1002_adsc.', 'chemsuschem': '10.1002_cssc.',
    'chemasianj': '10.1002_asia.', 'asianjoc': '10.1002_ajoc.',
    'slct': '10.1002_slct.', 'chemcatchem': '10.1002_cctc.',
    'chemistryselect': '10.1002_slct.',
}


def _extract_embedded_doi(fp_name):
    if not fp_name: return None
    s = re.sub(r'\.json$', '', fp_name).lower()
    m = re.search(r'(10\.\d{4,5}_\S+)', s)
    if not m: return None
    s = m.group(1)
    s = _NOCITE_CUTOFF.sub('', s)
    s = re.sub(r'_\d{1,3}$', '', s)
    return s if s.startswith('10.') else None


def paper_id(doi, fp_name):
    if doi:
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_supplementary.*|_si1|si_1)$', '', doi.lower())
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_si1|si_1)', '', pid)
        return pid
    embedded = _extract_embedded_doi(fp_name)
    if embedded: return embedded
    base = re.sub(r'\.json$', '', fp_name)
    base = re.sub(r'_p\d+_t\d+.*$', '', base)
    base = re.sub(r'(_sup_?\d*|_si_?\d*|_supl_?\d*|_si1|si_1)', '', base)
    return base.lower()


def _article_number_token(s):
    if not s: return None
    s = s.lower()
    s = re.sub(r'\.json$', '', s)
    s = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_supplementary.*|_si1|si_1).*$', '', s)
    s = re.sub(r'_p\d+_t\d+.*$', '', s)
    m = re.search(r'(?:^|[\._/])(?:e|ejoc\.|anie\.|ange\.|chem\.|adsc\.|cssc\.|slct\.|asia\.|ajoc\.|cctc\.|ardp\.)(20\d{7})(?:$|[^\d])', s)
    if m: return m.group(1)
    m = re.search(r'(?:^|[\._/])e(20\d{6})(?:$|[^\d])', s)
    if m: return m.group(1)
    m = re.search(r's\-?(\d{4})\-(\d{6,})', s)
    if m: return m.group(1) + m.group(2)
    m = re.search(r'acs\.\w+\.(\d{1,2}[a-z]\d{4,5})', s)
    if m: return m.group(1)
    return None


def build_paper_alias_table(raw_dir):
    raw_dir = Path(raw_dir)
    by_key = _dd(list)
    for fp in raw_dir.rglob('*.json'):
        try:
            with open(fp) as f: d = json.load(f)
        except Exception:
            continue
        src = d.get('source') or {}
        if not isinstance(src, dict): src = {}
        doi = src.get('doi', '') or ''
        journal = (src.get('journal', '') or '').lower()
        tok = _article_number_token(doi) if doi else _article_number_token(fp.name)
        if not tok: continue
        old_pid = paper_id(doi, fp.name)
        by_key[(journal, tok)].append((doi, fp.name, old_pid))
    alias = {}
    for (journal, tok), entries in by_key.items():
        doi_entries = [e for e in entries if e[0]]
        if doi_entries:
            canonical = doi_entries[0][2]
        elif journal in _WILEY_JOURNAL_TO_DOI_PREFIX:
            canonical = _WILEY_JOURNAL_TO_DOI_PREFIX[journal] + tok
        else:
            continue
        for doi, fname, old_pid in entries:
            if old_pid != canonical:
                alias[old_pid] = canonical
    return alias


def canonical_paper_id(doi, fp_name, alias_table=None):
    pid = paper_id(doi, fp_name)
    return alias_table.get(pid, pid) if alias_table else pid


def parse_yield_string(s):
    if not s: return None
    val = str(s).strip().lower().replace('％', '%').replace(' ', '')
    if val in ('', '-', 'n.d.', 'nd', 'n.d', 'n.r.', 'nr', 'n.r'): return None
    if val in ('trace', 'traces'): return 0.5
    try: return float(val.rstrip('%'))
    except (ValueError, TypeError): return None


def parse_smiles_list(field):
    if not field: return []
    if isinstance(field, list):
        out = []
        for x in field:
            if isinstance(x, dict) and x.get('smiles'):
                out.append(x['smiles'])
            elif isinstance(x, str) and x:
                out.append(x)
        return out
    return []


def first_smiles(field):
    xs = parse_smiles_list(field)
    return xs[0] if xs else ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw', default='/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')
    ap.add_argument('--out_db', default=str(PROJECT_ROOT / 'data' / 'reaction_db_paper.pkl'))
    ap.add_argument('--out_index', default=str(PROJECT_ROOT / 'data' / 'faiss_index_paper.bin'))
    ap.add_argument('--out_npy', default=str(PROJECT_ROOT / 'data' / 'reaction_matrix_paper.npy'))
    args = ap.parse_args()

    raw = Path(args.raw)
    print(f'Building alias table from {raw}...')
    alias = build_paper_alias_table(raw)
    print(f'  alias entries: {len(alias)}')

    print('Loading ModelManager (for FP)...')
    mm = ModelManager()

    print(f'Scanning paper JSONs in {raw}...')
    db = []
    fps = []
    n_paper = 0
    n_no_rxn = 0
    n_bad_fp = 0
    for jf in raw.rglob('*.json'):
        try: d = json.load(open(jf))
        except: continue
        src = d.get('source') or {}
        doi = src.get('doi') or ''
        journal = src.get('journal') or ''
        citation = src.get('citation') or ''
        pid = canonical_paper_id(doi, jf.name, alias)
        n_paper += 1

        for ri, r in enumerate(d.get('reactions') or []):
            rs = parse_smiles_list(r.get('reactants'))
            ps = parse_smiles_list(r.get('products'))
            if not rs or not ps:
                n_no_rxn += 1; continue
            rxn = '.'.join(rs) + '>>' + '.'.join(ps)

            # FP
            try:
                fp = compute_reaction_fingerprint(rs, ps, mm.mol_extractor)
            except Exception:
                n_bad_fp += 1; continue
            if fp is None or len(fp) != 6144:
                n_bad_fp += 1; continue

            # yield (取第一个 product 的 yield)
            yld = None
            for p in r.get('products') or []:
                if isinstance(p, dict):
                    yld = parse_yield_string(p.get('yield'))
                    if yld is not None: break

            cond = r.get('conditions') or {}
            entry = {
                'reaction_smiles': rxn,
                'reactants': rs,
                'products': ps,
                'yield': yld,
                'anode': cond.get('anode'),
                'cathode': cond.get('cathode'),
                'cell_type': cond.get('cell_type'),
                'electrolyte': first_smiles(r.get('electrolytes')),
                'solvents': parse_smiles_list(r.get('solvents')),
                'reagent': first_smiles(r.get('reagents')),
                'reagents': parse_smiles_list(r.get('reagents')),
                'catalyst': first_smiles(r.get('catalysts')),
                'catalysts': parse_smiles_list(r.get('catalysts')),
                'ligands': parse_smiles_list(r.get('ligands')),
                'additives': parse_smiles_list(r.get('additives')),
                'current_mA': cond.get('current_mA'),
                'current_density_mA_cm2': cond.get('current_density'),
                'potential_V': cond.get('potential_V'),
                'paper_id': pid,
                'paper_file': str(jf.relative_to(raw)),
                'journal': journal,
                'citation': citation,
            }
            db.append(entry)
            fps.append(fp.astype(np.float32))

        if n_paper % 200 == 0:
            print(f'  scanned {n_paper} papers, db size = {len(db)}', flush=True)

    print(f'\n[OK] {n_paper} papers, {len(db)} reactions kept, {n_no_rxn} skipped (no smiles), {n_bad_fp} skipped (bad fp)')

    # Build matrix
    M = np.stack(fps, axis=0)
    norms = np.linalg.norm(M, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    M = M / norms
    print(f'matrix shape: {M.shape}')

    Path(args.out_db).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out_db, 'wb') as f: pickle.dump(db, f)
    print(f'  wrote db: {args.out_db}')

    # Try FAISS; fall back to npy
    try:
        import faiss
        idx = faiss.IndexFlatIP(M.shape[1])
        idx.add(M)
        faiss.write_index(idx, args.out_index)
        print(f'  wrote faiss: {args.out_index}')
    except Exception as e:
        print(f'  (faiss skipped: {e}) saving npy instead')
        np.save(args.out_npy, M)
        print(f'  wrote npy: {args.out_npy}')


if __name__ == '__main__':
    main()
