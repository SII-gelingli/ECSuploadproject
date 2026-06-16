"""Stand-alone test eval for Stage-2 用量回归 (V2 head, teacher-forced category indices)."""
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

from models.condition_stage2 import ConditionStage2, AMOUNT_FIELDS, HEAD_KEYS
from scripts.train_stage2 import Stage2Dataset, transform_amount, inverse_transform


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default=str(project_root / 'data_audited_v3_clean'))
    parser.add_argument('--ckpt', default=str(project_root / 'checkpoints/two_stage/stage2_clean_v1.pt'))
    parser.add_argument('--out', default=str(project_root / 'checkpoints/two_stage/experiments/stage2_clean_v1_test.json'))
    args = parser.parse_args()

    DATA_DIR = Path(args.data_dir)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.loads((DATA_DIR / 'stats.json').read_text())
    amount_stats = json.loads((DATA_DIR / 'amount_stats.json').read_text())
    nc = stats['num_classes']
    print(f'test n={len(test_records)} device={device}')

    test_ds = Stage2Dataset(test_records, amount_stats)
    test_loader = DataLoader(test_ds, batch_size=256, shuffle=False, num_workers=2)

    ckpt = torch.load(args.ckpt, map_location=device, weights_only=False)
    fp_dim = ckpt.get('fp_dim', 6144)
    hidden_dims = tuple(ckpt.get('hidden_dims', (512, 256)))
    dropout = ckpt.get('dropout', 0.2)
    model = ConditionStage2(num_classes=nc, fp_dim=fp_dim,
                             hidden_dims=hidden_dims, dropout=dropout).to(device)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()
    print(f'  ckpt epoch={ckpt.get("epoch","?")} val score={ckpt.get("val_score","?")}')

    # Collect per-field preds & gts (in raw units)
    pred_all = {f: [] for f in AMOUNT_FIELDS}
    gt_all = {f: [] for f in AMOUNT_FIELDS}

    with torch.no_grad():
        for batch in test_loader:
            fp = batch['fp'].to(device)
            cat_idx = {k: batch[k].to(device) for k in HEAD_KEYS if k in batch}
            out = model(fp, cat_idx)
            masks = batch['mask'].numpy()
            for i, f in enumerate(AMOUNT_FIELDS):
                pred_norm = out[f].squeeze(-1).cpu().numpy()
                pred_raw = inverse_transform(pred_norm, amount_stats[f])
                gt_raw_norm = batch['targets'][:, i].numpy()
                gt_raw = inverse_transform(gt_raw_norm, amount_stats[f])
                for j in range(len(pred_raw)):
                    if masks[j, i] > 0:
                        pred_all[f].append(float(pred_raw[j]))
                        gt_all[f].append(float(gt_raw[j]))

    # Compute MAE, RMSE, R², 容差准确率
    result = {}
    # 容差定义 (per CLASSIFICATION_DESIGN's recommendation)
    TOL = {
        'catalyst_equiv': 0.2,        # ± 0.2 equiv
        'reagent_equiv': 0.2,         # ± 0.2 equiv
        'ligand_equiv': 0.05,         # ± 0.05 equiv
        'additive_equiv': 0.2,
        'electrolyte_M': 0.05,        # ± 0.05 M
        'current_mA': 0.20,           # ± 20% (relative)
        'current_density': 0.20,
        'potential_V': 0.2,           # ± 0.2 V
        'temperature_C': 5.0,         # ± 5 °C
        'time_h': 0.25,               # ± 25% (relative)
    }
    REL_TOL = {'current_mA', 'current_density', 'time_h'}

    print(f'\n[TEST] Stage-2 amount regression:')
    print(f"{'field':<22}{'n':>5}{'MAE':>10}{'RMSE':>10}{'R²':>8}{'within tol':>12}")
    avg_mae_std = 0
    n_fields = 0
    for f in AMOUNT_FIELDS:
        preds = np.asarray(pred_all[f]); gts = np.asarray(gt_all[f])
        n = len(preds)
        if n < 2:
            print(f"{f:<22}{n:>5}  (skip)")
            result[f] = {'n': n}
            continue
        mae = float(np.mean(np.abs(preds - gts)))
        rmse = float(np.sqrt(np.mean((preds - gts)**2)))
        ss_tot = float(np.var(gts))
        ss_res = float(np.mean((gts - preds)**2))
        r2 = 1.0 - ss_res / max(ss_tot, 1e-8)
        # 容差准确率
        tol = TOL[f]
        if f in REL_TOL:
            within = float(np.mean(np.abs(preds - gts) / np.maximum(np.abs(gts), 1e-6) <= tol))
        else:
            within = float(np.mean(np.abs(preds - gts) <= tol))
        # MAE / raw_std
        raw_std = amount_stats[f]['raw_std']
        mae_std = mae / max(raw_std, 1e-6)
        avg_mae_std += mae_std
        n_fields += 1
        print(f"{f:<22}{n:>5}{mae:>10.3f}{rmse:>10.3f}{r2:>8.3f}{within*100:>11.1f}%")
        result[f] = {'n': n, 'mae': mae, 'rmse': rmse, 'r2': r2, 'within_tol': within,
                     'tol': tol, 'mae_norm': mae_std}

    avg_mae_std /= max(n_fields, 1)
    result['avg_mae_norm'] = avg_mae_std
    print(f"\n  AVG MAE/std = {avg_mae_std:.3f}")
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    print(f'Saved -> {out_path}')


if __name__ == '__main__':
    main()
