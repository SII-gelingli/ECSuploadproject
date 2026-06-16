"""跑小模型 (ConditionStage1HierSetV3+SMI+FineE) 在全 test 上的预测, 输出 JSON 给 LLM ablation 用."""
import sys, json
from pathlib import Path

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
# Need scripts/ as an importable namespace pkg so train_stage1_hier_set_v3 can `from scripts.X import Y`
import types as _types
_pkg = _types.ModuleType('scripts')
_pkg.__path__ = [str(project_root / 'scripts')]
sys.modules['scripts'] = _pkg

from models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3, SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS, FINE_ELECTRODE_HEADS,
)
from models.condition_stage1_set import decode_set, decode_set_topk
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('train_stage1_hier_set_v3',
    str(project_root / 'scripts' / 'train_stage1_hier_set_v3.py'))
_mod = _ilu.module_from_spec(_spec); sys.modules['train_stage1_hier_set_v3'] = _mod
_spec.loader.exec_module(_mod)
HierSetV3Dataset = _mod.HierSetV3Dataset
collate_fn = _mod.collate_fn

DATA_DIR = project_root / 'data_audited_v3_clean'
CKPT = project_root / 'checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt'
OUT_JSON = project_root.parent / 'eval_results' / 'small_model_test_predictions.json'


def topk(logits, name_map, k=3):
    probs = F.softmax(logits, dim=-1)
    tp, ti = torch.topk(probs, min(k, probs.size(-1)), dim=-1)
    return [(name_map.get(int(i), f'?({i})'), float(p)) for i, p in zip(ti, tp)]


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Loading test data + ckpt...')
    test = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.load(open(DATA_DIR / 'stats.json'))
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    nc = stats['num_classes']; nc_v3 = stats['num_classes_v3']

    # name maps for each head
    name_maps = {}
    for h in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
        if h in vocab:
            name_maps[h] = {v: k for k, v in vocab[h].items()}
    for h, names in vocab.get('__v3__', {}).items():
        name_maps[h] = {i: n for i, n in enumerate(names)}
    import importlib
    sys.path.insert(0, str(project_root.parent))
    from config import ELECTRODE_NAMES
    name_maps['anode'] = dict(ELECTRODE_NAMES)
    name_maps['cathode'] = dict(ELECTRODE_NAMES)

    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=0.3, class_embed_dim=32,
    ).to(device)
    ckpt = torch.load(CKPT, map_location=device, weights_only=False)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()

    coll = lambda b: collate_fn(b, nc)
    loader = DataLoader(HierSetV3Dataset(test), batch_size=128, shuffle=False,
                        num_workers=2, collate_fn=coll)

    # Heads to capture
    SINGLE_HEAD_INFO = [
        ('anode_material',   '阳极材料',   nc_v3['anode_material'],   name_maps['anode_material']),
        ('cathode_material', '阴极材料',   nc_v3['cathode_material'], name_maps['cathode_material']),
        ('cell_class_v3',    '池型',       nc_v3['cell_class_v3'],    name_maps['cell_class_v3']),
        ('electrolyte_cation', '电解质 cation', nc_v3['electrolyte_cation'], name_maps['electrolyte_cation']),
        ('electrolyte_anion',  '电解质 anion',  nc_v3['electrolyte_anion'],  name_maps['electrolyte_anion']),
        ('catalyst_class_v3',  '催化剂大类',     nc_v3['catalyst_class_v3'],  name_maps['catalyst_class_v3']),
        ('solvent_class_v3',   '溶剂大类',       nc_v3['solvent_class_v3'],   name_maps['solvent_class_v3']),
    ]
    SET_HEAD_INFO = [
        ('solvent',  '溶剂',     nc['solvent'],  name_maps['solvent']),
        ('reagent',  '试剂',     nc['reagent'],  name_maps['reagent']),
        ('catalyst', '催化剂',   nc['catalyst'], name_maps['catalyst']),
    ]

    rxn_to_pred = {}
    idx = 0
    print(f'Inferring on {len(test)} test reactions...')
    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher=None)
            bsz = fp.size(0)
            for i in range(bsz):
                r = test[idx]; idx += 1
                rs = r.get('reactant_smiles', []); ps = r.get('product_smiles', [])
                rxn = ('.'.join(rs) if isinstance(rs, list) else str(rs)) + '>>' + \
                       ('.'.join(ps) if isinstance(ps, list) else str(ps))

                pred = {}
                # Single heads — top-3 each
                for hname, label, n, nm in SINGLE_HEAD_INFO:
                    pred[hname] = [(name, float(p)) for name, p in topk(out[hname][i], nm, k=3)]

                # Set heads — top-3 SMILES + natural slot set (model's actual set output)
                for hname, label, n, nm in SET_HEAD_INFO:
                    slots = out[hname][i:i+1]
                    no_obj = nc[hname]
                    cand_ids = decode_set_topk(slots, no_obj, K_total=3)[0]
                    probs_per_slot = F.softmax(slots[0], dim=-1)
                    max_probs = probs_per_slot[:, :no_obj].max(dim=0).values
                    pred[f'{hname}_set_top3'] = [(nm.get(c, '?'), float(max_probs[c])) for c in cand_ids if c < no_obj][:3]
                    pred_ids = decode_set(slots, no_obj)[0]
                    pred[f'{hname}_set_natural'] = [nm.get(int(c), '?') for c in pred_ids]

                rxn_to_pred[rxn] = pred
            if idx % 500 == 0:
                print(f'  {idx}/{len(test)}', flush=True)
    print(f'  done: {idx}')

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(rxn_to_pred, indent=1, default=str))
    print(f'\n[OK] saved to {OUT_JSON}  ({OUT_JSON.stat().st_size/1e6:.2f} MB)')


if __name__ == '__main__':
    main()
