"""给 data_audited_v3/{train,val,test}.pt 加 reagent_class 标签 (0=ABSENT, 1=OTHER, 2+=具体类)。

同时更新 stats.json 加 num_classes['reagent_class']。
"""
import sys, json
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch
from tqdm import tqdm
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from utils.reagent_classifier import classify_reagent, get_class_name, N_CLASSES

DATA_DIR = project_root / 'data_audited_v3'


def main():
    # 加载 vocab 反查 reagent_label → SMILES
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    reagent_smi2idx = vocab['reagent']
    # 反向: idx → smi (idx=0 是 ABSENT, idx=1 是 OTHER, idx>=2 是 真实 SMILES)
    idx2smi = {v: k for k, v in reagent_smi2idx.items()}
    print(f"Reagent vocab size: {len(reagent_smi2idx)}")

    # 预先把每个 reagent idx 转成 class (一次性，避免每条反应都跑 SMARTS)
    idx2class = {0: 0, 1: 1}  # ABSENT/OTHER 直接对应
    for smi, idx in tqdm(reagent_smi2idx.items(), desc="classify vocab"):
        if smi in ('__ABSENT__', '__OTHER__'):
            idx2class[idx] = 0 if smi == '__ABSENT__' else 1
        else:
            idx2class[idx] = classify_reagent(smi)

    # 1. 给每条 record 加 reagent_class label (从 reagent label 反查)
    distribution = {'train': Counter(), 'val': Counter(), 'test': Counter()}
    for split in ['train', 'val', 'test']:
        recs = torch.load(DATA_DIR / f'{split}.pt', weights_only=False)
        for r in tqdm(recs, desc=f"label {split}"):
            reagent_idx = r['labels']['reagent']
            cls = idx2class.get(reagent_idx, 0)
            r['labels']['reagent_class'] = cls
            distribution[split][cls] += 1
        torch.save(recs, DATA_DIR / f'{split}.pt')
        print(f"  Saved {split}.pt with {len(recs)} records")

    # 2. 更新 stats.json
    stats = json.load(open(DATA_DIR / 'stats.json'))
    stats['num_classes']['reagent_class'] = N_CLASSES
    json.dump(stats, open(DATA_DIR / 'stats.json', 'w'), indent=2)
    print(f"\nstats.json: reagent_class 类别数 = {N_CLASSES}")

    print("\n各 split 类分布 (top 10):")
    for split in ['train', 'val', 'test']:
        print(f"\n{split} (n={sum(distribution[split].values())}):")
        for cls, cnt in distribution[split].most_common(10):
            name = get_class_name(cls)
            pct = cnt / sum(distribution[split].values()) * 100
            print(f"  {cls:2d} {name:<25} {cnt:5d} ({pct:5.1f}%)")


if __name__ == "__main__":
    main()
