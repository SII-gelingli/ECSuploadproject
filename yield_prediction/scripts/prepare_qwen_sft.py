"""
Generate ChatML SFT dataset for Qwen condition-recommendation fine-tuning.

- Re-reads raw v2 JSONs under reactions_by_journal_alkene_ec_audited/
- Reuses the existing paper-level split (data_audited/split_meta.json):
  test = papers with year >= 2025, val = held-out subset of rest, train = remainder.
- Emits one JSONL per split with {"messages": [system, user, assistant]} entries.
- Target conditions: anode / cathode / cell_type / electrolyte / solvents / reagents / catalysts.
- A reaction is kept iff it has both reactant and product SMILES AND at least one
  non-empty condition field (we are predicting conditions, so empty targets are useless).
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction")
AUDITED_ROOT = Path("/inspire/hdd/global_user/gelingli-253114010248/WDproject2/reactions_by_journal_alkene_ec_audited")
SPLIT_META = PROJECT / "data_audited" / "split_meta.json"
OUT_DIR = PROJECT / "data_qwen_sft"


SYSTEM_PROMPT = (
    "You are an expert in electrochemical organic synthesis. "
    "Given an alkene electrochemistry reaction (reactants and product as SMILES), "
    "recommend reaction conditions. "
    "Respond with a single JSON object containing the keys: "
    "anode, cathode, cell_type, electrolytes, solvents, reagents, catalysts. "
    "Each of electrolytes/solvents/reagents/catalysts is a list of SMILES strings "
    "(empty list if not used). anode and cathode are short electrode-material strings "
    "(e.g. \"Pt\", \"graphite\", \"Mg\", \"Ni foam\"); cell_type is a short descriptor "
    "(e.g. \"undivided\", \"divided\", \"flow\"). Use \"\" for unknown string fields. "
    "Do not include any text outside the JSON object."
)


def paper_id(doi: str, fp_name: str) -> str:
    """Match prepare_data_audited.paper_id() exactly so we hit the existing split."""
    if doi:
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_supplementary.*|_si1|si_1)$', '', doi.lower())
        pid = re.sub(r'(_si_?\d*|_sup_?\d*|_supl_?\d*|_si1|si_1)', '', pid)
        return pid
    base = re.sub(r'\.json$', '', fp_name)
    base = re.sub(r'_p\d+_t\d+.*$', '', base)
    base = re.sub(r'(_sup_?\d*|_si_?\d*|_supl_?\d*|_si1|si_1)', '', base)
    return base.lower()


def smiles_list(items):
    out = []
    seen = set()
    for it in items or []:
        if not isinstance(it, dict):
            continue
        s = (it.get('smiles') or '').strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def build_target(rxn: dict):
    """Return condition target dict, or None if every field is empty."""
    cond = rxn.get('conditions') or {}
    ec = (cond.get('electrochemistry') or {}) if isinstance(cond, dict) else {}

    anode = (ec.get('anode') or '').strip()
    cathode = (ec.get('cathode') or '').strip()
    cell_type = (ec.get('cell_type') or '').strip()

    electrolytes = smiles_list(rxn.get('electrolytes'))
    if not electrolytes:
        # fall back to electrochemistry.electrolyte if it looks like a SMILES
        e_str = (ec.get('electrolyte') or '').strip()
        if e_str and any(c in e_str for c in '[]()=+-'):
            electrolytes = [e_str]
    solvents = smiles_list(rxn.get('solvents'))
    reagents = smiles_list(rxn.get('reagents'))
    catalysts = smiles_list(rxn.get('catalysts'))

    has_any = (
        anode or cathode or cell_type
        or electrolytes or solvents or reagents or catalysts
    )
    if not has_any:
        return None
    return {
        "anode": anode,
        "cathode": cathode,
        "cell_type": cell_type,
        "electrolytes": electrolytes,
        "solvents": solvents,
        "reagents": reagents,
        "catalysts": catalysts,
    }


def build_user_prompt(rxn: dict) -> str | None:
    """Format the user turn: reactants >> products (canonical SMILES kept as-is)."""
    reactants = smiles_list(rxn.get('reactants'))
    products = smiles_list(rxn.get('products'))
    if not reactants or not products:
        return None
    rxn_smiles = (rxn.get('reaction_smiles') or '').strip()
    user = f"Reactants: {'.'.join(reactants)}\nProducts: {'.'.join(products)}"
    if rxn_smiles:
        user += f"\nReaction SMILES: {rxn_smiles}"
    user += "\n\nRecommend reaction conditions."
    return user


def main():
    split_meta = json.loads(SPLIT_META.read_text())
    test_set = set(split_meta['test_papers'])
    val_set = set(split_meta['val_papers'])
    test_year = split_meta['test_year_threshold']
    print(f"Loaded split: test_year>={test_year}, test={len(test_set)} val={len(val_set)} papers")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(AUDITED_ROOT.rglob("*.json"))
    print(f"Scanning {len(files)} raw JSON files...")

    bucket = {"train": [], "val": [], "test": []}
    paper_to_split = {}
    skip = Counter()

    for fp in files:
        try:
            d = json.loads(fp.read_text())
        except Exception:
            skip['load_fail'] += 1
            continue
        src = d.get('source') or {}
        doi = src.get('doi') or ''
        pid = paper_id(doi, fp.name)
        if pid in test_set:
            split = 'test'
        elif pid in val_set:
            split = 'val'
        else:
            split = 'train'
        paper_to_split[pid] = split

        for rxn in d.get('reactions') or []:
            user = build_user_prompt(rxn)
            if user is None:
                skip['missing_smiles'] += 1
                continue
            target = build_target(rxn)
            if target is None:
                skip['no_conditions'] += 1
                continue
            assistant = json.dumps(target, ensure_ascii=False, separators=(',', ':'))
            bucket[split].append({
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": assistant},
                ],
                "paper_id": pid,
            })

    paper_split_count = Counter(paper_to_split.values())
    print("\nPaper-level distribution (after merging duplicate paper_ids):")
    for k in ('train', 'val', 'test'):
        print(f"  {k}: {paper_split_count[k]} papers")
    print("\nReaction counts per split:")
    for k in ('train', 'val', 'test'):
        print(f"  {k}: {len(bucket[k])} reactions")
    print(f"\nSkipped: {dict(skip)}")

    for split, rows in bucket.items():
        out = OUT_DIR / f"{split}.jsonl"
        with out.open('w') as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"wrote {out}  ({len(rows)} lines)")

    stats = {
        "source_root": str(AUDITED_ROOT),
        "split_meta_source": str(SPLIT_META),
        "test_year_threshold": test_year,
        "system_prompt": SYSTEM_PROMPT,
        "paper_split": dict(paper_split_count),
        "reaction_split": {k: len(v) for k, v in bucket.items()},
        "skipped": dict(skip),
    }
    (OUT_DIR / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False))
    print(f"\nwrote {OUT_DIR / 'stats.json'}")


if __name__ == "__main__":
    main()
