"""把 data_audited_v3_clean 的反应 FP 从 Morgan 替换成 DRFP, 保留其他所有 label。

输出: data_audited_v3_clean_drfp/{train,val,test}.pt
每个 record 的 reactant_fp/product_fp/diff_fp 全替换成 DRFP 各 2048 bits, 拼接成 6144D。

实际上 DRFP 是反应级别的 (不分 reactant/product 两侧), 所以策略:
  fp_reactant = DRFP(rxn_smiles) 前 2048
  fp_product  = DRFP(rxn_smiles) 中间 2048
  fp_diff     = DRFP(rxn_smiles) 后 2048
让模型继续按 6144D 输入处理, 但底层是 DRFP 同一个 6144D 表征切 3 份。

更干净版本: DRFP 直接 6144D → reactant_fp 字段, product_fp/diff_fp 填 0 → 但这样浪费, 不如全用 DRFP。
我们就用 **DRFP 6144D 全填到 reactant_fp 位置, product/diff fp 全 0**, encoder 就只看 DRFP 6144D。
"""
import sys, json
from pathlib import Path
from tqdm import tqdm

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import torch
from drfp import DrfpEncoder

SRC = Path('yield_prediction/data_audited_v3_clean')
DST = Path('yield_prediction/data_audited_v3_clean_drfp')
DST.mkdir(exist_ok=True)


def build_rxn_smi(r):
    """从 record 构造 reaction SMILES."""
    rs = r['reactant_smiles']
    ps = r['product_smiles']
    # rs/ps 是 list of SMILES
    if isinstance(rs, list): rs = '.'.join(rs)
    if isinstance(ps, list): ps = '.'.join(ps)
    return f'{rs}>>{ps}'


def main():
    for split in ['train', 'val', 'test']:
        recs = torch.load(SRC / f'{split}.pt', weights_only=False)
        print(f'{split}: {len(recs)} records, computing DRFP 6144D...')
        rxn_smis = [build_rxn_smi(r) for r in recs]
        # Batch DRFP 6144D (减少 hash 碰撞 vs 2048)
        fps = DrfpEncoder.encode(rxn_smis, n_folded_length=6144, radius=3, rings=True)
        # 切成 3 份 2048 匹配现有 dataset (Dataset 拼回 6144)
        for r, fp in tqdm(zip(recs, fps), total=len(recs), desc=f'  update {split}'):
            arr = np.asarray(fp, dtype=np.float32)
            assert arr.shape == (6144,), f'unexpected shape {arr.shape}'
            r['reactant_fp'] = arr[:2048]
            r['product_fp']  = arr[2048:4096]
            r['diff_fp']     = arr[4096:6144]
        torch.save(recs, DST / f'{split}.pt')
        print(f'  saved {split}.pt')

    # Copy non-pt metadata
    import shutil
    for fn in ['vocab.json', 'stats.json', 'amount_stats.json', 'fg_stats.json',
               'xtb_stats.json', 'split_meta.json', 'xtb_class_table.pt']:
        if (SRC/fn).exists(): shutil.copy(SRC/fn, DST/fn)

    # 更新 stats.json: feature_dim 没变 (6144), 但标注 DRFP
    stats = json.load(open(DST / 'stats.json'))
    stats['fp_type'] = 'DRFP'
    stats['fp_radius'] = 3
    stats['fp_size_effective'] = 2048
    stats['fp_size_padded'] = 6144  # 前 2048 是 DRFP, 后 4096 是 0
    json.dump(stats, open(DST / 'stats.json', 'w'), indent=2)
    print(f'\\n→ Saved to {DST}/')


if __name__ == '__main__':
    main()
