"""化学严格反应聚类:用 rdkit 解析 atom-mapped SMILES, 抽反应中心 (键变化的原子) 作为签名.
同签名 = 同化学变化类型. Test 反应继承同签名 train 反应的 winning conditions."""
import sys, json, time, re
from pathlib import Path
from collections import defaultdict, Counter

sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages')
sys.path.insert(0, '/inspire/hdd/global_user/gelingli-253914010248/WDproject2/condition_agent')

from rdkit import Chem
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

DATA = Path('data/reaction_templates/reactions_mapped_rxnmapper.json')
OUT_DIR = Path('eval_results/template_analysis')
OUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_y(x):
    if x is None: return None
    if isinstance(x, (int, float)): return float(x)
    return None


def canonical_smi(smi):
    try:
        m = Chem.MolFromSmiles(smi)
        return Chem.MolToSmiles(m) if m else smi
    except Exception:
        return smi


def reaction_center_signature(mapped_rxn):
    """从 atom-mapped SMILES 抽 反应中心签名.
    返回 frozenset of (atom_symbol, frozenset(bonds_gained), frozenset(bonds_lost))
    + unmapped (无对应) atom 也作 trace 信号 (键被打破的 group atom)
    """
    if not mapped_rxn or '>>' not in mapped_rxn:
        return None
    try:
        rs, ps = mapped_rxn.split('>>', 1)
        if ' |' in ps: ps = ps.split(' |')[0]
        if ' |' in rs: rs = rs.split(' |')[0]
        rmol = Chem.MolFromSmiles(rs)
        pmol = Chem.MolFromSmiles(ps)
        if rmol is None or pmol is None: return None
    except Exception:
        return None

    # Build mapping number → atom
    r_atoms = {a.GetAtomMapNum(): a for a in rmol.GetAtoms() if a.GetAtomMapNum() > 0}
    p_atoms = {a.GetAtomMapNum(): a for a in pmol.GetAtoms() if a.GetAtomMapNum() > 0}

    def bond_set(atom):
        """对原子的所有键, 返回 frozenset 键签名 = (邻居原子 symbol, bond_type)"""
        out = []
        for b in atom.GetBonds():
            other = b.GetOtherAtom(atom)
            other_sym = other.GetSymbol()
            other_map = other.GetAtomMapNum()
            bt = b.GetBondTypeAsDouble()
            out.append((other_sym, other_map if other_map > 0 else 0, bt))
        return frozenset(out)

    # 对每个 mapped 共有原子, 看其键发生了什么变化
    changes = []
    common_maps = set(r_atoms.keys()) & set(p_atoms.keys())
    for m in common_maps:
        ra, pa = r_atoms[m], p_atoms[m]
        rb, pb = bond_set(ra), bond_set(pa)
        if rb != pb:
            sym = ra.GetSymbol()
            gained = pb - rb
            lost = rb - pb
            # Normalize: 忽略 邻居原子 map number (只看邻居 atom symbol + bond type)
            gained_anon = frozenset((s, bt) for s, _, bt in gained)
            lost_anon = frozenset((s, bt) for s, _, bt in lost)
            changes.append((sym, gained_anon, lost_anon))

    return frozenset(changes) if changes else None


def main():
    print(f'Loading rxnmapper output from {DATA}...')
    records = json.load(open(DATA))
    print(f'  {len(records)} records')

    # Compute reaction-center signatures
    print('\nComputing reaction-center signatures...')
    t0 = time.time()
    n_sig_ok = 0; n_sig_fail = 0
    for i, r in enumerate(records):
        sig = reaction_center_signature(r.get('mapped'))
        r['rc_sig'] = sig
        if sig is None: n_sig_fail += 1
        else: n_sig_ok += 1
        if (i+1) % 5000 == 0:
            print(f'  {i+1}/{len(records)} ({(i+1)/(time.time()-t0):.0f} rxn/s)', flush=True)
    print(f'  signature OK: {n_sig_ok}, fail: {n_sig_fail}')

    # Cluster by signature
    sig2rxns = defaultdict(list)
    for r in records:
        if r.get('rc_sig') is not None:
            sig2rxns[r['rc_sig']].append(r)
    print(f'  unique signatures: {len(sig2rxns)}')

    # Distribution
    sizes = sorted([len(v) for v in sig2rxns.values()], reverse=True)
    print(f'\n=== Cluster size distribution ===')
    for label, lo, hi in [('singletons', 1, 1), ('2-5', 2, 5), ('6-10', 6, 10),
                          ('11-50', 11, 50), ('51-100', 51, 100), ('>100', 101, 999999)]:
        n = sum(1 for s in sizes if lo <= s <= hi)
        cov = sum(s for s in sizes if lo <= s <= hi)
        print(f'  {label:15s}: {n:4d} clusters, {cov:5d} reactions covered '
              f'({cov/n_sig_ok*100:5.1f}%)')

    # Test / train split
    import torch
    test = torch.load('yield_prediction/data_audited_v3_clean/test.pt', weights_only=False)
    sm = json.load(open('yield_prediction/data_audited_v3_clean/split_meta.json'))
    test_pids = set(sm['test_papers'])
    test_rxn_smis = set()
    for tr in test:
        test_rxn_smis.add('.'.join(tr['reactant_smiles']) + '>>' + '.'.join(tr['product_smiles']))
    SUFFIX = re.compile(r'(_sup_?\d*|_supl_?\d*|_si_?\d*|_esi_?\d*|_sm_?\d*)$', re.I)
    def base_pid(d): return SUFFIX.sub('', d).lower() if d else ''

    train_recs = []; test_recs = []
    for r in records:
        if base_pid(r.get('paper_id', '')) in test_pids or r.get('rxn') in test_rxn_smis:
            test_recs.append(r)
        else:
            train_recs.append(r)
    print(f'\n  train: {len(train_recs)}, test: {len(test_recs)}')

    # Build train-side signature → winning conditions
    print('\nAggregating train winning conditions per signature...')
    train_sigs = defaultdict(list)
    for r in train_recs:
        if r.get('rc_sig') is not None:
            train_sigs[r['rc_sig']].append(r)
    print(f'  train unique signatures: {len(train_sigs)}')

    # For each test record, check if its signature exists in train
    print('\n=== Test coverage by reaction-center signature ===')
    test_with_sig = 0; test_sig_in_train = 0; test_winners_avail = 0
    for r in test_recs:
        if r.get('rc_sig') is None: continue
        test_with_sig += 1
        if r['rc_sig'] in train_sigs:
            test_sig_in_train += 1
            # Check if any train reaction in same cluster has yield>50%
            high = [tr for tr in train_sigs[r['rc_sig']] if tr.get('yield') is not None and tr['yield'] > 50]
            if high: test_winners_avail += 1
    print(f'  test records with signature: {test_with_sig}/{len(test_recs)} ({test_with_sig/len(test_recs)*100:.1f}%)')
    print(f'  test signature found in train: {test_sig_in_train}/{test_with_sig} ({test_sig_in_train/max(test_with_sig,1)*100:.1f}%)')
    print(f'  test with winning-conditions available: {test_winners_avail} ({test_winners_avail/len(test_recs)*100:.1f}%)')

    # Build the lookup: sig (as JSON-encodable str) → train rxn list with winning conditions
    def sig_to_key(sig):
        return json.dumps(sorted([
            [a, sorted([list(p) for p in g]), sorted([list(p) for p in l])]
            for a, g, l in sig
        ]))

    # Build winners by sig
    print('\nBuilding sig → winners JSON for downstream eval...')
    sig_winners = {}
    list_fields = ('electrolytes','solvents','reagents','catalysts')
    for sig, rs in train_sigs.items():
        high = [r for r in rs if r.get('yield') is not None and r['yield'] > 50]
        if not high: continue
        winners = {f: set() for f in list_fields}
        for r in high:
            for f in list_fields:
                smis = sorted([canonical_smi(s) for s in (r.get('cond', {}).get(f, []) or []) if s])
                if smis:
                    winners[f].add(tuple(smis))
        sig_winners[sig_to_key(sig)] = {
            'n_train_rxns': len(rs),
            'n_high_yield': len(high),
            **{f: [list(t) for t in winners[f]] for f in list_fields},
        }

    (OUT_DIR / 'rc_sig_winners.json').write_text(json.dumps(sig_winners, indent=1, default=str))
    print(f'  saved {OUT_DIR}/rc_sig_winners.json ({len(sig_winners)} clusters with winners)')

    # Save per-record reaction-center sig for downstream re-eval
    print('\nSaving per-record sig + train/test flag...')
    out_recs = []
    for r in records:
        out_recs.append({
            'rxn': r.get('rxn'),
            'paper_id': r.get('paper_id'),
            'yield': r.get('yield'),
            'rc_sig_key': sig_to_key(r['rc_sig']) if r.get('rc_sig') is not None else None,
            'in_test': base_pid(r.get('paper_id', '')) in test_pids or r.get('rxn') in test_rxn_smis,
        })
    (OUT_DIR / 'records_with_rc_sig.json').write_text(json.dumps(out_recs, default=str))
    print(f'  saved {OUT_DIR}/records_with_rc_sig.json')

    # Summary stats for the user
    print(f'\n=== Summary ===')
    print(f'  Total reactions: {len(records)}')
    print(f'  Reactions with reaction-center signature: {n_sig_ok}')
    print(f'  Unique reaction-center signatures: {len(sig2rxns)}')
    print(f'  Test coverage with train precedent: {test_sig_in_train/len(test_recs)*100:.1f}%')
    print(f'  Test coverage with winning conditions: {test_winners_avail/len(test_recs)*100:.1f}%')


if __name__ == '__main__':
    main()
