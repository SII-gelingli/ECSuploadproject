"""Eval ConditionStage1HierSetV3 on test.pt."""
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

from models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3, SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS, FINE_ELECTRODE_HEADS,
)
from models.condition_stage1_set import decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

SMI_HEADS = list(SMI_FROM_CLASS.keys())

import argparse
DEFAULT_DATA_DIR = project_root / 'data_audited_v3'
DEFAULT_CKPT = project_root / 'checkpoints' / 'two_stage' / 'stage1_hier_set_v3_smi.pt'
DEFAULT_OUT = project_root / 'checkpoints' / 'two_stage' / 'experiments' / 'hier_set_v3_smi_test.json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default=str(DEFAULT_DATA_DIR))
    parser.add_argument('--ckpt', default=str(DEFAULT_CKPT))
    parser.add_argument('--out', default=str(DEFAULT_OUT))
    args = parser.parse_args()
    DATA_DIR = Path(args.data_dir); CKPT_PATH = Path(args.ckpt)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Loading test data from {DATA_DIR}")
    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    nc = stats['num_classes']
    nc_v3 = stats['num_classes_v3']
    print(f"test={len(test_records)}  device={device}")

    coll = lambda b: collate_fn(b, nc)
    test_loader = DataLoader(HierSetV3Dataset(test_records), batch_size=128,
                              shuffle=False, num_workers=2, collate_fn=coll)

    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=0.3,
        class_embed_dim=32, cat_tag_embed_dim=8,
    ).to(device)
    ckpt = torch.load(CKPT_PATH, map_location=device, weights_only=False)
    sd = ckpt.get('model_state_dict') or ckpt.get('model_state') or ckpt.get('state_dict') or ckpt
    model.load_state_dict(sd)
    model.eval()
    print(f"Loaded ckpt: {CKPT_PATH}")
    print(f"  ckpt epoch={ckpt.get('epoch','?')} val_single={ckpt.get('val_single_avg','?')} "
          f"val_set_f1={ckpt.get('val_set_f1','?')} val_tag_f1={ckpt.get('val_tag_f1','?')}")

    all_keys = SINGLE_HEADS_V3 + FINE_ELECTRODE_HEADS + HIER_KEYS + SMI_HEADS
    sums = {k: {'top1': 0, 'top3': 0, 'top5': 0} for k in all_keys}
    tag_correct = np.zeros(CAT_TAG_BITS); tag_total = 0
    tag_pred_pos = np.zeros(CAT_TAG_BITS); tag_gt_pos = np.zeros(CAT_TAG_BITS)
    tag_tp = np.zeros(CAT_TAG_BITS)
    set_preds = {h: [] for h in SET_HEADS}
    set_gts = {h: [] for h in SET_HEADS}
    topk_recall = {h: {f'top{kk}': 0 for kk in [5, 10, 20]} for h in SET_HEADS}
    n = 0
    with torch.no_grad():
        for batch in test_loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher=None)
            bsz = fp.size(0); n += bsz
            for k in all_keys:
                tgt = batch[k].to(device)
                r = topk_accuracy_single(out[k], tgt, ks=(1, 3, 5))
                for kk, v in r.items():
                    sums[k][kk] += v
            tag_logits = out[CAT_TAG_KEY]
            tag_pred = (torch.sigmoid(tag_logits) > 0.5).float().cpu().numpy()
            tag_gt = batch[CAT_TAG_KEY].numpy()
            tag_correct += (tag_pred == tag_gt).sum(axis=0)
            tag_total += bsz
            tag_pred_pos += tag_pred.sum(axis=0)
            tag_gt_pos += tag_gt.sum(axis=0)
            tag_tp += ((tag_pred == 1) & (tag_gt == 1)).sum(axis=0)
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
    print(f"\n[TEST] v3 single + hier + SMI head:")
    for k in all_keys:
        t1 = sums[k]['top1'] / n; t3 = sums[k]['top3'] / n; t5 = sums[k]['top5'] / n
        print(f"  {k:<22} Top1={t1*100:5.2f}% Top3={t3*100:5.2f}% Top5={t5*100:5.2f}%")
        result[k] = {'top1': t1, 'top3': t3, 'top5': t5}
    single_avg = float(np.mean([sums[k]['top1'] / n for k in SINGLE_HEADS_V3]))
    hier_avg = float(np.mean([sums[k]['top1'] / n for k in HIER_KEYS]))
    smi_avg = float(np.mean([sums[k]['top1'] / n for k in SMI_HEADS]))
    print(f"  AVG single (7) = {single_avg*100:.2f}%, AVG hier (3) = {hier_avg*100:.2f}%, AVG smi (2) = {smi_avg*100:.2f}%")
    result['summary_single_avg7'] = single_avg
    result['summary_hier_avg3'] = hier_avg
    result['summary_smi_avg2'] = smi_avg

    TAG_NAMES = ['mediator', 'photoredox', 'HAT', 'chiral']
    print(f"\n[TEST] catalyst tag multi-label:")
    tag_f1s = []
    for b in range(CAT_TAG_BITS):
        acc = tag_correct[b] / tag_total
        p = tag_tp[b] / max(tag_pred_pos[b], 1)
        r = tag_tp[b] / max(tag_gt_pos[b], 1)
        f1 = 2*p*r / max(p+r, 1e-6)
        tag_f1s.append(f1)
        print(f"  {TAG_NAMES[b]:<12} acc={acc*100:5.2f}% prec={p*100:5.2f}% recall={r*100:5.2f}% F1={f1*100:5.2f}%")
        result[f'tag_{TAG_NAMES[b]}'] = {'acc': acc, 'precision': p, 'recall': r, 'f1': f1}
    tag_avg_f1 = float(np.mean(tag_f1s))
    print(f"  AVG tag F1 = {tag_avg_f1*100:.2f}%")
    result['tag_avg_f1'] = tag_avg_f1

    print(f"\n[TEST] set heads (具体 SMILES):")
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
    result['set_avg_f1'] = set_avg_f1
    score = 0.35 * single_avg + 0.15 * hier_avg + 0.1 * smi_avg + 0.1 * tag_avg_f1 + 0.3 * set_avg_f1
    result['score'] = score
    print(f"\n[TEST] set AVG F1 = {set_avg_f1*100:.2f}%  score = {score:.4f}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Saved -> {out_path}")


if __name__ == '__main__':
    main()
