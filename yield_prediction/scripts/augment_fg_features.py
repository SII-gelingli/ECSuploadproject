"""把 72 维 FG 计数特征加到 data_audited_v3/{train,val,test}.pt 的 'fg_feat' 字段。

同时保存 train 集均值/std 用于归一化, 写入 data_audited_v3/fg_stats.json。
"""
import sys, json
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
sys.path.insert(0, str(project_root))
from utils.fg_features import reaction_fg_features, REACTION_FG_DIM

DATA_DIR = project_root / 'data_audited_v3'


def main():
    all_fg_train = []
    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f"FG {split}"):
            fg = reaction_fg_features(r.get('reactant_smiles', []), r.get('product_smiles', []))
            r['fg_feat'] = fg.tolist()
            if split == 'train':
                all_fg_train.append(fg)
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f"  saved {split}.pt ({len(recs)} records)")

    arr = np.array(all_fg_train)
    mean = arr.mean(axis=0)
    std = arr.std(axis=0)
    std = np.where(std < 1e-6, 1.0, std)
    json.dump({
        'mean': mean.tolist(),
        'std': std.tolist(),
        'dim': REACTION_FG_DIM,
        'description': '22 FG counts + heavy_atoms + ring_count per molecule, aggregated to reactant + product + diff (72 dims)',
    }, open(DATA_DIR / 'fg_stats.json', 'w'), indent=2)
    print(f"\nSaved {DATA_DIR / 'fg_stats.json'}")
    print(f"Sample mean (first 6 FGs): {[round(m,2) for m in mean[:6]]}")


if __name__ == "__main__":
    main()
