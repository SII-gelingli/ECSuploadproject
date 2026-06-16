"""
端到端评估: 在 data_audited_v3/test.pt (2025+ papers) 上跑 Stage-1 + Stage-2
(用 Stage-1 argmax 喂 Stage-2，不再 teacher forcing)，输出完整指标。
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
from torch.utils.data import DataLoader

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1 import ConditionStage1, HEAD_KEYS
from models.condition_stage1_cond import ConditionStage1Cond
from models.condition_stage1_chain import ConditionStage1Chain
from models.condition_stage2 import ConditionStage2, AMOUNT_FIELDS
from scripts.train_stage1 import Stage1Dataset, topk_accuracy
from scripts.train_stage2 import inverse_transform

DATA_DIR = project_root / 'data_audited_v3'
CKPT_DIR = project_root / 'checkpoints' / 'two_stage'

ABSENT_INDEX = {'anode': 22, 'cathode': 22, 'cell_type': 3,
                'solvent': 0, 'electrolyte': 0, 'catalyst': 0,
                'reagent': 0, 'ligand': 0, 'additive': 0}

# 容差 (原单位)
TOLERANCE = {
    'catalyst_equiv': 0.05,   # ±0.05 equiv (cat 通常 1-10 mol% = 0.01-0.1 equiv)
    'reagent_equiv': 0.3,     # ±0.3 equiv
    'ligand_equiv': 0.05,     # ±0.05 equiv
    'additive_equiv': 0.3,    # ±0.3 equiv
    'electrolyte_M': 0.05,    # ±0.05 M
    'current_mA': 0.2,        # ±20% relative
    'current_density': 0.2,   # ±20% relative
    'potential_V': 0.2,       # ±0.2 V
    'temperature_C': 5.0,     # ±5 °C
    'time_h': 0.25,           # ±25% relative
}
RELATIVE_TOL_FIELDS = {'current_mA', 'current_density', 'time_h'}


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    ckpt1 = torch.load(CKPT_DIR / 'stage1_best.pt', weights_only=False)
    ckpt2 = torch.load(CKPT_DIR / 'stage2_best.pt', weights_only=False)
    nc = ckpt1['num_classes']
    print(f"Stage-1 best epoch {ckpt1['epoch']} val_avg_top1={ckpt1['val_avg_top1']:.4f}")
    print(f"Stage-2 best epoch {ckpt2['epoch']} val_score={ckpt2['val_score']:.4f}")

    if ckpt1.get('chain'):
        m1 = ConditionStage1Chain(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                                   hidden_dims=tuple(ckpt1['hidden_dims']),
                                   dropout=ckpt1.get('dropout', 0.3),
                                   cond_embed_dim=ckpt1.get('cond_embed_dim', 32)).to(device)
        print(f"  使用 chain (solvent→electrolyte→reagent) Stage-1")
    elif ckpt1.get('cond_decode'):
        m1 = ConditionStage1Cond(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                                  hidden_dims=tuple(ckpt1['hidden_dims']),
                                  dropout=ckpt1.get('dropout', 0.3),
                                  cond_embed_dim=ckpt1.get('cond_embed_dim', 32)).to(device)
        print(f"  使用 全链 conditional decoding Stage-1")
    else:
        m1 = ConditionStage1(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                              hidden_dims=tuple(ckpt1['hidden_dims']),
                              dropout=ckpt1.get('dropout', 0.3)).to(device)
    m1.load_state_dict(ckpt1['model_state_dict'])
    m1.eval()

    m2 = ConditionStage2(num_classes=nc, fp_dim=ckpt2['fp_dim'],
                          hidden_dims=tuple(ckpt2['hidden_dims']),
                          dropout=ckpt2.get('dropout', 0.2)).to(device)
    m2.load_state_dict(ckpt2['model_state_dict'])
    m2.eval()

    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    amount_stats = json.loads((DATA_DIR / 'amount_stats.json').read_text())
    print(f"\nTest set: {len(test_records)} reactions from 2025+ papers")

    # Stage-1 / Stage-2 各自决定是否用 xTB/FG，独立准备 fp
    s1_use_xtb = bool(ckpt1.get('use_xtb'))
    s1_use_fg = bool(ckpt1.get('use_fg'))
    s2_use_xtb = bool(ckpt2.get('use_xtb'))
    s2_use_fg = bool(ckpt2.get('use_fg'))
    xtb_mean = xtb_std = None
    fg_mean = fg_std = None
    if s1_use_xtb or s2_use_xtb:
        xtb_stats = json.loads((DATA_DIR / 'xtb_stats.json').read_text())
        xtb_mean = np.asarray(xtb_stats['mean'], dtype=np.float32)
        xtb_std = np.asarray(xtb_stats['std'], dtype=np.float32)
    if s1_use_fg or s2_use_fg:
        fg_stats = json.loads((DATA_DIR / 'fg_stats.json').read_text())
        fg_mean = np.asarray(fg_stats['mean'], dtype=np.float32)
        fg_std = np.asarray(fg_stats['std'], dtype=np.float32)
    print(f"  Stage-1: use_xtb={s1_use_xtb} use_fg={s1_use_fg}")
    print(f"  Stage-2: use_xtb={s2_use_xtb} use_fg={s2_use_fg}")

    # Stage-1 dataset 用 Stage-1 的 feature 设置
    ds = Stage1Dataset(test_records,
                        xtb_mean=xtb_mean if s1_use_xtb else None,
                        xtb_std=xtb_std if s1_use_xtb else None,
                        fg_mean=fg_mean if s1_use_fg else None,
                        fg_std=fg_std if s1_use_fg else None)
    loader = DataLoader(ds, batch_size=256, shuffle=False, num_workers=2)

    # 收集
    # Stage-1: 每 head 的 Top-K + 含 ABSENT / 排除 ABSENT 两种口径
    head_metrics = {k: {'top1_all': 0, 'top3_all': 0, 'top5_all': 0,
                        'top1_non_absent': 0, 'top3_non_absent': 0, 'top5_non_absent': 0,
                        'n': 0, 'n_non_absent': 0,
                        'absent_correct': 0, 'absent_predicted': 0, 'absent_actual': 0}
                    for k in HEAD_KEYS}
    joint_correct = 0
    n_total = 0

    # Stage-2: 每字段 MAE / 容差准确率 / R²
    amount_preds = {f: [] for f in AMOUNT_FIELDS}
    amount_tgts = {f: [] for f in AMOUNT_FIELDS}
    amount_masks = {f: [] for f in AMOUNT_FIELDS}

    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            bsz = fp.size(0)
            n_total += bsz

            logits = m1(fp)
            # 用 argmax 作为种类预测 (推理流程)
            cat_pred = {k: logits[k].argmax(dim=-1) for k in HEAD_KEYS}

            # Stage-1 指标
            per_head_correct_top1 = []
            for k in HEAD_KEYS:
                tgt = batch[k].to(device)
                res = topk_accuracy(logits[k], tgt, ks=(1, 3, 5))
                head_metrics[k]['top1_all'] += res.get('top1', 0)
                head_metrics[k]['top3_all'] += res.get('top3', 0)
                head_metrics[k]['top5_all'] += res.get('top5', 0)
                head_metrics[k]['n'] += bsz

                pred1 = logits[k].argmax(dim=-1)
                per_head_correct_top1.append(pred1 == tgt)

                # ABSENT 子集 (target == ABSENT_INDEX)
                absent_idx = ABSENT_INDEX[k]
                is_absent_target = tgt == absent_idx
                is_absent_pred = pred1 == absent_idx
                head_metrics[k]['absent_actual'] += int(is_absent_target.sum())
                head_metrics[k]['absent_predicted'] += int(is_absent_pred.sum())
                head_metrics[k]['absent_correct'] += int((is_absent_target & is_absent_pred).sum())

                # 非 ABSENT 子集的 Top-K
                non_absent = ~is_absent_target
                if non_absent.sum() > 0:
                    logits_na = logits[k][non_absent]
                    tgt_na = tgt[non_absent]
                    res_na = topk_accuracy(logits_na, tgt_na, ks=(1, 3, 5))
                    head_metrics[k]['top1_non_absent'] += res_na.get('top1', 0)
                    head_metrics[k]['top3_non_absent'] += res_na.get('top3', 0)
                    head_metrics[k]['top5_non_absent'] += res_na.get('top5', 0)
                    head_metrics[k]['n_non_absent'] += int(non_absent.sum())

            joint = torch.stack(per_head_correct_top1, dim=0).all(dim=0)
            joint_correct += int(joint.sum())
            # Stage-2 由下面 sequential loop 处理（因为 fp 维度可能不同）

    # Stage-2 单独走一遍 test_records, 顺序对齐
    print("\nRe-running Stage-2 on test (sequential)...")
    BATCH = 256
    n_records = len(test_records)
    with torch.no_grad():
        for start in range(0, n_records, BATCH):
            end = min(start + BATCH, n_records)
            batch_rec = test_records[start:end]
            # 分别为 Stage-1 / Stage-2 准备 fp（两者 use_xtb/use_fg 可能不同）
            fps1_list, fps2_list = [], []
            for r in batch_rec:
                base = np.concatenate([r['reactant_fp'], r['product_fp'], r['diff_fp']]).astype(np.float32)
                fp1 = base.copy()
                if s1_use_xtb and 'xtb_feat' in r:
                    xtb = (np.asarray(r['xtb_feat'], dtype=np.float32) - xtb_mean) / xtb_std
                    fp1 = np.concatenate([fp1, xtb.astype(np.float32)])
                if s1_use_fg and 'fg_feat' in r:
                    fg = (np.asarray(r['fg_feat'], dtype=np.float32) - fg_mean) / fg_std
                    fp1 = np.concatenate([fp1, fg.astype(np.float32)])
                fps1_list.append(fp1)
                fp2 = base.copy()
                if s2_use_xtb and 'xtb_feat' in r:
                    xtb = (np.asarray(r['xtb_feat'], dtype=np.float32) - xtb_mean) / xtb_std
                    fp2 = np.concatenate([fp2, xtb.astype(np.float32)])
                if s2_use_fg and 'fg_feat' in r:
                    fg = (np.asarray(r['fg_feat'], dtype=np.float32) - fg_mean) / fg_std
                    fp2 = np.concatenate([fp2, fg.astype(np.float32)])
                fps2_list.append(fp2)
            fps1 = torch.from_numpy(np.stack(fps1_list)).float().to(device)
            fps2 = torch.from_numpy(np.stack(fps2_list)).float().to(device)
            cats = {}
            logits = m1(fps1)
            for k in HEAD_KEYS:
                cats[k] = logits[k].argmax(dim=-1)
            amt_pred = m2(fps2, cats)
            for i, f in enumerate(AMOUNT_FIELDS):
                p_norm = amt_pred[f].cpu().numpy()
                t_norm = np.zeros(len(batch_rec), dtype=np.float32)
                mask = np.zeros(len(batch_rec), dtype=np.float32)
                for j, r in enumerate(batch_rec):
                    if r['amount_mask'][i] > 0:
                        s = amount_stats[f]
                        # transform raw → normalized for comparison reference
                        if s['transform'] == 'log':
                            tt = np.log(r['amount_values'][i] + s['offset'])
                        elif s['transform'] == 'temperature':
                            tt = (r['amount_values'][i] - 25) / 30.0
                        else:
                            tt = r['amount_values'][i]
                        t_norm[j] = (tt - s['norm_mean']) / max(1e-8, s['norm_std'])
                        mask[j] = 1
                amount_preds[f].append(p_norm)
                amount_tgts[f].append(t_norm)
                amount_masks[f].append(mask)

    # 汇总 Stage-1 指标
    print("\n" + "=" * 70)
    print("Stage-1 种类预测 — TEST (2025+ papers)")
    print("=" * 70)
    print(f"\n样本数: {n_total}, Joint Top-1 (9 heads all match) = {joint_correct/n_total*100:.2f}%")

    print(f"\n{'head':<13} {'#':>6} {'Top1':>7} {'Top3':>7} {'Top5':>7}  | non-ABSENT only:  {'Top1':>7} {'Top3':>7} {'Top5':>7}")
    stage1_report = {}
    for k in HEAD_KEYS:
        m = head_metrics[k]
        n = m['n']
        top1 = m['top1_all'] / n if n else 0
        top3 = m['top3_all'] / n if n else 0
        top5 = m['top5_all'] / n if n else 0
        nna = m['n_non_absent']
        top1_na = m['top1_non_absent'] / nna if nna else 0
        top3_na = m['top3_non_absent'] / nna if nna else 0
        top5_na = m['top5_non_absent'] / nna if nna else 0
        print(f"{k:<13} {n:>6} {top1:>7.4f} {top3:>7.4f} {top5:>7.4f}  |  "
              f"{top1_na:>7.4f} {top3_na:>7.4f} {top5_na:>7.4f}  (n_na={nna})")
        stage1_report[k] = {
            'n': n, 'top1': round(top1, 4), 'top3': round(top3, 4), 'top5': round(top5, 4),
            'top1_non_absent': round(top1_na, 4),
            'top3_non_absent': round(top3_na, 4),
            'top5_non_absent': round(top5_na, 4),
            'n_non_absent': nna,
            'absent_actual': m['absent_actual'],
            'absent_predicted': m['absent_predicted'],
            'absent_correct': m['absent_correct'],
            'absent_precision': round(m['absent_correct'] / max(1, m['absent_predicted']), 4),
            'absent_recall': round(m['absent_correct'] / max(1, m['absent_actual']), 4),
        }

    print("\nABSENT 预测准确性 (模型说'不需要'时是否对):")
    print(f"{'head':<13} {'actual':>8} {'predicted':>10} {'correct':>8} {'precision':>10} {'recall':>8}")
    for k in HEAD_KEYS:
        r = stage1_report[k]
        print(f"{k:<13} {r['absent_actual']:>8} {r['absent_predicted']:>10} {r['absent_correct']:>8} "
              f"{r['absent_precision']:>10.4f} {r['absent_recall']:>8.4f}")

    # 汇总 Stage-2 指标
    print("\n" + "=" * 70)
    print("Stage-2 用量预测 — TEST (2025+ papers, 端到端用 Stage-1 argmax)")
    print("=" * 70)
    print(f"\n{'field':<20} {'#':>6} {'MAE':>10} {'RMSE':>10} {'R²':>8} {'in-tol%':>10}")
    stage2_report = {}
    for f in AMOUNT_FIELDS:
        p = np.concatenate(amount_preds[f])
        t = np.concatenate(amount_tgts[f])
        m = np.concatenate(amount_masks[f]).astype(bool)
        if m.sum() == 0:
            print(f"{f:<20} {'-':>6} {'-':>10} {'-':>10} {'-':>8} {'-':>10}")
            stage2_report[f] = {'n': 0}
            continue
        p_real = inverse_transform(p[m], amount_stats[f])
        t_real = inverse_transform(t[m], amount_stats[f])
        mae = float(np.mean(np.abs(p_real - t_real)))
        rmse = float(np.sqrt(np.mean((p_real - t_real) ** 2)))
        ss_res = np.sum((t_real - p_real) ** 2)
        ss_tot = np.sum((t_real - t_real.mean()) ** 2) + 1e-8
        r2 = float(1 - ss_res / ss_tot)
        tol = TOLERANCE[f]
        if f in RELATIVE_TOL_FIELDS:
            within = float(np.mean(np.abs(p_real - t_real) / np.abs(t_real + 1e-6) < tol)) * 100
        else:
            within = float(np.mean(np.abs(p_real - t_real) < tol)) * 100
        print(f"{f:<20} {int(m.sum()):>6} {mae:>10.3f} {rmse:>10.3f} {r2:>8.3f} {within:>9.1f}%")
        stage2_report[f] = {
            'n': int(m.sum()), 'mae': round(mae, 4), 'rmse': round(rmse, 4),
            'r2': round(r2, 4), 'within_tol_pct': round(within, 2),
            'tolerance': tol,
        }

    # 保存
    out = {
        'test_size': n_total,
        'joint_top1': round(joint_correct / n_total, 4),
        'stage1': stage1_report,
        'stage2': stage2_report,
        'stage1_ckpt_epoch': ckpt1['epoch'],
        'stage2_ckpt_epoch': ckpt2['epoch'],
    }
    out_path = CKPT_DIR / 'two_stage_test_metrics.json'
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\n✓ Saved metrics to {out_path}")


if __name__ == "__main__":
    main()
