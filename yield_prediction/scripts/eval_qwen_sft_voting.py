"""Evaluate Qwen LoRA with two improvements over eval_qwen_sft.py:

A) Multi-sample voting (self-consistency): generate K samples per query,
   vote on the mode of each field's normalized prediction.

B) Loose electrode evaluation: merges carbon-family electrodes
   (graphite/carbon/carbon_felt/graphite_felt/glassy_carbon/pencil_graphite/bdd)
   into a single class. Other electrodes (Pt/Mg/Zn/Ni/etc) unchanged.

Reports four numbers per field:
  * strict_top1  — single sample, original normalization (= eval_qwen_sft.py baseline)
  * strict_voted — K-sample mode vote, original normalization
  * loose_top1   — single sample, carbon-merged normalization
  * loose_voted  — K-sample mode vote, carbon-merged normalization

Usage:
  python3 scripts/eval_qwen_sft_voting.py --K 5 [other flags same as eval_qwen_sft.py]
"""
import argparse
import json
import sys
from pathlib import Path
from collections import Counter

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

from utils.electrode_normalizer import electrode_to_id, normalize_electrode


# Carbon-family loose grouping
CARBON_FAMILY = {'graphite', 'carbon', 'carbon_felt', 'graphite_felt', 'glassy_carbon', 'pencil_graphite', 'bdd'}


def electrode_id_strict(name):
    return electrode_to_id(name or '')


def electrode_id_loose(name):
    """Merge carbon-family into a single canonical id; keep others identical."""
    norm = normalize_electrode(name or '')
    if norm in CARBON_FAMILY:
        return -1  # sentinel for carbon-family
    return electrode_to_id(name or '')


def encode_cell_type(cell_type):
    if cell_type is None or str(cell_type).strip() == '':
        return 5
    ct = str(cell_type).lower().strip().strip('"\'()')
    if any(k in ct for k in ('undivi', 'undvi', 'udivi', 'unndiv', 'undiv')): return 0
    if any(k in ct for k in ('beaker', 'electrasyn', 'three-neck', 'bottle', 'flask', 'schlenk')): return 0
    if any(k in ct for k in ('h-cell', 'h-type', 'h cell', 'diaphragm', 'two-compartment', 'compartment')): return 1
    if 'divided' in ct or 'devided' in ct or 'separation' in ct or 'ex-cell' in ct: return 1
    if 'flow' in ct or 'vapourtec' in ct: return 2
    if 'sealed' in ct: return 3
    if 'electrochem' in ct or 'electrolysis' in ct or 'electrolytic' in ct or 'reactor' in ct: return 4
    return 5


_RDKIT_SILENCED = False
def _silence_rdkit():
    global _RDKIT_SILENCED
    if _RDKIT_SILENCED: return
    try:
        from rdkit import RDLogger
        RDLogger.DisableLog('rdApp.*')
        _RDKIT_SILENCED = True
    except Exception:
        pass


def canonical(smi):
    _silence_rdkit()
    try:
        from rdkit import Chem
        m = Chem.MolFromSmiles(smi)
        return Chem.MolToSmiles(m) if m else None
    except Exception:
        return None


def canon_set(lst):
    out = set()
    for s in lst or []:
        c = canonical(s)
        if c: out.add(c)
    return out


def canon_first(lst):
    for s in lst or []:
        c = canonical(s)
        if c: return c
    return None


def canon_set_key(lst):
    """Sorted tuple of canonical SMILES — hashable for voting."""
    return tuple(sorted(canon_set(lst)))


def parse_json_block(text):
    s = text.find('{')
    if s < 0: return None
    depth = 0
    in_str = False
    esc = False
    for i in range(s, len(text)):
        ch = text[i]
        if esc: esc = False; continue
        if ch == '\\': esc = True; continue
        if ch == '"': in_str = not in_str; continue
        if in_str: continue
        if ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                try: return json.loads(text[s:i+1])
                except Exception: return None
    return None


def vote_mode(values):
    """Mode of hashable values; None values are dropped."""
    vals = [v for v in values if v is not None]
    if not vals: return None
    return Counter(vals).most_common(1)[0][0]


def evaluate_one(preds, gold, electrode_fn):
    """preds: list of K parsed JSON dicts (or None for failures).
    gold: parsed gold JSON dict.
    electrode_fn: electrode_id_strict or electrode_id_loose.
    Returns metrics dict for this query."""
    gold_anode = electrode_fn(gold.get('anode', ''))
    gold_cathode = electrode_fn(gold.get('cathode', ''))
    gold_cell = encode_cell_type(gold.get('cell_type', ''))

    # Collect normalized predictions across K samples
    anodes = [electrode_fn(p.get('anode', '')) if p else None for p in preds]
    cathodes = [electrode_fn(p.get('cathode', '')) if p else None for p in preds]
    cells = [encode_cell_type(p.get('cell_type', '')) if p else None for p in preds]

    m = {}
    # voted top-1 (mode across K)
    m['anode'] = vote_mode(anodes) == gold_anode
    m['cathode'] = vote_mode(cathodes) == gold_cathode
    m['cell_type'] = vote_mode(cells) == gold_cell
    # any-of-K (oracle: at least one sample hits)
    m['anode_anyK'] = any(a == gold_anode for a in anodes if a is not None)
    m['cathode_anyK'] = any(a == gold_cathode for a in cathodes if a is not None)
    m['cell_type_anyK'] = any(a == gold_cell for a in cells if a is not None)

    for field in ('electrolytes', 'solvents', 'reagents', 'catalysts'):
        gold_set = canon_set_key(gold.get(field, []))
        gold_first = canon_first(gold.get(field, []))
        pred_sets = [canon_set_key(p.get(field, []) if p else []) for p in preds]
        pred_firsts = [canon_first(p.get(field, []) if p else []) for p in preds]
        m[f'{field}_exact_set'] = vote_mode(pred_sets) == gold_set
        m[f'{field}_first'] = vote_mode(pred_firsts) == gold_first
        m[f'{field}_exact_set_anyK'] = any(s == gold_set for s in pred_sets)
        m[f'{field}_first_anyK'] = any(f == gold_first for f in pred_firsts)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='/inspire/hdd/global_public/public_models/Qwen/Qwen3-14B')
    ap.add_argument('--adapter', default=str(PROJECT / 'checkpoints' / 'qwen3_14b_lora_v1' / 'best'))
    ap.add_argument('--test', default=str(PROJECT / 'data_qwen_sft_v3' / 'test.jsonl'))
    ap.add_argument('--out', default=str(PROJECT / 'eval_results' / 'qwen3_14b_lora_v1_voted.json'))
    ap.add_argument('--K', type=int, default=5, help='samples per query')
    ap.add_argument('--temperature', type=float, default=0.7)
    ap.add_argument('--top_p', type=float, default=0.9)
    ap.add_argument('--batch_size', type=int, default=4, help='queries per batch (× K = sequences in flight)')
    ap.add_argument('--max_new_tokens', type=int, default=512)
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    print(f"base={args.base}\nadapter={args.adapter}\nK={args.K} T={args.temperature} top_p={args.top_p}")

    tok = AutoTokenizer.from_pretrained(args.base, trust_remote_code=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = 'left'

    base = AutoModelForCausalLM.from_pretrained(
        args.base,
        dtype=torch.bfloat16,
        attn_implementation='sdpa',  # forward-only is safe with sdpa
    ).to('cuda')
    model = PeftModel.from_pretrained(base, args.adapter).eval()
    print('Model + adapter loaded', flush=True)

    test = []
    with open(args.test) as f:
        for line in f:
            test.append(json.loads(line))
    if args.limit:
        test = test[:args.limit]
    print(f'test n={len(test)}', flush=True)

    # Compute and accumulate metrics for both strict & loose
    METRIC_KEYS = [
        'anode', 'cathode', 'cell_type',
        *(f'{f}_exact_set' for f in ('electrolytes','solvents','reagents','catalysts')),
        *(f'{f}_first' for f in ('electrolytes','solvents','reagents','catalysts')),
    ]
    ANYK_KEYS = [k + '_anyK' for k in METRIC_KEYS]

    strict_hits = Counter({k: 0 for k in METRIC_KEYS + ANYK_KEYS})
    loose_hits = Counter({k: 0 for k in METRIC_KEYS + ANYK_KEYS})
    n_parse_fail_all_K = 0
    n_parse_fail_any = 0

    results = []

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
                do_sample=True,
                temperature=args.temperature,
                top_p=args.top_p,
                num_return_sequences=args.K,
                pad_token_id=tok.pad_token_id,
                eos_token_id=tok.eos_token_id,
            )
        # out shape: [batch * K, prompt_len + gen_len]
        gen_only = out[:, enc.input_ids.shape[1]:]
        gen_texts = tok.batch_decode(gen_only, skip_special_tokens=True)
        # gen_texts is flat list of length batch*K, where idx = b*K + k
        for b, item in enumerate(batch):
            gold = json.loads(item['messages'][-1]['content'])
            preds = []
            for k in range(args.K):
                txt = gen_texts[b * args.K + k]
                preds.append(parse_json_block(txt))
            n_none = sum(1 for p in preds if p is None)
            if n_none == args.K: n_parse_fail_all_K += 1
            if n_none > 0: n_parse_fail_any += 1

            m_strict = evaluate_one(preds, gold, electrode_id_strict)
            m_loose = evaluate_one(preds, gold, electrode_id_loose)
            for k in METRIC_KEYS:
                if m_strict[k]: strict_hits[k] += 1
                if m_loose[k]: loose_hits[k] += 1
            for k in ANYK_KEYS:
                if m_strict[k]: strict_hits[k] += 1
                if m_loose[k]: loose_hits[k] += 1

            results.append({
                'paper_id': item.get('paper_id'),
                'gold': gold,
                'preds': preds,
                'strict': m_strict,
                'loose': m_loose,
            })
        done = min(i + args.batch_size, len(test))
        if done % 32 == 0 or done == len(test):
            print(f'[{done}/{len(test)}] parse_fail_all_K={n_parse_fail_all_K} parse_fail_any={n_parse_fail_any}', flush=True)

    n = len(test)

    def fmt(hits, header):
        out = f'\n=== {header} (n={n}) ===\n'
        out += f'{"metric":35s}  voted   any-of-K\n'
        for k in METRIC_KEYS:
            voted = hits[k] / n * 100
            anyk = hits[k + '_anyK'] / n * 100
            out += f'  {k:33s}  {voted:6.2f}%  {anyk:6.2f}%\n'
        return out

    print(fmt(strict_hits, 'STRICT (original electrode_to_id)'))
    print(fmt(loose_hits, 'LOOSE  (carbon-family merged)'))
    print(f'JSON parse: all_K_fail={n_parse_fail_all_K}/{n}, any_fail={n_parse_fail_any}/{n}')

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump({
            'n': n, 'K': args.K, 'temperature': args.temperature, 'top_p': args.top_p,
            'parse_fail_all_K': n_parse_fail_all_K,
            'parse_fail_any': n_parse_fail_any,
            'strict': {k: strict_hits[k] for k in METRIC_KEYS + ANYK_KEYS},
            'loose':  {k: loose_hits[k] for k in METRIC_KEYS + ANYK_KEYS},
            'strict_rate': {k: strict_hits[k]/n for k in METRIC_KEYS + ANYK_KEYS},
            'loose_rate':  {k: loose_hits[k]/n for k in METRIC_KEYS + ANYK_KEYS},
            'detail': results,
        }, f, ensure_ascii=False, indent=2)
    print(f'\nwrote {args.out}')


if __name__ == '__main__':
    main()
