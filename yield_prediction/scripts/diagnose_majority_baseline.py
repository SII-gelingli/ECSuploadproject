"""诊断模型是否真在学习 vs 只蒙最常见类.

对每个 head 计算:
1. Train 集 majority 类 (永远预测它能拿多少 test 准确率)
2. Model 实际 Top-1 准确率
3. Model 预测分布的熵 (越高=越分散, 0=永远猜同一类)
4. Per-class precision/recall (是否能召回稀有类)
"""
import sys, json
from pathlib import Path
from collections import Counter

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3, SINGLE_HEADS_V3, HIER_KEYS, SMI_FROM_CLASS,
    CAT_TAG_KEY, K_SLOTS, FINE_ELECTRODE_HEADS,
)
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

DATA_DIR = project_root / 'data_audited_v3_clean'
CKPT = project_root / 'checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt'


def label_key_for_head(h, nc, nc_v3):
    """Return the record label key for a given output head."""
    if h in nc_v3: return h
    if h == 'anode_fine': return 'anode_fine'
    if h == 'cathode_fine': return 'cathode_fine'
    return h


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    train = torch.load(DATA_DIR / 'train.pt', weights_only=False)
    test = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.load(open(DATA_DIR / 'stats.json'))
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    nc = stats['num_classes']; nc_v3 = stats['num_classes_v3']

    # Name maps
    name_maps = {}
    for h in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
        if h in vocab: name_maps[h] = {v: k for k, v in vocab[h].items()}
    for h, names in vocab.get('__v3__', {}).items():
        name_maps[h] = {i: n for i, n in enumerate(names)}

    # Load model
    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=0.3, class_embed_dim=32,
    ).to(device)
    ckpt = torch.load(CKPT, map_location=device, weights_only=False)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()

    coll = lambda b: collate_fn(b, nc)
    loader = DataLoader(HierSetV3Dataset(test), batch_size=128, shuffle=False,
                        num_workers=2, collate_fn=coll)

    # Heads to check (single + hier + fine)
    HEADS = [
        ('anode_material', 15, 'anode_material'),
        ('anode_fine', nc['anode_fine'], 'anode_fine'),
        ('cathode_material', 15, 'cathode_material'),
        ('cathode_fine', nc['cathode_fine'], 'cathode_fine'),
        ('cell_class_v3', 4, 'cell_class_v3'),
        ('electrolyte_cation', 23, 'electrolyte_cation'),
        ('electrolyte_anion', 26, 'electrolyte_anion'),
        ('reagent_class_v3', 103, 'reagent_class_v3'),
        ('catalyst_class_v3', 49, 'catalyst_class_v3'),
        ('solvent_class_v3', 27, 'solvent_class_v3'),
    ]

    # === Collect predictions ===
    pred_top1 = {h[0]: [] for h in HEADS}
    gt_all = {h[0]: [] for h in HEADS}
    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher=None)
            for hname, nclass, lblkey in HEADS:
                top1 = out[hname].argmax(dim=-1).cpu().numpy()
                pred_top1[hname].extend(top1.tolist())
                gt_all[hname].extend(batch[hname].numpy().tolist())

    # === Analyze each head ===
    print(f'\n{"="*120}')
    print(f"{'Head':<22} {'N':>4} {'Train majority':<35} {'Major %':>8} {'Model T1 %':>11} {'Δ vs major':>11} {'Pred entropy':>13}")
    print(f'{"-"*120}')

    summary = []
    for hname, nclass, lblkey in HEADS:
        # Train majority class
        train_cnt = Counter([r['labels'][lblkey] for r in train])
        train_top_idx, train_top_n = train_cnt.most_common(1)[0]
        train_top_name = name_maps.get(hname, {}).get(train_top_idx, f'?({train_top_idx})')

        # Test distribution
        test_cnt = Counter(gt_all[hname])
        # Majority baseline acc = % of test samples whose GT == train majority class
        major_acc = test_cnt.get(train_top_idx, 0) / max(len(gt_all[hname]), 1)

        # Model Top-1 acc
        model_acc = sum(1 for p, g in zip(pred_top1[hname], gt_all[hname]) if p == g) / max(len(gt_all[hname]), 1)

        # Pred distribution entropy
        pred_cnt = Counter(pred_top1[hname])
        probs = np.array([v / sum(pred_cnt.values()) for v in pred_cnt.values()])
        ent = -np.sum(probs * np.log(probs + 1e-12))
        max_ent = np.log(min(nclass, len(pred_cnt)) + 1e-12) if pred_cnt else 1
        # 也算 GT 分布的熵作为对比
        gt_probs = np.array([v / sum(test_cnt.values()) for v in test_cnt.values()])
        gt_ent = -np.sum(gt_probs * np.log(gt_probs + 1e-12))

        delta = (model_acc - major_acc) * 100
        summary.append({
            'head': hname, 'n_classes': nclass,
            'major_class': train_top_name, 'major_acc': major_acc, 'model_acc': model_acc,
            'delta': delta, 'pred_entropy': ent, 'gt_entropy': gt_ent,
            'pred_unique_classes': len(pred_cnt),
            'gt_unique_classes': len(test_cnt),
            'pred_cnt': pred_cnt, 'test_cnt': test_cnt,
        })

        print(f"{hname:<22} {nclass:>4} {train_top_name[:33]:<35} "
              f"{major_acc*100:>7.2f}% {model_acc*100:>10.2f}% "
              f"{delta:>+10.2f}% {ent:>10.3f} / GT {gt_ent:.3f}")

    # === Per-class detail ===
    print(f'\n\n{"="*120}')
    print('每个 head 的预测分布 (Top-5 by count):')
    print(f'{"="*120}')
    for s in summary:
        h = s['head']; nm = name_maps.get(h, {})
        print(f"\n--- {h} (N={s['n_classes']} 类) ---")
        total = sum(s['pred_cnt'].values())
        gt_total = sum(s['test_cnt'].values())
        print(f"  模型实际使用了 {s['pred_unique_classes']} / {s['n_classes']} 类 (GT 用了 {s['gt_unique_classes']} 类)")
        print(f"  熵: 模型 = {s['pred_entropy']:.3f}, GT = {s['gt_entropy']:.3f} "
              f"(均匀分布 = {np.log(s['n_classes']):.3f})")
        # Top 5 模型预测 vs GT
        print(f"  {'Rank':<5} {'模型预测类':<35} {'pred %':>10} {'GT %':>10}")
        for i, (cls_id, cnt) in enumerate(s['pred_cnt'].most_common(5)):
            name = nm.get(cls_id, f'?({cls_id})')
            pp = cnt / max(total, 1) * 100
            gp = s['test_cnt'].get(cls_id, 0) / max(gt_total, 1) * 100
            print(f"  {i+1:<5} {name[:33]:<35} {pp:>9.2f}% {gp:>9.2f}%")

    # === Final verdict ===
    print(f'\n\n{"="*120}')
    print('结论')
    print(f'{"="*120}')
    pure_majority = sum(1 for s in summary if s['delta'] < 1.0 and s['pred_unique_classes'] <= 3)
    weak_majority = sum(1 for s in summary if 1.0 <= s['delta'] < 5.0)
    real_learn = sum(1 for s in summary if s['delta'] >= 5.0)
    print(f"\n  ✓ 真正学到东西 (>+5% vs majority): {real_learn} / {len(summary)} head")
    print(f"  ~ 边际改善 (1-5% vs majority): {weak_majority}")
    print(f"  ✗ 退化到 majority (≤1% + 用 ≤3 类): {pure_majority}")
    print()
    if pure_majority > 0:
        print("⚠️ 有 head 实际上跟 majority baseline 没区别 (可能是数据极度不平衡 + 模型偷懒)")
    if real_learn >= len(summary) // 2:
        print("✓ 大部分 head 真在学习, 不是纯蒙")


if __name__ == '__main__':
    main()
