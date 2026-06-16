"""LLM ablation: Pure LLM vs +reaction-retrieval vs +reaction+mechanism on test set.

设计:
- 同一 test 集 (data_audited_v3_clean/test.pt), subsample N 条
- 三组 prompt (system 一致, user 末尾追加不同的 retrieval 上下文):
    A. pure        — 只反应 SMILES
    B. +rxn        — A + top-K 相似反应 (train-only, paper 级零泄漏)
    C. +rxn+mech   — B + 机理摘要 (seed paper + matches, 同样过滤)
- 模型: Claude Sonnet 4.6 (anthropic SDK)
- 评测: 复用 eval_qwen_sft.compare() 算 set/first/any/exact 各种命中

Usage:
  ANTHROPIC_API_KEY=xxx python3 scripts/eval_llm_ablation.py [--n 300] [--out_dir eval_results/llm_ablation]
"""
import os, sys, json, time, random, argparse, traceback
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

for _p in (
    '/inspire/hdd/global_user/gelingli-253114010248/python_packages/site_packages_312/dist-packages',
    '/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent',
):
    if _p not in sys.path: sys.path.insert(0, _p)

import torch
import anthropic
try:
    import openai as _openai_sdk
except ImportError:
    _openai_sdk = None

project_root = Path(__file__).parent.parent
# condition_agent root takes priority for models.loader / utils.smiles_utils / rag.*
ca_root = project_root.parent
if str(ca_root) not in sys.path[:2]:
    sys.path.insert(0, str(ca_root))

from rag.retriever import ReactionRetriever
from rag.mechanism_retriever import MechanismRetriever
from models.loader import ModelManager
from utils.smiles_utils import compute_reaction_fingerprint

# eval_qwen_sft + electrode_normalizer use yield_prediction/utils/ namespace,
# which clashes with condition_agent/utils/. Load them via importlib + register
# in sys.modules so internal "from utils.electrode_normalizer" resolves.
import importlib.util as _ilu
def _load_path_module(name: str, path: Path):
    spec = _ilu.spec_from_file_location(name, str(path))
    mod = _ilu.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
_en = _load_path_module(
    'utils.electrode_normalizer',
    project_root / 'utils' / 'electrode_normalizer.py',
)
_eqs = _load_path_module(
    '_eval_qwen_sft_mod',
    project_root / 'scripts' / 'eval_qwen_sft.py',
)
compare = _eqs.compare
parse_json_block = _eqs.parse_json_block
canon_set = _eqs.canon_set
electrode_to_id = _eqs.electrode_to_id
encode_cell_type = _eqs.encode_cell_type


SYSTEM_PROMPT = (
    "You are an expert in electrochemical organic synthesis. Given an alkene electrochemistry "
    "reaction (reactants and product as SMILES), recommend reaction conditions. "
    "CRITICAL OUTPUT FORMAT REQUIREMENT: Your response MUST be ONLY a single JSON object — "
    "no analysis, no markdown, no explanations, no code fences, no prose before or after. "
    "Just the raw JSON object starting with { and ending with }. "
    "The JSON object must contain exactly these keys: anode, cathode, cell_type, electrolytes, "
    "solvents, reagents, catalysts, ligands, additives. anode and cathode are short "
    'electrode-material strings (e.g. "graphite", "platinum", "carbon_felt"); cell_type is '
    '"undivided", "divided", "flow", or "". Each of electrolytes/solvents/reagents/catalysts/'
    "ligands/additives is a list of SMILES strings (empty list if not used). "
    "Output format example (replace values with your recommendation):\n"
    '{"anode":"carbon","cathode":"platinum","cell_type":"undivided","electrolytes":'
    '["CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F"],"solvents":["CC#N"],"reagents":[],'
    '"catalysts":[],"ligands":[],"additives":[]}'
)


def build_user_msg_A(rxn_smiles, reactants, products):
    return (
        f"This is an ALKENE ELECTROCHEMISTRY reaction. Recommend conditions for running it "
        f"as an electrochemical (electrolysis) transformation — NOT as conventional chemistry. "
        f"Reactants: {'.'.join(reactants)}\n"
        f"Products: {'.'.join(products)}\n\n"
        f"OUTPUT FORMAT REQUIREMENT: Respond with a SINGLE raw JSON object using EXACTLY these "
        f"9 keys (no other keys):\n"
        f'{{"anode": "<electrode material as short string, e.g. graphite, carbon_felt, platinum>", '
        f'"cathode": "<same format>", '
        f'"cell_type": "<undivided / divided / flow>", '
        f'"electrolytes": ["<SMILES of supporting electrolyte>", ...], '
        f'"solvents": ["<SMILES>", ...], '
        f'"reagents": ["<SMILES of any added reagents>", ...], '
        f'"catalysts": ["<SMILES of any catalysts>", ...], '
        f'"ligands": ["<SMILES of any ligands>", ...], '
        f'"additives": ["<SMILES of any additives>", ...]}}\n'
        f"\n"
        f"All list values must be SMILES strings of chemicals (or empty list if not used). "
        f"NO analysis, NO markdown, NO prose. Start your response IMMEDIATELY with `{{` and end with `}}`."
    )


def fmt_rxn_match(m):
    """Format one similar-reaction result for prompt."""
    parts = [
        f"  Reaction: {m['reaction_smiles']}",
        f"    similarity: {m.get('similarity', '?'):.3f}  yield: {m.get('yield', '?')}",
        f"    anode: {m.get('anode', '?')}  cathode: {m.get('cathode', '?')}  cell: {m.get('cell_type', '?')}",
        f"    electrolyte: {m.get('electrolyte', '')}",
        f"    solvents: {m.get('solvents', [])}",
        f"    reagent: {m.get('reagent', '')}",
        f"    catalyst: {m.get('catalyst', '')}",
    ]
    return '\n'.join(parts)


def build_user_msg_B(rxn_smiles, reactants, products, rxn_matches):
    base = build_user_msg_A(rxn_smiles, reactants, products)
    if not rxn_matches:
        return base + "\n\n(No similar reactions found in the database.)"
    ctx = '\n'.join(fmt_rxn_match(m) for m in rxn_matches)
    return base + (
        f"\n\nFor reference, here are the top {len(rxn_matches)} most similar reactions "
        f"from the literature database (paper-level filtered to avoid leakage):\n{ctx}"
    )


def fmt_mech_match(m):
    fams = ', '.join(m.get('mechanism_family') or [])
    return (
        f"  DOI: {m.get('doi','')}  (score {m.get('combined_score','?')}, families: [{fams}])\n"
        f"    summary: {m.get('rxn_class_summary','')}\n"
        f"    electron_flow: {(m.get('electron_flow','') or '')[:300]}\n"
        f"    rate_determining_step: {(m.get('rate_determining_step','') or '')[:200]}"
    )


def build_user_msg_C(rxn_smiles, reactants, products, rxn_matches, mech_result):
    base = build_user_msg_B(rxn_smiles, reactants, products, rxn_matches)
    if not mech_result or (not mech_result.get('seed_paper') and not mech_result.get('matches')):
        return base + "\n\n(No mechanism context available for this reaction.)"
    parts = []
    seed = mech_result.get('seed_paper')
    if seed:
        fams = ', '.join(seed.get('mechanism_family') or [])
        parts.append(
            f"Mechanism for THIS reaction's paper:\n"
            f"  summary: {seed.get('rxn_class_summary','')}\n"
            f"  families: [{fams}]\n"
            f"  electron_flow: {(seed.get('electron_flow','') or '')[:400]}"
        )
    matches = mech_result.get('matches') or []
    if matches:
        m_ctx = '\n'.join(fmt_mech_match(m) for m in matches[:3])
        parts.append(f"Mechanistically similar papers (top {len(matches[:3])}):\n{m_ctx}")
    if not parts:
        return base
    return base + "\n\nMECHANISM CONTEXT:\n" + '\n\n'.join(parts)


def fmt_topk(items, k=3):
    if not items: return '(none)'
    return ', '.join(f'{n} ({p*100:.1f}%)' for n, p in items[:k])


def fmt_smi_topk(items, k=3):
    if not items: return '(none)'
    return ', '.join(f'{n} ({p*100:.0f}%)' for n, p in items[:k])


def build_user_msg_D(rxn_smiles, reactants, products, rxn_matches, mech_result, small_pred):
    """D = C + small model predictions (a domain-trained classifier's top-K guesses)."""
    base = build_user_msg_C(rxn_smiles, reactants, products, rxn_matches, mech_result)
    if not small_pred:
        return base + "\n\n(No small-model prediction available.)"
    lines = [
        "SMALL-MODEL HINTS (Hier+Set v3 — a specialized 10M-param classifier",
        "  trained on 24K alkene-electrochemistry reactions, predictions are top-K with confidence):",
        f"  anode material top-3:   {fmt_topk(small_pred.get('anode_material'))}",
        f"  cathode material top-3: {fmt_topk(small_pred.get('cathode_material'))}",
        f"  cell type top-3:        {fmt_topk(small_pred.get('cell_class_v3'))}",
        f"  electrolyte cation:     {fmt_topk(small_pred.get('electrolyte_cation'))}",
        f"  electrolyte anion:      {fmt_topk(small_pred.get('electrolyte_anion'))}",
        f"  catalyst class top-3:   {fmt_topk(small_pred.get('catalyst_class_v3'))}",
        f"  solvent class top-3:    {fmt_topk(small_pred.get('solvent_class_v3'))}",
        f"  solvent SMILES top-3:   {fmt_smi_topk(small_pred.get('solvent_set_top3'))}",
        f"  reagent SMILES top-3:   {fmt_smi_topk(small_pred.get('reagent_set_top3'))}",
        f"  catalyst SMILES top-3:  {fmt_smi_topk(small_pred.get('catalyst_set_top3'))}",
        f"  solvent natural set:    {small_pred.get('solvent_set_natural') or []}",
        f"  reagent natural set:    {small_pred.get('reagent_set_natural') or []}",
        f"  catalyst natural set:   {small_pred.get('catalyst_set_natural') or []}",
    ]
    return base + "\n\n" + "\n".join(lines)


# ── single-reaction worker ────────────────────────────────────

def call_claude(client, model, system, user, max_tokens=4096, retries=2):
    """Backend-agnostic: client is either anthropic.Anthropic or openai.OpenAI."""
    last_err = None
    is_openai = (_openai_sdk is not None) and isinstance(client, _openai_sdk.OpenAI)
    for attempt in range(retries + 1):
        try:
            # Opus 4.7+ rejects temperature param
            is_new_opus = ('opus-4-7' in model or 'opus-4-8' in model or 'opus-4-9' in model)
            extra = {} if is_new_opus else {'temperature': 0.0}
            if is_openai:
                # Force JSON-only output via response_format (works with newer Claude proxies)
                kwargs = dict(model=model, max_tokens=max_tokens,
                              messages=[{"role": "system", "content": system},
                                        {"role": "user", "content": user}],
                              **extra)
                try:
                    r = client.chat.completions.create(
                        **kwargs, response_format={"type": "json_object"})
                except Exception:
                    # Proxy doesn't support response_format → fall back to plain
                    r = client.chat.completions.create(**kwargs)
                return r.choices[0].message.content or ''
            else:
                r = client.messages.create(
                    model=model, max_tokens=max_tokens, system=system,
                    messages=[{"role": "user", "content": user}],
                    **extra,
                )
                return r.content[0].text if r.content else ''
        except Exception as e:
            if 'rate' in str(e).lower() or 'limit' in str(e).lower():
                time.sleep(2 ** attempt + random.random())
            else:
                time.sleep(1 + attempt)
            last_err = e
    raise last_err


def process_one(idx, rec, rxn_retriever, mech_retriever, exclude_pids, exclude_rxns,
                client, model, top_k_rxn=5, small_pred_map=None):
    rs = list(rec['reactant_smiles']); ps = list(rec['product_smiles'])
    rxn_smiles = '.'.join(rs) + '>>' + '.'.join(ps)

    # Build retrieval context (shared between B, C, D)
    fp = compute_reaction_fingerprint(rs, ps, process_one.mol_extractor)
    rxn_matches = rxn_retriever.search(
        fp, top_k=top_k_rxn, threshold=0.0,
        exclude_paper_ids=exclude_pids,
        exclude_reaction_smiles=exclude_rxns,
    )
    mech_result = mech_retriever.search_by_reaction(
        rxn_smiles, top_k=3,
        exclude_paper_ids=exclude_pids,
        exclude_reaction_smiles=exclude_rxns,
    )
    small_pred = (small_pred_map or {}).get(rxn_smiles) if small_pred_map is not None else None

    out = {'idx': idx, 'rxn': rxn_smiles, 'yield_gt': rec.get('yield'),
           'n_rxn_matches': len(rxn_matches),
           'mech_seed_found': bool(mech_result.get('seed_paper')),
           'mech_seed_excluded': bool(mech_result.get('seed_excluded')),
           'mech_n_matches': len(mech_result.get('matches') or []),
           'small_pred_found': small_pred is not None}

    # Build gold dict (mirroring qwen test.jsonl gold)
    gold = build_gold(rec)
    out['gold'] = gold

    # Build group prompts (A/B/C always; D only when small_pred_map provided)
    msgs = {
        'A': build_user_msg_A(rxn_smiles, rs, ps),
        'B': build_user_msg_B(rxn_smiles, rs, ps, rxn_matches),
        'C': build_user_msg_C(rxn_smiles, rs, ps, rxn_matches, mech_result),
    }
    if small_pred_map is not None:
        msgs['D'] = build_user_msg_D(rxn_smiles, rs, ps, rxn_matches, mech_result, small_pred)

    for grp, user in msgs.items():
        out[f'{grp}_user_prompt'] = user  # 保存完整 prompt (审计/复现用)
        try:
            text = call_claude(client, model, SYSTEM_PROMPT, user)
            pred = parse_json_block(text)
            out[f'{grp}_pred_raw'] = text
            out[f'{grp}_pred'] = pred
            out[f'{grp}_metrics'] = compare(pred or {}, gold) if pred else None
        except Exception as e:
            out[f'{grp}_error'] = str(e)
            out[f'{grp}_pred_raw'] = None
            out[f'{grp}_pred'] = None
            out[f'{grp}_metrics'] = None
    return out


def build_gold(rec):
    """从 test.pt 的 vocab labels 重建 gold JSON (镜像 qwen test.jsonl assistant 字段)."""
    # 简化: 直接用记录里的原始字符串字段
    return {
        'anode': rec.get('anode', '') or '',
        'cathode': rec.get('cathode', '') or '',
        'cell_type': rec.get('cell_type', '') or '',
        'electrolytes': rec.get('electrolyte_smiles_list', []) or [],
        'solvents': rec.get('solvent_smiles_list', []) or [],
        'reagents': rec.get('reagent_smiles_list', []) or [],
        'catalysts': rec.get('catalyst_smiles_list', []) or [],
        'ligands': rec.get('ligand_smiles_list', []) or [],
        'additives': rec.get('additive_smiles_list', []) or [],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=300)
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--out_dir', default=str(project_root / 'eval_results' / 'llm_ablation'))
    ap.add_argument('--top_k_rxn', type=int, default=5)
    ap.add_argument('--model', default='claude-sonnet-4-6')
    ap.add_argument('--concurrency', type=int, default=4)
    ap.add_argument('--dedup', action='store_true',
                    help='Collapse duplicate rxn SMILES rows: LLM called once per unique rxn, results broadcast back')
    ap.add_argument('--small_model_json', default=None,
                    help='Path to small-model per-reaction predictions JSON to enable D group')
    ap.add_argument('--groups', default='ABC',
                    help='Which groups to run, e.g. ABC, ABCD, or D')
    ap.add_argument('--limit_save_chars', type=int, default=10000,
                    help='truncate Claude raw responses longer than this; default 10K (almost never triggers)')
    args = ap.parse_args()

    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)

    print('Loading test set + split_meta...')
    data_dir = project_root / 'data_audited_v3_clean'
    test = torch.load(data_dir / 'test.pt', weights_only=False)
    sm = json.load(open(data_dir / 'split_meta.json'))
    exclude_pids = set(sm['test_papers'])
    # 跨 paper 同反应防泄漏: 把所有 test 反应 SMILES 也加入排除集
    exclude_rxns = set()
    for r in test:
        exclude_rxns.add('.'.join(r['reactant_smiles']) + '>>' + '.'.join(r['product_smiles']))
    print(f'  test={len(test)}, exclude_paper_ids={len(exclude_pids)}, '
          f'exclude_reaction_smiles={len(exclude_rxns)}')

    # Need gold strings — rebuild from qwen test.jsonl (already has same ordering)
    qwen_test = []
    with open(data_dir.parent / 'data_qwen_sft_v3' / 'test.jsonl') as f:
        for line in f:
            r = json.loads(line)
            assistant = None
            for m in r['messages']:
                if m['role'] == 'assistant':
                    try: assistant = json.loads(m['content'])
                    except: assistant = None
                    break
            qwen_test.append(assistant or {})
    assert len(qwen_test) == len(test), f'qwen {len(qwen_test)} != test {len(test)}'

    # 把 qwen gold 注入到 test rec (替代 rec.get)
    for i, rec in enumerate(test):
        g = qwen_test[i]
        rec['anode'] = g.get('anode', '')
        rec['cathode'] = g.get('cathode', '')
        rec['cell_type'] = g.get('cell_type', '')
        rec['electrolyte_smiles_list'] = g.get('electrolytes', []) or []
        rec['solvent_smiles_list'] = g.get('solvents', []) or []
        rec['reagent_smiles_list'] = g.get('reagents', []) or []
        rec['catalyst_smiles_list'] = g.get('catalysts', []) or []
        rec['ligand_smiles_list'] = g.get('ligands', []) or []
        rec['additive_smiles_list'] = g.get('additives', []) or []

    # Subsample
    random.seed(args.seed)
    n = min(args.n, len(test))
    idxs = sorted(random.sample(range(len(test)), n))
    print(f'subsample n={n}')

    # Dedup: collapse to unique rxn smiles; LLM called once, results broadcast back
    rxn_to_first_idx = {}  # rxn_smiles -> first idx that has it
    if args.dedup:
        for idx in idxs:
            rxn = '.'.join(test[idx]['reactant_smiles']) + '>>' + '.'.join(test[idx]['product_smiles'])
            rxn_to_first_idx.setdefault(rxn, idx)
        unique_idxs = sorted(set(rxn_to_first_idx.values()))
        print(f'  dedup: {n} rows -> {len(unique_idxs)} unique rxn SMILES '
              f'({len(unique_idxs)/n*100:.1f}%, saved {n-len(unique_idxs)} LLM calls per group)')
        call_idxs = unique_idxs
    else:
        call_idxs = idxs

    print('Loading retrievers + ModelManager...')
    rxn_retr = ReactionRetriever('data/faiss_index_paper.bin', 'data/reaction_db_paper.pkl')
    mech_retr = MechanismRetriever('data/mechanism_kb')
    mm = ModelManager()
    process_one.mol_extractor = mm.mol_extractor

    # Load small-model predictions if D group requested
    small_pred_map = None
    if args.small_model_json:
        print(f'Loading small-model predictions: {args.small_model_json}')
        small_pred_map = json.load(open(args.small_model_json))
        print(f'  {len(small_pred_map)} unique rxn predictions loaded')

    api_key = os.environ.get('ANTHROPIC_API_KEY', '') or os.environ.get('ANTHROPIC_AUTH_TOKEN', '')
    base_url = os.environ.get('ANTHROPIC_BASE_URL') or None
    if not api_key:
        raise RuntimeError('Set ANTHROPIC_API_KEY or ANTHROPIC_AUTH_TOKEN env var')
    # Auto-detect backend: if base_url contains '/openai' path or env var BACKEND=openai, use OpenAI SDK
    backend = os.environ.get('LLM_BACKEND', 'auto').lower()
    if backend == 'auto':
        backend = 'openai' if base_url and '/openai' in base_url else 'anthropic'
    if backend == 'openai':
        if _openai_sdk is None:
            raise RuntimeError('openai SDK required for openai backend')
        client = _openai_sdk.OpenAI(api_key=api_key, base_url=base_url)
        print(f'  using OpenAI-compat backend: {base_url}')
    else:
        client = anthropic.Anthropic(api_key=api_key, base_url=base_url)
        print(f'  using Anthropic backend: {base_url}')

    n_calls = len(call_idxs)
    groups_str = args.groups.upper()
    n_groups = len(groups_str)
    print(f'Calling Claude ({args.model}) on {n_calls} reactions × {n_groups} groups [{groups_str}] = {n_calls*n_groups} calls, '
          f'concurrency={args.concurrency} (dedup={args.dedup}, small_model={"yes" if small_pred_map else "no"})...')
    call_results = {}  # idx -> result dict
    done = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {
            ex.submit(process_one, idx, test[idx], rxn_retr, mech_retr,
                      exclude_pids, exclude_rxns, client, args.model, args.top_k_rxn,
                      small_pred_map): idx
            for idx in call_idxs
        }
        for fu in as_completed(futures):
            idx = futures[fu]
            try:
                call_results[idx] = fu.result()
            except Exception as e:
                call_results[idx] = {'idx': idx, 'error': f'{e}\n{traceback.format_exc()[:2000]}'}
            done += 1
            if done % 10 == 0 or done == n_calls:
                rate = done / max(time.time() - t0, 1e-3)
                eta = (n_calls - done) / rate
                print(f'  {done}/{n_calls}  ({rate:.2f} rxn/s, eta {eta/60:.1f} min)', flush=True)

    # Now broadcast: each of the n sampled rows gets a result. For dedup, look up by its rxn_smiles.
    results = [None] * n
    if args.dedup:
        for pos, idx in enumerate(idxs):
            rxn = '.'.join(test[idx]['reactant_smiles']) + '>>' + '.'.join(test[idx]['product_smiles'])
            src_idx = rxn_to_first_idx[rxn]
            src = call_results.get(src_idx)
            if src is None or 'rxn' not in src:
                results[pos] = src  # error case, keep as-is
            else:
                # Copy result but rewrite gold to THIS row's gold (since duplicate rows have
                # different ground-truth conditions even if rxn smiles are same)
                copied = dict(src)
                # gold is recomputed below; replace with this row's gold
                copied['gold'] = build_gold(test[idx])
                copied['idx'] = idx
                # Re-score metrics against this row's gold
                from importlib import import_module  # avoid name shadow
                for grp in args.groups.upper():
                    pred = copied.get(f'{grp}_pred')
                    if pred:
                        copied[f'{grp}_metrics'] = compare(pred, copied['gold'])
                    else:
                        copied[f'{grp}_metrics'] = None
                results[pos] = copied
    else:
        for pos, idx in enumerate(idxs):
            results[pos] = call_results.get(idx)

    # Save raw + aggregate
    raw_path = out_dir / 'raw_results.json'
    # Trim raw_text + user prompts to avoid bloat
    for r in results:
        if r is None: continue
        for grp in args.groups.upper():
            for key in (f'{grp}_pred_raw', f'{grp}_user_prompt'):
                t = r.get(key)
                if isinstance(t, str) and len(t) > args.limit_save_chars:
                    r[key] = t[:args.limit_save_chars] + '…[truncated]'
    raw_path.write_text(json.dumps(results, indent=2, default=str))
    print(f'\n[OK] saved raw (incl. prompts + responses) to {raw_path}')

    # Aggregate
    keys = ['anode', 'cathode', 'cell_type',
            'electrolytes_first', 'electrolytes_exact_set',
            'solvents_first', 'solvents_exact_set',
            'reagents_first', 'reagents_exact_set',
            'catalysts_first', 'catalysts_exact_set']
    grps = list(args.groups.upper())
    sums = {g: {k: 0 for k in keys} for g in grps}
    parse_fail = {g: 0 for g in grps}
    valid = {g: 0 for g in grps}
    # GT-nonempty + exact_set 真本事
    nonempty_total = {f: 0 for f in ('electrolytes','solvents','reagents','catalysts')}
    nonempty_hit = {g: {f: 0 for f in nonempty_total} for g in grps}
    list_fields = list(nonempty_total)

    for r in results:
        if r is None or 'error' in r and not any(r.get(f'{g}_pred') for g in grps): continue
        g_gold = r.get('gold') or {}
        # nonempty totals (only counted once per reaction)
        for f in list_fields:
            if canon_set(g_gold.get(f, []) or []): nonempty_total[f] += 1
        for g in grps:
            mt = r.get(f'{g}_metrics')
            if not mt:
                parse_fail[g] += 1; continue
            valid[g] += 1
            for k in keys:
                if mt.get(k): sums[g][k] += 1
            # nonempty hit
            pred = r.get(f'{g}_pred') or {}
            for f in list_fields:
                g_set = canon_set(g_gold.get(f, []) or [])
                p_set = canon_set(pred.get(f, []) or [])
                if g_set and g_set == p_set:
                    nonempty_hit[g][f] += 1

    n_real = len([r for r in results if r is not None])
    agg = {
        'n_total': n_real,
        'parse_fail': parse_fail,
        'valid': valid,
        'sums': sums,
        'rates': {g: {k: sums[g][k] / max(n_real, 1) for k in keys} for g in grps},
        'nonempty_total': nonempty_total,
        'nonempty_hit': nonempty_hit,
        'nonempty_rate': {g: {f: nonempty_hit[g][f] / max(nonempty_total[f], 1) for f in list_fields} for g in grps},
    }
    agg_path = out_dir / 'aggregate.json'
    agg_path.write_text(json.dumps(agg, indent=2))
    print(f'[OK] aggregate → {agg_path}')

    # Print summary
    print('\n=== Ablation summary ===')
    GRP_LABEL = {'A':'A pure', 'B':'B +rxn', 'C':'C +rxn+mech', 'D':'D +rxn+mech+small'}
    headers = [GRP_LABEL.get(g, g) for g in grps]
    head_str = '  '.join(f'{h:>17s}' for h in headers)
    print(f'{"field":30s}  {head_str}')
    for k in keys:
        cells = '  '.join(f'{agg["rates"][g][k]*100:>16.2f}%' for g in grps)
        print(f'{k:30s}  {cells}')
    print()
    for f in list_fields:
        nt = nonempty_total[f]
        cells = '  '.join(
            f'{nonempty_hit[g][f]:>4d}/{nt}={nonempty_hit[g][f]/max(nt,1)*100:>5.1f}%'
            for g in grps
        )
        print(f'{f+" (GT非空 set✓)":30s}  {cells}')


if __name__ == '__main__':
    main()
