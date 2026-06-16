"""为每个 head 的每个 class 预计算 11D xTB 描述符。

输出:
  data_audited_v3_clean/xtb_class_table.pt   — dict {head: tensor[N_classes, 11]}

策略:
  - SMILES vocab head (solvent/electrolyte/catalyst/reagent/ligand/additive):
      每个 idx → 对应 SMILES → xtb_cache 查 11D 向量, 缺失/失败用 0.
  - Class vocab head (v3 类: anode_material/cathode_material/cell_class_v3/
    electrolyte_cation/electrolyte_anion/ligand_class_v3/additive_class_v3/
    reagent_class_v3/catalyst_class_v3/solvent_class_v3):
      对每个 v3 类, 找训练集中所有该类样本的对应 SMILES 列表,
      取 xtb 11D 的平均(只在 QC 数据有效时计入).
  - 类粒度规范化: 每个 head 内做 z-score (跨类), 失败位置用 0(=均值).
"""
import sys, json
from pathlib import Path
from collections import defaultdict

for _p in ('/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import torch

project_root = Path(__file__).resolve().parent.parent
DATA_DIR = project_root / 'data_audited_v3_clean'
CACHE = project_root / 'data' / 'xtb_cache.json'
OUT_FILE = DATA_DIR / 'xtb_class_table.pt'


def get_xtb(cache, smi):
    """Return 11D vector, or None if invalid/all-zero QC."""
    if smi not in cache:
        return None
    v = cache[smi]
    if len(v) != 11:
        return None
    arr = np.asarray(v, dtype=np.float32)
    return arr


def has_qc(vec):
    return vec is not None and any(abs(x) > 1e-9 for x in vec[:6])


def main():
    cache = json.load(open(CACHE))['cache']
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    stats = json.load(open(DATA_DIR / 'stats.json'))
    nc = stats['num_classes']
    nc_v3 = stats['num_classes_v3']
    DIM = 11

    print(f'Cache size: {len(cache)}, 准备构建 xTB class table...')

    table = {}

    # --- A. SMILES vocab heads (直接索引)
    SMI_HEADS = ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']
    for h in SMI_HEADS:
        n = nc[h]
        mat = np.zeros((n, DIM), dtype=np.float32)
        mask = np.zeros(n, dtype=np.bool_)
        inv = {v: k for k, v in vocab[h].items()}
        n_ok = 0; n_qc = 0
        for idx in range(n):
            smi = inv.get(idx, None)
            if smi is None or smi.startswith('__'):
                continue
            vec = get_xtb(cache, smi)
            if vec is None:
                continue
            mat[idx] = vec
            mask[idx] = True
            n_ok += 1
            if has_qc(vec): n_qc += 1
        print(f'  [{h:<12}] {n_ok}/{n} 有特征, {n_qc}/{n} 有 QC 数据 ({n_qc/n*100:.1f}%)')
        table[h] = {'feat': mat, 'mask': mask.astype(np.float32)}

    # --- B. v3 class heads (类聚合: 对每个类, 平均其所有 SMILES 的 xtb)
    # 通过 train.pt 找每个 v3 class 对应的 SMILES 集合
    train = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    # 头映射: v3_class_head -> (smi_head, 类id)
    HIER_MAP = {
        'reagent_class_v3': 'reagent',
        'catalyst_class_v3': 'catalyst',
        'solvent_class_v3': 'solvent',
        'ligand_class_v3': 'ligand',
        'additive_class_v3': 'additive',
    }
    # anode_material / cathode_material / electrolyte_cation / electrolyte_anion /
    # cell_class_v3 不直接对应 SMILES — 取相关字段的 xtb 平均
    AGG_MAP = {
        'anode_material': 'anode',      # 但 anode 不是 SMILES
        'cathode_material': 'cathode',
        'electrolyte_cation': 'electrolyte',
        'electrolyte_anion': 'electrolyte',
    }

    # B1. hier 类 — 通过 SMILES vocab 聚合
    for v3_head, smi_head in HIER_MAP.items():
        n = nc_v3[v3_head]
        sums = np.zeros((n, DIM), dtype=np.float64)
        cnts = np.zeros(n, dtype=np.int64)
        inv = {v: k for k, v in vocab[smi_head].items()}
        for r in train:
            v3_id = int(r['labels'][v3_head])
            smi_id = int(r['labels'][smi_head])
            smi = inv.get(smi_id, None)
            if smi is None or smi.startswith('__'): continue
            vec = get_xtb(cache, smi)
            if vec is None: continue
            sums[v3_id] += vec
            cnts[v3_id] += 1
        mat = np.zeros((n, DIM), dtype=np.float32)
        mask = np.zeros(n, dtype=np.bool_)
        for i in range(n):
            if cnts[i] > 0:
                mat[i] = sums[i] / cnts[i]
                mask[i] = True
        print(f'  [{v3_head:<22}] {int(mask.sum())}/{n} 类有特征 (聚合 train SMILES)')
        table[v3_head] = {'feat': mat, 'mask': mask.astype(np.float32)}

    # B2. electrolyte_cation / electrolyte_anion — 通过 electrolyte SMILES 聚合
    for v3_head in ('electrolyte_cation', 'electrolyte_anion'):
        n = nc_v3[v3_head]
        sums = np.zeros((n, DIM), dtype=np.float64)
        cnts = np.zeros(n, dtype=np.int64)
        inv = {v: k for k, v in vocab['electrolyte'].items()}
        for r in train:
            id3 = int(r['labels'][v3_head])
            smi_id = int(r['labels']['electrolyte'])
            smi = inv.get(smi_id, None)
            if smi is None or smi.startswith('__'): continue
            vec = get_xtb(cache, smi)
            if vec is None: continue
            sums[id3] += vec
            cnts[id3] += 1
        mat = np.zeros((n, DIM), dtype=np.float32)
        mask = np.zeros(n, dtype=np.bool_)
        for i in range(n):
            if cnts[i] > 0:
                mat[i] = sums[i] / cnts[i]
                mask[i] = True
        print(f'  [{v3_head:<22}] {int(mask.sum())}/{n} 类有特征 (聚合 electrolyte)')
        table[v3_head] = {'feat': mat, 'mask': mask.astype(np.float32)}

    # B3. anode_material / cathode_material — 没有 SMILES, 跳过(留 0)
    # 也建表但全 0 (模型不会从中得到信号)
    for v3_head in ('anode_material', 'cathode_material', 'cell_class_v3'):
        n = nc_v3[v3_head]
        mat = np.zeros((n, DIM), dtype=np.float32)
        mask = np.zeros(n, dtype=np.float32)
        print(f'  [{v3_head:<22}] 0/{n} (材料家族无 SMILES, 跳过)')
        table[v3_head] = {'feat': mat, 'mask': mask}

    # --- C. z-score 规范化 (每个 head 单独, 跨类)
    for h in table:
        feat = table[h]['feat']  # (N, 11)
        mask = table[h]['mask']  # (N,)
        if mask.sum() == 0:
            print(f'  [{h:<22}] 全无特征, 跳过规范化')
            continue
        # 只用 mask=True 行算 mean/std
        valid = feat[mask.astype(np.bool_)]
        mu = valid.mean(axis=0)
        sigma = valid.std(axis=0) + 1e-6
        normalized = (feat - mu) / sigma
        # mask=0 的行重置为 0
        normalized[mask.astype(np.bool_) == False] = 0.0
        table[h]['feat'] = normalized
        table[h]['mu'] = mu
        table[h]['sigma'] = sigma

    # Save
    torch.save(table, OUT_FILE)
    print(f'\\nSaved xTB class table → {OUT_FILE}')
    for h, d in table.items():
        feat = d['feat']
        mask = d['mask']
        print(f'  {h:<22} feat={feat.shape} mask_valid={int(mask.sum())}/{len(mask)}')


if __name__ == '__main__':
    main()
