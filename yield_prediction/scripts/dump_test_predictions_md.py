"""把 test 集所有反应的 Top-3 预测 vs GT 输出到 markdown 可视化."""
import sys, json
from pathlib import Path
from collections import Counter

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

from models.condition_stage1_hier_set_v3 import (
    ConditionStage1HierSetV3, SINGLE_HEADS_V3, HIER_KEYS, SET_HEADS, SMI_FROM_CLASS,
    CAT_TAG_KEY, CAT_TAG_BITS, K_SLOTS, FINE_ELECTRODE_HEADS,
)
from models.condition_stage1_set import decode_set, decode_set_topk
from scripts.train_stage1_hier_set_v3 import HierSetV3Dataset, collate_fn

DATA_DIR = project_root / 'data_audited_v3_clean'
CKPT = project_root / 'checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt'
OUT_DIR = project_root / 'checkpoints/two_stage/experiments/test_predictions_md'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def topk(logits, name_map, k=3):
    probs = F.softmax(logits, dim=-1)
    tp, ti = torch.topk(probs, min(k, probs.size(-1)), dim=-1)
    return [(name_map.get(int(i), f'?({i})'), float(p)) for i, p in zip(ti, tp)]


RAW_SRC = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')


def build_paper_lookup():
    """反向查表: reaction_smiles_key -> [(paper_file_relative, reaction_idx, yield)]"""
    print(f'Building paper lookup from {RAW_SRC}...')
    lookup = {}
    for jf in RAW_SRC.rglob('*.json'):
        try:
            d = json.load(open(jf))
        except Exception:
            continue
        for ri, r in enumerate(d.get('reactions', [])):
            rs = r.get('reactants', []); ps = r.get('products', [])
            if isinstance(rs, list) and rs and isinstance(rs[0], dict):
                rs = [x.get('smiles') for x in rs if isinstance(x, dict) and x.get('smiles')]
            if isinstance(ps, list) and ps and isinstance(ps[0], dict):
                ps = [x.get('smiles') for x in ps if isinstance(x, dict) and x.get('smiles')]
            if not rs or not ps: continue
            key = '.'.join(rs) + '>>' + '.'.join(ps)
            yld_raw = r.get('yield')
            yld_v = None
            if isinstance(yld_raw, dict): yld_v = yld_raw.get('value')
            elif isinstance(yld_raw, (int, float)): yld_v = yld_raw
            elif isinstance(yld_raw, str):
                import re
                m = re.search(r'(\d+(?:\.\d+)?)', yld_raw)
                if m: yld_v = float(m.group(1))
            paper_rel = str(jf.relative_to(RAW_SRC))
            lookup.setdefault(key, []).append((paper_rel, ri, yld_v))
    print(f'  {len(lookup)} unique reactions in raw data')
    return lookup


def main():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Loading test data from {DATA_DIR}')
    test = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    stats = json.load(open(DATA_DIR / 'stats.json'))
    vocab = json.load(open(DATA_DIR / 'vocab.json'))
    nc = stats['num_classes']; nc_v3 = stats['num_classes_v3']
    print(f'{len(test)} test reactions')
    paper_lookup = build_paper_lookup()

    # Build idx → name maps
    name_maps = {}
    for h in ['solvent', 'electrolyte', 'catalyst', 'reagent', 'ligand', 'additive']:
        if h in vocab:
            name_maps[h] = {v: k for k, v in vocab[h].items()}
    for h, names in vocab.get('__v3__', {}).items():
        name_maps[h] = {i: n for i, n in enumerate(names)}
    # anode/cathode use ELECTRODE_NAMES from config (V2 vocab)
    import importlib
    sys.path.insert(0, str(project_root.parent))
    from config import ELECTRODE_NAMES
    name_maps['anode'] = dict(ELECTRODE_NAMES)
    name_maps['cathode'] = dict(ELECTRODE_NAMES)

    # Load model
    model = ConditionStage1HierSetV3(
        num_classes=nc, num_classes_v3=nc_v3, fp_dim=6144,
        hidden_dims=(1024, 768, 512), dropout=0.3, class_embed_dim=32,
    ).to(device)
    ckpt = torch.load(CKPT, map_location=device, weights_only=False)
    model.load_state_dict(ckpt['model_state_dict']); model.eval()

    coll = lambda b: collate_fn(b, nc)
    loader = DataLoader(HierSetV3Dataset(test), batch_size=128, shuffle=False,
                        num_workers=2, collate_fn=coll)

    # Heads to show in MD
    SINGLE_HEAD_INFO = [
        ('anode_material', '阳极 (材料)', nc_v3['anode_material'], name_maps['anode_material']),
        ('anode_fine', '阳极 (细类)', nc['anode_fine'], name_maps['anode_fine']),
        ('cathode_material', '阴极 (材料)', nc_v3['cathode_material'], name_maps['cathode_material']),
        ('cathode_fine', '阴极 (细类)', nc['cathode_fine'], name_maps['cathode_fine']),
        ('cell_class_v3', '池型', nc_v3['cell_class_v3'], name_maps['cell_class_v3']),
        ('electrolyte_cation', '电解质 cation', nc_v3['electrolyte_cation'], name_maps['electrolyte_cation']),
        ('electrolyte_anion', '电解质 anion', nc_v3['electrolyte_anion'], name_maps['electrolyte_anion']),
        ('reagent_class_v3', '试剂大类', nc_v3['reagent_class_v3'], name_maps['reagent_class_v3']),
        ('catalyst_class_v3', '催化剂大类', nc_v3['catalyst_class_v3'], name_maps['catalyst_class_v3']),
        ('solvent_class_v3', '溶剂大类', nc_v3['solvent_class_v3'], name_maps['solvent_class_v3']),
    ]
    SET_HEAD_INFO = [
        ('solvent', '溶剂 set', nc['solvent'], name_maps['solvent']),
        ('reagent', '试剂 set', nc['reagent'], name_maps['reagent']),
        ('catalyst', '催化剂 set', nc['catalyst'], name_maps['catalyst']),
    ]

    # Collect predictions for all reactions
    all_preds = []  # list of dicts: {'rxn', 'yield', 'gt': {head: ...}, 'pred': {head: [(label, prob)...]}}
    idx = 0
    with torch.no_grad():
        for batch in loader:
            fp = batch['fp'].to(device)
            out = model(fp, teacher=None)
            bsz = fp.size(0)
            for i in range(bsz):
                r = test[idx]; idx += 1
                # Build reaction display
                rs = r.get('reactant_smiles', [])
                ps = r.get('product_smiles', [])
                rxn = ('.'.join(rs) if isinstance(rs, list) else str(rs)) + '>>' + \
                       ('.'.join(ps) if isinstance(ps, list) else str(ps))
                # Look up source paper
                paper_matches = paper_lookup.get(rxn, [])
                # 多个 match (同反应在多个 paper 出现) — 优先 yield 接近的
                yld_t = r.get('yield')
                best_paper, best_ri = None, None
                if paper_matches:
                    if yld_t is not None:
                        # pick by closest yield
                        best = min(paper_matches, key=lambda x: abs((x[2] or -999) - yld_t))
                        best_paper, best_ri, _ = best
                    else:
                        best_paper, best_ri, _ = paper_matches[0]
                rec = {
                    'rxn': rxn,
                    'yield': r.get('yield'),
                    'paper': best_paper,
                    'paper_ri': best_ri,
                    'n_paper_matches': len(paper_matches),
                    'gt': {},
                    'pred': {},
                }
                # Single + hier + fine single heads
                for hname, label, n, nm in SINGLE_HEAD_INFO:
                    gt_idx = int(r['labels'].get(hname, 0))
                    rec['gt'][hname] = nm.get(gt_idx, f'?({gt_idx})')
                    rec['pred'][hname] = topk(out[hname][i], nm, k=3)
                # Set heads: GT 是 set_labels
                #   - pred_topk: top-3 跨 slot 候选 (用于显示)
                #   - pred_set:  K=4 slot 各自 argmax 去重去 no_obj (模型真实"集合预测")
                for hname, label, n, nm in SET_HEAD_INFO:
                    gt_set = r.get('set_labels', {}).get(hname, [])
                    rec['gt'][hname] = [nm.get(int(idx_), '?') for idx_ in gt_set]
                    slots = out[hname][i:i+1]
                    no_obj = nc[hname]
                    # 显示用 top-3
                    cand_ids = decode_set_topk(slots, no_obj, K_total=3)[0]
                    probs_per_slot = F.softmax(slots[0], dim=-1)
                    max_probs = probs_per_slot[:, :no_obj].max(dim=0).values
                    rec['pred'][hname] = [
                        (nm.get(c, '?'), float(max_probs[c])) for c in cand_ids if c < no_obj
                    ][:3]
                    # 模型自然 set 输出 (slot argmax 去重去 no_obj)
                    pred_ids = decode_set(slots, no_obj)[0]
                    rec.setdefault('pred_set', {})[hname] = [nm.get(int(c), '?') for c in pred_ids]
                all_preds.append(rec)
            print(f'  {idx}/{len(test)}', flush=True)

    print(f'\nProcessed {len(all_preds)} reactions')

    # === 生成 MD: 分文件输出 ===
    PER_FILE = 500  # 每 500 反应一个文件
    n_files = (len(all_preds) + PER_FILE - 1) // PER_FILE
    HEAD_DISPLAY = [(h, l, n) for h, l, n, _ in SINGLE_HEAD_INFO] + \
                   [(h, l, n) for h, l, n, _ in SET_HEAD_INFO]

    # 汇总统计
    #   - single head: top1 / top3 (普通分类)
    #   - set head:    exact_set (pred_set == gt_set, 严格, 对应千问 _exact_set)
    #                  any_top3  (top-3 候选与 GT 集合任意命中, 宽松)
    #                  GT 非空 + exact: 排除 GT={__ABSENT__} 的 "白送命中"
    ABSENT_TOKEN = '__ABSENT__'
    head_stats = {}
    for head, label, n in HEAD_DISPLAY:
        is_set = any(head == h for h, _, _, _ in SET_HEAD_INFO)
        total = 0
        if is_set:
            exact = 0; any_hit = 0
            gt_nonempty = 0; exact_nonempty = 0
            for rec in all_preds:
                gt_set = set(rec['gt'][head]) - {''}
                if not gt_set: continue
                pred_set_natural = set(rec.get('pred_set', {}).get(head, []))
                top3_set = {p[0] for p in rec['pred'][head]}
                total += 1
                ok_exact = (pred_set_natural == gt_set)
                if ok_exact:
                    exact += 1
                if top3_set & gt_set:
                    any_hit += 1
                # GT 非空 = GT 集合去 ABSENT 后非空
                if (gt_set - {ABSENT_TOKEN}):
                    gt_nonempty += 1
                    if ok_exact:
                        exact_nonempty += 1
            head_stats[head] = {'label': label, 'n_classes': n, 'total': total,
                                'is_set': True,
                                'exact': exact, 'any_hit': any_hit,
                                'exact_pct': exact/max(total, 1)*100,
                                'any_pct': any_hit/max(total, 1)*100,
                                'gt_nonempty': gt_nonempty,
                                'exact_nonempty': exact_nonempty,
                                'exact_nonempty_pct': exact_nonempty/max(gt_nonempty, 1)*100}
        else:
            top1 = 0; top3 = 0
            for rec in all_preds:
                gt = rec['gt'][head]
                preds = rec['pred'][head]
                if not gt or gt.startswith('__'): continue
                total += 1
                if preds and preds[0][0] == gt: top1 += 1
                if any(p[0] == gt for p in preds[:3]): top3 += 1
            head_stats[head] = {'label': label, 'n_classes': n, 'total': total,
                                'is_set': False,
                                'top1': top1, 'top3': top3,
                                'top1_pct': top1/max(total, 1)*100,
                                'top3_pct': top3/max(total, 1)*100}

    # 写 SUMMARY 文件
    summary_path = OUT_DIR / 'INDEX.md'
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# Test 集预测 vs GT 完整可视化\n\n")
        f.write(f"**Test 反应数**: {len(all_preds)}\n")
        _ep = ckpt.get('epoch', '?')
        _v_single = ckpt.get('val_single_avg', None)
        _v_setf1 = ckpt.get('val_set_f1', None)
        _score = (0.4 * _v_single + 0.6 * _v_setf1) if (_v_single is not None and _v_setf1 is not None) else None
        _score_str = f"{_score:.4f}" if _score is not None else "?"
        f.write(f"**模型**: ConditionStage1HierSetV3+SMI+FineE (epoch {_ep}, val score {_score_str})\n")
        f.write(f"**ckpt**: `stage1_hier_set_v3_smi_fineE.pt`\n\n")

        f.write(f"## 单类 Head 总体准确率 (在 test 集 {len(all_preds)} 反应上)\n\n")
        f.write(f"| Head | 类数 | 有效样本 | Top-1 命中 | Top-1 % | Top-3 命中 | Top-3 % |\n")
        f.write(f"|------|------|--------|-----------|---------|------------|---------|\n")
        for head, label, n in HEAD_DISPLAY:
            s = head_stats[head]
            if s['is_set']: continue
            f.write(f"| {label} (`{head}`) | {n} | {s['total']} | "
                    f"{s['top1']} | {s['top1_pct']:.2f}% | "
                    f"{s['top3']} | {s['top3_pct']:.2f}% |\n")

        f.write(f"\n## Set Head 总体准确率\n\n")
        f.write(f"- **exact_set**: 模型 K=4 slot 自然预测集合与 GT 集合**完全相等** (严格, 对应千问 `_exact_set`)\n")
        f.write(f"- **GT 非空 + exact**: 仅统计 GT 集合去 `__ABSENT__` 后**非空**的反应, 排除 \"GT=空 / 模型也猜空\" 的白送命中 — **真本事口径**\n")
        f.write(f"- **any (top-3)**: top-3 候选中**至少 1 个**出现在 GT 集合里 (宽松参考, 旧 'Hit ✓' 口径)\n\n")
        f.write(f"| Head | 类数 | 总样本 | exact_set | exact % | **GT 非空** | **set✓且 GT 非空** | **GT 非空命中率** | any 命中 | any % |\n")
        f.write(f"|------|------|-------|----------|---------|------------|-------------------|------------------|---------|-------|\n")
        for head, label, n in HEAD_DISPLAY:
            s = head_stats[head]
            if not s['is_set']: continue
            f.write(f"| {label} (`{head}`) | {n} | {s['total']} | "
                    f"{s['exact']} | {s['exact_pct']:.2f}% | "
                    f"**{s['gt_nonempty']}** | **{s['exact_nonempty']}** | "
                    f"**{s['exact_nonempty_pct']:.2f}%** | "
                    f"{s['any_hit']} | {s['any_pct']:.2f}% |\n")

        f.write(f"\n## 分文件\n\n")
        f.write(f"反应按 ID 分成 {n_files} 个文件 (每文件 {PER_FILE} 反应):\n\n")
        for i in range(n_files):
            start = i * PER_FILE + 1
            end = min((i+1) * PER_FILE, len(all_preds))
            f.write(f"- [Part {i+1}: 反应 #{start}-#{end}](part_{i+1:02d}.md)\n")
        f.write(f"\n## 字段说明\n\n")
        f.write(f"- **粗类 vs 细类**: anode_material (15) 是材料家族 (carbon/Pt/...), anode_fine (43) 是材料 × 形状 (graphite_rod / Pt_plate / RVC / ...)\n")
        f.write(f"- **Set head**: 多组分 K=4 slot 预测. Top-3 列出最高概率的 3 个 SMILES (跨 slot, 仅用于显示).\n")
        f.write(f"  - **`set ✓` = 模型 K=4 slot argmax 去重去 no_obj 得到的集合 == GT 集合** (严格, 对应千问 `_exact_set`)\n")
        f.write(f"  - `any ✓` = top-3 候选与 GT 至少有 1 个重合 (宽松参考)\n")
        f.write(f"- **Single head 'Hit' 列**: top-3 任意命中 ✓/✗, 后缀 `(T1✓)` 表示 top-1 就命中\n")
        f.write(f"- **GT 含 ABSENT**: 表示该字段实际为空 (反应不需要该条件)\n")
        f.write(f"- **置信度 (conf)**: softmax 概率, 反映模型对该预测的把握\n")

    # 写各 part 文件
    for fi in range(n_files):
        start = fi * PER_FILE
        end = min(start + PER_FILE, len(all_preds))
        part_path = OUT_DIR / f'part_{fi+1:02d}.md'
        with open(part_path, 'w', encoding='utf-8') as f:
            f.write(f"# Test 预测 part {fi+1} — 反应 #{start+1}-#{end}\n\n")
            f.write(f"[← 返回 INDEX](INDEX.md)\n\n")
            for ri in range(start, end):
                rec = all_preds[ri]
                yld = rec['yield']
                yld_str = f"yield={yld}%" if yld is not None else ""
                rxn = rec['rxn']
                if len(rxn) > 120: rxn = rxn[:117] + '…'
                f.write(f"### Reaction #{ri+1}  {yld_str}\n\n")
                paper = rec.get('paper')
                paper_ri = rec.get('paper_ri')
                if paper:
                    paper_rel = f"reactions_by_journal_alkene_ec_audited/{paper}"
                    f.write(f"**Source paper**: [`{paper}`]({paper_rel}) (反应 idx 在该 JSON 内 = #{paper_ri})\n\n")
                else:
                    f.write(f"**Source paper**: _(not found in raw data)_\n\n")
                f.write(f"```\n{rxn}\n```\n\n")
                f.write(f"| Head | 类数 | GT | Top-1 (conf) | Top-2 | Top-3 | Hit |\n")
                f.write(f"|------|------|----|---------------|-------|-------|-----|\n")
                for head, label, n in HEAD_DISPLAY:
                    gt = rec['gt'][head]
                    preds = rec['pred'][head]
                    if isinstance(gt, list):
                        gt_set = set(gt) - {''}
                        gt_str = ' + '.join(f"`{x[:18]}`" for x in (gt or ['—'])) if gt_set else '—'
                        pred_strs = [f"`{p[0][:18]}` ({p[1]*100:.0f}%)" for p in preds]
                        while len(pred_strs) < 3: pred_strs.append('—')
                        # 严格 set 命中: 模型 K=4 slot 自然预测集合 == GT 集合
                        pred_set_natural = set(rec.get('pred_set', {}).get(head, []))
                        top3_set = {p[0] for p in preds}
                        if not gt_set:
                            hit = '∅'  # GT 空
                        else:
                            set_ok = (pred_set_natural == gt_set)
                            any_ok = bool(top3_set & gt_set)
                            hit = f"set {'✓' if set_ok else '✗'} / any {'✓' if any_ok else '✗'}"
                    else:
                        gt_str = f"`{gt[:30]}`" if gt else '—'
                        pred_strs = [f"`{p[0][:30]}` ({p[1]*100:.1f}%)" for p in preds]
                        while len(pred_strs) < 3: pred_strs.append('—')
                        hit_top1 = '✓' if (preds and preds[0][0] == gt) else ''
                        hit_top3 = '✓' if any(p[0] == gt for p in preds[:3]) else '✗'
                        hit = f"{hit_top3}" + (f" (T1✓)" if hit_top1 else "")
                    f.write(f"| {label} | {n} | {gt_str} | {pred_strs[0]} | {pred_strs[1]} | {pred_strs[2]} | {hit} |\n")
                f.write(f"\n---\n\n")
        print(f'  Wrote {part_path.name} ({end-start} reactions)')

    print(f'\n✓ All MD files saved to {OUT_DIR}/')
    print(f'  Index: {summary_path}')
    print(f'  {n_files} part files')


if __name__ == '__main__':
    main()
