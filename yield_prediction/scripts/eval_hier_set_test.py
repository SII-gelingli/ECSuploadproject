"""Eval ConditionStage1HierSet on test.pt."""
import sys, json
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

from models.condition_stage1_hier_set import (
    ConditionStage1HierSet, PARALLEL_HEADS, SET_HEADS, K_SLOTS,
)
from models.condition_stage1_set import decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single
from scripts.train_stage1_hier_set import HierSetDataset, collate_fn

DATA_DIR = project_root / 'data_audited_v3'
CKPT_PATH = project_root / 'checkpoints' / 'two_stage' / 'stage1_best.pt'


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Loading test data from {DATA_DIR}")
    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    print(f"test={len(test_records)}  device={device}")

    coll = lambda b: collate_fn(b, nc)
    test_loader = DataLoader(HierSetDataset(test_records), batch_size=128,
                              shuffle=False, num_workers=2, collate_fn=coll)

    model = ConditionStage1HierSet(num_classes=nc, fp_dim=6144,
                                    hidden_dims=(1024, 768, 512), dropout=0.3,
                                    class_embed_dim=32).to(device)
    ckpt = torch.load(CKPT_PATH, map_location=device, weights_only=False)
    sd = ckpt.get('model_state_dict') or ckpt.get('model_state') or ckpt.get('state_dict') or ckpt
    model.load_state_dict(sd)
    print(f"  ckpt epoch={ckpt.get('epoch','?')} val_single={ckpt.get('val_single_avg','?')} val_set_f1={ckpt.get('val_set_f1','?')}")
    model.eval()
    print(f"Loaded ckpt: {CKPT_PATH}")

    single_keys = list(PARALLEL_HEADS) + ['reagent_class']
    sums = {k: {'top1': 0, 'top3': 0, 'top5': 0} for k in single_keys}
    set_preds = {h: [] for h in SET_HEADS}
    set_gts = {h: [] for h in SET_HEADS}
    topk_recall = {h: {f'top{kk}': 0 for kk in [5, 10, 20]} for h in SET_HEADS}
    n = 0
    with torch.no_grad():
        for batch in test_loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher_class=None)
            bsz = fp.size(0); n += bsz
            for k in single_keys:
                tgt = batch[k].to(device)
                r = topk_accuracy_single(out[k], tgt, ks=(1, 3, 5))
                for kk, v in r.items():
                    sums[k][kk] += v
            for h in SET_HEADS:
                slots = out[h]; no_obj = nc[h]
                set_preds[h].extend(decode_set(slots, no_obj))
                gt_p = batch[f'{h}_set'].cpu().numpy()
                gt_l = batch[f'{h}_len'].cpu().numpy()
                cand = decode_set_topk(slots, no_obj, K_total=20)
                for i in range(bsz):
                    set_gts[h].append(gt_p[i, :gt_l[i]].tolist())
                    gt_set = set(gt_p[i, :gt_l[i]].tolist())
                    if not gt_set:
                        continue
                    for kk in [5, 10, 20]:
                        if gt_set & set(cand[i][:kk]):
                            topk_recall[h][f'top{kk}'] += 1

    result = {}
    print(f"\n[TEST] 单标签 head:")
    for k in single_keys:
        t1 = sums[k]['top1'] / n; t3 = sums[k]['top3'] / n; t5 = sums[k]['top5'] / n
        print(f"  {k:<14} Top1={t1*100:5.2f}% Top3={t3*100:5.2f}% Top5={t5*100:5.2f}%")
        result[k] = {'top1': t1, 'top3': t3, 'top5': t5}
    single_avg = np.mean([sums[k]['top1'] / n for k in PARALLEL_HEADS])  # 6 single (no rc)
    rc_top1 = sums['reagent_class']['top1'] / n
    print(f"  AVG (6 single)  {single_avg*100:5.2f}%  reagent_class Top-1 = {rc_top1*100:5.2f}%")

    # 8-head avg (no cell_type): anode/cathode/electrolyte/ligand/additive/solvent_set/reagent_set_F1/catalyst_set_F1
    # 不带 cell_type: 5 single + 3 set top-1 indicator
    # ↑ 此处先报 6-single-avg
    result['summary_single_avg6'] = single_avg
    result['reagent_class_top1'] = rc_top1

    print(f"\n[TEST] Set heads:")
    set_avg_f1 = 0
    for h in SET_HEADS:
        r, p, f1 = set_metrics(set_preds[h], set_gts[h])
        set_avg_f1 += f1
        t5 = topk_recall[h]['top5'] / n
        t10 = topk_recall[h]['top10'] / n
        t20 = topk_recall[h]['top20'] / n
        print(f"  {h:<10} Recall={r*100:6.2f}% Precision={p*100:6.2f}% F1={f1*100:6.2f}%  "
              f"Top5={t5*100:5.2f}%  Top10={t10*100:5.2f}%  Top20={t20*100:5.2f}%")
        result[f'{h}_set'] = {'recall': r, 'precision': p, 'f1': f1,
                              'top5': t5, 'top10': t10, 'top20': t20}
    set_avg_f1 /= len(SET_HEADS)
    score = 0.5 * single_avg + 0.5 * set_avg_f1
    print(f"\n[TEST] AVG set F1 = {set_avg_f1*100:.2f}%  Score = {score:.4f}")

    # 8-head avg (排除 cell_type/reagent_class, 用 set F1 当 set head)
    single_keys_no_cell = [k for k in PARALLEL_HEADS if k != 'cell_type']
    val_singles = [sums[k]['top1'] / n for k in single_keys_no_cell]
    set_f1s = []
    for h in SET_HEADS:
        r, p, f1 = set_metrics(set_preds[h], set_gts[h])
        set_f1s.append(f1)
    avg8 = float(np.mean(val_singles + set_f1s))
    print(f"\n[TEST] 8-head AVG (5 single + 3 set F1) = {avg8*100:.2f}%")
    result['avg8'] = avg8
    result['set_avg_f1'] = set_avg_f1
    result['score'] = score

    out_path = project_root / 'checkpoints' / 'two_stage' / 'experiments' / 'hier_set_test_newdata.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Saved -> {out_path}")


if __name__ == '__main__':
    main()
