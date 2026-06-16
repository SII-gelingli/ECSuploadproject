"""Eval ConditionStage1HierSetV3XTB on test.pt."""
import sys, json, argparse
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

from models.condition_stage1_hier_set_v3_xtb import (
    ConditionStage1HierSetV3XTB,
    SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS,
)
from models.condition_stage1_set import decode_set, decode_set_topk
from scripts.train_stage1_set import set_metrics, topk_accuracy_single
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

SMI_HEADS = list(SMI_FROM_CLASS.keys())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default=str(project_root / 'data_audited_v3_clean'))
    parser.add_argument('--ckpt', default=str(project_root / 'checkpoints/two_stage/stage1_hier_set_v3_xtb.pt'))
    parser.add_argument('--out', default=str(project_root / 'checkpoints/two_stage/experiments/hier_set_v3_xtb_test.json'))
    args = parser.parse_args()

    DATA_DIR = Path(args.data_dir)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.load(open(DATA_DIR / 'stats.json'))
    nc, nc_v3 = stats['num_classes'], stats['num_classes_v3']
    xtb_table = torch.load(DATA_DIR / 'xtb_class_table.pt', weights_only=False)
    print(f'test={len(test_records)} device={device}')

    coll = lambda b: collate_fn(b, nc)
    loader = DataLoader(HierSetV3Dataset(test_records), batch_size=128, shuffle=False,
                        num_workers=2, collate_fn=coll)

    model = ConditionStage1HierSetV3XTB(
        num_classes=nc, num_classes_v3=nc_v3, xtb_class_table=xtb_table,
        fp_dim=6144, hidden_dims=(1024,768,512), dropout=0.3,
        class_embed_dim=32, cat_tag_embed_dim=8, xtb_mlp_hidden=64,
    ).to(device)
    ckpt = torch.load(args.ckpt, map_location=device, weights_only=False)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()
    print(f"Loaded ckpt epoch={ckpt['epoch']} val_set_f1={ckpt['val_set_f1']:.4f}")

    all_keys = SINGLE_HEADS_V3 + HIER_KEYS + SMI_HEADS
    sums = {k: {'top1':0, 'top3':0, 'top5':0} for k in all_keys}
    tag_tp = np.zeros(CAT_TAG_BITS); tag_pred = np.zeros(CAT_TAG_BITS)
    tag_gt = np.zeros(CAT_TAG_BITS); tag_total = 0
    set_preds = {h: [] for h in SET_HEADS}; set_gts = {h: [] for h in SET_HEADS}
    exact = {h: 0 for h in SET_HEADS}
    topk_recall = {h: {f'top{kk}':0 for kk in [5,10,20]} for h in SET_HEADS}
    joint_exact = 0
    n = 0
    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher=None)
            bsz = fp.size(0); n += bsz
            for k in all_keys:
                tgt = batch[k].to(device)
                r = topk_accuracy_single(out[k], tgt, ks=(1,3,5))
                for kk, v in r.items(): sums[k][kk] += v
            tl = out[CAT_TAG_KEY]
            tp = (torch.sigmoid(tl) > 0.5).float().cpu().numpy()
            tg = batch[CAT_TAG_KEY].numpy()
            tag_total += bsz; tag_pred += tp.sum(axis=0); tag_gt += tg.sum(axis=0)
            tag_tp += ((tp==1)&(tg==1)).sum(axis=0)
            per_h = []
            for h in SET_HEADS:
                slots = out[h]; no_obj = nc[h]
                pred = decode_set(slots, no_obj)
                set_preds[h].extend(pred)
                gt_p = batch[f'{h}_set'].cpu().numpy()
                gt_l = batch[f'{h}_len'].cpu().numpy()
                cand = decode_set_topk(slots, no_obj, K_total=20)
                mb = []
                for i in range(bsz):
                    gt_set = set(gt_p[i, :gt_l[i]].tolist())
                    set_gts[h].append(gt_p[i, :gt_l[i]].tolist())
                    ps = set(pred[i])
                    m = (ps == gt_set); mb.append(m)
                    if m: exact[h] += 1
                    if not gt_set: continue
                    for kk in [5,10,20]:
                        if gt_set & set(cand[i][:kk]): topk_recall[h][f'top{kk}'] += 1
                per_h.append(mb)
            for i in range(bsz):
                if all(per_h[hi][i] for hi in range(3)): joint_exact += 1

    result = {}
    print(f'\n[TEST] v3 single + hier + SMI head:')
    for k in all_keys:
        t1 = sums[k]['top1']/n; t3 = sums[k]['top3']/n; t5 = sums[k]['top5']/n
        print(f'  {k:<22} Top1={t1*100:5.2f}% Top3={t3*100:5.2f}% Top5={t5*100:5.2f}%')
        result[k] = {'top1': t1, 'top3': t3, 'top5': t5}
    single_avg = float(np.mean([sums[k]['top1']/n for k in SINGLE_HEADS_V3]))
    hier_avg = float(np.mean([sums[k]['top1']/n for k in HIER_KEYS]))
    smi_avg = float(np.mean([sums[k]['top1']/n for k in SMI_HEADS]))
    print(f'  AVG single (7) = {single_avg*100:.2f}%, AVG hier (3) = {hier_avg*100:.2f}%, AVG smi (2) = {smi_avg*100:.2f}%')
    result.update({'summary_single_avg7': single_avg, 'summary_hier_avg3': hier_avg, 'summary_smi_avg2': smi_avg})

    TAG_NAMES = ['mediator', 'photoredox', 'HAT', 'chiral']
    print(f'\n[TEST] catalyst tag multi-label:')
    tag_f1s = []
    for b in range(CAT_TAG_BITS):
        acc = (tag_tp[b] + (tag_total - tag_pred[b] - tag_gt[b] + tag_tp[b])) / tag_total if tag_total > 0 else 0
        p = tag_tp[b] / max(tag_pred[b], 1)
        r = tag_tp[b] / max(tag_gt[b], 1)
        f1 = 2*p*r / max(p+r, 1e-6); tag_f1s.append(f1)
        print(f'  {TAG_NAMES[b]:<12} prec={p*100:5.2f}% recall={r*100:5.2f}% F1={f1*100:5.2f}%')
        result[f'tag_{TAG_NAMES[b]}'] = {'precision': p, 'recall': r, 'f1': f1}
    tag_avg = float(np.mean(tag_f1s))
    result['tag_avg_f1'] = tag_avg
    print(f'  AVG tag F1 = {tag_avg*100:.2f}%')

    print(f'\n[TEST] set heads (具体 SMILES):')
    set_avg = 0
    for h in SET_HEADS:
        r, p, f1 = set_metrics(set_preds[h], set_gts[h])
        set_avg += f1
        t5 = topk_recall[h]['top5']/n; t10 = topk_recall[h]['top10']/n; t20 = topk_recall[h]['top20']/n
        ex = exact[h]/n
        print(f'  {h:<10} Recall={r*100:6.2f}% Prec={p*100:6.2f}% F1={f1*100:6.2f}% '
              f'Exact={ex*100:5.2f}% Top5={t5*100:5.2f}% Top10={t10*100:5.2f}% Top20={t20*100:5.2f}%')
        result[f'{h}_set'] = {'recall':r, 'precision':p, 'f1':f1, 'exact':ex,
                              'top5':t5, 'top10':t10, 'top20':t20}
    set_avg /= len(SET_HEADS)
    exact_avg = float(np.mean([exact[h]/n for h in SET_HEADS]))
    joint = joint_exact / n
    print(f'\n  set AVG F1 = {set_avg*100:.2f}%')
    print(f'  strict Exact AVG = {exact_avg*100:.2f}%')
    print(f'  Joint Exact (3 set 同时全对) = {joint*100:.2f}%')
    result.update({'set_avg_f1': set_avg, 'strict_exact_avg': exact_avg, 'joint_exact': joint})

    # 6-head AVG
    avg6 = (sums['anode_material']['top1']/n + sums['cathode_material']['top1']/n
            + (sums['electrolyte_cation']['top1']/n + sums['electrolyte_anion']['top1']/n)/2
            + result['solvent_set']['f1'] + result['reagent_set']['f1'] + result['catalyst_set']['f1']) / 6
    print(f'\n6-head AVG (no ligand/additive) = {avg6*100:.2f}%')
    result['avg6_head'] = avg6

    out_path = Path(args.out); out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    print(f'Saved -> {out_path}')

if __name__ == '__main__':
    main()
