"""GNN Stage-1 test 集评估: per-head + joint Top-K."""
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
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.condition_stage1_gnn import ConditionStage1GNN
from models.condition_stage1 import HEAD_KEYS
from scripts.train_stage1_gnn import GNNStage1Dataset, collate_fn, graph_to_device

ABSENT_INDEX = {'anode': 22, 'cathode': 22, 'cell_type': 3,
                'solvent': 0, 'electrolyte': 0, 'catalyst': 0,
                'reagent': 0, 'ligand': 0, 'additive': 0}


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    ckpt_path = Path(sys.argv[1]) if len(sys.argv) > 1 else \
                project_root / 'checkpoints/two_stage/experiments/stage1_gnn.pt'
    print(f"Loading {ckpt_path}")
    ckpt = torch.load(ckpt_path, weights_only=False)
    nc = ckpt['num_classes']
    print(f"epoch={ckpt['epoch']} val_top1={ckpt['val_avg_top1']:.4f}")

    m = ConditionStage1GNN(num_classes=nc, gnn_hidden=ckpt['gnn_hidden'],
                            gnn_layers=ckpt['gnn_layers'], gnn_heads=ckpt['gnn_heads'],
                            dropout=ckpt['dropout']).to(device)
    m.load_state_dict(ckpt['model_state_dict'])
    m.eval()

    test_records = torch.load(project_root / 'data_audited_v3/test.pt', weights_only=False)
    ds = GNNStage1Dataset(test_records)
    loader = DataLoader(ds, batch_size=64, shuffle=False, num_workers=0, collate_fn=collate_fn)

    KS = [1, 3, 5, 10, 20]
    head_topk = {k: {f'top{kk}': 0 for kk in KS} for k in HEAD_KEYS}
    head_topk_na = {k: {f'top{kk}': 0 for kk in KS} for k in HEAD_KEYS}
    head_n_na = {k: 0 for k in HEAD_KEYS}
    absent_actual = {k: 0 for k in HEAD_KEYS}
    absent_pred = {k: 0 for k in HEAD_KEYS}
    absent_correct = {k: 0 for k in HEAD_KEYS}
    joint = {k: 0 for k in KS}
    joint8 = {k: 0 for k in KS}
    total = 0
    with torch.no_grad():
        for batch in loader:
            rg = graph_to_device(batch['r_graph'], device)
            pg = graph_to_device(batch['p_graph'], device)
            logits = m(rg, pg)
            bsz = batch['yield'].size(0); total += bsz
            ink = {k: [] for k in KS}
            for h in HEAD_KEYS:
                tgt = batch[h].to(device); lg = logits[h]
                for k in KS:
                    kk = min(k, lg.size(-1))
                    _, pred = lg.topk(kk, dim=-1)
                    in_k = pred.eq(tgt.view(-1, 1)).any(dim=1)
                    head_topk[h][f'top{k}'] += int(in_k.sum())
                    ink[k].append(in_k)
                pred1 = lg.argmax(dim=-1)
                a_t = tgt == ABSENT_INDEX[h]
                a_p = pred1 == ABSENT_INDEX[h]
                absent_actual[h] += int(a_t.sum())
                absent_pred[h] += int(a_p.sum())
                absent_correct[h] += int((a_t & a_p).sum())
                non_a = ~a_t
                if non_a.sum() > 0:
                    head_n_na[h] += int(non_a.sum())
                    lg_na = lg[non_a]; tgt_na = tgt[non_a]
                    for k in KS:
                        kk = min(k, lg_na.size(-1))
                        _, p_na = lg_na.topk(kk, dim=-1)
                        head_topk_na[h][f'top{k}'] += int(p_na.eq(tgt_na.view(-1, 1)).any(dim=1).sum())
            for k in KS:
                s = torch.stack(ink[k], dim=0)
                joint[k] += int(s.all(dim=0).sum())
                joint8[k] += int((s.sum(dim=0) >= 8).sum())

    print(f"\nTest set: {total} reactions\n")
    print(f"{'head':<14}{'Top1':>8}{'Top3':>8}{'Top5':>8}{'Top10':>8}{'Top20':>8}  | non-ABSENT: {'Top1':>7}{'Top3':>7}")
    for h in HEAD_KEYS:
        line = f"{h:<14}"
        for k in KS:
            line += f"{head_topk[h][f'top{k}']/total*100:>7.2f}%"
        nn = head_n_na[h]
        line += f"  |  {head_topk_na[h]['top1']/max(1,nn)*100:>6.2f}%{head_topk_na[h]['top3']/max(1,nn)*100:>6.2f}%"
        print(line)
    avg = {k: np.mean([head_topk[h][f'top{k}']/total for h in HEAD_KEYS]) for k in KS}
    print(f"{'AVG':<14}{avg[1]*100:>7.2f}%{avg[3]*100:>7.2f}%{avg[5]*100:>7.2f}%{avg[10]*100:>7.2f}%{avg[20]*100:>7.2f}%")
    print(f"\nJoint Top-K:")
    print(f"  K     9/9     >=8/9")
    for k in KS:
        print(f"  Top-{k:<3d} {joint[k]/total*100:5.2f}%  {joint8[k]/total*100:5.2f}%")

    print(f"\nABSENT 预测可靠性:")
    print(f"  {'head':<14}{'actual':>7}{'pred':>7}{'correct':>9}{'prec':>8}{'recall':>8}")
    for h in HEAD_KEYS:
        prec = absent_correct[h] / max(1, absent_pred[h])
        rec = absent_correct[h] / max(1, absent_actual[h])
        print(f"  {h:<14}{absent_actual[h]:>7}{absent_pred[h]:>7}{absent_correct[h]:>9}{prec*100:>7.2f}%{rec*100:>7.2f}%")


if __name__ == "__main__":
    main()
