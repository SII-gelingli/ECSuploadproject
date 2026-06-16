"""给 data_audited_v3/{train,val,test}.pt 添加 xtb_feat (33 维) 字段。

xtb_feat = [reactant_agg(11), product_agg(11), diff(11)]
然后用 train 集均值/标准差归一化，存到 data_audited_v3/xtb_stats.json。
"""
import sys
import json
from pathlib import Path

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np
import torch
from tqdm import tqdm

project_root = Path(__file__).parent.parent
DATA_DIR = project_root / 'data_audited_v3'
CACHE_PATH = project_root / 'data' / 'xtb_cache.json'

# 11 维 = 6 xTB QC + 5 RDKit
FEAT_DIM = 11
ZERO = [0.0] * FEAT_DIM


def load_cache():
    obj = json.load(open(CACHE_PATH))
    cache = obj.get('cache', obj)
    return cache


def aggregate(cache, smiles_list):
    """对多个 SMILES 取均值。空列表返回零向量。"""
    if not smiles_list:
        return np.zeros(FEAT_DIM)
    vecs = []
    for smi in smiles_list:
        if not smi:
            continue
        v = cache.get(smi)
        if v is None:
            continue
        vecs.append(np.array(v, dtype=np.float64))
    if not vecs:
        return np.zeros(FEAT_DIM)
    return np.mean(vecs, axis=0)


def main():
    cache = load_cache()
    print(f"Loaded xtb_cache with {len(cache)} entries\n")

    # 加 xtb_feat 字段到每条记录
    all_feats_train = []
    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f"Augment {split}"):
            r_feat = aggregate(cache, r.get('reactant_smiles', []))
            p_feat = aggregate(cache, r.get('product_smiles', []))
            d_feat = p_feat - r_feat
            full = np.concatenate([r_feat, p_feat, d_feat])  # 33 维
            r['xtb_feat'] = full.tolist()
            if split == 'train':
                all_feats_train.append(full)
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f"  saved {split}.pt with xtb_feat ({len(recs)} records)")

    # 用 train 集计算归一化统计
    arr = np.array(all_feats_train)  # (N, 33)
    mean = arr.mean(axis=0)
    std = arr.std(axis=0)
    # 防止除 0
    std = np.where(std < 1e-6, 1.0, std)
    stats = {
        'mean': mean.tolist(),
        'std': std.tolist(),
        'dim': 33,
        'description': '11×3: reactant_agg + product_agg + diff. 11 = 6 xTB QC (total_energy, gap, HOMO, LUMO, dipole, Gsolv) + 5 RDKit (heavy, MW, rotbonds, TPSA, LogP)',
    }
    json.dump(stats, open(DATA_DIR / 'xtb_stats.json', 'w'), indent=2)
    print(f"\nSaved {DATA_DIR / 'xtb_stats.json'}")
    print(f"Sample mean (first 6): {[round(m, 3) for m in mean[:6]]}")
    print(f"Sample std (first 6):  {[round(s, 3) for s in std[:6]]}")


if __name__ == "__main__":
    main()
