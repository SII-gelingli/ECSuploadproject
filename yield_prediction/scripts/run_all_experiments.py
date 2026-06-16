"""对 experiments/ 里 4 个 Stage-1 变体批量跑 test eval + Joint Top-K。

固定 Stage-2 用 stage2_baseline.pt，因为 Stage-2 不显著受 FG 影响（甚至 FG 让 Stage-2 变差）。
输出: experiments/experiment_log.json
"""
import sys, json, copy
from pathlib import Path

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path: sys.path.insert(0, _p)

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

DATA_DIR = project_root / 'data_audited_v3'
EXP_DIR = project_root / 'checkpoints' / 'two_stage' / 'experiments'

ABSENT_INDEX = {'anode': 22, 'cathode': 22, 'cell_type': 3,
                'solvent': 0, 'electrolyte': 0, 'catalyst': 0,
                'reagent': 0, 'ligand': 0, 'additive': 0}

VARIANTS = [
    ('baseline',   'stage1_baseline.pt'),
    ('fg_only',    'stage1_fg.pt'),
    ('cond_only',  'stage1_cond.pt'),
    ('fg_cond',    'stage1_fg_cond.pt'),
    ('chain_only', 'stage1_chain.pt'),
    ('fg_chain',   'stage1_fg_chain.pt'),
]
STAGE2_CKPT = EXP_DIR / 'stage2_baseline.pt'


def build_fp(record, use_xtb=False, use_fg=False, xtb_mean=None, xtb_std=None, fg_mean=None, fg_std=None):
    fp = np.concatenate([record['reactant_fp'], record['product_fp'], record['diff_fp']]).astype(np.float32)
    if use_xtb and 'xtb_feat' in record:
        x = (np.asarray(record['xtb_feat'], dtype=np.float32) - xtb_mean) / xtb_std
        fp = np.concatenate([fp, x.astype(np.float32)])
    if use_fg and 'fg_feat' in record:
        f = (np.asarray(record['fg_feat'], dtype=np.float32) - fg_mean) / fg_std
        fp = np.concatenate([fp, f.astype(np.float32)])
    return fp


def eval_variant(variant_name, ckpt_path, test_records, fg_stats, amount_stats, device='cuda'):
    print(f"\n{'='*60}\n>> 变体: {variant_name}  ckpt: {ckpt_path.name}\n{'='*60}")
    ckpt1 = torch.load(ckpt_path, weights_only=False)
    nc = ckpt1['num_classes']
    is_cond = bool(ckpt1.get('cond_decode'))
    is_chain = bool(ckpt1.get('chain'))
    use_fg1 = bool(ckpt1.get('use_fg'))
    print(f"  fp_dim={ckpt1['fp_dim']}  use_fg={use_fg1}  cond={is_cond}  chain={is_chain}"
          f"  best_epoch={ckpt1['epoch']}  val_top1={ckpt1['val_avg_top1']:.4f}")

    if is_chain:
        m1 = ConditionStage1Chain(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                                   hidden_dims=tuple(ckpt1['hidden_dims']),
                                   dropout=ckpt1.get('dropout', 0.3),
                                   cond_embed_dim=ckpt1.get('cond_embed_dim', 32)).to(device)
    elif is_cond:
        m1 = ConditionStage1Cond(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                                  hidden_dims=tuple(ckpt1['hidden_dims']),
                                  dropout=ckpt1.get('dropout', 0.3),
                                  cond_embed_dim=ckpt1.get('cond_embed_dim', 32)).to(device)
    else:
        m1 = ConditionStage1(num_classes=nc, fp_dim=ckpt1['fp_dim'],
                              hidden_dims=tuple(ckpt1['hidden_dims']),
                              dropout=ckpt1.get('dropout', 0.3)).to(device)
    m1.load_state_dict(ckpt1['model_state_dict'])
    m1.eval()

    # Stage-2
    ckpt2 = torch.load(STAGE2_CKPT, weights_only=False)
    m2 = ConditionStage2(num_classes=nc, fp_dim=ckpt2['fp_dim'],
                          hidden_dims=tuple(ckpt2['hidden_dims']),
                          dropout=ckpt2.get('dropout', 0.2)).to(device)
    m2.load_state_dict(ckpt2['model_state_dict'])
    m2.eval()

    fg_mean = np.asarray(fg_stats['mean'], dtype=np.float32)
    fg_std = np.asarray(fg_stats['std'], dtype=np.float32)

    # Stage-1 per-head + joint Top-K
    KS = [1, 3, 5, 10, 20]
    head_metrics = {k: {f'top{kk}': 0 for kk in KS} for k in HEAD_KEYS}
    head_non_absent_metrics = {k: {f'top{kk}': 0 for kk in KS} for k in HEAD_KEYS}
    head_n_non_absent = {k: 0 for k in HEAD_KEYS}
    absent_actual = {k: 0 for k in HEAD_KEYS}
    absent_pred = {k: 0 for k in HEAD_KEYS}
    absent_correct = {k: 0 for k in HEAD_KEYS}
    joint_all = {k: 0 for k in KS}
    joint_8 = {k: 0 for k in KS}
    total = 0

    with torch.no_grad():
        BATCH = 256
        for start in range(0, len(test_records), BATCH):
            batch_rec = test_records[start:start + BATCH]
            fps = np.stack([build_fp(r, use_fg=use_fg1, fg_mean=fg_mean, fg_std=fg_std)
                             for r in batch_rec])
            fps = torch.from_numpy(fps).float().to(device)
            logits = m1(fps)
            bsz = fps.size(0); total += bsz
            in_topk = {k: [] for k in KS}
            for h in HEAD_KEYS:
                tgt = torch.tensor([r['labels'][h] for r in batch_rec], dtype=torch.long, device=device)
                lg = logits[h]
                for k in KS:
                    kk = min(k, lg.size(-1))
                    _, pred = lg.topk(kk, dim=-1)
                    in_k = pred.eq(tgt.view(-1, 1)).any(dim=1)
                    head_metrics[h][f'top{k}'] += int(in_k.sum())
                    in_topk[k].append(in_k)
                pred1 = lg.argmax(dim=-1)
                absent_idx = ABSENT_INDEX[h]
                is_a_t = tgt == absent_idx
                is_a_p = pred1 == absent_idx
                absent_actual[h] += int(is_a_t.sum())
                absent_pred[h] += int(is_a_p.sum())
                absent_correct[h] += int((is_a_t & is_a_p).sum())
                # non-absent topk
                non_a = ~is_a_t
                if non_a.sum() > 0:
                    head_n_non_absent[h] += int(non_a.sum())
                    lg_na = lg[non_a]
                    tgt_na = tgt[non_a]
                    for k in KS:
                        kk = min(k, lg_na.size(-1))
                        _, pna = lg_na.topk(kk, dim=-1)
                        in_na = pna.eq(tgt_na.view(-1, 1)).any(dim=1)
                        head_non_absent_metrics[h][f'top{k}'] += int(in_na.sum())
            for k in KS:
                stacked = torch.stack(in_topk[k], dim=0)
                joint_all[k] += int(stacked.all(dim=0).sum())
                joint_8[k] += int((stacked.sum(dim=0) >= 8).sum())

    # Stage-2 amount eval (use stage2_baseline, fp_dim=6144, no FG)
    print("  跑 Stage-2 用量回归 ...")
    field_pred = {f: [] for f in AMOUNT_FIELDS}
    field_tgt = {f: [] for f in AMOUNT_FIELDS}
    with torch.no_grad():
        for start in range(0, len(test_records), BATCH):
            batch_rec = test_records[start:start + BATCH]
            fps1 = np.stack([build_fp(r, use_fg=use_fg1, fg_mean=fg_mean, fg_std=fg_std)
                              for r in batch_rec])
            fps1 = torch.from_numpy(fps1).float().to(device)
            fps2 = np.stack([build_fp(r, use_fg=False) for r in batch_rec])
            fps2 = torch.from_numpy(fps2).float().to(device)
            logits = m1(fps1)
            cats = {h: logits[h].argmax(dim=-1) for h in HEAD_KEYS}
            amt = m2(fps2, cats)
            for i, f in enumerate(AMOUNT_FIELDS):
                s = amount_stats[f]
                p_norm = amt[f].cpu().numpy()
                # 反归一化
                p_unscaled = p_norm * s['norm_std'] + s['norm_mean']
                if s['transform'] == 'log':
                    p_raw = np.exp(p_unscaled) - s['offset']
                elif s['transform'] == 'temperature':
                    p_raw = p_unscaled * 30 + 25
                else:
                    p_raw = p_unscaled
                for j, r in enumerate(batch_rec):
                    if r['amount_mask'][i] > 0:
                        field_pred[f].append(float(p_raw[j]))
                        field_tgt[f].append(float(r['amount_values'][i]))

    tol_def = {'catalyst_equiv': 0.05, 'reagent_equiv': 0.3, 'ligand_equiv': 0.05,
               'additive_equiv': 0.3, 'electrolyte_M': 0.05, 'current_mA': 0.2,
               'current_density': 0.2, 'potential_V': 0.2, 'temperature_C': 5.0, 'time_h': 0.25}
    REL = {'current_mA', 'current_density', 'time_h'}

    field_metrics = {}
    for f in AMOUNT_FIELDS:
        if not field_pred[f]:
            field_metrics[f] = {'n': 0}
            continue
        p = np.array(field_pred[f]); t = np.array(field_tgt[f])
        mae = float(np.mean(np.abs(p - t)))
        rmse = float(np.sqrt(np.mean((p - t)**2)))
        ss_res = np.sum((t - p)**2); ss_tot = np.sum((t - t.mean())**2) + 1e-8
        r2 = float(1 - ss_res / ss_tot)
        if f in REL:
            wt = np.abs(p - t) / np.clip(np.abs(t), 0.01, None) <= tol_def[f]
        else:
            wt = np.abs(p - t) <= tol_def[f]
        within_tol = float(wt.mean() * 100)
        field_metrics[f] = {'n': int(len(p)), 'mae': round(mae,3), 'rmse': round(rmse,3),
                             'r2': round(r2,3), 'within_tol_pct': round(within_tol,1)}

    # 整理结果
    result = {
        'variant': variant_name,
        'ckpt': str(ckpt_path.name),
        'val_avg_top1': float(ckpt1['val_avg_top1']),
        'best_epoch': int(ckpt1['epoch']),
        'use_fg': use_fg1,
        'cond_decode': is_cond,
        'test_size': total,
        'stage1': {},
        'stage2': field_metrics,
        'joint': {},
    }
    for h in HEAD_KEYS:
        result['stage1'][h] = {
            'n': total,
            'top1': round(head_metrics[h]['top1']/total, 4),
            'top3': round(head_metrics[h]['top3']/total, 4),
            'top5': round(head_metrics[h]['top5']/total, 4),
            'top10': round(head_metrics[h]['top10']/total, 4),
            'top20': round(head_metrics[h]['top20']/total, 4),
            'n_non_absent': head_n_non_absent[h],
            'top1_non_absent': round(head_non_absent_metrics[h]['top1']/max(1,head_n_non_absent[h]), 4),
            'top3_non_absent': round(head_non_absent_metrics[h]['top3']/max(1,head_n_non_absent[h]), 4),
            'absent_actual': absent_actual[h],
            'absent_predicted': absent_pred[h],
            'absent_correct': absent_correct[h],
            'absent_precision': round(absent_correct[h]/max(1,absent_pred[h]), 4),
            'absent_recall': round(absent_correct[h]/max(1,absent_actual[h]), 4),
        }
    for k in KS:
        result['joint'][f'top{k}'] = {
            'all_9': round(joint_all[k]/total, 4),
            'min_8': round(joint_8[k]/total, 4),
        }
    avg_t1 = np.mean([result['stage1'][h]['top1'] for h in HEAD_KEYS])
    result['avg_top1'] = round(float(avg_t1), 4)

    # 打印简要表
    print(f"\n  Stage-1 AVG Top-1 = {avg_t1*100:.2f}%   Joint Top-1 = {joint_all[1]/total*100:.2f}%   Top-10 = {joint_all[10]/total*100:.2f}%   Top-20 = {joint_all[20]/total*100:.2f}%")
    return result


def main():
    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    fg_stats = json.loads((DATA_DIR / 'fg_stats.json').read_text())
    amount_stats = json.loads((DATA_DIR / 'amount_stats.json').read_text())
    print(f"Test size: {len(test_records)}")

    all_results = {}
    for name, ckpt in VARIANTS:
        path = EXP_DIR / ckpt
        if not path.exists():
            print(f"!!! {path} not found, skipping")
            continue
        all_results[name] = eval_variant(name, path, test_records, fg_stats, amount_stats)

    out = EXP_DIR / 'experiment_log.json'
    json.dump(all_results, open(out, 'w'), indent=2)
    print(f"\n✓ 全部实验日志保存到 {out}")

    # 简要对比表
    print("\n" + "="*70)
    print(f"{'变体':<14}{'val_top1':>11}{'AVG_top1':>11}{'Joint1':>9}{'Joint5':>9}{'Joint10':>10}{'Joint20':>10}")
    print("-"*70)
    for name in all_results:
        r = all_results[name]
        print(f"{name:<14}{r['val_avg_top1']*100:>10.2f}%{r['avg_top1']*100:>10.2f}%"
              f"{r['joint']['top1']['all_9']*100:>8.2f}%{r['joint']['top5']['all_9']*100:>8.2f}%"
              f"{r['joint']['top10']['all_9']*100:>9.2f}%{r['joint']['top20']['all_9']*100:>9.2f}%")


if __name__ == "__main__":
    main()
