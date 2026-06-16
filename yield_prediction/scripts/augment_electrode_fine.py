"""给 data_audited_v3_clean 加 anode_fine / cathode_fine 细粒度标签.

Vocab 从实际数据构建 (≥3 样本的细类保留, 否则归 'unknown_electrode').
输出: 更新 train/val/test.pt + stats.json (num_classes['anode_fine'/'cathode_fine'])
       + vocab.json (anode_fine_classes/cathode_fine_classes)
"""
import sys, json
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import torch
from tqdm import tqdm

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from utils.electrode_fine_classifier import classify_electrode_fine

DATA_DIR = project_root / 'data_audited_v3_clean'
SRC = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')


def main():
    # === 1. 扫 raw 数据建 vocab ===
    raw_anode = Counter(); raw_cathode = Counter()
    paper_lookup = {}  # paper_id (from filename) → list of (anode_raw, cathode_raw)
    print('Scanning raw data...')
    for jf in tqdm(list(SRC.rglob('*.json'))):
        try:
            d = json.load(open(jf))
        except: continue
        # paper_id 从文件名生成
        pid = jf.stem.lower()
        # 取该 paper 所有反应的电极
        for r in d.get('reactions', []):
            co = r.get('conditions', {}).get('electrochemistry', {})
            a = (co.get('anode') or '').strip()
            ca = (co.get('cathode') or '').strip()
            ac = classify_electrode_fine(a)
            cc = classify_electrode_fine(ca)
            raw_anode[ac] += 1
            raw_cathode[cc] += 1
            paper_lookup.setdefault(pid, []).append((ac, cc))

    # vocab: 频次 ≥3 才保留, 否则归 unknown
    MIN_FREQ = 3
    anode_keep = [c for c, n in raw_anode.most_common() if n >= MIN_FREQ]
    cathode_keep = [c for c, n in raw_cathode.most_common() if n >= MIN_FREQ]
    # 必须含 ABSENT + unknown
    for must in ['ABSENT', 'unknown_electrode']:
        if must not in anode_keep: anode_keep.append(must)
        if must not in cathode_keep: cathode_keep.append(must)
    anode_vocab = anode_keep
    cathode_vocab = cathode_keep
    print(f'\nAnode fine vocab: {len(anode_vocab)} classes')
    print(f'Cathode fine vocab: {len(cathode_vocab)} classes')

    anode_id = {n: i for i, n in enumerate(anode_vocab)}
    cathode_id = {n: i for i, n in enumerate(cathode_vocab)}
    UNK_A = anode_id['unknown_electrode']
    UNK_C = cathode_id['unknown_electrode']

    # === 2. 给 train/val/test.pt 加 label ===
    # 需要从 records 反查原始电极 (但 records 没存 raw text)
    # → 用 records 的 reactant_smiles + product_smiles 找原始 json
    # 简化: 直接重新扫 raw json, 用 reaction_smiles 配对
    # 这里取巧: rebuild mapping by reaction_smiles
    print('\nBuilding reaction → fine_electrode mapping from raw JSONs...')
    rxn_to_fine = {}  # (rxn_smiles_str) → (anode_fine_id, cathode_fine_id, paper_id)
    for jf in tqdm(list(SRC.rglob('*.json'))):
        try:
            d = json.load(open(jf))
        except: continue
        pid = jf.stem.lower()
        for r in d.get('reactions', []):
            rs = r.get('reactants', []); ps = r.get('products', [])
            if isinstance(rs, list) and rs and isinstance(rs[0], dict):
                rs = [x.get('smiles') for x in rs if isinstance(x, dict) and x.get('smiles')]
            if isinstance(ps, list) and ps and isinstance(ps[0], dict):
                ps = [x.get('smiles') for x in ps if isinstance(x, dict) and x.get('smiles')]
            if not rs or not ps: continue
            key = '.'.join(rs) + '>>' + '.'.join(ps)
            co = r.get('conditions', {}).get('electrochemistry', {})
            a = (co.get('anode') or '').strip()
            ca = (co.get('cathode') or '').strip()
            ac = classify_electrode_fine(a)
            cc = classify_electrode_fine(ca)
            a_id = anode_id.get(ac, UNK_A)
            c_id = cathode_id.get(cc, UNK_C)
            rxn_to_fine[key] = (a_id, c_id)

    print(f'\nIndexed {len(rxn_to_fine)} unique reactions')

    # 给每个 split 加 label
    n_matched = 0; n_total = 0
    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f'augment {split}'):
            n_total += 1
            rs = r.get('reactant_smiles', [])
            ps = r.get('product_smiles', [])
            if isinstance(rs, list): rs_join = '.'.join(rs)
            else: rs_join = str(rs)
            if isinstance(ps, list): ps_join = '.'.join(ps)
            else: ps_join = str(ps)
            key = rs_join + '>>' + ps_join
            if key in rxn_to_fine:
                a_id, c_id = rxn_to_fine[key]
                n_matched += 1
            else:
                a_id, c_id = UNK_A, UNK_C
            r['labels']['anode_fine'] = a_id
            r['labels']['cathode_fine'] = c_id
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f'  {split} done')
    print(f'\nMatched {n_matched}/{n_total} reactions to fine electrode labels')

    # === 3. 更新 stats + vocab ===
    stats = json.load(open(DATA_DIR / 'stats.json'))
    stats['num_classes']['anode_fine'] = len(anode_vocab)
    stats['num_classes']['cathode_fine'] = len(cathode_vocab)
    json.dump(stats, open(DATA_DIR / 'stats.json', 'w'), indent=2)

    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    vocab.setdefault('__v3__', {})
    vocab['__v3__']['anode_fine'] = anode_vocab
    vocab['__v3__']['cathode_fine'] = cathode_vocab
    json.dump(vocab, open(DATA_DIR / 'vocab.json', 'w'), ensure_ascii=False, indent=1)

    print(f"\n✓ Saved. anode_fine={len(anode_vocab)} cathode_fine={len(cathode_vocab)}")
    print('Top 15 anode fine classes:')
    for c, n in raw_anode.most_common(15):
        if c in anode_id:
            print(f'  {c:<35} (idx {anode_id[c]:2d}) {n} reactions')


if __name__ == '__main__':
    main()
