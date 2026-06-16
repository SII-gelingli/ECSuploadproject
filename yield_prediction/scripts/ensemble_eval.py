"""异构 ensemble: GNN+aux 和 MoE_balanced 的 logit 加权融合。

两种方案:
- A. 简单 logit 加权平均 (扫描多个权重)
- B. Cascade: GNN 给 Top-K 候选 → MoE 在 K 内重排
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
import torch.nn.functional as F
from torch.utils.data import DataLoader
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1 import HEAD_KEYS
from models.condition_stage1_gnn import ConditionStage1GNN
from models.condition_stage1_moe import ConditionStage1MoE
from scripts.train_stage1 import Stage1Dataset
from scripts.train_stage1_gnn import GNNStage1Dataset, collate_fn, graph_to_device

DATA_DIR = project_root / 'data_audited_v3'
EXP_DIR = project_root / 'checkpoints' / 'two_stage' / 'experiments'


def load_gnn(device='cuda'):
    ck = torch.load(EXP_DIR / 'stage1_gnn_aux.pt', weights_only=False)
    nc = ck['num_classes']
    m = ConditionStage1GNN(num_classes=nc, gnn_hidden=ck['gnn_hidden'],
                            gnn_layers=ck['gnn_layers'], gnn_heads=ck['gnn_heads'],
                            dropout=ck['dropout'],
                            extra_heads=['reagent_class']).to(device)
    m.load_state_dict(ck['model_state_dict']); m.eval()
    return m, nc


def load_moe(device='cuda'):
    ck = torch.load(EXP_DIR / 'stage1_moe_balanced.pt', weights_only=False)
    nc = ck['num_classes']
    m = ConditionStage1MoE(num_classes=nc, fp_dim=ck['fp_dim'],
                            hidden_dims=tuple(ck['hidden_dims']), dropout=ck['dropout'],
                            num_experts=ck['moe_experts'],
                            extra_heads=['reagent_class']).to(device)
    m.load_state_dict(ck['model_state_dict']); m.eval()
    return m, nc


def topk_indicators(logits, tgt, ks):
    out = {}
    for k in ks:
        kk = min(k, logits.size(-1))
        _, pred = logits.topk(kk, dim=-1)
        out[k] = pred.eq(tgt.view(-1, 1)).any(dim=1)
    return out


def evaluate(merged_logits_per_batch, gt_per_batch, n, label='ENSEMBLE'):
    KS = [1, 3, 5, 10, 20]
    sums = {k: {kk: 0 for kk in KS} for k in HEAD_KEYS}
    joint = {kk: 0 for kk in KS}
    for batch_logits, batch_gt in zip(merged_logits_per_batch, gt_per_batch):
        per_head_in_topk = {kk: [] for kk in KS}
        for h in HEAD_KEYS:
            ind = topk_indicators(batch_logits[h], batch_gt[h], KS)
            for kk in KS:
                sums[h][kk] += int(ind[kk].sum())
                per_head_in_topk[kk].append(ind[kk])
        for kk in KS:
            stacked = torch.stack(per_head_in_topk[kk], dim=0)
            joint[kk] += int(stacked.all(dim=0).sum())
    avg = {kk: np.mean([sums[h][kk] / n for h in HEAD_KEYS]) for kk in KS}
    return {
        'avg_top1': avg[1], 'avg_top3': avg[3], 'avg_top5': avg[5],
        'avg_top10': avg[10], 'avg_top20': avg[20],
        'joint_top1': joint[1] / n, 'joint_top3': joint[3] / n,
        'joint_top5': joint[5] / n, 'joint_top10': joint[10] / n,
        'joint_top20': joint[20] / n,
    }


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Loading GNN+aux ...")
    m_gnn, nc = load_gnn(device)
    print("Loading MoE_balanced ...")
    m_moe, _ = load_moe(device)

    print("Loading test data ...")
    recs = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    print(f"Test n={len(recs)}")

    # GNN dataset (graph)
    gnn_ds = GNNStage1Dataset(recs, extra_keys=['reagent_class'])
    gnn_loader = DataLoader(gnn_ds, batch_size=64, shuffle=False, num_workers=0, collate_fn=collate_fn)
    # MoE dataset (FP)
    moe_ds = Stage1Dataset(recs, extra_keys=['reagent_class'])
    moe_loader = DataLoader(moe_ds, batch_size=64, shuffle=False, num_workers=0)

    # 1. 收集每个 batch 的 GNN logits & MoE logits & GT 标签
    print("\nForward GNN+aux ...")
    gnn_logits_batches = []
    gt_batches = []
    with torch.no_grad():
        for batch in gnn_loader:
            rg = graph_to_device(batch['r_graph'], device)
            pg = graph_to_device(batch['p_graph'], device)
            logits = m_gnn(rg, pg)
            gnn_logits_batches.append({k: logits[k].detach() for k in HEAD_KEYS})
            gt_batches.append({k: batch[k].to(device) for k in HEAD_KEYS})

    print("Forward MoE_balanced ...")
    moe_logits_batches = []
    with torch.no_grad():
        for batch in moe_loader:
            fp = batch['fp'].to(device)
            logits = m_moe(fp)
            moe_logits_batches.append({k: logits[k].detach() for k in HEAD_KEYS})

    assert len(gnn_logits_batches) == len(moe_logits_batches), \
        f"Batch count mismatch: {len(gnn_logits_batches)} vs {len(moe_logits_batches)}"

    n = len(recs)

    # 2. 单模型 baseline (确认 forward 正确)
    print("\n=== 单模型 baseline ===")
    for name, batches in [('GNN+aux', gnn_logits_batches), ('MoE_balanced', moe_logits_batches)]:
        r = evaluate(batches, gt_batches, n, label=name)
        print(f"{name:<14} AVG Top-1={r['avg_top1']*100:.2f}%  Top-5={r['avg_top5']*100:.2f}%  Top-20={r['avg_top20']*100:.2f}%"
               f"  Joint Top-1={r['joint_top1']*100:.2f}%  Top-10={r['joint_top10']*100:.2f}%  Top-20={r['joint_top20']*100:.2f}%")

    # 3. 加权 ensemble (logit-level, softmax 归一化再加权)
    print(f"\n=== 加权 ensemble (logit-softmax 加权平均) ===")
    print(f"{'权重 (GNN, MoE)':<22} {'AVG T1':>8} {'AVG T5':>8} {'AVG T20':>8} {'Joint T1':>10} {'Joint T10':>10} {'Joint T20':>10}")
    weights = [(0.0, 1.0), (0.3, 0.7), (0.5, 0.5), (0.7, 0.3), (1.0, 0.0)]
    results = {}
    for w_g, w_m in weights:
        merged = []
        for gb, mb in zip(gnn_logits_batches, moe_logits_batches):
            merged_batch = {}
            for h in HEAD_KEYS:
                # 对每个 head: softmax(GNN) * w_g + softmax(MoE) * w_m (混合是概率分布)
                pg = F.softmax(gb[h], dim=-1)
                pm = F.softmax(mb[h], dim=-1)
                merged_batch[h] = w_g * pg + w_m * pm
            merged.append(merged_batch)
        r = evaluate(merged, gt_batches, n)
        results[(w_g, w_m)] = r
        print(f"  ({w_g:.1f}, {w_m:.1f})        "
               f"  {r['avg_top1']*100:>7.2f}% {r['avg_top5']*100:>7.2f}% {r['avg_top20']*100:>7.2f}%"
               f"   {r['joint_top1']*100:>8.2f}% {r['joint_top10']*100:>8.2f}% {r['joint_top20']*100:>8.2f}%")

    # 4. Cascade: GNN 给 Top-K 候选 → 在候选内用 MoE 概率重排 Top-1
    print(f"\n=== Cascade: GNN Top-K 候选 + MoE 重排 ===")
    print(f"{'cand K':<8} {'AVG Top-1':>10}  {'Joint Top-1':>12}")
    for cand_k in [3, 5, 10, 20]:
        cascade_top1_correct = {h: 0 for h in HEAD_KEYS}
        cascade_joint_top1 = 0
        for gb, mb, gt in zip(gnn_logits_batches, moe_logits_batches, gt_batches):
            joint_correct = None
            for h in HEAD_KEYS:
                # GNN 给 Top-K 候选
                kk = min(cand_k, gb[h].size(-1))
                _, gnn_top_k = gb[h].topk(kk, dim=-1)  # (B, K)
                # MoE 在 K 内取最高分
                moe_probs = F.softmax(mb[h], dim=-1)  # (B, num_classes)
                cand_probs = moe_probs.gather(1, gnn_top_k)  # (B, K)
                best_within_k = cand_probs.argmax(dim=-1)  # (B,)
                pred = gnn_top_k.gather(1, best_within_k.unsqueeze(-1)).squeeze(-1)
                correct = pred == gt[h]
                cascade_top1_correct[h] += int(correct.sum())
                if joint_correct is None:
                    joint_correct = correct.clone()
                else:
                    joint_correct = joint_correct & correct
            cascade_joint_top1 += int(joint_correct.sum())
        avg = np.mean([cascade_top1_correct[h] / n for h in HEAD_KEYS])
        joint = cascade_joint_top1 / n
        print(f"  K={cand_k:<5}  {avg*100:>9.2f}%  {joint*100:>11.2f}%")

    # 5. 保存结果
    out = {
        'weighted_ensemble': {f'gnn_{w_g}_moe_{w_m}': {k: float(v) for k, v in r.items()}
                                for (w_g, w_m), r in results.items()},
    }
    json.dump(out, open(EXP_DIR / 'ensemble_eval.json', 'w'), indent=2)
    print(f"\n✓ Saved {EXP_DIR / 'ensemble_eval.json'}")


if __name__ == "__main__":
    main()
