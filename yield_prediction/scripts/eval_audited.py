"""加载 checkpoints/audited/condition_best.pt，在 data_audited/test.pt (2025+ 论文) 上做完整评估。"""
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
from torch.utils.data import DataLoader

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_recommender import ConditionRecommender
from scripts.train_audited import (
    PreparedConditionDataset,
    CONDITION_KEYS,
    UNKNOWN_INDEX,
    topk_accuracy,
)

DATA_DIR = project_root / 'data_audited'
CKPT_DIR = project_root / 'checkpoints' / 'audited'


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    ckpt = torch.load(CKPT_DIR / 'condition_best.pt', weights_only=False)
    nc = ckpt['num_classes']
    print(f"Loaded ckpt epoch={ckpt['epoch']}  val_top1={ckpt['val_top1']:.4f}  val_top3={ckpt['val_top3']:.4f}")

    model = ConditionRecommender(
        reaction_dim=ckpt['reaction_dim'],
        hidden_dim=ckpt['hidden_dim'],
        num_anode_materials=nc['anode'],
        num_cathode_materials=nc['cathode'],
        num_cell_types=nc['cell_type'],
        num_electrolytes=nc['electrolyte'],
        num_solvents=nc['solvent'],
        num_reagents=nc['reagent'],
        num_catalysts=nc['catalyst'],
    ).to(device)
    model.load_state_dict(ckpt['model_state_dict'])
    model.eval()

    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    print(f"Test set: {len(test_records)} reactions from 2025+ papers")

    ds = PreparedConditionDataset(test_records, mode='condition')
    loader = DataLoader(ds, batch_size=128, shuffle=False, num_workers=2)

    # 评估两套：与/不与 Unknown 屏蔽
    sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5, 10)} for k in CONDITION_KEYS}
    sums_no_mask = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5, 10)} for k in CONDITION_KEYS}
    n = 0
    # 同时统计真实标签里是 UNK 的样本数 (这些样本无法被正确预测，因为我们屏蔽了 UNK)
    unk_count = {k: 0 for k in CONDITION_KEYS}

    with torch.no_grad():
        for batch in loader:
            fp = batch['reaction_fp'].to(device)
            preds = model(fp)
            bsz = fp.size(0)
            n += bsz
            for k in CONDITION_KEYS:
                logits = preds[f'{k}_logits']
                tgt = batch[k].to(device)
                r_m = topk_accuracy(logits, tgt, ks=(1, 3, 5, 10), mask_idx=UNKNOWN_INDEX[k])
                r_nm = topk_accuracy(logits, tgt, ks=(1, 3, 5, 10), mask_idx=None)
                for kk in r_m:
                    sums[k][kk] += r_m[kk]
                for kk in r_nm:
                    sums_no_mask[k][kk] += r_nm[kk]
                unk_count[k] += (tgt == UNKNOWN_INDEX[k]).sum().item()

    def normalize(s):
        return {k: {kk: round(s[k][kk] / n, 4) for kk in s[k]} for k in CONDITION_KEYS}

    masked = normalize(sums)
    unmasked = normalize(sums_no_mask)

    # 排除 UNK 标签后的 conditional 准确率（看模型在"真有条件信息的样本"上有多准）
    cond_sums = {k: {f'top{kv}': 0.0 for kv in (1, 3, 5, 10)} for k in CONDITION_KEYS}
    cond_n = {k: 0 for k in CONDITION_KEYS}
    with torch.no_grad():
        for batch in loader:
            fp = batch['reaction_fp'].to(device)
            preds = model(fp)
            for k in CONDITION_KEYS:
                logits = preds[f'{k}_logits']
                tgt = batch[k].to(device)
                non_unk = tgt != UNKNOWN_INDEX[k]
                if non_unk.sum() == 0:
                    continue
                logits_f = logits[non_unk]
                tgt_f = tgt[non_unk]
                r = topk_accuracy(logits_f, tgt_f, ks=(1, 3, 5, 10), mask_idx=UNKNOWN_INDEX[k])
                for kk in r:
                    cond_sums[k][kk] += r[kk]
                cond_n[k] += non_unk.sum().item()
    cond_acc = {
        k: {kk: round(cond_sums[k][kk] / max(1, cond_n[k]), 4) for kk in cond_sums[k]}
        for k in CONDITION_KEYS
    }

    # 打印
    def print_table(title, table):
        print(f"\n{title}")
        print(f"  {'Condition':<13} {'Top1':>7} {'Top3':>7} {'Top5':>7} {'Top10':>7}")
        for k in CONDITION_KEYS:
            r = table[k]
            print(f"  {k:<13} {r['top1']:7.4f} {r['top3']:7.4f} {r['top5']:7.4f} {r['top10']:7.4f}")
        avg = {kk: round(np.mean([table[k][kk] for k in CONDITION_KEYS]), 4)
               for kk in ('top1', 'top3', 'top5', 'top10')}
        print(f"  {'AVG':<13} {avg['top1']:7.4f} {avg['top3']:7.4f} {avg['top5']:7.4f} {avg['top10']:7.4f}")
        return avg

    print(f"\nTotal test reactions: {n}")
    print(f"Per-condition Unknown-label counts in test set:")
    for k in CONDITION_KEYS:
        print(f"  {k}: {unk_count[k]}/{n}  ({unk_count[k]/n*100:.1f}% unknown)")

    avg_masked = print_table("=== TEST (UNK index masked from predictions, all samples) ===", masked)
    avg_unmasked = print_table("=== TEST (no masking, raw predictions, all samples) ===", unmasked)
    avg_cond = print_table("=== TEST (only samples whose true label is NOT UNK) ===", cond_acc)

    out = {
        'best_epoch': ckpt['epoch'],
        'best_val_top1': ckpt['val_top1'],
        'test_size': n,
        'unknown_label_counts': unk_count,
        'metrics_masked': masked,
        'metrics_unmasked': unmasked,
        'metrics_non_unk_only': cond_acc,
        'avg_masked': avg_masked,
        'avg_unmasked': avg_unmasked,
        'avg_non_unk_only': avg_cond,
    }
    out_path = CKPT_DIR / 'condition_eval_final.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
