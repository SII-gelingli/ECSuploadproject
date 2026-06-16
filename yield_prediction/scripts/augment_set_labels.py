"""给 data_audited_v3/*.pt 加 set_labels 字段, 用于 Set Prediction 训练。

只对最多组分的三个 head 做 set:
- solvent (44.7% multi)
- reagent (28% multi)
- catalyst (19.8% multi)

set_labels[head]: list of int (vocab indices), 最多 K_MAX=4。
不在 vocab 的 SMILES 转成 OTHER (idx=1)。空 → [0] (ABSENT)。
"""
import sys, json
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import torch
from tqdm import tqdm
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
DATA_DIR = project_root / 'data_audited_v3'
RAW_ROOT = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')

# Set heads
SET_HEADS = ['solvent', 'reagent', 'catalyst']
K_MAX = 4  # 每个 head 最多保留 4 个组分

# ABSENT=0, OTHER=1
IDX_ABSENT = 0
IDX_OTHER = 1


def load_vocab():
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    # vocab[head] = {smi: idx}, idx start from 2
    return {h: vocab[h] for h in SET_HEADS}


_canon_cache = {}


def canonicalize(smi):
    if not smi: return smi
    if smi in _canon_cache: return _canon_cache[smi]
    try:
        from rdkit import Chem
        mol = Chem.MolFromSmiles(smi)
        canon = Chem.MolToSmiles(mol, canonical=True) if mol else smi
    except Exception:
        canon = smi
    _canon_cache[smi] = canon
    return canon


def get_smiles_list_from_rxn(rxn, role):
    """从 v2 reaction 的某个 role list 取所有有 SMILES 的条目 (canonical 化)"""
    items = rxn.get(role + 's') or rxn.get(role) or []
    return [canonicalize(it.get('smiles')) for it in items if isinstance(it, dict) and it.get('smiles')]


def smiles_to_idx(smiles, vocab_h):
    """SMILES → vocab idx, 不在词表 → OTHER"""
    return vocab_h.get(smiles, IDX_OTHER)


def main():
    vocabs = load_vocab()
    print(f"Vocab sizes: solvent={len(vocabs['solvent'])}, reagent={len(vocabs['reagent'])}, catalyst={len(vocabs['catalyst'])}")

    # 我们需要从 raw json 重新读 multi-SMILES (data_audited_v3 里只存了第一个)
    # 先建 paper_id → raw smiles set 索引
    print("\nLoading raw v2 data to extract multi-substance info ...")
    raw_index = {}  # (doi, page, table_index, row_index) → {role: [smiles]}
    for fp in tqdm(list(RAW_ROOT.rglob('*.json')), desc='raw'):
        try:
            d = json.loads(fp.read_text())
        except: continue
        for rxn in d.get('reactions', []):
            src = rxn.get('source', {})
            key = (src.get('doi', ''), src.get('page', -1),
                   src.get('table_index', -1), src.get('row_index', -1))
            roles = {}
            for role in SET_HEADS:
                smis = get_smiles_list_from_rxn(rxn, role)
                if smis:
                    roles[role] = smis
            if roles:
                raw_index[key] = roles
    print(f"  Built raw index: {len(raw_index)} keys")

    # 对每个 split 增广 set_labels
    distribution = {split: {h: Counter() for h in SET_HEADS} for split in ['train','val','test']}
    fallback_count = {split: 0 for split in ['train','val','test']}

    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f"set {split}"):
            set_labels = {}
            # 用 first-smiles + label 反查; 但还需要 raw multi-smiles
            # data_audited_v3 不直接保存 source key, 所以我们用 reactant SMILES 作 key 近似
            # 简化方案: 用 record 的 reactant_smiles + product_smiles 拼成签名匹配 raw_index
            # 实际上 raw_index 是 dict, 我们改用 reaction_smiles 字段
            # data_audited_v3 records 应该有 reactant_smiles
            r_smi = tuple(sorted(r.get('reactant_smiles', [])))
            p_smi = tuple(sorted(r.get('product_smiles', [])))
            # 双向匹配 raw_index (因为 source key 在 v3 数据没存)
            matched = None
            # 简便起见: 把 raw_index 重建为 reactant→roles
            # 但要遍历整个 raw_index 太慢; 改为预先按 (reactant_set, product_set) 建索引
            # 这里先用 fallback: 用 first-smiles 标作单元素 set
            if matched is None:
                for h in SET_HEADS:
                    first_idx = r['labels'][h]
                    if first_idx == IDX_ABSENT:
                        set_labels[h] = [IDX_ABSENT]
                    else:
                        set_labels[h] = [first_idx]  # fallback: 单元素
                fallback_count[split] += 1
            r['set_labels'] = set_labels
            for h in SET_HEADS:
                distribution[split][h][len(set_labels[h])] += 1
        # 不存了, 走 raw_index 二次遍历
        # 实际上为了完整, 我们重做: 用 (sorted reactant smi tuple) 作 key 建索引
        # 但这里先放着, 下一步重做

    # 注意: 上面 fallback 全部走了"单元素", 没拿到真实 multi-set
    # 现在重建: raw_index 用 (sorted reactant tuple) 作 key (因为同一篇论文同一行的反应在 v3 里也是这样切割)
    print("\nRebuilding raw index by reactant tuple ...")
    raw_by_reactant = {}
    for fp in tqdm(list(RAW_ROOT.rglob('*.json')), desc='raw2'):
        try:
            d = json.loads(fp.read_text())
        except: continue
        for rxn in d.get('reactions', []):
            reactants = rxn.get('reactants') or []
            r_smis = tuple(sorted([r.get('smiles') for r in reactants if isinstance(r, dict) and r.get('smiles')]))
            if not r_smis: continue
            roles = {}
            for role in SET_HEADS:
                smis = get_smiles_list_from_rxn(rxn, role)
                if smis:
                    roles[role] = smis
            if roles:
                # 同一 reactant 可能多次出现 (同篇论文不同条件), 我们保留最长的 set
                cur = raw_by_reactant.get(r_smis, {})
                for h, smis in roles.items():
                    if h not in cur or len(smis) > len(cur[h]):
                        cur[h] = smis
                raw_by_reactant[r_smis] = cur
    print(f"  raw_by_reactant: {len(raw_by_reactant)} unique reactant sets")

    # 第二遍正式增广
    distribution = {split: {h: Counter() for h in SET_HEADS} for split in ['train','val','test']}
    match_count = {split: 0 for split in ['train','val','test']}
    no_match_count = {split: 0 for split in ['train','val','test']}

    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f"set2 {split}"):
            r_smi = tuple(sorted(r.get('reactant_smiles', [])))
            raw_roles = raw_by_reactant.get(r_smi)
            set_labels = {}
            if raw_roles:
                match_count[split] += 1
                for h in SET_HEADS:
                    if h in raw_roles:
                        # 取所有 smiles 转 idx
                        idxs = [smiles_to_idx(s, vocabs[h]) for s in raw_roles[h]][:K_MAX]
                        # 去重保序
                        seen = set(); uniq = []
                        for i in idxs:
                            if i not in seen:
                                seen.add(i); uniq.append(i)
                        set_labels[h] = uniq if uniq else [IDX_ABSENT]
                    else:
                        set_labels[h] = [IDX_ABSENT]
            else:
                no_match_count[split] += 1
                # fallback to first-smiles label
                for h in SET_HEADS:
                    set_labels[h] = [r['labels'][h]]
            r['set_labels'] = set_labels
            for h in SET_HEADS:
                distribution[split][h][len(set_labels[h])] += 1
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f"  {split}: matched {match_count[split]}, fallback {no_match_count[split]}")

    print(f"\nSet 大小分布:")
    for split in ['train', 'val', 'test']:
        print(f"\n{split}:")
        for h in SET_HEADS:
            c = distribution[split][h]
            tot = sum(c.values())
            line = f"  {h:<10}"
            for k in [1, 2, 3, 4]:
                line += f"  {k}={c.get(k,0)/tot*100:5.1f}%"
            print(line)


if __name__ == "__main__":
    main()
