#!/usr/bin/env python
"""
Gradio Web UI for the Electrochemical Condition Agent.

Two tabs:
  1. Agent Chat — Full LLM-powered ReAct conversation (needs API key)
  2. Tool Demo — Direct tool calls without API key

Usage:
    pip install gradio>=4.0
    python web_app.py                    # default port 7860
    python web_app.py --port 8080
    python web_app.py --device cuda
    python web_app.py --share            # create public link
"""
import sys
import os
import json
import threading
import queue
import argparse
from pathlib import Path
from typing import Optional

# Project path setup
_this_dir = Path(__file__).parent
sys.path.insert(0, str(_this_dir))

from config import AgentConfig, ELECTRODE_NAMES, CELL_TYPE_NAMES, UNKNOWN_INDICES

# Conversation storage
_CONVERSATIONS_DIR = _this_dir / "data" / "conversations"
_AUTO_SAVE_DIR = _CONVERSATIONS_DIR / "auto"  # 自动保存子目录
_EXPERIMENTS_DIR = _this_dir / "data" / "experiments"  # 表单实验记录

import gradio as gr

# ── Global singletons (thread-safe, lazy-loaded) ─────────────────

_init_lock = threading.Lock()
_model_manager = None
_tool_executor = None
_retriever = None
_mechanism_retriever = None
_device = "cpu"


def _ensure_globals():
    """Lazy-initialize ModelManager, ToolExecutor, ReactionRetriever, MechanismRetriever."""
    global _model_manager, _tool_executor, _retriever, _mechanism_retriever

    if _tool_executor is not None:
        return

    with _init_lock:
        if _tool_executor is not None:
            return

        from models.loader import ModelManager
        from agent.tools import ToolExecutor

        _model_manager = ModelManager(device=_device)

        config = AgentConfig(device=_device)
        try:
            from rag.retriever import ReactionRetriever
            if Path(config.reaction_db_path).exists():
                _retriever = ReactionRetriever(
                    config.faiss_index_path, config.reaction_db_path
                )
        except Exception:
            pass

        try:
            from rag.mechanism_retriever import MechanismRetriever
            from config import MECHANISM_KB_DIR
            if Path(MECHANISM_KB_DIR).exists():
                _mechanism_retriever = MechanismRetriever(MECHANISM_KB_DIR)
        except Exception:
            pass

        _tool_executor = ToolExecutor(_model_manager, _retriever, _mechanism_retriever)


# ── Image rendering helpers ──────────────────────────────────────

def _render_mol_image(smiles_list, legends=None):
    """Render a grid of molecules as inline markdown image."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Draw
        import base64 as b64mod, io

        mols, mol_legends = [], []
        for i, smi in enumerate(smiles_list):
            mol = Chem.MolFromSmiles(smi)
            if mol:
                mols.append(mol)
                mol_legends.append(legends[i] if legends and i < len(legends) else smi)
        if not mols:
            return ""
        img = Draw.MolsToGridImage(mols, molsPerRow=4, subImgSize=(250, 200),
                                   legends=mol_legends)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        b64 = b64mod.b64encode(buf.getvalue()).decode()
        return f"\n\n![Molecules](data:image/png;base64,{b64})"
    except Exception:
        return ""


def _render_rxn_image(reaction_smiles, legend=""):
    """Render a single reaction as inline markdown image."""
    try:
        from rdkit.Chem import AllChem, Draw
        import base64 as b64mod, io

        rxn = AllChem.ReactionFromSmarts(reaction_smiles, useSmiles=True)
        img = Draw.ReactionToImage(rxn, subImgSize=(300, 200))
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        b64 = b64mod.b64encode(buf.getvalue()).decode()
        label = legend or "Reaction"
        return f"\n\n**{label}**\n\n![{label}](data:image/png;base64,{b64})"
    except Exception:
        return ""


def _render_rxn_images(smiles_list, legends=None):
    """Render multiple reactions as inline markdown images."""
    parts = []
    for i, smi in enumerate(smiles_list):
        if not smi:
            continue
        legend = legends[i] if legends and i < len(legends) else f"Reaction {i+1}"
        rendered = _render_rxn_image(smi, legend)
        if rendered:
            parts.append(rendered)
    return "\n".join(parts)


# ── Markdown formatting helpers ──────────────────────────────────

def _fmt_molecular_info(results: list) -> str:
    if not results:
        return "_No results._"
    lines = [
        "| SMILES | Valid | Formula | MW | Atoms | Rings | LogP | TPSA |",
        "|--------|-------|---------|-----|-------|-------|------|------|",
    ]
    for r in results:
        valid = "Yes" if r.get("valid") else "No"
        smiles = r.get("canonical_smiles") or r.get("smiles", "")
        formula = r.get("formula", "")
        mw = r.get("molecular_weight", "")
        if isinstance(mw, float):
            mw = f"{mw:.2f}"
        atoms = r.get("num_atoms", "")
        rings = r.get("num_rings", "")
        logp = r.get("logp", "")
        if isinstance(logp, float):
            logp = f"{logp:.2f}"
        tpsa = r.get("tpsa", "")
        if isinstance(tpsa, float):
            tpsa = f"{tpsa:.1f}"
        lines.append(f"| `{smiles}` | {valid} | {formula} | {mw} | {atoms} | {rings} | {logp} | {tpsa} |")
    return "\n".join(lines)


def _fmt_recommendations(recs: dict, title: str = "Recommendations") -> str:
    if not recs:
        return "_No recommendations._"
    sections = [f"### {title}\n"]
    for cond_type in ["anode", "cathode", "cell_type", "electrolyte",
                      "solvent", "reagent", "catalyst"]:
        items = recs.get(cond_type, [])
        if not items:
            continue
        sections.append(f"**{cond_type.replace('_', ' ').title()}**\n")
        sections.append("| Rank | Label | Confidence |")
        sections.append("|------|-------|------------|")
        for i, item in enumerate(items, 1):
            conf = item.get("confidence", 0)
            sections.append(f"| {i} | `{item.get('label', '?')}` | {conf:.4f} |")
        sections.append("")
    return "\n".join(sections)


def _fmt_yield_predictions(preds: list) -> str:
    if not preds:
        return "_No predictions._"
    lines = [
        "| # | Anode | Cathode | Cell Type | Solvent | Electrolyte | Predicted Yield |",
        "|---|-------|---------|-----------|---------|-------------|-----------------|",
    ]
    for i, p in enumerate(preds, 1):
        c = p.get("conditions", {})
        yld = p.get("predicted_yield", "?")
        lines.append(
            f"| {i} | {c.get('anode', '')} | {c.get('cathode', '')} | "
            f"{c.get('cell_type', '')} | `{c.get('solvent', '')}` | "
            f"`{c.get('electrolyte', '')}` | **{yld}%** |"
        )
    return "\n".join(lines)


def _fmt_similar_reactions(results: list, db_size: int = 0) -> str:
    if not results:
        return "_No similar reactions found above threshold._"
    lines = [f"_Database size: {db_size} reactions_\n"]
    for i, r in enumerate(results, 1):
        sim = r.get("similarity", 0)
        yld = r.get("yield")
        rxn = r.get("reaction_smiles", "")
        cond = r.get("conditions", {})
        lines.append(f"**#{i}** — Similarity: **{sim:.4f}**" +
                      (f", Yield: **{yld}%**" if yld is not None else ""))
        lines.append(f"```\n{rxn}\n```")
        cond_parts = []
        for key in ["anode", "cathode", "cell_type", "electrolyte",
                     "solvents", "reagent", "catalyst"]:
            val = cond.get(key, "")
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val) if val else ""
            if val:
                cond_parts.append(f"**{key}**: {val}")
        if cond_parts:
            lines.append("  " + " | ".join(cond_parts))
        lines.append("")
    return "\n".join(lines)


def _fmt_joint_schemes(schemes: list) -> str:
    if not schemes:
        return "_No joint schemes generated._"
    lines = [
        "| # | Anode | Cathode | Cell Type | Electrolyte | Solvent | Reagent | Catalyst | Joint Prob |",
        "|---|-------|---------|-----------|-------------|---------|---------|----------|------------|",
    ]
    for i, s in enumerate(schemes, 1):
        prob = s.get("joint_probability", 0)
        row = [str(i)]
        for key in ["anode", "cathode", "cell_type", "electrolyte",
                     "solvent", "reagent", "catalyst"]:
            val = s.get(key, {})
            if isinstance(val, dict):
                row.append(val.get("label", "?"))
            else:
                row.append(str(val))
        row.append(f"{prob:.6f}")
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════
#  Tab 1: Agent Chat
# ═══════════════════════════════════════════════════════════════════

def _create_agent_for_session(api_key, base_url, model_name, device, temperature=1.0, backend="openai"):
    """Create a new ElectrochemAgent instance for a Gradio session."""
    _ensure_globals()
    from agent.loop import ElectrochemAgent

    config = AgentConfig(device=device)
    config.backend = backend or "openai"
    if api_key:
        config.api_key = api_key
    if base_url:
        config.base_url = base_url
    if model_name:
        config.model = model_name
    if temperature is not None:
        config.temperature = float(temperature)

    # Only require API key for Anthropic backend; vLLM doesn't need one
    if config.backend == "anthropic" and not config.api_key:
        raise ValueError(
            "API key is required for Anthropic backend. Set ANTHROPIC_API_KEY env var or enter it above."
        )
    return ElectrochemAgent(config, _model_manager, _retriever, _mechanism_retriever)


# ─────────── Tool result visual rendering ────────────────────────

def _bar(conf: float, width: int = 10) -> str:
    """Simple unicode confidence bar (eg ████░░░░░░)."""
    try:
        n = max(0, min(width, int(round(conf * width))))
    except Exception:
        n = 0
    return "█" * n + "░" * (width - n)


def _render_recommend_conditions(result_str: str) -> str:
    """Convert recommend_conditions_default JSON into a chemist-friendly markdown."""
    try:
        d = json.loads(result_str)
    except Exception:
        return f"<details><summary>Result (raw)</summary>\n\n```\n{result_str[:2000]}\n```\n\n</details>"
    if "error" in d:
        return f"**Error from recommender:** {d['error']}"

    out = []
    out.append("### 🧪 推荐反应条件")
    model = d.get('model_type', '?')
    out.append(f"_Model: {model}_\n")

    rec = d.get('recommendations', {})
    # 单类 head (anode/cathode/cell_type/electrolyte) 用表格紧凑显示
    out.append("#### ⚡ 电化学设置 (Top-3)")
    out.append("| Head | Top-1 | Top-2 | Top-3 |")
    out.append("|------|-------|-------|-------|")
    for h, label in [('anode', '阳极 (材料)'), ('anode_fine', '阳极 (细类)'),
                     ('cathode', '阴极 (材料)'), ('cathode_fine', '阴极 (细类)'),
                     ('cell_type', '池型'), ('electrolyte', '电解质')]:
        items = rec.get(h, [])
        if not items: continue  # skip if model doesn't have this head (old ckpt)
        row = [label]
        for item in items[:3]:
            lbl = item.get('label', '?')
            conf = item.get('confidence', 0)
            row.append(f"`{lbl}` ({conf*100:.1f}%)")
        while len(row) < 4:
            row.append("—")
        out.append("| " + " | ".join(row) + " |")
    out.append("")

    # 模型实际预测的多组分混合 (set head 实际输出, 重点突出)
    pred_sets = d.get('predicted_sets', {})
    if pred_sets:
        out.append("#### ⭐ 模型预测的多组分混合 (实际推荐)")
        for h, label in [('solvent', '溶剂'), ('catalyst', '催化剂'), ('reagent', '试剂')]:
            ps = pred_sets.get(h, [])
            if not ps:
                out.append(f"- **{label}**: (无, 模型预测所有 slot = no_obj)")
                continue
            count = len(ps)
            if count == 1:
                p = ps[0]
                out.append(f"- **{label}** (单组分): `{p['smiles']}` &nbsp;({p['confidence']*100:.1f}%)")
            else:
                combo = " + ".join(f"`{p['smiles']}`" for p in ps)
                confs = ", ".join(f"{p['confidence']*100:.1f}%" for p in ps)
                out.append(f"- **{label}** ({count} 组分混合): {combo} &nbsp;_({confs})_")
        out.append("")

    # Set head 备选候选 (Top-K SMILES 单独排序展示)
    out.append("#### 🧪 备选候选 (Top-5 单独 SMILES, 不同于实际多组分预测)")
    for h, label in [('solvent', '溶剂'), ('catalyst', '催化剂'), ('reagent', '试剂')]:
        items = rec.get(h, [])
        if not items:
            continue
        lines = []
        for i, item in enumerate(items[:5], 1):
            smi = item.get('smiles') or item.get('label', '?')
            conf = item.get('confidence', 0)
            lines.append(f"   {i}. `{smi}` &nbsp;{_bar(conf)} {conf*100:.1f}%")
        out.append(f"**{label}**:")
        out.append("<br>".join(lines))
        out.append("")

    # ligand / additive single SMILES
    for h, label in [('ligand', '配体'), ('additive', '添加剂')]:
        items = rec.get(h, [])
        if not items: continue
        top = items[0]
        smi = top.get('label', '?')
        conf = top.get('confidence', 0)
        if smi.upper() == 'ABSENT' or smi == '__ABSENT__':
            out.append(f"**{label}**: ABSENT (无, {conf*100:.1f}%)")
        else:
            out.append(f"**{label}**: `{smi}` ({conf*100:.1f}%)")
    out.append("")

    # Catalyst mech tags
    tags = d.get('catalyst_mech_tags', [])
    if tags:
        out.append("#### 🏷️ 催化机制标签")
        tag_lines = []
        for t in tags:
            name = t.get('tag', '?')
            prob = t.get('probability', 0)
            pos = t.get('predicted_positive', False)
            mark = "✓" if pos else "○"
            tag_lines.append(f"{mark} **{name}** ({prob*100:.1f}%)")
        out.append(" &nbsp; ".join(tag_lines))
        out.append("")

    # Stage-2 amounts
    amts = d.get('amounts', {})
    if amts and 'error' not in amts:
        out.append("#### 🔬 用量预测 (Stage-2)")
        out.append("| 参数 | 推荐值 | 单位 |")
        out.append("|------|-------|------|")
        rows = [
            ('current_mA', '电流', 'mA'),
            ('current_density', '电流密度', 'mA/cm²'),
            ('potential_V', '电位', 'V'),
            ('temperature_C', '温度', '°C'),
            ('time_h', '时间', 'h'),
            ('electrolyte_M', '电解质浓度', 'M'),
            ('catalyst_equiv', '催化剂', 'equiv'),
            ('reagent_equiv', '试剂', 'equiv'),
            ('ligand_equiv', '配体', 'equiv'),
            ('additive_equiv', '添加剂', 'equiv'),
        ]
        for k, label, unit in rows:
            if k in amts:
                out.append(f"| {label} | {amts[k]} | {unit} |")
        out.append("")
    elif amts and 'error' in amts:
        out.append(f"_Stage-2 用量预测失败: {amts['error']}_")

    # v3 hier classes 简洁列出
    v3 = d.get('v3_hier_classes', {})
    if v3:
        out.append("<details><summary>🔍 化学层次类别 (Hier classes)</summary>")
        for hk, label in [('reagent_class', '试剂大类'), ('catalyst_class', '催化剂大类'),
                          ('solvent_class', '溶剂大类'), ('ligand_class', '配体骨架'),
                          ('additive_class', '添加剂类')]:
            items = v3.get(hk, [])
            if not items: continue
            top3 = [f"`{x.get('label','?')}`({x.get('confidence',0)*100:.0f}%)" for x in items[:3]]
            out.append(f"- **{label}**: " + " · ".join(top3))
        out.append("</details>")

    # Optionally include raw JSON in collapsed
    out.append("\n<details><summary>📄 完整 JSON (debug)</summary>\n\n```json\n"
                + json.dumps(d, ensure_ascii=False, indent=2) + "\n```\n\n</details>")

    return "\n".join(out)


def _render_similar_reactions(result_str: str) -> str:
    """Render search_similar_reactions JSON as a readable list."""
    try:
        d = json.loads(result_str)
    except Exception:
        return f"```\n{result_str[:2000]}\n```"
    if "error" in d:
        return f"**Error:** {d['error']}"
    out = []
    out.append(f"### 🔍 相似反应 (检索)")
    out.append(f"_数据库: {d.get('database_size', '?')} 个反应, 找到 {d.get('num_results', 0)} 个相似_\n")
    for i, rxn in enumerate(d.get('similar_reactions', [])[:5], 1):
        sim = rxn.get('similarity', 0)
        y = rxn.get('yield')
        c = rxn.get('conditions', {})
        out.append(f"**#{i}** &nbsp;相似度: `{sim:.3f}`&nbsp;&nbsp; 收率: `{y if y is not None else '?'}%`")
        out.append(f"   `{rxn.get('reaction_smiles','?')[:120]}...`")
        a = c.get('anode', '?'); ca = c.get('cathode', '?'); ct = c.get('cell_type', '?')
        out.append(f"   电极: {a} / {ca} &nbsp; 池: {ct}")
        if c.get('electrolyte'):
            out.append(f"   电解质: `{c['electrolyte'][:60]}`")
        sv = c.get('solvents', []) or []
        if sv:
            out.append(f"   溶剂: " + ", ".join(f"`{s[:40]}`" for s in sv[:3]))
        if c.get('reagent'):
            out.append(f"   试剂: `{c['reagent'][:60]}`")
        if c.get('catalyst'):
            out.append(f"   催化剂: `{c['catalyst'][:60]}`")
        out.append("")
    return "\n".join(out)


def _render_search_mechanism(result_str: str) -> str:
    """Render search_mechanism JSON as a readable markdown card."""
    try:
        d = json.loads(result_str)
    except Exception:
        return f"```\n{result_str[:2000]}\n```"
    if "error" in d:
        return f"**Error:** {d['error']}"

    out = []
    mode = d.get('mode', 'reaction')
    out.append(f"### 🧪 机理检索 (mode={mode})")

    if mode == 'reaction':
        seed = d.get('seed_paper')
        if not seed:
            out.append(d.get('message', '_无机理记录_'))
            return "\n".join(out)
        out.append(f"\n**查询反应所在 paper**: `{seed.get('doi','?')}` / *{seed.get('journal','?')}*")
        if seed.get('rxn_class_summary'):
            out.append(f"\n> {seed['rxn_class_summary']}")
        fams = seed.get('mechanism_family') or []
        if fams:
            out.append(f"\n**机理家族**: " + " · ".join(f"`{f}`" for f in fams))
        if seed.get('electrochemical_role'):
            out.append(f"\n<details><summary>电化学角色 / electron flow</summary>\n\n"
                       f"- **role**: {seed['electrochemical_role'][:600]}\n"
                       f"- **electron flow**: {seed.get('electron_flow','')[:600]}\n\n</details>")
    else:
        qf = d.get('query_families') or []
        out.append(f"\n**查询家族**: " + (" · ".join(f"`{f}`" for f in qf) if qf else "_(空)_"))
        if d.get('free_text'):
            out.append(f"\n**自由文本**: _{d['free_text'][:200]}_")

    matches = d.get('matches', [])
    if not matches:
        out.append("\n_无机理相似 paper_")
        return "\n".join(out)

    out.append(f"\n**机理相似 paper Top-{len(matches)}**:\n")
    for i, m in enumerate(matches, 1):
        out.append(f"**#{i}** &nbsp;score=`{m.get('combined_score',0)}` "
                   f"&nbsp;fam_jac=`{m.get('family_jaccard',0)}` "
                   f"&nbsp;text_cos=`{m.get('text_cosine',0)}`")
        out.append(f"   📄 `{m.get('doi','?')}` / *{m.get('journal','?')}*")
        if m.get('shared_families'):
            out.append(f"   共享家族: " + " · ".join(f"`{f}`" for f in m['shared_families']))
        if m.get('rxn_class_summary'):
            out.append(f"   > {m['rxn_class_summary'][:200]}")
        if m.get('electron_flow'):
            out.append(f"   <details><summary>electron flow / 证据</summary>\n\n"
                       f"   - flow: {m['electron_flow'][:500]}\n"
                       f"   - evidence: {m.get('evidence_types_used') or []} "
                       f"({m.get('evidence_strength','?')})\n\n   </details>")
        out.append("")
    return "\n".join(out)


def _run_agent_chat(agent, user_message, event_queue):
    """Run agent.chat() in a background thread, piping events to a queue."""
    def callback(event_type, data):
        event_queue.put((event_type, data))

    try:
        final = agent.chat(user_message, display_callback=callback)
        event_queue.put(("__done__", final))
    except Exception as e:
        import traceback
        traceback.print_exc()
        event_queue.put(("__error__", f"{type(e).__name__}: {e}"))


def agent_chat_fn(user_message, chat_history, agent_state,
                  api_key, base_url, model_name, device, temperature,
                  backend,
                  debate_enabled, recommender_b_model, judge_model):
    """
    Non-generator: run agent.chat() or debate synchronously, return final result.
    Blocking but avoids Gradio SSR/streaming serialization issues.
    """
    if not user_message or not user_message.strip():
        return chat_history, agent_state, ""

    user_message = user_message.strip()
    chat_history = list(chat_history or [])

    # Initialize agent if needed
    if agent_state is None:
        try:
            agent_state = _create_agent_for_session(
                api_key, base_url, model_name, device, temperature, backend
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            chat_history.append({"role": "user", "content": user_message})
            chat_history.append({"role": "assistant",
                                 "content": f"**Error initializing agent:** {e}"})
            return chat_history, agent_state, ""

        # Inject loaded conversation history so Claude can continue the context
        if chat_history:
            for msg in chat_history:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if role in ("user", "assistant") and content:
                    agent_state.conversation.append({"role": role, "content": content})

    chat_history.append({"role": "user", "content": user_message})

    # ── Debate mode ──────────────────────────────────────────
    if debate_enabled:
        from agent.debate_config import DebateConfig
        from agent.debate_orchestrator import DebateOrchestrator

        debate_config = DebateConfig(
            enabled=True,
            recommender_b_model=recommender_b_model or "gpt-5.4",
            judge_model=judge_model or "gemini-3.1-pro-preview",
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"),
            base_url=base_url or os.environ.get("ANTHROPIC_BASE_URL"),
        )
        orchestrator = DebateOrchestrator(agent_state, debate_config)

        try:
            result = orchestrator.run_debate(user_message)
        except Exception as e:
            chat_history.append({"role": "assistant",
                                 "content": f"**Debate Error:** {type(e).__name__}: {e}"})
            return chat_history, agent_state, ""

        # Build structured debate display
        sections = []
        if result.recommendation_a:
            sections.append(
                f"<details open><summary><b>Proposal A (Claude + Tools)</b></summary>\n\n"
                f"{result.recommendation_a}\n\n</details>"
            )
        if result.recommendation_b:
            sections.append(
                f"<details><summary><b>Proposal B ({recommender_b_model or 'GPT'})</b></summary>\n\n"
                f"{result.recommendation_b}\n\n</details>"
            )
        if result.critique_of_a or result.critique_of_b:
            critique_text = ""
            if result.critique_of_a:
                critique_text += f"**Critique of Proposal A (by B):**\n\n{result.critique_of_a}\n\n"
            if result.critique_of_b:
                critique_text += f"**Critique of Proposal B (by A):**\n\n{result.critique_of_b}\n\n"
            sections.append(
                f"<details><summary><b>Cross-Critique</b></summary>\n\n"
                f"{critique_text}</details>"
            )
        if result.revision_a or result.revision_b:
            revision_text = ""
            if result.revision_a:
                revision_text += f"**Revised Proposal A:**\n\n{result.revision_a}\n\n"
            if result.revision_b:
                revision_text += f"**Revised Proposal B:**\n\n{result.revision_b}\n\n"
            sections.append(
                f"<details><summary><b>Revised Proposals</b></summary>\n\n"
                f"{revision_text}</details>"
            )
        if result.judgment:
            sections.append(
                f"### Final Judgment ({judge_model or 'Gemini'})\n\n"
                f"{result.judgment}"
            )
        elif result.final_answer:
            sections.append(
                f"### Final Answer (fallback)\n\n{result.final_answer}"
            )

        # Show errors if any
        if result.errors:
            error_lines = "\n".join(f"- {e}" for e in result.errors)
            sections.append(
                f"<details><summary><b>Warnings / Errors ({len(result.errors)})</b></summary>\n\n"
                f"{error_lines}\n\n</details>"
            )

        phases_info = f"\n\n_Phases completed: {', '.join(result.phases_completed)}_"
        content = "\n\n---\n\n".join(sections) + phases_info
        chat_history.append({"role": "assistant", "content": content})
        return chat_history, agent_state, ""

    # ── Standard single-model mode ───────────────────────────
    eq = queue.Queue()
    thread = threading.Thread(
        target=_run_agent_chat, args=(agent_state, user_message, eq), daemon=True
    )
    thread.start()

    # Collect all events
    assistant_parts = []
    while True:
        try:
            event_type, data = eq.get(timeout=900)
        except queue.Empty:
            assistant_parts.append("_Agent timed out._")
            break

        if event_type == "__done__":
            assistant_parts.append(data)
            break
        elif event_type == "__error__":
            assistant_parts.append(f"**Error:** {data}")
            break
        elif event_type == "thinking":
            assistant_parts.append(
                f"<details><summary>Thinking...</summary>\n\n{data}\n\n</details>"
            )
        elif event_type == "tool_call":
            name = data.get("name", "?")
            inp = json.dumps(data.get("input", {}), indent=2)
            assistant_parts.append(
                f"**Tool call: `{name}`**\n```json\n{inp}\n```"
            )
        elif event_type == "tool_result":
            name = data.get("name", "?")
            result_str = data.get("result", "")

            if name == "draw_reaction":
                try:
                    parsed = json.loads(result_str)
                    img_parts = []
                    for img_info in parsed.get("images", []):
                        legend = img_info.get("legend", "")
                        b64_uri = img_info.get("image_base64", "")
                        if b64_uri:
                            img_parts.append(f"**{legend}**\n\n![{legend}]({b64_uri})")
                    if img_parts:
                        assistant_parts.append("\n\n".join(img_parts))
                    else:
                        assistant_parts.append(f"_draw_reaction: {parsed.get('message', 'no images')}_")
                except Exception:
                    assistant_parts.append("_draw_reaction result could not be parsed_")
            elif name == "recommend_conditions_default":
                # 友好可视化: 转 markdown 表格 + 折叠 raw JSON
                rendered = _render_recommend_conditions(result_str)
                assistant_parts.append(rendered)
            elif name == "search_similar_reactions":
                rendered = _render_similar_reactions(result_str)
                assistant_parts.append(rendered)
            elif name == "search_mechanism":
                rendered = _render_search_mechanism(result_str)
                assistant_parts.append(rendered)
            else:
                assistant_parts.append(
                    f"<details><summary>Result from {name}</summary>\n\n"
                    f"```\n{result_str}\n```\n\n</details>"
                )
        elif event_type == "response":
            continue

    content = "\n\n".join(p for p in assistant_parts if p)
    chat_history.append({"role": "assistant", "content": content})
    return chat_history, agent_state, ""


def reset_chat_fn():
    return [], None


# ── Report generation ─────────────────────────────────────────

_REPORTS_DIR = _this_dir / "data" / "reports"

def _generate_report(chat_history):
    """Generate an HTML lab report from the latest assistant response."""
    if not chat_history:
        return None

    # Find last user question and assistant answer
    last_user = ""
    last_assistant = ""
    for msg in reversed(chat_history):
        role = msg.get("role", "") if isinstance(msg, dict) else ""
        content = msg.get("content", "") if isinstance(msg, dict) else ""
        # content may be a list (multimodal) — flatten to string
        if isinstance(content, list):
            parts = []
            for part in content:
                if isinstance(part, str):
                    parts.append(part)
                elif isinstance(part, dict):
                    parts.append(part.get("text", str(part)))
                else:
                    parts.append(str(part))
            content = "\n".join(parts)
        if not isinstance(content, str):
            content = str(content)
        if role == "assistant" and not last_assistant:
            last_assistant = content
        elif role == "user" and not last_user:
            last_user = content
        if last_user and last_assistant:
            break

    if not last_assistant:
        return None

    from datetime import datetime
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    file_ts = now.strftime("%Y%m%d_%H%M%S")

    # Convert markdown in assistant content to simple HTML
    import re
    body = last_assistant
    # Bold
    body = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', body)
    # Inline code
    body = re.sub(r'`([^`\n]+?)`', r'<code>\1</code>', body)
    # Code blocks
    body = re.sub(
        r'```(\w*)\n(.*?)```',
        r'<pre><code>\2</code></pre>',
        body,
        flags=re.DOTALL,
    )
    # Headers
    body = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', body, flags=re.MULTILINE)
    body = re.sub(r'^### (.+)$', r'<h3>\1</h3>', body, flags=re.MULTILINE)
    body = re.sub(r'^## (.+)$', r'<h2>\1</h2>', body, flags=re.MULTILINE)
    # Horizontal rule
    body = body.replace('\n---\n', '<hr>')
    # Tables: convert markdown tables to HTML
    def _convert_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2:
            return match.group(0)
        html = '<table>\n<thead><tr>'
        headers = [c.strip() for c in lines[0].strip('|').split('|')]
        for h in headers:
            html += f'<th>{h}</th>'
        html += '</tr></thead>\n<tbody>\n'
        for line in lines[2:]:  # skip separator row
            cells = [c.strip() for c in line.strip('|').split('|')]
            html += '<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>\n'
        html += '</tbody></table>'
        return html
    body = re.sub(r'(?:^\|.+\|$\n?){2,}', _convert_table, body, flags=re.MULTILINE)
    # Images (inline base64)
    body = re.sub(
        r'!\[([^\]]*)\]\((data:image/[^)]+)\)',
        r'<figure><img src="\2" alt="\1" style="max-width:100%;border-radius:6px;"><figcaption>\1</figcaption></figure>',
        body,
    )
    # <details> blocks pass through as-is
    # Line breaks
    body = re.sub(r'\n\n+', '</p><p>', body)
    body = f'<p>{body}</p>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Electrochemical Experiment Report</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1f2937; background: #fff; line-height: 1.7;
    max-width: 900px; margin: 0 auto; padding: 2rem;
  }}
  .report-header {{
    border-bottom: 3px solid #2563eb;
    padding-bottom: 1.5rem; margin-bottom: 2rem;
  }}
  .report-header h1 {{
    font-size: 1.6rem; font-weight: 700; color: #111827;
    margin-bottom: 0.3rem;
  }}
  .report-header .meta {{
    color: #6b7280; font-size: 0.85rem;
  }}
  .report-header .meta span {{
    display: inline-block; margin-right: 1.5rem;
  }}
  .query-box {{
    background: #f0f5ff; border-left: 4px solid #2563eb;
    padding: 1rem 1.2rem; border-radius: 0 8px 8px 0;
    margin-bottom: 2rem; font-size: 0.95rem; color: #1e40af;
  }}
  .query-box .label {{ font-weight: 600; margin-bottom: 0.3rem; }}
  .content h2 {{ font-size: 1.25rem; color: #111827; margin: 1.5rem 0 0.8rem; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.4rem; }}
  .content h3 {{ font-size: 1.1rem; color: #1f2937; margin: 1.2rem 0 0.6rem; }}
  .content h4 {{ font-size: 1rem; color: #374151; margin: 1rem 0 0.5rem; }}
  .content p {{ margin-bottom: 0.8rem; }}
  .content strong {{ color: #111827; }}
  .content code {{
    background: #f3f4f6; padding: 0.15rem 0.4rem;
    border-radius: 4px; font-size: 0.88em; color: #dc2626;
  }}
  .content pre {{
    background: #f8fafc; border: 1px solid #e5e7eb;
    border-radius: 8px; padding: 1rem; overflow-x: auto;
    margin: 0.8rem 0;
  }}
  .content pre code {{
    background: none; padding: 0; color: #1f2937; font-size: 0.85rem;
  }}
  .content table {{
    width: 100%; border-collapse: collapse; margin: 0.8rem 0;
    font-size: 0.88rem;
  }}
  .content th {{
    background: #f0f5ff; color: #1e40af; font-weight: 600;
    text-align: left; padding: 0.6rem 0.8rem;
    border-bottom: 2px solid #2563eb;
  }}
  .content td {{
    padding: 0.5rem 0.8rem; border-bottom: 1px solid #e5e7eb;
  }}
  .content tr:hover td {{ background: #f9fafb; }}
  .content hr {{
    border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0;
  }}
  .content figure {{
    text-align: center; margin: 1rem 0;
  }}
  .content figcaption {{
    font-size: 0.82rem; color: #6b7280; margin-top: 0.3rem;
  }}
  .content details {{
    border: 1px solid #e5e7eb; border-radius: 8px;
    padding: 0.8rem 1rem; margin: 0.8rem 0;
  }}
  .content summary {{
    cursor: pointer; font-weight: 600; color: #2563eb;
  }}
  .footer {{
    margin-top: 3rem; padding-top: 1rem;
    border-top: 1px solid #e5e7eb;
    text-align: center; color: #9ca3af; font-size: 0.78rem;
  }}
  @media print {{
    body {{ padding: 1cm; max-width: 100%; }}
    .report-header {{ border-bottom-color: #000; }}
    .query-box {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="report-header">
  <h1>Electrochemical Experiment Report</h1>
  <div class="meta">
    <span>Generated: {timestamp}</span>
    <span>Source: Electrochemical Condition Agent</span>
  </div>
</div>

<div class="query-box">
  <div class="label">Research Query</div>
  <div>{last_user}</div>
</div>

<div class="content">
{body}
</div>

<div class="footer">
  Generated by Electrochemical Condition Agent &mdash; AI-driven reaction condition optimization
</div>
</body>
</html>"""

    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = _REPORTS_DIR / f"report_{file_ts}.html"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return str(filepath)


# ── Conversation save/load ────────────────────────────────────

def _auto_save_path(session_id: str) -> Path:
    """Path to auto-saved conversation for a session."""
    _AUTO_SAVE_DIR.mkdir(parents=True, exist_ok=True)
    safe_id = "".join(c for c in (session_id or "anon") if c.isalnum() or c in "-_")[:48] or "anon"
    return _AUTO_SAVE_DIR / f"{safe_id}.json"


def _auto_save_conversation(chat_history, session_id):
    """Auto-save the current chat to data/conversations/auto/{session_id}.json.
    Called automatically after each agent reply via .then() chaining."""
    if not chat_history or not session_id:
        return
    try:
        from datetime import datetime
        path = _auto_save_path(session_id)
        # Read existing name if available, else generate
        existing_name = None
        if path.exists():
            try:
                existing_name = json.load(open(path)).get('name')
            except Exception:
                pass
        if not existing_name:
            first_user_msg = next((m.get('content') for m in chat_history if m.get('role') == 'user'), '')
            # content 可能是 str 或 list (multimodal/tuple format)
            if isinstance(first_user_msg, (list, tuple)):
                first_user_msg = ' '.join(str(x) for x in first_user_msg if isinstance(x, str))
            elif not isinstance(first_user_msg, str):
                first_user_msg = str(first_user_msg or '')
            preview = first_user_msg[:30].replace('\n', ' ').strip() or 'Untitled'
            existing_name = f"[auto] {preview}"
        data = {
            'name': existing_name,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'auto_saved': True,
            'session_id': session_id,
            'messages': chat_history,
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'[auto-save] failed: {e}')


def _restore_session_on_load(request: 'gr.Request'):
    """On page load, try to restore previous session for this browser tab."""
    if request is None:
        return [], None, ""
    sid = getattr(request, 'session_hash', None)
    if not sid:
        return [], None, ""
    path = _auto_save_path(sid)
    if not path.exists():
        return [], None, sid
    try:
        data = json.load(open(path, encoding='utf-8'))
        msgs = data.get('messages', [])
        return msgs, None, sid
    except Exception:
        return [], None, sid


def _list_conversations():
    """List saved conversations as [(display_name, file_path), ...], newest first.
    Includes both manual saves (top-level .json) and auto-saved sessions (auto/ subdir)."""
    _CONVERSATIONS_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(_CONVERSATIONS_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
    # 也列出 auto/ 下的
    if _AUTO_SAVE_DIR.exists():
        files += sorted(_AUTO_SAVE_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
    choices = []
    for f in files:
        try:
            with open(f) as fh:
                data = json.load(fh)
            name = data.get("name", f.stem)
            created = data.get("created_at", "")
            n_msgs = len(data.get("messages", []))
            label = f"{name}  ({created}, {n_msgs} msgs)"
            choices.append((label, str(f)))
        except Exception:
            continue
    return choices


def _save_conversation_fn(chat_history, conv_name):
    """Save current conversation to a JSON file."""
    if not chat_history:
        return gr.update(), "No conversation to save."
    name = (conv_name or "").strip()
    if not name:
        from datetime import datetime
        name = f"Conversation {datetime.now().strftime('%m-%d %H:%M')}"
    _CONVERSATIONS_DIR.mkdir(parents=True, exist_ok=True)
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() or c in "-_ " else "" for c in name).strip().replace(" ", "_")
    filename = f"{timestamp}_{safe_name}.json"
    filepath = _CONVERSATIONS_DIR / filename
    data = {
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": chat_history,
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    choices = _list_conversations()
    return gr.update(choices=choices, value=str(filepath)), f"Saved: **{name}**"


def _load_conversation_fn(conv_path):
    """Load a saved conversation from JSON."""
    if not conv_path:
        return gr.update(), None, "No conversation selected."
    try:
        with open(conv_path, encoding="utf-8") as f:
            data = json.load(f)
        messages = data.get("messages", [])
        name = data.get("name", "")
        return messages, None, f"Loaded: **{name}** ({len(messages)} messages)"
    except Exception as e:
        return gr.update(), gr.update(), f"Load error: {e}"


def _delete_conversation_fn(conv_path):
    """Delete a saved conversation."""
    if not conv_path:
        return gr.update(), "No conversation selected."
    try:
        p = Path(conv_path)
        name = p.stem
        try:
            with open(p) as f:
                name = json.load(f).get("name", name)
        except Exception:
            pass
        p.unlink()
        choices = _list_conversations()
        return gr.update(choices=choices, value=None), f"Deleted: **{name}**"
    except Exception as e:
        return gr.update(), f"Delete error: {e}"


# ═══════════════════════════════════════════════════════════════════
#  Experiment Form Storage + BO/LLM optimization helpers
# ═══════════════════════════════════════════════════════════════════

def _experiments_path(session_id: str) -> Path:
    """Path to experiment log for a session."""
    _EXPERIMENTS_DIR.mkdir(parents=True, exist_ok=True)
    safe = "".join(c for c in (session_id or "anon") if c.isalnum() or c in "-_")[:48] or "anon"
    return _EXPERIMENTS_DIR / f"{safe}.json"


def _load_experiments(session_id: str) -> list:
    """Load experiment log for session, returns list of records."""
    p = _experiments_path(session_id)
    if not p.exists():
        return []
    try:
        return json.load(open(p, encoding='utf-8')).get('experiments', [])
    except Exception:
        return []


def _save_experiments(session_id: str, exps: list):
    """Persist experiment log."""
    p = _experiments_path(session_id)
    from datetime import datetime
    data = {'session_id': session_id,
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'n': len(exps),
            'experiments': exps}
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _add_experiment(session_id: str, record: dict) -> list:
    """Append a new experiment record, return updated list."""
    from datetime import datetime
    exps = _load_experiments(session_id)
    record = dict(record)
    record.setdefault('id', len(exps) + 1)
    record.setdefault('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    exps.append(record)
    _save_experiments(session_id, exps)
    return exps


def _experiments_to_csv(session_id: str) -> Optional[str]:
    """Export experiments to CSV file, return path or None if empty."""
    exps = _load_experiments(session_id)
    if not exps:
        return None
    import csv, tempfile
    # Flatten records
    keys = ['id', 'timestamp', 'reaction_smiles', 'anode', 'cathode', 'cell_type',
            'electrolyte', 'solvents', 'reagents', 'catalyst', 'ligand', 'additive',
            'current_mA', 'potential_V', 'temperature_C', 'time_h',
            'electrolyte_M', 'catalyst_equiv', 'reagent_equiv',
            'observed_yield', 'selectivity', 'notes']
    out_path = Path(tempfile.gettempdir()) / f"experiments_{session_id[:12]}.csv"
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore')
        w.writeheader()
        for e in exps:
            row = {k: e.get(k, '') for k in keys}
            # list 字段拼接
            for lk in ['solvents', 'reagents']:
                if isinstance(row[lk], list):
                    row[lk] = ' + '.join(map(str, row[lk]))
            w.writerow(row)
    return str(out_path)


def _format_experiments_table(exps: list) -> str:
    """Render experiment list as markdown table."""
    if not exps:
        return "_(暂无实验记录, 提交后会出现在这里)_"
    rows = ["| # | 时间 | 阳极 | 阴极 | 溶剂 | 催化剂 | 电流 mA | 温度 °C | yield % |",
            "|---|------|------|------|------|------|---------|---------|---------|"]
    for e in exps[-20:][::-1]:  # show recent 20
        rxn_short = (e.get('reaction_smiles') or '')[:24] + '…'
        solvs = e.get('solvents', [])
        if isinstance(solvs, list): solvs = ' + '.join(solvs[:2])
        cat = (e.get('catalyst') or '')[:18]
        rows.append(f"| {e.get('id','?')} | {e.get('timestamp','?')[-8:]} | "
                    f"{e.get('anode','?')} | {e.get('cathode','?')} | "
                    f"`{(solvs or '?')[:18]}` | `{cat or '?'}` | "
                    f"{e.get('current_mA','?')} | {e.get('temperature_C','?')} | "
                    f"**{e.get('observed_yield','?')}** |")
    return "\n".join(rows)


def _bo_suggest_next(session_id: str, reaction_smiles: str, n_suggest: int = 3) -> str:
    """Run BO optimizer with experiment history to suggest next conditions."""
    exps = _load_experiments(session_id)
    if not exps:
        return "_(没有实验记录, 先 submit 一次再做 BO 推荐)_"
    _ensure_globals()
    try:
        # 用 optimize_conditions_bo tool 接口
        # 把所有历史 observe 注入
        for e in exps:
            if e.get('observed_yield') is None: continue
            conds = {k: e.get(k) for k in ['anode', 'cathode', 'cell_type', 'electrolyte',
                                              'solvent', 'reagent', 'catalyst']}
            _tool_executor.execute('optimize_conditions_bo', {
                'reaction_smiles': reaction_smiles,
                'mode': 'observe',
                'observed_conditions': conds,
                'observed_yield': float(e.get('observed_yield', 0.0)),
            })
        # 让 BO 推下一轮
        r = _tool_executor.execute('optimize_conditions_bo', {
            'reaction_smiles': reaction_smiles,
            'mode': 'suggest',
            'n_suggestions': n_suggest,
            'acq_func': 'ei',
        })
        d = json.loads(r)
        if 'error' in d:
            return f"**BO 失败:** {d['error']}"
        lines = [f"### 🎯 BO 推荐下一轮 (基于 {d.get('n_observations', '?')} 个历史观测)"]
        for i, s in enumerate(d.get('suggestions', []), 1):
            c = s.get('conditions', {})
            yld = s.get('predicted_yield', 0)
            unc = s.get('uncertainty', 0)
            lines.append(f"**#{i}** 预测 yield = `{yld:.1f} ± {unc:.1f}%`")
            for k, v in c.items():
                if v: lines.append(f"   - {k}: `{v}`")
            lines.append("")
        return "\n".join(lines)
    except Exception as e:
        return f"**BO 失败:** {type(e).__name__}: {e}"


def _llm_suggest_next(session_id: str, reaction_smiles: str,
                       api_key: str, base_url: str, model_name: str) -> str:
    """Ask LLM to suggest next conditions based on history."""
    exps = _load_experiments(session_id)
    if not exps:
        return "_(没有实验记录, 先 submit 一次再做 LLM 推荐)_"
    if not api_key:
        return "**LLM 失败:** 缺 API key, 在 Chat tab 的 API Settings 配置"
    try:
        from openai import OpenAI
        bu = base_url or ""
        if bu and not bu.rstrip('/').endswith('/v1'):
            bu = bu.rstrip('/') + '/v1'
        client = OpenAI(api_key=api_key, base_url=bu or None)

        # 构造历史摘要
        history_str = []
        for e in exps:
            history_str.append(
                f"- conditions: anode={e.get('anode')}, cathode={e.get('cathode')}, "
                f"cell={e.get('cell_type')}, electrolyte={e.get('electrolyte')}, "
                f"solvents={e.get('solvents')}, reagent={e.get('reagent')}, "
                f"catalyst={e.get('catalyst')}, "
                f"current={e.get('current_mA')}mA, T={e.get('temperature_C')}°C, "
                f"t={e.get('time_h')}h "
                f"→ yield = {e.get('observed_yield')}% "
                f"(notes: {e.get('notes', '')[:80]})"
            )

        prompt = (
            "You are an electrochemistry expert. The user is iteratively optimizing "
            f"conditions for this reaction:\n\n  {reaction_smiles}\n\n"
            "Past experimental observations:\n" + "\n".join(history_str) +
            "\n\nBased on these results, suggest **3 next conditions** to try. "
            "Each suggestion should change ONE or FEW variables vs the best-yielding observation. "
            "Reasoning should be brief and chemistry-informed. Output as a markdown list."
        )
        resp = client.chat.completions.create(
            model=model_name or 'claude-opus-4-6',
            max_tokens=1500,
            temperature=0.7,
            messages=[{'role': 'user', 'content': prompt}],
        )
        return f"### 🤖 LLM 推荐下一轮\n\n{resp.choices[0].message.content}"
    except Exception as e:
        return f"**LLM 失败:** {type(e).__name__}: {e}"


# ═══════════════════════════════════════════════════════════════════
#  Tab 2: Tool Demo
# ═══════════════════════════════════════════════════════════════════

def tool_validate_smiles(smiles_text):
    _ensure_globals()
    smiles_list = [s.strip() for s in smiles_text.split(",") if s.strip()]
    if not smiles_list:
        return "Please enter at least one SMILES string."
    result = json.loads(_tool_executor.execute("validate_smiles", {
        "smiles_list": smiles_list,
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    md = _fmt_molecular_info(result.get("results", []))
    valid_smiles = [r.get("canonical_smiles") or r.get("smiles", "")
                    for r in result.get("results", []) if r.get("valid")]
    if valid_smiles:
        md += _render_mol_image(valid_smiles)
    return md


def tool_parse_reaction(reaction_smiles):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    result = json.loads(_tool_executor.execute("parse_reaction", {
        "reaction_smiles": reaction_smiles.strip(),
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    rxn_smi = result.get('reaction_smiles', reaction_smiles.strip())
    md = f"**Reaction:** `{rxn_smi}`\n\n"
    md += _render_rxn_image(rxn_smi, "Reaction Structure")
    md += f"\n\n**Reactants ({result.get('num_reactants', 0)}):**\n\n"
    md += _fmt_molecular_info(result.get("reactants", []))
    r_smiles = [r.get("canonical_smiles") or r.get("smiles", "")
                for r in result.get("reactants", []) if r.get("valid")]
    if r_smiles:
        md += _render_mol_image(r_smiles)
    md += f"\n\n**Products ({result.get('num_products', 0)}):**\n\n"
    md += _fmt_molecular_info(result.get("products", []))
    p_smiles = [r.get("canonical_smiles") or r.get("smiles", "")
                for r in result.get("products", []) if r.get("valid")]
    if p_smiles:
        md += _render_mol_image(p_smiles)
    return md


def tool_recommend_conditions(reaction_smiles, top_k):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    result = json.loads(_tool_executor.execute("recommend_conditions_default", {
        "reaction_smiles": reaction_smiles.strip(),
        "top_k": int(top_k),
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    md = _render_rxn_image(reaction_smiles.strip(), "Reaction Structure")
    md += f"\n\n**Model:** {result.get('model_type', '?')}\n\n"
    md += _fmt_recommendations(result.get("recommendations", {}),
                                title="Top-k Condition Recommendations")
    return md


def tool_generate_cvae(reaction_smiles, num_samples, temperature, top_k):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    result = json.loads(_tool_executor.execute("generate_conditions_cvae", {
        "reaction_smiles": reaction_smiles.strip(),
        "num_samples": int(num_samples),
        "temperature": float(temperature),
        "top_k": int(top_k),
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    md = _render_rxn_image(reaction_smiles.strip(), "Reaction Structure")
    md += f"\n\n**Model:** {result.get('model_type', '?')} | "
    md += f"Samples: {result.get('num_samples', '?')} | "
    md += f"Temperature: {result.get('temperature', '?')} | "
    md += f"Unique schemes: {result.get('num_unique_schemes', 0)}\n\n"
    md += _fmt_recommendations(result.get("topk_recommendations", {}),
                                title="Per-Condition Top-k (z=0, deterministic)")
    md += "\n### Joint Condition Schemes (diverse sampling)\n\n"
    md += _fmt_joint_schemes(result.get("joint_schemes", []))
    return md


def tool_predict_yield(reaction_smiles, solvent_smiles, electrolyte_smiles,
                       anode_idx, cathode_idx, cell_type_idx):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    result = json.loads(_tool_executor.execute("predict_yield", {
        "reaction_smiles": reaction_smiles.strip(),
        "conditions": [{
            "solvent_smiles": solvent_smiles.strip() if solvent_smiles else "",
            "electrolyte_smiles": electrolyte_smiles.strip() if electrolyte_smiles else "",
            "anode_index": int(anode_idx),
            "cathode_index": int(cathode_idx),
            "cell_type_index": int(cell_type_idx),
        }],
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    md = _render_rxn_image(reaction_smiles.strip(), "Reaction Structure")
    md += "\n\n" + _fmt_yield_predictions(result.get("yield_predictions", []))
    return md


def tool_search_similar(reaction_smiles, top_k, threshold):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    result = json.loads(_tool_executor.execute("search_similar_reactions", {
        "reaction_smiles": reaction_smiles.strip(),
        "top_k": int(top_k),
        "threshold": float(threshold),
    }))
    if "error" in result:
        return f"**Error:** {result['error']}"
    md = _render_rxn_image(reaction_smiles.strip(), "Query Reaction")
    md += "\n\n" + _fmt_similar_reactions(
        result.get("similar_reactions", []),
        db_size=result.get("database_size", 0),
    )
    # Draw all similar reactions
    similar = result.get("similar_reactions", [])
    if similar:
        rxn_smiles = [r.get("reaction_smiles", "") for r in similar]
        rxn_legends = [
            f"Similar #{i+1} (sim: {r.get('similarity', 0):.3f}"
            + (f", yield: {r.get('yield')}%" if r.get('yield') is not None else "")
            + ")"
            for i, r in enumerate(similar)
        ]
        md += _render_rxn_images(rxn_smiles, rxn_legends)
    return md


def autofill_conditions(reaction_smiles):
    _ensure_globals()
    if not reaction_smiles or not reaction_smiles.strip():
        return "", "", 0, 0, 0
    try:
        result = json.loads(_tool_executor.execute("recommend_conditions_default", {
            "reaction_smiles": reaction_smiles.strip(),
            "top_k": 1,
        }))
        if "error" in result:
            return "", "", 0, 0, 0
        recs = result.get("recommendations", {})
        solvent = recs.get("solvent", [{}])[0].get("label", "")
        electrolyte = recs.get("electrolyte", [{}])[0].get("label", "")
        anode_idx = recs.get("anode", [{}])[0].get("index", 0)
        cathode_idx = recs.get("cathode", [{}])[0].get("index", 0)
        cell_type_idx = recs.get("cell_type", [{}])[0].get("index", 0)
        return solvent, electrolyte, anode_idx, cathode_idx, cell_type_idx
    except Exception:
        return "", "", 0, 0, 0


# ═══════════════════════════════════════════════════════════════════
#  Tab 3: Bayesian Optimization — backend functions
# ═══════════════════════════════════════════════════════════════════

_bo_lock = threading.Lock()


def _create_bo_optimizer(reaction_smiles, prior_mode="rag_mean"):
    """Create and initialize a BayesianConditionOptimizer for a reaction.

    Args:
        reaction_smiles: target reaction SMILES
        prior_mode: GP prior strategy — "m3", "rag_mean", or "none"
    """
    _ensure_globals()
    from bayesian_opt import BayesianConditionOptimizer, ConditionSpace, WarmStarter

    config = AgentConfig(device=_device)
    space = ConditionSpace(vocab_path=config.vocab_path)

    # Test if retriever actually works before passing it
    usable_retriever = None
    if _retriever is not None:
        try:
            _retriever._ensure_loaded()
            usable_retriever = _retriever
        except Exception:
            pass

    warm_starter = WarmStarter(retriever=usable_retriever, model_manager=_model_manager)

    # Build yield predictor function (used in m3 mode and as oracle in offline search)
    def yield_predictor_fn(conditions):
        try:
            result = json.loads(_tool_executor.execute("predict_yield", {
                "reaction_smiles": reaction_smiles,
                "conditions": [{
                    "solvent_smiles": conditions.get("solvent_smiles", ""),
                    "electrolyte_smiles": conditions.get("electrolyte_smiles", ""),
                    "anode_index": conditions.get("anode_index", 0),
                    "cathode_index": conditions.get("cathode_index", 0),
                    "cell_type_index": conditions.get("cell_type_index", 0),
                }],
            }))
            preds = result.get("yield_predictions", [])
            if preds:
                return float(preds[0].get("predicted_yield", 0))
        except Exception:
            pass
        return 0.0

    optimizer = BayesianConditionOptimizer(
        condition_space=space,
        warm_starter=warm_starter,
        yield_predictor_fn=yield_predictor_fn,
        prior_mode=prior_mode,
        retriever=usable_retriever,
        model_manager=_model_manager,
    )
    return optimizer


def _fmt_smiles_combo(smiles_str):
    """Format a SMILES string for display."""
    if not smiles_str:
        return 'N/A'
    return f"`{smiles_str}`"


def _fmt_bo_card(c, rank=None, extra_fields=None):
    """Format a condition dict as a readable markdown card (not a table row).

    Args:
        c: condition dict
        rank: optional rank number
        extra_fields: optional dict of extra info to show (e.g. {'Yield': '75%'})
    """
    header = f"**#{rank}**" if rank else ""
    if extra_fields:
        extras = " | ".join(f"**{k}:** {v}" for k, v in extra_fields.items())
        header = f"{header} {extras}" if header else extras

    anode = ELECTRODE_NAMES.get(c.get('anode_index', 0), '?')
    cathode = ELECTRODE_NAMES.get(c.get('cathode_index', 0), '?')
    cell = CELL_TYPE_NAMES.get(c.get('cell_type_index', 0), '?')

    lines = [header] if header else []
    lines.append(f"- **Anode:** {anode} | **Cathode:** {cathode} | **Cell Type:** {cell}")

    for key, label in [('solvent', 'Solvent'), ('electrolyte', 'Electrolyte'),
                        ('reagent', 'Reagent'), ('catalyst', 'Catalyst')]:
        smiles = c.get(f'{key}_smiles', '')
        lines.append(f"- **{label}:** {_fmt_smiles_combo(smiles)}")

    return "\n".join(lines)


def bo_offline_search(reaction_smiles, n_iter, acq_func, prior_mode, progress=gr.Progress()):
    """Run offline BO search and return results as markdown."""
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    reaction_smiles = reaction_smiles.strip()

    try:
        progress(0, desc="Initializing Bayesian optimizer...")
        optimizer = _create_bo_optimizer(reaction_smiles, prior_mode=prior_mode)

        progress(0.1, desc="Running BO search...")
        results = optimizer.search_optimal(
            reaction_smiles=reaction_smiles,
            n_iter=int(n_iter),
            acq_func=acq_func,
            verbose=False,
        )

        if not results:
            return "No results found."

        progress(0.9, desc="Formatting results...")

        md = _render_rxn_image(reaction_smiles, "Target Reaction")
        md += f"\n\n### Bayesian Optimization Results\n"
        md += f"**Iterations:** {int(n_iter)} | **Acquisition:** {acq_func.upper()} | **Prior:** {prior_mode}\n\n"

        # RAG diagnostics
        if prior_mode == "rag_mean" and optimizer._rag_prior is not None:
            diag = optimizer._rag_prior.diagnostics()
            md += f"**RAG prior:** pool={diag['pool_size']}"
            if diag['pool_size'] > 0:
                yd = diag['yield_distribution_in_pool']
                md += f", yield {yd[0]:.0f}–{yd[4]:.0f}% (median {yd[2]:.0f}%)"
            md += f", fallbacks={diag['n_fallback_empty_pool']}\n\n"
        md += f"**Note:** Offline mode yield = M3 oracle prediction (M3 tends to predict ~100%)\n\n"

        # Results as cards
        for i, r in enumerate(results[:10], 1):
            extra = {
                'Yield': f"**{r['yield']}%**",
                'Iter': str(r['iteration']),
                'Phase': r['phase'],
            }
            md += _fmt_bo_card(r['conditions'], rank=i, extra_fields=extra)
            md += "\n\n---\n\n"

        # Convergence info
        bo_results = [r for r in results if r['phase'] == 'bo']
        if bo_results:
            best_yield = results[0]['yield']
            md += f"\n**Best yield found:** {best_yield}%\n"

        progress(1.0, desc="Done!")
        return md

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"**Error:** {e}"


def bo_rerank(reaction_smiles, top_k, alpha, beta_ucb, prior_mode, progress=gr.Progress()):
    """Rerank M1 candidates using GP-UCB and return results."""
    if not reaction_smiles or not reaction_smiles.strip():
        return "Please enter a reaction SMILES."
    reaction_smiles = reaction_smiles.strip()

    try:
        progress(0, desc="Getting M1 predictions...")
        _ensure_globals()

        # Get M1 top-k recommendations
        result = json.loads(_tool_executor.execute("recommend_conditions_default", {
            "reaction_smiles": reaction_smiles,
            "top_k": int(top_k),
        }))
        if "error" in result:
            return f"**Error:** {result['error']}"

        recs = result.get("recommendations", {})

        progress(0.3, desc="Building candidates...")

        # Build candidate condition dicts from M1 predictions
        from bayesian_opt import ConditionSpace
        config = AgentConfig(device=_device)
        space = ConditionSpace(vocab_path=config.vocab_path)
        candidates = space.get_m1_candidates(recs, top_k=int(top_k))

        # Extract M1 probabilities (use product of per-condition confidences)
        m1_probs = []
        for cand in candidates:
            prob = 1.0
            for key in ['anode', 'cathode', 'cell_type', 'solvent', 'electrolyte', 'reagent', 'catalyst']:
                idx = cand.get(f'{key}_index', 0)
                items = recs.get(key, [])
                for item in items:
                    if item.get('index') == idx:
                        prob *= item.get('confidence', 0.01)
                        break
            m1_probs.append(prob)

        progress(0.5, desc="Running GP-UCB reranking...")
        optimizer = _create_bo_optimizer(reaction_smiles, prior_mode=prior_mode)
        ranked = optimizer.rerank_candidates(
            candidates=candidates,
            reaction_smiles=reaction_smiles,
            alpha=float(alpha),
            beta_ucb=float(beta_ucb),
            m1_probs=m1_probs,
        )

        if not ranked:
            return "No candidates to rerank."

        progress(0.9, desc="Formatting results...")

        md = _render_rxn_image(reaction_smiles, "Target Reaction")
        md += f"\n\n### GP-UCB Reranked Conditions\n"
        md += f"**Alpha (M1 weight):** {alpha} | **Beta (UCB exploration):** {beta_ucb}\n\n"
        for i, r in enumerate(ranked[:15], 1):
            extra = {
                'Score': f"**{r['combined_score']:.4f}**",
                'GP Mean': f"{r['gp_mean']:.1f}",
                'GP Std': f"{r['gp_std']:.1f}",
                'UCB': f"{r['ucb']:.1f}",
            }
            md += _fmt_bo_card(r['conditions'], rank=i, extra_fields=extra)
            md += "\n\n---\n\n"

        progress(1.0, desc="Done!")
        return md

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"**Error:** {e}"


def _fmt_suggestions_list(details):
    """Format suggestion details into markdown cards."""
    md = ""
    for i, d in enumerate(details, 1):
        extra = {
            'Pred. Yield': f"{d.get('predicted_mean', 0):.1f}%",
            'Uncertainty': f"±{d.get('predicted_std', 0):.1f}",
        }
        md += _fmt_bo_card(d['conditions'], rank=i, extra_fields=extra)
        md += "\n\n"
    return md


def bo_iterative_init(reaction_smiles, n_suggest, prior_mode):
    """Initialize BO for iterative mode. Returns (state_dict, display_md)."""
    if not reaction_smiles or not reaction_smiles.strip():
        return None, "Please enter a reaction SMILES."
    reaction_smiles = reaction_smiles.strip()
    n_suggest = int(n_suggest)

    try:
        optimizer = _create_bo_optimizer(reaction_smiles, prior_mode=prior_mode)
        optimizer.initialize(reaction_smiles)

        # Get first suggestions
        details = optimizer.suggest_with_details(n=n_suggest, acq_func='ei')

        state = {
            'optimizer': optimizer,
            'reaction_smiles': reaction_smiles,
            'history': [],
            'round': 0,
            'last_details': details,
            'n_suggest': n_suggest,
        }

        md = _render_rxn_image(reaction_smiles, "Target Reaction")
        md += "\n\n### Bayesian Optimization — Iterative Mode\n"
        md += f"**Initialized!** Prior mode: `{prior_mode}` | Suggesting **{n_suggest}** conditions per round.\n\n"

        # Diagnostics
        n_obs = optimizer.surrogate.n_observations
        md += f"**GP warm-start:** {n_obs} observations"
        if n_obs > 0:
            y_obs = optimizer.surrogate.y_observed
            md += f" (yield range: {min(y_obs):.1f}–{max(y_obs):.1f}%, mean: {sum(y_obs)/len(y_obs):.1f}%)"
        md += "\n\n"

        if prior_mode == "rag_mean" and optimizer._rag_prior is not None:
            diag = optimizer._rag_prior.diagnostics()
            md += f"**RAG prior pool:** {diag['pool_size']} entries"
            if diag['pool_size'] > 0:
                yd = diag['yield_distribution_in_pool']
                md += f" | yield: {yd[0]:.0f}–{yd[4]:.0f}% (median {yd[2]:.0f}%)"
                md += f" | mean rxn sim: {diag['mean_rxn_sim_in_pool']:.3f}"
            else:
                md += " (empty → fallback 57.8%)"
            md += "\n\n"

            # Sample prior values for first few suggestions
            if details:
                prior_vals = [optimizer._rag_prior(d['conditions']) for d in details[:5]]
                md += f"**Prior values for top suggestions:** {', '.join(f'{v:.1f}%' for v in prior_vals)}\n\n"

        md += "**Suggested conditions to try:**\n\n"
        md += _fmt_suggestions_list(details)
        md += "\n**Next step:** Run experiments, fill in yields below (one per line: `suggestion#,yield`), then submit."
        return state, md

    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"**Error:** {e}"


def bo_iterative_observe(state, observations_text, n_suggest):
    """
    Record observations and get next suggestions.

    observations_text: one observation per line, format: "suggestion#,yield"
      e.g. "1,75.2" or multiple lines:
        1,75.2
        3,60.0
    """
    if state is None:
        return None, "Please initialize first."

    try:
        optimizer = state['optimizer']
        last_details = state.get('last_details', [])
        n_suggest = int(n_suggest)

        # Parse observations
        lines = [l.strip() for l in observations_text.strip().split('\n') if l.strip()]
        if not lines:
            return state, "**Error:** Please enter at least one observation (format: `suggestion#,yield`)."

        recorded = []
        for line in lines:
            parts = line.replace(' ', '').split(',')
            if len(parts) < 2:
                return state, f"**Error:** Invalid format `{line}`. Use `suggestion#,yield` (e.g. `1,75.2`)."
            try:
                idx = int(parts[0]) - 1  # 0-indexed
                yield_val = float(parts[1])
            except ValueError:
                return state, f"**Error:** Cannot parse `{line}`. Use `suggestion#,yield` (e.g. `1,75.2`)."

            if idx < 0 or idx >= len(last_details):
                return state, f"**Error:** Suggestion #{idx+1} does not exist. Valid range: 1-{len(last_details)}."

            chosen = last_details[idx]['conditions']
            optimizer.observe(chosen, yield_val)
            state['round'] += 1
            state['history'].append({
                'round': state['round'],
                'yield': yield_val,
                'conditions': chosen,
            })
            recorded.append((idx + 1, yield_val))

        # Get next suggestions
        new_details = optimizer.suggest_with_details(n=n_suggest, acq_func='ei')
        state['last_details'] = new_details
        state['n_suggest'] = n_suggest

        best = optimizer.get_best()

        md = f"### Recorded {len(recorded)} observation(s)\n\n"
        for sid, yld in recorded:
            md += f"- Suggestion #{sid} → yield **{yld}%**\n"

        if best:
            md += f"\n**Best so far:** {best['yield']:.1f}% (after {best['n_observations']} observations)\n\n"

        # History table
        md += "\n**Experiment History:**\n\n| Round | Yield |\n|-------|-------|\n"
        for h in state['history']:
            md += f"| {h['round']} | {h['yield']}% |\n"

        md += f"\n**Next {n_suggest} suggestions:**\n\n"
        md += _fmt_suggestions_list(new_details)

        return state, md

    except Exception as e:
        import traceback
        traceback.print_exc()
        return state, f"**Error:** {e}"


# ═══════════════════════════════════════════════════════════════════
#  Build Gradio App
# ═══════════════════════════════════════════════════════════════════

EXAMPLE_REACTION = "CC(=O)c1ccccc1>>CC(O)c1ccccc1"

EXAMPLE_REACTIONS = [
    ["Please analyze this electrochemical reaction and recommend optimal conditions: CC(=O)c1ccccc1>>CC(O)c1ccccc1"],
    ["Recommend conditions for the Kolbe electrolysis: CCCC(=O)[O-]>>CCCCCCCC"],
    ["What are the best electrochemical conditions for: c1ccc(Br)cc1>>c1ccc(-c2ccccc2)cc1"],
    ["Search for similar reactions and predict yield for: CC=O>>CC(O)O"],
]

ANODE_CHOICES = [(f"{v} ({k})", k) for k, v in sorted(ELECTRODE_NAMES.items()) if k != UNKNOWN_INDICES['anode']]
CATHODE_CHOICES = [(f"{v} ({k})", k) for k, v in sorted(ELECTRODE_NAMES.items()) if k != UNKNOWN_INDICES['cathode']]
CELL_TYPE_CHOICES = [(f"{v} ({k})", k) for k, v in sorted(CELL_TYPE_NAMES.items()) if k != UNKNOWN_INDICES['cell_type']]

# ── Custom CSS ───────────────────────────────────────────────────
CUSTOM_CSS = """
/* ══════════════════════════════════════════════════════
   CSS Custom Properties
   ══════════════════════════════════════════════════════ */
:root {
    --bg-primary:    #ffffff;
    --bg-secondary:  #f8fafc;
    --bg-tertiary:   #f1f5f9;
    --bg-card:       #ffffff;
    --bg-input:      #ffffff;
    --border-light:  #e5e7eb;
    --border-medium: #d1d5db;
    --text-primary:  #111827;
    --text-secondary:#4b5563;
    --text-muted:    #9ca3af;
    --accent:        #2563eb;
    --accent-light:  #3b82f6;
    --accent-bg:     #eff6ff;
    --accent-border: #bfdbfe;
    --accent-shadow: rgba(37,99,235,0.15);
    --shadow-sm:     0 1px 2px rgba(0,0,0,0.05);
    --shadow-md:     0 4px 12px rgba(0,0,0,0.08);
    --chat-user-bg:  #2563eb;
    --chat-bot-bg:   #f9fafb;
    --chat-bot-border:#e5e7eb;
    --sidebar-bg:    #f9fafb;
    --sidebar-border:#e5e7eb;
    --radius-sm:     6px;
    --radius-md:     10px;
    --radius-lg:     14px;
    --transition:    0.2s ease;
}

.dark-mode {
    --bg-primary:    #111827;
    --bg-secondary:  #1f2937;
    --bg-tertiary:   #374151;
    --bg-card:       #1f2937;
    --bg-input:      #1f2937;
    --border-light:  #374151;
    --border-medium: #4b5563;
    --text-primary:  #f9fafb;
    --text-secondary:#d1d5db;
    --text-muted:    #6b7280;
    --accent:        #60a5fa;
    --accent-light:  #93c5fd;
    --accent-bg:     rgba(37,99,235,0.15);
    --accent-border: #1e40af;
    --accent-shadow: rgba(96,165,250,0.12);
    --shadow-sm:     0 1px 2px rgba(0,0,0,0.2);
    --shadow-md:     0 4px 12px rgba(0,0,0,0.25);
    --chat-user-bg:  #3b82f6;
    --chat-bot-bg:   #1f2937;
    --chat-bot-border:#374151;
    --sidebar-bg:    #1f2937;
    --sidebar-border:#374151;
}

@media (prefers-color-scheme: dark) {
    :root:not(.light-mode) {
        --bg-primary:    #111827;
        --bg-secondary:  #1f2937;
        --bg-tertiary:   #374151;
        --bg-card:       #1f2937;
        --bg-input:      #1f2937;
        --border-light:  #374151;
        --border-medium: #4b5563;
        --text-primary:  #f9fafb;
        --text-secondary:#d1d5db;
        --text-muted:    #6b7280;
        --accent:        #60a5fa;
        --accent-light:  #93c5fd;
        --accent-bg:     rgba(37,99,235,0.15);
        --accent-border: #1e40af;
        --accent-shadow: rgba(96,165,250,0.12);
        --shadow-sm:     0 1px 2px rgba(0,0,0,0.2);
        --shadow-md:     0 4px 12px rgba(0,0,0,0.25);
        --chat-user-bg:  #3b82f6;
        --chat-bot-bg:   #1f2937;
        --chat-bot-border:#374151;
        --sidebar-bg:    #1f2937;
        --sidebar-border:#374151;
    }
}

/* ══════════════════════════════════════════════════════
   Global — full width
   ══════════════════════════════════════════════════════ */
.gradio-container {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 2rem !important;
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

/* ══════════════════════════════════════════════════════
   Header — light gradient with subtle animation
   ══════════════════════════════════════════════════════ */
@keyframes headerShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.app-header {
    background: linear-gradient(135deg, #3b82f6 0%, #6366f1 35%, #8b5cf6 65%, #3b82f6 100%);
    background-size: 200% 200%;
    animation: headerShift 10s ease infinite;
    color: white;
    text-align: center;
    padding: 2.2rem 2rem 1.8rem;
    border-radius: var(--radius-lg);
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}
.app-header::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 500px 250px at 25% 40%, rgba(255,255,255,0.12) 0%, transparent 70%),
        radial-gradient(ellipse 350px 350px at 75% 60%, rgba(255,255,255,0.08) 0%, transparent 60%);
    pointer-events: none;
}
.app-header::after {
    content: '';
    position: absolute;
    inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='20' cy='20' r='0.8' fill='rgba(255,255,255,0.12)'/%3E%3C/svg%3E");
    pointer-events: none;
}
.app-header h1 {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0 0 0.4rem 0;
    letter-spacing: -0.3px;
    position: relative;
}
.app-header .subtitle {
    font-size: 0.95rem;
    opacity: 0.92;
    margin: 0 0 1.2rem 0;
    font-weight: 400;
    position: relative;
}
.app-header .badges {
    display: flex;
    justify-content: center;
    gap: 0.6rem;
    flex-wrap: wrap;
    position: relative;
}
.app-header .badges span {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    padding: 0.38rem 1rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    transition: background 0.2s;
}
.app-header .badges span:hover {
    background: rgba(255,255,255,0.3);
}
.header-actions {
    position: absolute;
    top: 0.8rem;
    right: 1rem;
    z-index: 10;
}
.dark-toggle {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
}
.dark-toggle:hover {
    background: rgba(255,255,255,0.32);
}

/* ══════════════════════════════════════════════════════
   Tabs
   ══════════════════════════════════════════════════════ */
.tabs > .tab-nav {
    border-bottom: 2px solid var(--border-light) !important;
    gap: 0 !important;
}
.tabs > .tab-nav > button {
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.75rem 1.8rem !important;
    border-radius: var(--radius-sm) var(--radius-sm) 0 0 !important;
    border: none !important;
    color: var(--text-muted) !important;
    transition: all var(--transition) !important;
    background: transparent !important;
}
.tabs > .tab-nav > button.selected {
    color: var(--accent) !important;
    background: var(--accent-bg) !important;
    border-bottom: 2px solid var(--accent) !important;
}
.tabs > .tab-nav > button:hover:not(.selected) {
    color: var(--text-primary) !important;
    background: var(--bg-secondary) !important;
}

/* ══════════════════════════════════════════════════════
   Sidebar
   ══════════════════════════════════════════════════════ */
.sidebar-col {
    background: var(--sidebar-bg) !important;
    border-right: 1px solid var(--sidebar-border) !important;
    border-radius: var(--radius-lg) !important;
    padding: 0.5rem !important;
    min-width: 280px !important;
}
.sidebar-col .gr-accordion {
    background: var(--bg-card) !important;
    border-color: var(--border-light) !important;
}
.sidebar-section-title {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    padding: 0.6rem 0.8rem 0.3rem;
    margin: 0;
}

/* ══════════════════════════════════════════════════════
   Chat
   ══════════════════════════════════════════════════════ */
.message.bot .message-bubble-border {
    background: var(--chat-bot-bg) !important;
    border: 1px solid var(--chat-bot-border) !important;
    border-radius: var(--radius-lg) var(--radius-lg) var(--radius-lg) 4px !important;
}
.message.user .message-bubble-border {
    background: var(--chat-user-bg) !important;
    border: none !important;
    color: white !important;
    border-radius: var(--radius-lg) var(--radius-lg) 4px var(--radius-lg) !important;
}
.message.user .message-bubble-border * { color: white !important; }
.chatbot {
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-light) !important;
    box-shadow: var(--shadow-sm) !important;
    background: var(--bg-primary) !important;
}

/* ══════════════════════════════════════════════════════
   Input area
   ══════════════════════════════════════════════════════ */
.input-row {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-lg) !important;
    padding: 0.4rem !important;
    transition: border-color var(--transition), box-shadow var(--transition) !important;
}
.input-row:focus-within {
    border-color: var(--accent-light) !important;
    box-shadow: 0 0 0 3px var(--accent-shadow) !important;
}
.input-row textarea {
    border-radius: var(--radius-md) !important;
    border: none !important;
    background: var(--bg-input) !important;
    color: var(--text-primary) !important;
    padding: 0.7rem 0.9rem !important;
    font-size: 0.95rem !important;
}

/* ══════════════════════════════════════════════════════
   Buttons
   ══════════════════════════════════════════════════════ */
button.primary {
    background: var(--accent) !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    min-height: 42px !important;
    transition: all var(--transition) !important;
    color: white !important;
}
button.primary:hover {
    opacity: 0.9 !important;
}
button.secondary {
    border-radius: var(--radius-md) !important;
    font-weight: 500 !important;
    border: 1px solid var(--border-medium) !important;
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    transition: all var(--transition) !important;
}
button.secondary:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}
button.stop { border-radius: var(--radius-md) !important; }
.send-btn {
    min-height: 50px !important;
    font-size: 0.95rem !important;
}

/* ══════════════════════════════════════════════════════
   Accordion
   ══════════════════════════════════════════════════════ */
.gr-accordion {
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-lg) !important;
    margin-bottom: 0.6rem !important;
    overflow: hidden !important;
    background: var(--bg-card) !important;
}
.gr-accordion:hover {
    border-color: var(--border-medium) !important;
}
.gr-accordion > .label-wrap {
    padding: 0.85rem 1.1rem !important;
    font-weight: 600 !important;
    color: var(--text-primary) !important;
    background: var(--bg-card) !important;
}

/* ══════════════════════════════════════════════════════
   Tool Demo Capability Cards — clean style
   ══════════════════════════════════════════════════════ */
.capability-cards {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0.6rem;
    margin-bottom: 1rem;
}
.cap-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 1rem 0.6rem;
    text-align: center;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-secondary);
    transition: border-color 0.2s;
}
.cap-card:hover {
    border-color: var(--accent-border);
}
.cap-card .cap-icon {
    font-size: 1.5rem;
    display: block;
    margin-bottom: 0.3rem;
}

/* Sticky reaction input */
.sticky-input {
    position: sticky;
    top: 0;
    z-index: 50;
    background: var(--bg-primary) !important;
    padding: 0.6rem 0 !important;
    border-bottom: 1px solid var(--border-light);
    margin-bottom: 0.6rem;
}

/* ══════════════════════════════════════════════════════
   Misc
   ══════════════════════════════════════════════════════ */
.conv-status {
    font-size: 0.85rem !important;
    padding: 0.4rem 0 !important;
    color: var(--text-muted);
}
.gr-input, .gr-text-input, .gr-dropdown {
    border-radius: var(--radius-sm) !important;
    background: var(--bg-input) !important;
    color: var(--text-primary) !important;
    border-color: var(--border-light) !important;
}
label > span {
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
    font-size: 0.85rem !important;
}
.tab-description {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 0.8rem 1rem;
    margin-bottom: 0.8rem;
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.5;
}

/* ══════════════════════════════════════════════════════
   Footer
   ══════════════════════════════════════════════════════ */
.app-footer {
    text-align: center;
    padding: 1.2rem 0 0.8rem;
    color: var(--text-muted);
    font-size: 0.78rem;
    border-top: 1px solid var(--border-light);
    margin-top: 1.5rem;
}
.app-footer .footer-tech {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    flex-wrap: wrap;
    margin-bottom: 0.5rem;
}
.app-footer .footer-tech span {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    padding: 0.25rem 0.7rem;
    border-radius: var(--radius-sm);
    font-size: 0.72rem;
    font-weight: 500;
    color: var(--text-secondary);
}

/* ══════════════════════════════════════════════════════
   Results, Examples, Slider, Scrollbar
   ══════════════════════════════════════════════════════ */
.tool-result-area {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-md) !important;
    padding: 1rem !important;
}
.gr-examples {
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-light) !important;
    overflow: hidden !important;
}
input[type="range"] { accent-color: var(--accent) !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-medium); border-radius: 3px; }

/* ══════════════════════════════════════════════════════
   Responsive
   ══════════════════════════════════════════════════════ */
@media (max-width: 768px) {
    .gradio-container { padding: 0 0.5rem !important; }
    .app-header { padding: 1.4rem 1rem 1.2rem; }
    .app-header h1 { font-size: 1.3rem; }
    .capability-cards { grid-template-columns: repeat(2, 1fr); }
    .sidebar-col { min-width: unset !important; border-right: none !important; border-bottom: 1px solid var(--sidebar-border) !important; }
}
@media (max-width: 480px) {
    .app-header h1 { font-size: 1.1rem; }
    .capability-cards { grid-template-columns: 1fr; }
}
"""


DARK_MODE_INIT_JS = """
function() {
    const root = document.documentElement;
    const saved = localStorage.getItem('echem-dark-mode');
    if (saved === 'true' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        root.classList.add('dark-mode');
    }
    window.toggleDarkMode = function() {
        root.classList.toggle('dark-mode');
        const isDark = root.classList.contains('dark-mode');
        localStorage.setItem('echem-dark-mode', isDark);
        const btn = document.querySelector('.dark-toggle');
        if (btn) btn.textContent = isDark ? '\\u2600\\ufe0f' : '\\ud83c\\udf19';
    };
    // Update button icon after DOM settles
    setTimeout(function() {
        const btn = document.querySelector('.dark-toggle');
        if (btn) btn.textContent = root.classList.contains('dark-mode') ? '\\u2600\\ufe0f' : '\\ud83c\\udf19';
    }, 200);
}
"""


APP_THEME = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Inter"),
    radius_size=gr.themes.sizes.radius_md,
    spacing_size=gr.themes.sizes.spacing_md,
    text_size=gr.themes.sizes.text_md,
)


def build_app():
    with gr.Blocks(
        title="Electrochemical Condition Agent",
    ) as app:

        # ── Header with dark mode toggle ─────────────────────
        gr.HTML(
            '<div class="app-header">'
            '  <div class="header-actions">'
            '    <button class="dark-toggle" onclick="toggleDarkMode()" title="Toggle dark mode"></button>'
            '  </div>'
            "  <h1>Electrochemical Condition Agent</h1>"
            '  <p class="subtitle">'
            "    AI-powered reaction condition optimization for electrochemical synthesis"
            "  </p>"
            '  <div class="badges">'
            "    <span>10 Specialized Tools</span>"
            "    <span>10,000+ Reactions</span>"
            "    <span>3 ML Models</span>"
            "    <span>RAG Retrieval</span>"
            "    <span>Multi-Model Debate</span>"
            "  </div>"
            "</div>"
        )

        # ══════════════════════════════════════════════════════
        #  Tab 1: Agent Chat — sidebar + main area
        # ══════════════════════════════════════════════════════
        with gr.Tab("Agent Chat"):
            gr.HTML(
                '<div class="tab-description">'
                "Chat with the LLM-powered ReAct agent. It autonomously calls "
                "<b>10 specialized tools</b> (substrate analysis, condition recommendation, "
                "CVAE generation, yield prediction, similarity search, etc.) to analyze "
                "your reaction and recommend optimal electrochemical conditions."
                "</div>"
            )

            # Default API settings — auto-detect local vLLM
            _vllm_local = False
            try:
                import urllib.request
                with urllib.request.urlopen("http://localhost:8000/v1/models", timeout=2) as resp:
                    _vllm_models = json.loads(resp.read())
                    _vllm_model_id = _vllm_models["data"][0]["id"] if _vllm_models.get("data") else ""
                    _vllm_local = bool(_vllm_model_id)
            except Exception:
                _vllm_model_id = ""

            if _vllm_local:
                _default_backend = "openai"
                _default_api_key = "EMPTY"
                _default_base_url = "http://localhost:8000/v1"
                _default_model = _vllm_model_id
            else:
                _default_backend = os.environ.get("LLM_BACKEND", "openai")
                _default_api_key = os.environ.get("ANTHROPIC_API_KEY", "")
                _default_base_url = os.environ.get(
                    "ANTHROPIC_BASE_URL",
                    "https://api.boyuerichdata.opensphereai.com/v1",
                )
                _default_model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-6")

            with gr.Row():
                # ── Left Sidebar ──────────────────────────
                with gr.Column(scale=1, min_width=280, elem_classes="sidebar-col"):
                    gr.HTML('<p class="sidebar-section-title">Configuration</p>')

                    with gr.Accordion("API Settings", open=False):
                        backend_input = gr.Dropdown(
                            label="Backend",
                            choices=["anthropic", "openai"],
                            value=_default_backend,
                            interactive=True,
                            info="Use 'openai' for vLLM or any OpenAI-compatible endpoint",
                        )
                        api_key_input = gr.Textbox(
                            label="API Key",
                            placeholder="sk-ant-... (or set env var)",
                            type="password",
                            value=_default_api_key,
                            interactive=True,
                        )
                        base_url_input = gr.Textbox(
                            label="Base URL",
                            placeholder="(optional)",
                            value=_default_base_url,
                            interactive=True,
                        )

                    with gr.Accordion("Model Settings", open=False):
                        model_input = gr.Textbox(
                            label="Model",
                            value=_default_model,
                            interactive=True,
                        )
                        device_input = gr.Dropdown(
                            label="Device",
                            choices=["cpu", "cuda"],
                            value=_device,
                            interactive=True,
                        )
                        temperature_input = gr.Slider(
                            label="Temperature",
                            minimum=0.0,
                            maximum=1.0,
                            value=1.0,
                            step=0.05,
                            interactive=True,
                        )

                    with gr.Accordion("Debate Mode", open=False):
                        debate_checkbox = gr.Checkbox(
                            label="Enable multi-model debate",
                            value=False,
                            interactive=True,
                        )
                        recommender_b_model_input = gr.Textbox(
                            label="Recommender B",
                            value="gpt-5.4",
                            interactive=True,
                        )
                        judge_model_input = gr.Textbox(
                            label="Judge Model",
                            value="gemini-3.1-pro-preview",
                            interactive=True,
                        )

                    gr.HTML('<p class="sidebar-section-title">Conversations</p>')

                    with gr.Accordion("Save / Load", open=False):
                        conv_name_input = gr.Textbox(
                            label="Name",
                            placeholder="Conversation name...",
                            interactive=True,
                        )
                        save_btn = gr.Button("Save", variant="primary", size="sm", min_width=80)
                        conv_dropdown = gr.Dropdown(
                            label="Saved",
                            choices=_list_conversations(),
                            interactive=True,
                        )
                        with gr.Row():
                            load_btn = gr.Button("Load", variant="secondary", size="sm", min_width=60)
                            delete_btn = gr.Button("Delete", variant="stop", size="sm", min_width=60)
                        conv_status = gr.Markdown(value="", elem_classes="conv-status")

                # ── Main Chat Area ────────────────────────
                with gr.Column(scale=3):
                    chatbot = gr.Chatbot(
                        label="",
                        height=580,
                        placeholder="Enter a reaction SMILES or ask about electrochemical conditions to get started...",
                        show_label=False,
                    )
                    agent_state = gr.State(None)

                    with gr.Row(elem_classes="input-row"):
                        chat_input = gr.Textbox(
                            label="Your message",
                            placeholder=(
                                "Enter a reaction SMILES or question...  "
                                "e.g. Recommend conditions for CC(=O)c1ccccc1>>CC(O)c1ccccc1"
                            ),
                            lines=2,
                            scale=5,
                            interactive=True,
                            show_label=False,
                        )
                        send_btn = gr.Button(
                            "Send", variant="primary", scale=1,
                            elem_classes="send-btn",
                            min_width=100,
                        )

                    with gr.Row():
                        reset_btn = gr.Button("Reset Conversation", variant="secondary", size="sm")
                        download_btn = gr.Button("Download Report", variant="secondary", size="sm")
                    report_file = gr.File(label="Report", visible=False, interactive=False)

                    gr.Examples(
                        examples=EXAMPLE_REACTIONS,
                        inputs=[chat_input],
                        label="Example Queries",
                    )

            # Wiring — agent_chat_fn returns (history, state, "")
            _chat_inputs = [
                chat_input, chatbot, agent_state,
                api_key_input, base_url_input, model_input, device_input,
                temperature_input,
                backend_input,
                debate_checkbox, recommender_b_model_input, judge_model_input,
            ]
            # gr.State holding browser session id (set on page load via demo.load)
            session_id_state = gr.State("")

            def _autosave_then_refresh(chat_history, sid):
                _auto_save_conversation(chat_history, sid)
                return gr.update(choices=_list_conversations())

            send_btn.click(
                fn=agent_chat_fn,
                inputs=_chat_inputs,
                outputs=[chatbot, agent_state, chat_input],
            ).then(
                fn=_autosave_then_refresh,
                inputs=[chatbot, session_id_state],
                outputs=[conv_dropdown],
            )
            chat_input.submit(
                fn=agent_chat_fn,
                inputs=_chat_inputs,
                outputs=[chatbot, agent_state, chat_input],
            ).then(
                fn=_autosave_then_refresh,
                inputs=[chatbot, session_id_state],
                outputs=[conv_dropdown],
            )
            reset_btn.click(
                fn=reset_chat_fn,
                outputs=[chatbot, agent_state],
            )

            def _download_report_fn(chat_history):
                path = _generate_report(chat_history)
                if path:
                    return gr.update(value=path, visible=True)
                return gr.update(visible=False)

            download_btn.click(
                fn=_download_report_fn,
                inputs=[chatbot],
                outputs=[report_file],
            )
            save_btn.click(
                fn=_save_conversation_fn,
                inputs=[chatbot, conv_name_input],
                outputs=[conv_dropdown, conv_status],
            )
            load_btn.click(
                fn=_load_conversation_fn,
                inputs=[conv_dropdown],
                outputs=[chatbot, agent_state, conv_status],
            )
            delete_btn.click(
                fn=_delete_conversation_fn,
                inputs=[conv_dropdown],
                outputs=[conv_dropdown, conv_status],
            )

        # ══════════════════════════════════════════════════════
        #  Tab 2: Tool Demo — sticky input + enhanced cards
        # ══════════════════════════════════════════════════════
        with gr.Tab("Tool Demo"):
            gr.HTML(
                '<div class="tab-description">'
                "Call the ML tools directly &mdash; <b>no API key needed</b>. "
                "Enter a reaction SMILES below and expand any tool section "
                "to see model predictions, similarity search results, and more."
                "</div>"
            )

            # Capability overview cards
            gr.HTML(
                '<div class="capability-cards">'
                '<div class="cap-card"><span class="cap-icon">🔬</span>Molecule<br>Validation</div>'
                '<div class="cap-card"><span class="cap-icon">🎯</span>Condition<br>Recommendation</div>'
                '<div class="cap-card"><span class="cap-icon">🧪</span>CVAE<br>Generation</div>'
                '<div class="cap-card"><span class="cap-icon">📊</span>Yield<br>Prediction</div>'
                '<div class="cap-card"><span class="cap-icon">🔎</span>Similarity<br>Search</div>'
                "</div>"
            )

            # Sticky reaction input
            with gr.Group(elem_classes="sticky-input"):
                reaction_input = gr.Textbox(
                    label="Reaction SMILES",
                    placeholder="reactants>>products  e.g. CC(=O)c1ccccc1>>CC(O)c1ccccc1",
                    value=EXAMPLE_REACTION,
                    interactive=True,
                )

            # Tool 1: Parse Reaction
            with gr.Accordion("🔬  Step 1 — Parse Reaction", open=False):
                gr.Markdown("Parse a reaction SMILES into reactants and products with molecular properties.")
                parse_btn = gr.Button("Parse Reaction", variant="primary", size="lg")
                parse_output = gr.Markdown(value="", elem_classes="tool-result-area")
                parse_btn.click(
                    fn=tool_parse_reaction,
                    inputs=[reaction_input],
                    outputs=[parse_output],
                )

            # Tool 2: Recommend Conditions
            with gr.Accordion("🎯  Step 2 — Recommend Conditions", open=False):
                gr.Markdown("Use the ConditionRecommender model to predict optimal conditions.")
                rec_topk = gr.Slider(
                    label="Top-k", minimum=1, maximum=10, value=3, step=1,
                )
                rec_btn = gr.Button("Recommend", variant="primary", size="lg")
                rec_output = gr.Markdown(value="", elem_classes="tool-result-area")
                rec_btn.click(
                    fn=tool_recommend_conditions,
                    inputs=[reaction_input, rec_topk],
                    outputs=[rec_output],
                )

            # Tool 3: Generate Conditions (CVAE)
            with gr.Accordion("🧪  Step 3 — Generate Conditions (CVAE)", open=False):
                gr.Markdown("Use the Categorical CVAE model to generate diverse condition schemes.")
                with gr.Row():
                    cvae_samples = gr.Slider(
                        label="Num Samples", minimum=1, maximum=50, value=10, step=1,
                    )
                    cvae_temp = gr.Slider(
                        label="Temperature", minimum=0.1, maximum=3.0, value=1.0, step=0.1,
                    )
                    cvae_topk = gr.Slider(
                        label="Top-k", minimum=1, maximum=10, value=3, step=1,
                    )
                cvae_btn = gr.Button("Generate", variant="primary", size="lg")
                cvae_output = gr.Markdown(value="", elem_classes="tool-result-area")
                cvae_btn.click(
                    fn=tool_generate_cvae,
                    inputs=[reaction_input, cvae_samples, cvae_temp, cvae_topk],
                    outputs=[cvae_output],
                )

            # Tool 4: Predict Yield
            with gr.Accordion("📊  Step 4 — Predict Yield", open=False):
                gr.Markdown(
                    "Predict reaction yield for specific conditions. "
                    "Use **Auto-fill** to populate from top-1 recommendations."
                )
                autofill_btn = gr.Button("Auto-fill from Recommendations", variant="secondary")
                with gr.Row():
                    yield_solvent = gr.Textbox(
                        label="Solvent SMILES", placeholder="e.g. CC#N",
                        interactive=True,
                    )
                    yield_electrolyte = gr.Textbox(
                        label="Electrolyte SMILES",
                        placeholder="e.g. [N+](=O)([O-])c1ccccc1",
                        interactive=True,
                    )
                with gr.Row():
                    yield_anode = gr.Dropdown(
                        label="Anode", choices=ANODE_CHOICES, value=0,
                        interactive=True,
                    )
                    yield_cathode = gr.Dropdown(
                        label="Cathode", choices=CATHODE_CHOICES, value=0,
                        interactive=True,
                    )
                    yield_cell = gr.Dropdown(
                        label="Cell Type", choices=CELL_TYPE_CHOICES, value=0,
                        interactive=True,
                    )
                yield_btn = gr.Button("Predict Yield", variant="primary", size="lg")
                yield_output = gr.Markdown(value="", elem_classes="tool-result-area")

                autofill_btn.click(
                    fn=autofill_conditions,
                    inputs=[reaction_input],
                    outputs=[yield_solvent, yield_electrolyte,
                             yield_anode, yield_cathode, yield_cell],
                )
                yield_btn.click(
                    fn=tool_predict_yield,
                    inputs=[reaction_input, yield_solvent, yield_electrolyte,
                            yield_anode, yield_cathode, yield_cell],
                    outputs=[yield_output],
                )

            # Tool 5: Search Similar Reactions
            with gr.Accordion("🔎  Step 5 — Search Similar Reactions", open=False):
                gr.Markdown("Search the reaction database for similar reactions using FAISS.")
                with gr.Row():
                    search_topk = gr.Slider(
                        label="Top-k", minimum=1, maximum=20, value=5, step=1,
                    )
                    search_thresh = gr.Slider(
                        label="Similarity Threshold",
                        minimum=0.0, maximum=1.0, value=0.3, step=0.05,
                    )
                search_btn = gr.Button("Search", variant="primary", size="lg")
                search_output = gr.Markdown(value="", elem_classes="tool-result-area")
                search_btn.click(
                    fn=tool_search_similar,
                    inputs=[reaction_input, search_topk, search_thresh],
                    outputs=[search_output],
                )

        # ══════════════════════════════════════════════════════
        #  Tab 3: Bayesian Optimization
        # ══════════════════════════════════════════════════════
        with gr.Tab("Bayesian Optimization"):
            gr.HTML(
                '<div class="tab-description">'
                "Use Bayesian optimization (GP surrogate + acquisition functions) to search, "
                "rerank, or iteratively optimize electrochemical conditions. "
                "<b>No API key needed</b> — runs locally with ML models."
                "</div>"
            )

            bo_reaction_input = gr.Textbox(
                label="Reaction SMILES",
                placeholder="reactants>>products  e.g. CC(=O)c1ccccc1>>CC(O)c1ccccc1",
                value=EXAMPLE_REACTION,
                interactive=True,
            )
            bo_prior_mode = gr.Dropdown(
                label="GP Prior Mode",
                choices=["rag_mean", "m3", "none"],
                value="rag_mean",
                info="rag_mean=RAG k-NN yield mean (recommended), m3=M3 YieldPredictor, none=no prior",
            )

            # ── Mode 1: Offline Search ──────────────────────
            with gr.Accordion("🔍  Offline Search — Auto BO with Yield Oracle", open=True):
                gr.Markdown(
                    "Automatically search for optimal conditions using Bayesian optimization. "
                    "The yield predictor model serves as the oracle to evaluate candidates."
                )
                with gr.Row():
                    bo_n_iter = gr.Slider(
                        label="BO Iterations", minimum=10, maximum=200, value=50, step=10,
                    )
                    bo_acq_func = gr.Dropdown(
                        label="Acquisition Function",
                        choices=["ei", "ucb", "thompson"],
                        value="ei",
                        info="EI=Expected Improvement, UCB=Upper Confidence Bound",
                    )
                bo_search_btn = gr.Button("Run BO Search", variant="primary", size="lg")
                bo_search_output = gr.Markdown(value="", elem_classes="tool-result-area")

                bo_search_btn.click(
                    fn=bo_offline_search,
                    inputs=[bo_reaction_input, bo_n_iter, bo_acq_func, bo_prior_mode],
                    outputs=[bo_search_output],
                )

            # ── Mode 2: M1 Reranking ───────────────────────
            with gr.Accordion("📊  M1 Reranking — GP-UCB Rerank of M1 Predictions", open=False):
                gr.Markdown(
                    "Combine the M1 condition recommender's confidence with GP-UCB yield estimates "
                    "to rerank candidate conditions. Higher alpha = trust M1 more; lower alpha = trust GP more."
                )
                with gr.Row():
                    bo_rerank_topk = gr.Slider(
                        label="M1 Top-k", minimum=3, maximum=10, value=5, step=1,
                    )
                    bo_alpha = gr.Slider(
                        label="Alpha (M1 weight)", minimum=0.0, maximum=1.0, value=0.5, step=0.05,
                        info="0=pure GP-UCB, 1=pure M1",
                    )
                    bo_beta = gr.Slider(
                        label="Beta (UCB exploration)", minimum=0.0, maximum=5.0, value=1.5, step=0.1,
                        info="Higher = more exploration",
                    )
                bo_rerank_btn = gr.Button("Rerank Candidates", variant="primary", size="lg")
                bo_rerank_output = gr.Markdown(value="", elem_classes="tool-result-area")

                bo_rerank_btn.click(
                    fn=bo_rerank,
                    inputs=[bo_reaction_input, bo_rerank_topk, bo_alpha, bo_beta, bo_prior_mode],
                    outputs=[bo_rerank_output],
                )

            # ── Mode 3: Iterative Experiment ────────────────
            with gr.Accordion("🧪  Iterative Experiment — Suggest → Observe → Repeat", open=False):
                gr.Markdown(
                    "Interactive Bayesian optimization loop for real experiments. "
                    "The system suggests conditions, you run the experiment, input the yield, "
                    "and the GP updates to give better suggestions."
                )
                bo_iter_state = gr.State(None)

                bo_n_suggest = gr.Slider(
                    label="Number of suggestions per round",
                    minimum=1, maximum=20, value=5, step=1,
                    info="How many candidate conditions to suggest each round",
                )
                bo_init_btn = gr.Button("Initialize BO", variant="primary", size="lg")
                bo_iter_output = gr.Markdown(value="", elem_classes="tool-result-area")

                bo_init_btn.click(
                    fn=bo_iterative_init,
                    inputs=[bo_reaction_input, bo_n_suggest, bo_prior_mode],
                    outputs=[bo_iter_state, bo_iter_output],
                )

                gr.Markdown("---\n**Record experiment results:**")
                bo_observations = gr.Textbox(
                    label="Observations (one per line: suggestion#,yield)",
                    placeholder="e.g.:\n1,75.2\n3,60.0\n5,82.1",
                    lines=5,
                    interactive=True,
                    info="Format: suggestion number, observed yield (%). Submit multiple experiments at once.",
                )
                bo_observe_btn = gr.Button("Submit Observations & Get Next", variant="primary", size="lg")

                bo_observe_btn.click(
                    fn=bo_iterative_observe,
                    inputs=[bo_iter_state, bo_observations, bo_n_suggest],
                    outputs=[bo_iter_state, bo_iter_output],
                )

        # ══════════════════════════════════════════════════════
        #  Tab 4: 实验反馈与优化 (Form mode + BO + LLM)
        # ══════════════════════════════════════════════════════
        with gr.Tab("🧪 实验反馈与优化"):
            gr.HTML(
                '<div class="tab-description">'
                "<b>表单模式</b>: 填写反应条件 + observed yield, 一键记录历史, 让 <b>BO (贝叶斯)</b> 或 "
                "<b>LLM</b> 帮你规划下一轮实验. 所有数据按当前 session 持久存储到 ECS, 支持 CSV 导出 + Chat 互通."
                "</div>"
            )

            # 表单内部的 session_id 来自上面 chat tab 的 session_id_state
            # 这里给个独立 textbox 显示，但用户一般不动
            exp_reaction_input = gr.Textbox(
                label="反应 SMILES",
                placeholder="reactants>>products  e.g. C=Cc1ccccc1.[K+].[I-]>>OC(c1ccccc1)CI",
                interactive=True,
            )

            gr.Markdown("### ⚡ 电化学设置")
            with gr.Row():
                exp_anode = gr.Dropdown(
                    label="阳极 (Anode)",
                    choices=["carbon", "platinum", "sacrificial_magnesium",
                             "sacrificial_iron", "sacrificial_zinc", "sacrificial_aluminum",
                             "stainless_steel", "nickel", "copper", "silver", "gold",
                             "titanium", "tin", "lead", "other_electrode", "ABSENT"],
                    value="carbon", allow_custom_value=True,
                )
                exp_cathode = gr.Dropdown(
                    label="阴极 (Cathode)",
                    choices=["platinum", "carbon", "nickel", "stainless_steel",
                             "sacrificial_iron", "copper", "silver", "tin", "lead",
                             "titanium", "ABSENT", "other_electrode"],
                    value="platinum", allow_custom_value=True,
                )
                exp_cell = gr.Dropdown(
                    label="池型 (Cell type)",
                    choices=["undivided", "divided", "flow", "ABSENT"],
                    value="undivided",
                )

            gr.Markdown("### 🔋 反应器参数")
            with gr.Row():
                exp_current_mA = gr.Number(label="电流 (mA)", value=10.0)
                exp_potential_V = gr.Number(label="电压 (V)", value=1.5)
                exp_temperature_C = gr.Number(label="温度 (°C)", value=25.0)
                exp_time_h = gr.Number(label="时间 (h)", value=4.0)

            gr.Markdown("### 📋 批量录入实验 (每行 = 一个实验)")
            gr.Markdown(
                "**填法**:\n"
                "- **共享字段**: 顶部 反应 SMILES + 阳极/阴极/池型 (本表所有行共用)\n"
                "- **每行物质**: 多组分用 `换行` / `,` / `;` 分隔. ⚠️ **不要用 `.`** (SMILES 里 `.` 是离子对/盐, 如 `[K+].[I-]` = KI 单一物质)\n"
                "- **每行用量**: 各物质类型有专门 equiv/M 列\n"
                "- **副产物**: 多个 SMILES 换行分隔, 占比 列也换行对齐 (第 1 行 vs 第 1 行)\n"
                "- **yield**: 留空 = 实验未做, 提交时跳过; 填 0-100 = 实测产率%\n"
                "- 点 **批量提交** 一次记录所有有 yield 的行\n"
            )

            # 隐藏 ▶ 兼容字段 (避免改 _form_inputs)
            exp_substances_df = gr.Dataframe(visible=False, value=[[""] * 4 for _ in range(1)])
            exp_yield = gr.Number(visible=False, value=None)
            exp_selectivity = gr.Textbox(visible=False, value='')
            exp_notes = gr.Textbox(visible=False, value='')
            exp_side_products_df = gr.Dataframe(visible=False, value=[[""] * 4])

            # ════════ 批量录入实验 dataframe (主表单, 默认显示) ═══════════════
            with gr.Group():
                exp_batch_df = gr.Dataframe(
                    headers=["电解质", "电解质 M",
                             "溶剂", "试剂",
                             "催化剂", "催化剂 equiv",
                             "配体", "添加剂",
                             "current_mA", "potential_V", "T_C", "time_h",
                             "yield %", "选择性",
                             "副产物 (SMILES, 换行分隔)", "副产物比例 (% 换行)",
                             "备注"],
                    datatype=["str", "number", "str", "str", "str", "number",
                              "str", "str", "number", "number", "number", "number",
                              "number", "str", "str", "str", "str"],
                    value=[[""] * 17 for _ in range(3)],
                    row_count=(3, "dynamic"),
                    interactive=True,
                    label="批量实验 (每行一个; 多组分换行分隔; 不需要留空)",
                    wrap=True,
                )
                with gr.Row():
                    exp_batch_submit_btn = gr.Button("📥 批量提交", variant="primary", size="lg")
                    exp_batch_prefill_btn = gr.Button("🎯 用模型 Top-3 预填", size="lg")
                    exp_batch_clear_btn = gr.Button("🗑️ 清空", size="lg")
                with gr.Row():
                    exp_bo_btn = gr.Button("🎲 BO 推荐下一轮", variant="secondary", size="lg")
                    exp_llm_btn = gr.Button("🤖 LLM 推荐下一轮", variant="secondary", size="lg")
                with gr.Row():
                    exp_export_btn = gr.Button("📤 导出 CSV", size="lg")
                    exp_push_chat_btn = gr.Button("💬 把当前表 push 到 Chat 分析 (最后一行)", size="lg")
                # 隐藏单次模式按钮 (兼容旧 wiring)
                exp_submit_btn = gr.Button(visible=False)
                exp_prefill_btn = gr.Button(visible=False)

            exp_csv_file = gr.File(label="导出文件", visible=False)

            gr.Markdown("### ⭐ 下一轮建议")
            with gr.Row():
                exp_bo_suggest = gr.Markdown(value="_(点 BO 按钮)_", elem_classes="tool-result-area")
                exp_llm_suggest = gr.Markdown(value="_(点 LLM 按钮)_", elem_classes="tool-result-area")

            gr.Markdown("### 📒 实验历史 (本 session)")
            exp_history_md = gr.Markdown(value=_format_experiments_table([]))
            exp_status = gr.Markdown(value="")

            # ── Wiring (handler 实现在外面)
            def _collect_form(reaction_smiles, anode, cathode, cell,
                              substances_df,
                              cur, vol, t, h,
                              yld, sel, notes,
                              side_products_df=None):
                """Pack form into a record dict.
                substances_df: list of rows [type, smiles, amount, unit] from gr.Dataframe.
                """
                # Parse substances dataframe
                solvents, reagents, ligands, additives, catalysts, electrolytes = [], [], [], [], [], []
                # Map dataframe (gr.Dataframe → pandas DataFrame or list of lists)
                rows_raw = substances_df
                if hasattr(rows_raw, 'values'):  # pandas DataFrame
                    rows = rows_raw.values.tolist()
                elif isinstance(rows_raw, list):
                    rows = rows_raw
                else:
                    rows = []
                for row in rows:
                    if not row or len(row) < 4: continue
                    typ, smi, amt, unit = (str(row[0] or '').strip(), str(row[1] or '').strip(),
                                            row[2], str(row[3] or '').strip())
                    if not smi or smi.lower() in ('', 'nan', 'none'): continue
                    try:
                        amt = float(amt) if amt not in (None, '', 'nan') else 0.0
                    except Exception:
                        amt = 0.0
                    if amt <= 0: continue   # 用量 0 跳过
                    entry = {'smiles': smi, 'amount': amt, 'unit': unit}
                    if '溶剂' in typ or typ.lower() == 'solvent':
                        solvents.append(entry)
                    elif '电解质' in typ or 'electroly' in typ.lower():
                        electrolytes.append(entry)
                    elif '试剂' in typ or typ.lower() == 'reagent':
                        reagents.append(entry)
                    elif '催化' in typ or 'catalyst' in typ.lower():
                        catalysts.append(entry)
                    elif '配体' in typ or 'ligand' in typ.lower():
                        ligands.append(entry)
                    elif '添加剂' in typ or 'additive' in typ.lower():
                        additives.append(entry)
                # Parse side products
                side_products = []
                sp_raw = side_products_df
                if hasattr(sp_raw, 'values'):
                    sp_rows = sp_raw.values.tolist()
                elif isinstance(sp_raw, list):
                    sp_rows = sp_raw
                else:
                    sp_rows = []
                for row in sp_rows:
                    if not row or len(row) < 4: continue
                    smi, pct, typ, sp_notes = (str(row[0] or '').strip(), row[1],
                                                str(row[2] or '').strip(), str(row[3] or '').strip())
                    if not smi or smi.lower() in ('', 'nan', 'none'): continue
                    try:
                        pct = float(pct) if pct not in (None, '', 'nan') else 0.0
                    except Exception:
                        pct = 0.0
                    if pct <= 0: continue
                    side_products.append({'smiles': smi, 'percent': pct,
                                           'type': typ, 'notes': sp_notes})

                # 简化 top-1 字段保留向后兼容 (csv, history)
                first_smi = lambda lst: (lst[0]['smiles'] if lst else '')
                return {
                    'reaction_smiles': (reaction_smiles or '').strip(),
                    'anode': anode or '', 'cathode': cathode or '', 'cell_type': cell or '',
                    'electrolytes': electrolytes,
                    'solvents_full': solvents,
                    'reagents_full': reagents,
                    'catalysts': catalysts,
                    'ligands': ligands,
                    'additives': additives,
                    'side_products': side_products,
                    # 向后兼容 CSV 顶层简化
                    'electrolyte': first_smi(electrolytes),
                    'electrolyte_M': (electrolytes[0]['amount'] if electrolytes else 0),
                    'solvents': [s['smiles'] for s in solvents],
                    'reagents': [r['smiles'] for r in reagents],
                    'catalyst': first_smi(catalysts),
                    'catalyst_equiv': (catalysts[0]['amount'] if catalysts else 0),
                    'reagent_equiv': (reagents[0]['amount'] if reagents else 0),
                    'ligand': first_smi(ligands),
                    'additive': first_smi(additives),
                    'current_mA': cur, 'potential_V': vol,
                    'temperature_C': t, 'time_h': h,
                    'observed_yield': yld, 'selectivity': sel or '',
                    'notes': notes or '',
                    'side_products_summary': '; '.join(
                        f"{sp['smiles']}({sp['percent']}% {sp['type']})"
                        for sp in side_products) if side_products else '',
                }

            def _exp_submit(sid, *fields):
                if not sid:
                    return "_(没有 session_id, 刷新页面重试)_", _format_experiments_table([])
                rec = _collect_form(*fields)
                if not rec.get('reaction_smiles'):
                    return "**错误**: 必须填反应 SMILES", _format_experiments_table(_load_experiments(sid))
                exps = _add_experiment(sid, rec)
                return (f"✅ 已记录第 #{len(exps)} 个实验 → `{_experiments_path(sid)}`",
                        _format_experiments_table(exps))

            def _exp_prefill_from_stage1(reaction_smiles):
                """Call Stage-1 + Stage-2, populate form fields with model's top-1 recommendations."""
                if not reaction_smiles or not reaction_smiles.strip():
                    return [gr.update()] * 9 + ["**错误**: 请先填反应 SMILES"]
                _ensure_globals()
                try:
                    r = _tool_executor.execute('recommend_conditions_default',
                                                {'reaction_smiles': reaction_smiles.strip(), 'top_k': 1})
                    d = json.loads(r)
                    rec = d.get('recommendations', {})
                    pred_sets = d.get('predicted_sets', {})
                    amts = d.get('amounts', {})
                    def top(h):
                        items = rec.get(h, [])
                        return items[0].get('label', '') if items else ''
                    # Build substance dataframe rows
                    rows = []
                    # 电解质 (V3 推荐是 cation-anion 字串, 需要拼成 SMILES — 简化: 取 cation/anion 单独显示)
                    elec_lbl = top('electrolyte') or ''  # e.g. "NEt4-BF4"
                    rows.append(["电解质", elec_lbl, amts.get('electrolyte_M', 0.1), "M"])
                    # 溶剂 (从 predicted_sets 拿)
                    for s in pred_sets.get('solvent', []) or []:
                        rows.append(["溶剂", s.get('smiles', ''), 1.0, "比例"])
                    if not pred_sets.get('solvent'):
                        rows.append(["溶剂", "", 0.0, "比例"])
                    # 试剂
                    for r2 in pred_sets.get('reagent', []) or []:
                        rows.append(["试剂", r2.get('smiles', ''), amts.get('reagent_equiv', 1.5), "equiv"])
                    if not pred_sets.get('reagent'):
                        rows.append(["试剂", "", 0.0, "equiv"])
                    # 催化剂
                    for c in pred_sets.get('catalyst', []) or []:
                        rows.append(["催化剂", c.get('smiles', ''), amts.get('catalyst_equiv', 0.1), "equiv"])
                    if not pred_sets.get('catalyst'):
                        rows.append(["催化剂", "", 0.0, "equiv"])
                    # 配体
                    lig = top('ligand')
                    if lig and lig != 'ABSENT':
                        rows.append(["配体", lig, amts.get('ligand_equiv', 0.1), "equiv"])
                    # 添加剂
                    addv = top('additive')
                    if addv and addv != 'ABSENT':
                        rows.append(["添加剂", addv, amts.get('additive_equiv', 1.0), "equiv"])
                    return [
                        gr.update(value=top('anode')),
                        gr.update(value=top('cathode')),
                        gr.update(value=top('cell_type')),
                        gr.update(value=rows),                                       # substances_df
                        gr.update(value=amts.get('current_mA', 10.0)),
                        gr.update(value=amts.get('potential_V', 1.5)),
                        gr.update(value=amts.get('temperature_C', 25.0)),
                        gr.update(value=amts.get('time_h', 4.0)),
                        "✅ 已预填模型推荐 (yield/notes 需手填; 用量 0 表示不用)",
                    ]
                except Exception as e:
                    return [gr.update()] * 8 + [f"**错误**: {type(e).__name__}: {e}"]

            def _exp_bo_suggest(sid, reaction_smiles):
                if not sid: return "_(无 session_id)_"
                return _bo_suggest_next(sid, reaction_smiles)

            def _exp_llm_suggest(sid, reaction_smiles, api_key, base_url, model_name):
                if not sid: return "_(无 session_id)_"
                return _llm_suggest_next(sid, reaction_smiles, api_key, base_url, model_name)

            def _exp_export_csv(sid):
                if not sid: return gr.update(visible=False), "_(无 session_id)_"
                p = _experiments_to_csv(sid)
                if not p:
                    return gr.update(visible=False), "_(没有实验记录可导出)_"
                return gr.update(value=p, visible=True), f"✅ 导出: {p}"

            def _exp_push_to_chat(sid, chat_history, agent_state_val,
                                   api_key, base_url, model_name, device, temperature, backend,
                                   debate_enabled, recommender_b_model, judge_model,
                                   rxn, anode, cathode, cell, batch_df):
                """Push the most recent batch row (with yield) to chat for agent analysis."""
                if not (rxn or '').strip():
                    return chat_history, agent_state_val, "**错误**: 先填顶部反应 SMILES"
                rows = batch_df.values.tolist() if hasattr(batch_df, 'values') else (batch_df or [])
                # Pick the last row with non-empty yield
                row = None
                for r in rows[::-1]:
                    if r and len(r) >= 13:
                        try:
                            if float(r[12]) is not None:
                                row = r; break
                        except Exception:
                            pass
                if row is None:
                    return chat_history, agent_state_val, "**错误**: 批量表里没有带 yield 的行可 push"
                elec, _, solvs, reags, cat, _, lig, addv, cur, vol, tc, th, yld, sel, sp_smis, sp_pcts, notes = row[:17]
                sp_part = f", 副产物={sp_smis} 比例={sp_pcts}" if sp_smis else ""
                msg = (f"实验反馈: 反应 `{rxn.strip()}` 用 anode={anode}, cathode={cathode}, "
                       f"cell={cell}, electrolyte={elec}, solvents={solvs}, "
                       f"reagent={reags}, catalyst={cat}, ligand={lig}, additive={addv}, "
                       f"current={cur}mA, V={vol}V, T={tc}°C, t={th}h, "
                       f"实际 yield = {yld}%, 选择性={sel or '?'}{sp_part}. "
                       f"备注: {notes or '无'}. "
                       f"请帮我分析为什么 yield 是这样, 并基于历史给下一轮建议.")
                try:
                    new_history, new_agent_state, _ = agent_chat_fn(
                        msg, chat_history, agent_state_val,
                        api_key, base_url, model_name, device, temperature, backend,
                        debate_enabled, recommender_b_model, judge_model,
                    )
                    return new_history, new_agent_state, "✅ 已 push 到 Chat 并跑 agent (切到 Chat tab 看回复)"
                except Exception as e:
                    fallback = list(chat_history or []) + [
                        {"role": "user", "content": msg},
                        {"role": "assistant", "content": f"_(agent 失败: {type(e).__name__}: {e})_"}
                    ]
                    return fallback, agent_state_val, f"⚠️ Agent 调用失败: {e}"

            # ── 批量提交 handler ──────────────────
            def _exp_batch_submit(sid, rxn, anode, cathode, cell, batch_df):
                """Submit N rows of batch experiment at once."""
                if not sid:
                    return "_(无 session_id)_", _format_experiments_table([])
                if not (rxn or '').strip():
                    return "**错误**: 请先填顶部反应 SMILES", _format_experiments_table(_load_experiments(sid))
                rows = batch_df.values.tolist() if hasattr(batch_df, 'values') else (batch_df or [])
                added = 0; skipped = 0
                for row in rows:
                    if not row or len(row) < 17: continue
                    (elec, elec_M, solvs, reags, cat, cat_eq, lig, addv,
                     cur, vol, tc, th, yld, sel,
                     sp_smis, sp_pcts, notes) = row[:17]
                    # 必须有 yield 才记录
                    try:
                        yld_v = float(yld) if yld not in (None, '', 'nan') else None
                    except Exception:
                        yld_v = None
                    if yld_v is None:
                        skipped += 1; continue
                    def _split(s):
                        """Split multi-component string by 换行 / `,` / `;` / `+` 仅.
                        ⚠️ 不用 `.` 拆分 (它在 SMILES 里表示离子对/混合物的一部分, 如 [K+].[I-] = KI 一个物质).
                        留空返回 []. 单个 SMILES 直接返回 1 元 list."""
                        if not s or str(s).lower() in ('nan', 'none'): return []
                        import re
                        parts = re.split(r'[\n,;+]+', str(s).strip())
                        return [p.strip() for p in parts if p.strip()]
                    solv_list = _split(solvs); reag_list = _split(reags)
                    def _num(x, dflt=0):
                        try: return float(x) if x not in (None, '', 'nan') else dflt
                        except: return dflt
                    # Parse side products
                    sp_smis_list = _split(sp_smis)
                    sp_pcts_list = _split(sp_pcts)
                    side_prods = []
                    for k, sm in enumerate(sp_smis_list):
                        pct = 0.0
                        if k < len(sp_pcts_list):
                            try: pct = float(sp_pcts_list[k])
                            except Exception: pct = 0.0
                        if pct > 0:
                            side_prods.append({'smiles': sm, 'percent': pct, 'type': '', 'notes': ''})

                    rec = {
                        'reaction_smiles': rxn.strip(),
                        'anode': anode, 'cathode': cathode, 'cell_type': cell,
                        'electrolyte': str(elec or ''), 'electrolyte_M': _num(elec_M, 0.1),
                        'solvents': solv_list,
                        'reagents': reag_list,
                        'catalyst': str(cat or ''), 'catalyst_equiv': _num(cat_eq, 0.1),
                        'ligand': str(lig or ''), 'additive': str(addv or ''),
                        'reagent_equiv': 1.0,  # 简化, 暂不支持每个试剂单独 equiv
                        'current_mA': _num(cur, 10),
                        'potential_V': _num(vol, 1.5),
                        'temperature_C': _num(tc, 25),
                        'time_h': _num(th, 4),
                        'observed_yield': yld_v,
                        'selectivity': str(sel or ''),
                        'side_products': side_prods,
                        'side_products_summary': '; '.join(
                            f"{sp['smiles']}({sp['percent']}%)" for sp in side_prods),
                        'notes': str(notes or ''),
                    }
                    _add_experiment(sid, rec)
                    added += 1
                exps = _load_experiments(sid)
                msg = f"✅ 批量记录: {added} 个 (跳过 {skipped} 个无 yield 行); 累计 {len(exps)} 个"
                return msg, _format_experiments_table(exps)

            def _exp_batch_prefill(rxn):
                """Fill batch dataframe with model Top-3 predictions (3 alternative configs)."""
                if not (rxn or '').strip():
                    return [[""] * 17 for _ in range(3)], "**错误**: 请先填反应 SMILES"
                _ensure_globals()
                try:
                    r = _tool_executor.execute('recommend_conditions_default',
                                                {'reaction_smiles': rxn.strip(), 'top_k': 3})
                    d = json.loads(r)
                    rec = d.get('recommendations', {})
                    pred_sets = d.get('predicted_sets', {})
                    amts = d.get('amounts', {})
                    # 3 行: 每行用 Top-i 物质 (Top-1, Top-2, Top-3) 作 alternative
                    rows = []
                    def get(h, i):
                        items = rec.get(h, [])
                        return items[i].get('label', '') if i < len(items) else ''
                    def get_smi(h, i):
                        items = rec.get(h, [])
                        return items[i].get('smiles') or items[i].get('label', '') if i < len(items) else ''
                    for i in range(3):
                        solvs_full = pred_sets.get('solvent', []) if i == 0 else []
                        solv_str = '\n'.join(s.get('smiles', '') for s in solvs_full) if solvs_full else get_smi('solvent', i)
                        reags_full = pred_sets.get('reagent', []) if i == 0 else []
                        reag_str = '\n'.join(s.get('smiles', '') for s in reags_full) if reags_full else get_smi('reagent', i)
                        rows.append([
                            get('electrolyte', i),
                            amts.get('electrolyte_M', 0.1),
                            solv_str,
                            reag_str,
                            get_smi('catalyst', i),
                            amts.get('catalyst_equiv', 0.1),
                            get('ligand', 0) if get('ligand', 0) != 'ABSENT' else '',
                            get('additive', 0) if get('additive', 0) != 'ABSENT' else '',
                            amts.get('current_mA', 10),
                            amts.get('potential_V', 1.5),
                            amts.get('temperature_C', 25),
                            amts.get('time_h', 4),
                            '',  # yield 留空让用户填
                            '',  # 选择性
                            f'模型 Top-{i+1} 推荐' if i > 0 else 'predicted_sets 主推',
                        ])
                    return rows, f"✅ 已用模型 Top-3 预填 3 行; yield 列留空, 实验后回填再批量提交"
                except Exception as e:
                    return [[""] * 15 for _ in range(3)], f"**错误**: {type(e).__name__}: {e}"

            def _exp_batch_clear():
                return [[""] * 15 for _ in range(3)], "已清空批量录入区"

            # form inputs in order matching _collect_form
            _form_inputs = [exp_reaction_input, exp_anode, exp_cathode, exp_cell,
                            exp_substances_df,
                            exp_current_mA, exp_potential_V, exp_temperature_C, exp_time_h,
                            exp_yield, exp_selectivity, exp_notes,
                            exp_side_products_df]

            # 批量提交 wiring
            exp_batch_submit_btn.click(
                fn=_exp_batch_submit,
                inputs=[session_id_state, exp_reaction_input, exp_anode, exp_cathode, exp_cell,
                        exp_batch_df],
                outputs=[exp_status, exp_history_md],
            )
            exp_batch_prefill_btn.click(
                fn=_exp_batch_prefill,
                inputs=[exp_reaction_input],
                outputs=[exp_batch_df, exp_status],
            )
            exp_batch_clear_btn.click(
                fn=_exp_batch_clear,
                outputs=[exp_batch_df, exp_status],
            )

            exp_submit_btn.click(
                fn=_exp_submit,
                inputs=[session_id_state] + _form_inputs,
                outputs=[exp_status, exp_history_md],
            )
            exp_prefill_btn.click(
                fn=_exp_prefill_from_stage1,
                inputs=[exp_reaction_input],
                outputs=[exp_anode, exp_cathode, exp_cell, exp_substances_df,
                         exp_current_mA, exp_potential_V, exp_temperature_C, exp_time_h,
                         exp_status],
            )
            exp_bo_btn.click(
                fn=_exp_bo_suggest,
                inputs=[session_id_state, exp_reaction_input],
                outputs=[exp_bo_suggest],
            )
            exp_llm_btn.click(
                fn=_exp_llm_suggest,
                inputs=[session_id_state, exp_reaction_input,
                        api_key_input, base_url_input, model_input],
                outputs=[exp_llm_suggest],
            )
            exp_export_btn.click(
                fn=_exp_export_csv,
                inputs=[session_id_state],
                outputs=[exp_csv_file, exp_status],
            )
            exp_push_chat_btn.click(
                fn=_exp_push_to_chat,
                inputs=[session_id_state, chatbot, agent_state,
                        api_key_input, base_url_input, model_input, device_input,
                        temperature_input, backend_input,
                        debate_checkbox, recommender_b_model_input, judge_model_input,
                        exp_reaction_input, exp_anode, exp_cathode, exp_cell, exp_batch_df],
                outputs=[chatbot, agent_state, exp_status],
            )

            # 切换到这个 tab 时自动加载历史
            def _refresh_exp_history(sid):
                return _format_experiments_table(_load_experiments(sid)) if sid else "_(无 session_id)_"
            # demo.load 已经设置 session_id, 不需要重复

        # ── Enhanced Footer ───────────────────────────────────
        gr.HTML(
            '<div class="app-footer">'
            '  <div class="footer-tech">'
            "    <span>LLM ReAct</span>"
            "    <span>PyTorch</span>"
            "    <span>RDKit</span>"
            "    <span>FAISS</span>"
            "    <span>Bayesian Opt</span>"
            "    <span>Gradio</span>"
            "  </div>"
            "  Electrochemical Condition Agent &mdash; AI-driven reaction optimization"
            "</div>"
        )

        # ── Auto-restore session on page load ─────────────────
        # Uses Gradio session_hash as browser-tab-unique session id.
        # If user reloads the same tab, prior chat history is restored.
        app.load(
            fn=_restore_session_on_load,
            inputs=None,
            outputs=[chatbot, agent_state, session_id_state],
        )

    return app


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════

def main():
    global _device

    parser = argparse.ArgumentParser(
        description="Gradio Web UI for Electrochemical Condition Agent"
    )
    parser.add_argument("--port", type=int, default=7880)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"])
    parser.add_argument("--share", action="store_true",
                        help="Create a public Gradio link")
    args = parser.parse_args()

    _device = args.device

    # When vLLM is using all GPUs, force local ML tools to CPU
    if _device == "cuda":
        try:
            import urllib.request
            with urllib.request.urlopen("http://localhost:8000/v1/models", timeout=2):
                print("NOTE: Local vLLM detected — forcing local ML tools to CPU to avoid GPU OOM.",
                      flush=True)
                _device = "cpu"
        except Exception:
            pass

    app = build_app()
    app.queue()
    app.launch(
        server_name=args.host,
        server_port=args.port,
        share=args.share,
        ssr_mode=False,
        theme=APP_THEME,
        css=CUSTOM_CSS,
        js=DARK_MODE_INIT_JS,
    )


if __name__ == "__main__":
    main()
