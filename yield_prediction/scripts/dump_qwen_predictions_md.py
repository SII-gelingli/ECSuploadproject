"""把千问 (Qwen3-8B SFT) 在 test 集每条反应的预测 vs GT 输出到 markdown."""
import sys, json, re
from pathlib import Path

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import torch

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

DATA_DIR = project_root / 'data_audited_v3_clean'
QWEN_EVAL = project_root / 'eval_results' / 'qwen3_8b_clean_v1.json'
OUT_DIR = project_root / 'eval_results' / 'qwen_predictions_md'
OUT_DIR.mkdir(parents=True, exist_ok=True)
PART_SIZE = 500

RAW_SRC = Path('/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited')


def build_paper_lookup():
    print(f'Building paper lookup from {RAW_SRC}...')
    lookup = {}
    for jf in RAW_SRC.rglob('*.json'):
        try:
            d = json.load(open(jf))
        except Exception:
            continue
        for ri, r in enumerate(d.get('reactions', [])):
            rs = r.get('reactants', [])
            ps = r.get('products', [])
            if isinstance(rs, list) and rs and isinstance(rs[0], dict):
                rs = [x.get('smiles') for x in rs if isinstance(x, dict) and x.get('smiles')]
            if isinstance(ps, list) and ps and isinstance(ps[0], dict):
                ps = [x.get('smiles') for x in ps if isinstance(x, dict) and x.get('smiles')]
            if not rs or not ps:
                continue
            key = '.'.join(rs) + '>>' + '.'.join(ps)
            yld_raw = r.get('yield')
            yld_v = None
            if isinstance(yld_raw, dict):
                yld_v = yld_raw.get('value')
            elif isinstance(yld_raw, (int, float)):
                yld_v = yld_raw
            elif isinstance(yld_raw, str):
                m = re.search(r'(\d+(?:\.\d+)?)', yld_raw)
                if m:
                    yld_v = float(m.group(1))
            paper_rel = str(jf.relative_to(RAW_SRC))
            lookup.setdefault(key, []).append((paper_rel, ri, yld_v))
    print(f'  {len(lookup)} unique reactions in raw data')
    return lookup


def fmt_list(x):
    if not x:
        return '_(empty)_'
    if isinstance(x, str):
        return f'`{x}`'
    return ' + '.join(f'`{s}`' for s in x)


def fmt_str(x):
    if x is None or x == '':
        return '_(empty)_'
    return f'`{x}`'


def hit_mark(b):
    return '✓' if b else '✗'


def canon_set_of(smiles_list):
    """对外暴露,用于 any_overlap 计算。和 eval_qwen_sft.canon_set 同口径。"""
    from scripts.eval_qwen_sft import canon_set
    return canon_set(smiles_list)


def list_field_row(name, gold_list, pred_list, m_set, m_any):
    """For SMILES list fields, show GT, pred, and set + any hits."""
    return (f'| {name} | {fmt_list(gold_list)} | {fmt_list(pred_list)} | '
            f'set {hit_mark(m_set)} / any {hit_mark(m_any)} |')


def single_field_row(name, gold, pred, hit):
    return f'| {name} | {fmt_str(gold)} | {fmt_str(pred)} | {hit_mark(hit)} |'


def render_reaction(i, test_rec, qwen_det, paper_info):
    rs = test_rec['reactant_smiles']
    ps = test_rec['product_smiles']
    rxn = '.'.join(rs) + '>>' + '.'.join(ps)
    yld = test_rec.get('yield')
    yld_s = f' yield={yld}%' if yld is not None else ''

    lines = [f'### Reaction #{i+1}{yld_s}', '']
    if paper_info:
        paper, ri = paper_info
        paper_rel = f'reactions_by_journal_alkene_ec_audited/{paper}'
        lines.append(f'**Source paper**: [`{paper}`]({paper_rel}) (反应 idx 在该 JSON 内 = #{ri})')
    else:
        lines.append('**Source paper**: _(not found in raw data)_')
    lines += ['', '```', rxn[:300] + ('…' if len(rxn) > 300 else ''), '```', '']

    g = qwen_det.get('gold') or {}
    p = qwen_det.get('pred') or {}
    mt = qwen_det.get('metrics') or {}

    lines.append('| 字段 | GT | Qwen Pred | Hit |')
    lines.append('|------|----|-----------|-----|')
    lines.append(single_field_row('anode', g.get('anode'), p.get('anode'), mt.get('anode', False)))
    lines.append(single_field_row('cathode', g.get('cathode'), p.get('cathode'), mt.get('cathode', False)))
    lines.append(single_field_row('cell_type', g.get('cell_type'), p.get('cell_type'), mt.get('cell_type', False)))
    for k in ('electrolytes', 'solvents', 'reagents', 'catalysts'):
        gl = g.get(k, []) or []
        pl = p.get(k, []) or []
        g_set = canon_set_of(gl)
        p_set = canon_set_of(pl)
        any_ok = bool(g_set & p_set) if g_set else (len(p_set) == 0)
        lines.append(list_field_row(
            k, gl, pl,
            mt.get(f'{k}_exact_set', False), any_ok))
    # ligands / additives (no aggregate metric reported; show for context)
    for k in ('ligands', 'additives'):
        gl = g.get(k, [])
        pl = p.get(k, [])
        same = set(gl or []) == set(pl or [])
        lines.append(f'| {k} | {fmt_list(gl)} | {fmt_list(pl)} | set {hit_mark(same)} |')
    lines += ['', '---', '']
    return '\n'.join(lines)


def main():
    print(f'Loading test data: {DATA_DIR}/test.pt')
    test_records = torch.load(DATA_DIR / 'test.pt', weights_only=False)
    n = len(test_records)
    print(f'  {n} test reactions')

    print(f'Loading qwen eval: {QWEN_EVAL}')
    qwen = json.load(open(QWEN_EVAL))
    detail = qwen['detail']
    assert len(detail) == n, f'qwen detail {len(detail)} != test {n}'

    paper_lookup = build_paper_lookup()

    # Resolve paper for each reaction (by rxn smiles + yield disambig)
    paper_resolved = []
    for i, rec in enumerate(test_records):
        rxn = '.'.join(rec['reactant_smiles']) + '>>' + '.'.join(rec['product_smiles'])
        matches = paper_lookup.get(rxn, [])
        if not matches:
            paper_resolved.append(None)
            continue
        yld = rec.get('yield')
        if yld is not None and len(matches) > 1:
            best = min(matches, key=lambda x: abs((x[2] or -999) - yld))
            paper_resolved.append((best[0], best[1]))
        else:
            paper_resolved.append((matches[0][0], matches[0][1]))

    # Aggregate metrics
    metric_keys = ['anode', 'cathode', 'cell_type',
                   'electrolytes_first', 'electrolytes_exact_set',
                   'solvents_first', 'solvents_exact_set',
                   'reagents_first', 'reagents_exact_set',
                   'catalysts_first', 'catalysts_exact_set']
    sums = {k: 0 for k in metric_keys}
    list_fields = ('electrolytes', 'solvents', 'reagents', 'catalysts')
    any_sums = {f: 0 for f in list_fields}
    # GT 非空(canonical 后非空) + set✓ 的真本事口径
    gt_nonempty = {f: 0 for f in list_fields}
    exact_nonempty = {f: 0 for f in list_fields}
    for d in detail:
        for k in metric_keys:
            if d.get('metrics', {}).get(k):
                sums[k] += 1
        g = d.get('gold') or {}
        p = d.get('pred') or {}
        for f in list_fields:
            g_set = canon_set_of(g.get(f, []) or [])
            p_set = canon_set_of(p.get(f, []) or [])
            # any
            if g_set:
                if g_set & p_set:
                    any_sums[f] += 1
            else:
                if not p_set:
                    any_sums[f] += 1
            # GT 非空 + exact
            if g_set:
                gt_nonempty[f] += 1
                if g_set == p_set:
                    exact_nonempty[f] += 1
    rates = {k: sums[k] / n for k in metric_keys}
    any_rates = {f: any_sums[f] / n for f in list_fields}
    nonempty_rates = {f: exact_nonempty[f] / max(gt_nonempty[f], 1) for f in list_fields}

    # Write parts
    n_parts = (n + PART_SIZE - 1) // PART_SIZE
    part_files = []
    for p in range(n_parts):
        start = p * PART_SIZE
        end = min(start + PART_SIZE, n)
        fname = f'part_{p+1:02d}.md'
        path = OUT_DIR / fname
        part_files.append((fname, start + 1, end))
        with open(path, 'w') as f:
            f.write(f'# Qwen3-8B 预测 part {p+1} — 反应 #{start+1}-#{end}\n\n')
            f.write('[← 返回 INDEX](INDEX.md)\n\n')
            for i in range(start, end):
                f.write(render_reaction(i, test_records[i], detail[i], paper_resolved[i]))
        print(f'  wrote {path} ({end-start} reactions)')

    # Write INDEX
    idx = OUT_DIR / 'INDEX.md'
    with open(idx, 'w') as f:
        f.write('# Qwen3-8B SFT — Test 集预测 vs GT 完整可视化\n\n')
        f.write(f'**Test 反应数**: {n}\n')
        f.write(f'**模型**: Qwen3-8B + LoRA SFT (`qwen3_8b_clean_v1`)\n')
        f.write(f'**数据**: `data_qwen_sft_v3/test.jsonl` (= `data_audited_v3_clean/test.pt`, 2025+ papers, strict zero-leakage)\n')
        f.write(f'**JSON 解析失败**: {qwen.get("json_parse_fail", 0)} / {n}\n\n')

        f.write('## 总体准确率\n\n')
        f.write('### 单字段 (电极 / cell_type)\n\n')
        f.write('| 字段 | 命中 | 准确率 |\n|------|------|-------|\n')
        for k in ('anode', 'cathode', 'cell_type'):
            f.write(f'| {k} | {sums[k]} / {n} | {rates[k]*100:.2f}% |\n')

        f.write('\n### 多元素字段 (SMILES list)\n\n')
        f.write('- **`set`**: pred 集合与 GT 集合 canonical 后**完全相等** (严格, 对应小模型 set head 同口径)\n')
        f.write('- **GT 非空 + set✓**: 仅统计 GT canonical 后**非空**的反应, 排除 "GT=空 / 模型也猜空" 的白送命中 — **真本事口径**\n')
        f.write('- `any`: pred 与 GT 集合至少 1 个 canonical SMILES 重合 (宽松参考)\n')
        f.write('- *`first` 是历史口径(只比第 1 个),只对 list 顺序敏感,不作主指标,仅供参考*\n\n')
        f.write('| 字段 | set 命中 | set % | **GT 非空** | **set✓且 GT 非空** | **GT 非空命中率** | any % | (参考) first % |\n')
        f.write('|------|---------|-------|------------|-------------------|------------------|-------|----------------|\n')
        for k in list_fields:
            f.write(f'| {k} | {sums[f"{k}_exact_set"]} / {n} | {rates[f"{k}_exact_set"]*100:.2f}% '
                    f'| **{gt_nonempty[k]}** | **{exact_nonempty[k]}** '
                    f'| **{nonempty_rates[k]*100:.2f}%** '
                    f'| {any_rates[k]*100:.2f}% '
                    f'| {rates[f"{k}_first"]*100:.2f}% |\n')

        f.write('\n## 分文件\n\n')
        f.write(f'反应按 ID 分成 {n_parts} 个文件 (每文件 {PART_SIZE} 反应):\n\n')
        for fname, lo, hi in part_files:
            f.write(f'- [Part {fname.split("_")[1].split(".")[0]}: 反应 #{lo}-#{hi}]({fname})\n')

        f.write('\n## 字段说明\n\n')
        f.write('- **GT** = 论文真值 (`data_audited_v3_clean/test.pt` 解码出的 canonical SMILES / 电极文本)\n')
        f.write('- **Qwen Pred** = 模型直接生成的 JSON 字段(未经 vocab 限制,可输出任意字符串)\n')
        f.write('- **Hit** 列:\n')
        f.write('  - 单字段(anode/cathode/cell_type):用 `electrode_to_id` / `encode_cell_type` 归一化后比较\n')
        f.write('  - 多元素字段:**`set ✓`** = pred 集合 == GT 集合(严格,主指标);`any ✓` = 至少 1 个重合(宽松参考)\n')
        f.write('  - electrolytes 单元素时 `set` 与 `any` 等价(EC 反应大多 1 个支持电解质)\n')
        f.write('- ligands / additives 大部分反应为空,仅显示供参考(无聚合准确率口径)\n')

    print(f'\n[OK] wrote {idx}')
    print(f'      + {n_parts} part files in {OUT_DIR}/')


if __name__ == '__main__':
    main()
