"""Evaluate a LoRA-finetuned Qwen on data_qwen_sft/test.jsonl.

Per-field top-1 accuracy:
- anode / cathode: normalized via electrode_to_id (matches MLP eval protocol).
- cell_type: normalized via encode_cell_type (same).
- electrolytes / solvents / reagents / catalysts: list of SMILES.
  * `_exact_set`: canonical SMILES set match (strict).
  * `_first`:     first element canonical match (matches MLP protocol).

Usage:
  python3 scripts/eval_qwen_sft.py [--adapter PATH] [--base PATH] [--out PATH]
"""
import argparse
import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

for _p in (
    "/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages",
    "/inspire/hdd/global_user/gelingli-253114010248/pip_packages",
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# 屏蔽 torchao：本地 0.11.0+git 太旧，PEFT 要求 ≥0.16.0 才会用。
import importlib.util as _iu
_orig_find_spec = _iu.find_spec
def _no_torchao(name, *a, **k):
    if name == "torchao" or name.startswith("torchao."):
        return None
    return _orig_find_spec(name, *a, **k)
_iu.find_spec = _no_torchao

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

PROJECT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction")
sys.path.insert(0, str(PROJECT))

from utils.electrode_normalizer import electrode_to_id


def encode_cell_type(cell_type):
    """Inlined from prepare_data_audited.py to keep eval lightweight."""
    if cell_type is None or str(cell_type).strip() == '':
        return 5
    ct = str(cell_type).lower().strip().strip('"\'()')
    if any(k in ct for k in ('undivi', 'undvi', 'udivi', 'unndiv', 'undiv')):
        return 0
    if any(k in ct for k in ('beaker', 'electrasyn', 'three-neck', 'bottle', 'flask', 'schlenk')):
        return 0
    if any(k in ct for k in ('h-cell', 'h-type', 'h cell', 'diaphragm', 'two-compartment', 'compartment')):
        return 1
    if 'divided' in ct or 'devided' in ct or 'separation' in ct or 'ex-cell' in ct:
        return 1
    if 'flow' in ct or 'vapourtec' in ct:
        return 2
    if 'sealed' in ct:
        return 3
    if 'electrochem' in ct or 'electrolysis' in ct or 'electrolytic' in ct or 'reactor' in ct:
        return 4
    return 5


_RDKIT_SILENCED = False


def _silence_rdkit():
    global _RDKIT_SILENCED
    if _RDKIT_SILENCED:
        return
    try:
        from rdkit import RDLogger
        RDLogger.DisableLog('rdApp.*')
        _RDKIT_SILENCED = True
    except Exception:
        pass


def canonical(smi: str):
    _silence_rdkit()
    try:
        from rdkit import Chem
        m = Chem.MolFromSmiles(smi)
        if m is None:
            return None
        return Chem.MolToSmiles(m)
    except Exception:
        return None


def canon_set(smiles_list):
    out = set()
    for s in smiles_list or []:
        c = canonical(s)
        if c:
            out.add(c)
    return out


def canon_first(smiles_list):
    for s in smiles_list or []:
        c = canonical(s)
        if c:
            return c
    return None


def parse_json_block(text: str):
    """Try to extract the first JSON object from the model's output."""
    s = text.find('{')
    if s < 0:
        return None
    # find matching closing brace by depth
    depth = 0
    in_string = False
    escape = False
    for i in range(s, len(text)):
        ch = text[i]
        if escape:
            escape = False
            continue
        if ch == '\\':
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[s:i+1])
                except Exception:
                    return None
    return None


def compare(pred: dict, gold: dict) -> dict:
    m = {}
    # electrodes: id comparison
    for k in ('anode', 'cathode'):
        m[k] = electrode_to_id(pred.get(k, '') or '') == electrode_to_id(gold.get(k, '') or '')
    # cell_type: id comparison
    m['cell_type'] = encode_cell_type(pred.get('cell_type', '')) == encode_cell_type(gold.get('cell_type', ''))
    # SMILES lists: set + first-only protocols
    for k in ('electrolytes', 'solvents', 'reagents', 'catalysts'):
        p_set = canon_set(pred.get(k, []))
        g_set = canon_set(gold.get(k, []))
        m[f'{k}_exact_set'] = p_set == g_set
        m[f'{k}_first'] = canon_first(pred.get(k, [])) == canon_first(gold.get(k, []))
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='/inspire/hdd/global_public/public_models/Qwen/Qwen2.5-3B-Instruct')
    ap.add_argument('--adapter', default=str(PROJECT / 'checkpoints' / 'qwen25_3b_lora_v1' / 'best'))
    ap.add_argument('--test', default=str(PROJECT / 'data_qwen_sft_v3' / 'test.jsonl'))
    ap.add_argument('--out', default=str(PROJECT / 'eval_results' / 'qwen25_3b_lora_v1.json'))
    ap.add_argument('--batch_size', type=int, default=16)
    ap.add_argument('--max_new_tokens', type=int, default=512)
    ap.add_argument('--limit', type=int, default=0, help='limit number of samples for quick test (0=all)')
    args = ap.parse_args()

    print(f"base   : {args.base}")
    print(f"adapter: {args.adapter}")
    print(f"test   : {args.test}")
    print(f"out    : {args.out}")

    tok = AutoTokenizer.from_pretrained(args.base, trust_remote_code=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = 'left'  # for generation

    base = AutoModelForCausalLM.from_pretrained(
        args.base,
        dtype=torch.bfloat16,
        attn_implementation='eager',
    ).to('cuda')
    model = PeftModel.from_pretrained(base, args.adapter)
    model.eval()
    print('Model + adapter loaded', flush=True)

    test = []
    with open(args.test) as f:
        for line in f:
            test.append(json.loads(line))
    if args.limit:
        test = test[:args.limit]
    print(f'test n={len(test)}', flush=True)

    ALL_METRICS = [
        'anode', 'cathode', 'cell_type',
        *(f'{f}_exact_set' for f in ('electrolytes', 'solvents', 'reagents', 'catalysts')),
        *(f'{f}_first' for f in ('electrolytes', 'solvents', 'reagents', 'catalysts')),
    ]
    results = []
    metric_hits = Counter({k: 0 for k in ALL_METRICS})
    n_parse_fail = 0

    for i in range(0, len(test), args.batch_size):
        batch = test[i:i+args.batch_size]
        prompts = [
            tok.apply_chat_template(item['messages'][:-1], tokenize=False, add_generation_prompt=True)
            for item in batch
        ]
        enc = tok(prompts, return_tensors='pt', padding=True, truncation=True, max_length=1024).to(model.device)
        with torch.no_grad():
            out = model.generate(
                **enc,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                num_beams=1,
                temperature=1.0,
                pad_token_id=tok.pad_token_id,
                eos_token_id=tok.eos_token_id,
            )
        gen_only = out[:, enc.input_ids.shape[1]:]
        gen_text = tok.batch_decode(gen_only, skip_special_tokens=True)

        for item, gen in zip(batch, gen_text):
            gold = json.loads(item['messages'][-1]['content'])
            pred = parse_json_block(gen)
            if pred is None:
                n_parse_fail += 1
                m = {k: False for k in (
                    'anode', 'cathode', 'cell_type',
                    *(f'{f}_exact_set' for f in ('electrolytes','solvents','reagents','catalysts')),
                    *(f'{f}_first' for f in ('electrolytes','solvents','reagents','catalysts')),
                )}
            else:
                m = compare(pred, gold)
            for k, v in m.items():
                if v:
                    metric_hits[k] += 1
            results.append({'paper_id': item.get('paper_id'), 'gold': gold, 'pred': pred, 'gen': gen, 'metrics': m})

        done = min(i + args.batch_size, len(test))
        print(f'[{done}/{len(test)}] parse_fail={n_parse_fail}', flush=True)

    n = len(test)
    summary = {k: metric_hits[k] / n for k in metric_hits}
    summary_str = '\n'.join(f'  {k:30s}: {metric_hits[k]:5d} / {n} = {metric_hits[k]/n*100:6.2f}%'
                            for k in sorted(metric_hits))
    print(f'\n=== Eval (n={n}, base={Path(args.base).name}, adapter={Path(args.adapter).parent.name}) ===')
    print(f'JSON parse fail: {n_parse_fail}/{n} = {n_parse_fail/n*100:.2f}%')
    print(summary_str)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump({
            'n': n,
            'json_parse_fail': n_parse_fail,
            'metrics': dict(metric_hits),
            'rate': summary,
            'detail': results,
        }, f, ensure_ascii=False, indent=2)
    print(f'\nwrote {args.out}')


if __name__ == '__main__':
    main()
