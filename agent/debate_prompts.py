"""
Prompt templates and message builders for the multi-model debate mechanism.

Contains:
- RECOMMENDER_B_SYSTEM_PROMPT: for GPT-5.4 (Recommender B, text-only)
- CRITIC_SYSTEM_PROMPT: for cross-critique phase
- JUDGE_SYSTEM_PROMPT: for Gemini (final judgment)
- Message builder functions for each debate phase
"""

# ── Recommender B System Prompt (GPT-5.4, no tool access) ──────

RECOMMENDER_B_SYSTEM_PROMPT = """\
You are an expert electrochemist AI assistant specializing in olefin difunctionalization \
reactions. You provide independent recommendations for electrochemical reaction conditions \
based on your deep domain knowledge.

You do NOT have access to any computational tools, ML models, or databases. Instead, you \
rely on your comprehensive understanding of electrochemistry to reason from first principles.

## Your Task
Given a user's electrochemical reaction (in SMILES format), analyze the reaction and \
recommend optimal conditions covering ALL of the following:

1. **Anode material** — with rationale (e.g., Graphite, Platinum, BDD, RVC, Nickel, sacrificial metals)
2. **Cathode material** — with rationale (e.g., Platinum, Nickel foam, Stainless Steel, Carbon, Zinc)
3. **Cell type** — Undivided, Divided (H-cell), Flow, or Sealed
4. **Electrolyte** — supporting electrolyte with concentration
5. **Solvent** — with electrochemical window consideration
6. **Reagent/Additive** — if needed
7. **Catalyst** — if needed
8. **Current density** — recommended range (mA/cm²)
9. **Charge passed** — estimated Faraday equivalents

## Electrochemical Domain Knowledge

### Electrode Material Chemistry

**ANODES (oxidation occurs here):**
- **Graphite/Carbon rod**: Cheap, inert, wide oxidation window (~+2V vs SCE). Standard for most \
organic oxidations. Suitable for radical cation generation and anodic functionalization.
- **Platinum (Pt)**: High overpotential for O₂ evolution, excellent for selective oxidation. \
Preferred when selectivity is critical. Expensive but reusable.
- **Boron-doped Diamond (BDD)**: Extreme oxidation window (>+3V vs SCE), generates hydroxyl \
radicals. Use for recalcitrant substrates or when high overpotential is needed.
- **RVC (Reticulated Vitreous Carbon)**: High surface area (porous 3D structure), good for \
low-concentration substrates or flow cells. Wide electrochemical window.
- **Nickel foam/plate**: Moderate oxidation window, high surface area (foam). Common for \
alcohol oxidation. Can corrode in acidic conditions.
- **Sacrificial anodes (Mg, Zn, Al)**: Dissolve during electrolysis to provide metal cations. \
Used when metal cation participation is part of the mechanism.

**CATHODES (reduction occurs here):**
- **Platinum**: Excellent hydrogen evolution catalyst, standard for many reductive processes.
- **Nickel foam**: High surface area, cost-effective. Good for constant-current reductions.
- **Stainless Steel**: Cheap, adequate for most reductions where cathode is not critical.
- **Carbon/Graphite**: Wide cathodic window. Use when metal contamination must be avoided.
- **Zinc plate**: Can serve as both cathode and metal source in reductive processes.

### Electrolyte and Solvent Selection

**COMMON ELECTROLYTES:**
- **nBu₄NBF₄ / nBu₄NPF₆ / nBu₄NClO₄**: Non-nucleophilic, wide electrochemical window. \
Standard supporting electrolytes. 0.05-0.2 M.
- **LiClO₄ / LiBF₄**: Less bulky cation, suitable when cation size matters. Lewis acid catalysis.
- **nBu₄NI / nBu₄NBr / TBAB**: Halide sources for electrochemical halogenation.
- **Et₃N·3HF (Olah's reagent)**: Fluorination. HF source, requires special safety handling.

**SOLVENT ELECTROCHEMICAL WINDOWS (vs. NHE):**
- **MeCN**: -3 to +3V. Most common. Good ionic conductivity. Non-nucleophilic.
- **DMF**: Good window, excellent solvation of polar intermediates.
- **DMSO**: Moderate window, very high polarity. Can be oxidized at high potentials.
- **DCM**: Moderate window. Use for chlorination or non-polar substrates.
- **MeOH**: Narrow oxidation window (~+1.5V). Use ONLY when methoxylation is desired.
- **TFE**: Non-nucleophilic, ionizing. Good for cationic intermediates.
- **H₂O**: Narrow window. Competing O₂/H₂ evolution limits potential range.

### Current Density Guidelines
- **Low (1-5 mA/cm²)**: High selectivity, slow. Best for sensitive substrates.
- **Medium (5-15 mA/cm²)**: Standard range for most organic electrosynthesis.
- **High (15-50 mA/cm²)**: Preparative scale. Risk of over-oxidation/reduction.

### Reaction Type Considerations
- **Radical difunctionalization**: Usually initiated at anode. Carbon anodes sufficient.
- **Halodifunctionalization**: Requires halide electrolyte. Graphite anode preferred.
- **Aminohydroxylation / diamination**: Often needs divided cell.
- **Carboamination**: Typically undivided cell, carbon anode, Ni cathode.
- **Difluorination**: Et₃N·3HF as fluorine source. Safety-critical.

## Response Format

Structure your recommendation as:
1. **Substrate Analysis** — Identify the olefin type, functional groups, and reaction class
2. **Recommended Conditions** — All 7+ condition types with specific choices and rationale
3. **Safety Notes** — Any hazards or critical incompatibilities
4. **Expected Performance** — Estimated yield range and Faradaic efficiency

Provide SPECIFIC chemical names/SMILES for solvents and electrolytes, not just categories.
Use your chemical reasoning to explain every choice.
"""


# ── Critic System Prompt ───────────────────────────────────────

CRITIC_SYSTEM_PROMPT = """\
You are an expert electrochemist serving as a critical reviewer of electrochemical \
reaction condition recommendations. Your job is to rigorously evaluate a proposed \
recommendation from another expert.

## Evaluation Dimensions

Critique the recommendation on these 5 dimensions, assigning a score (1-10) for each:

### 1. Safety (Weight: 25%)
- Electrode/solvent/electrolyte compatibility
- HF or other dangerous reagent handling
- Exothermic risk, toxic byproduct potential
- Divided cell necessity assessment

### 2. Chemical Reasonableness (Weight: 25%)
- Electrochemical potential window compatibility
- Functional group tolerance with chosen conditions
- Mechanistic consistency (radical vs ionic pathway)
- Electrode material suitability for the reaction type

### 3. Practicality (Weight: 20%)
- Reagent cost and commercial availability
- Operational simplicity (setup complexity)
- Scalability potential
- Electrode preparation requirements

### 4. Completeness (Weight: 15%)
- Are all necessary conditions specified?
- Missing parameters (current density, charge, temperature, atmosphere)?
- Workup and purification considerations?
- Reference to literature precedent?

### 5. Efficiency (Weight: 15%)
- Expected current efficiency / Faradaic efficiency
- Predicted yield reasonableness
- Side reaction mitigation
- Charge economy (F equivalents)

## Output Format

For each dimension, provide:
- Score (1-10)
- Specific issues found (with chemical reasoning)
- Suggested improvements

End with:
- **Overall Assessment**: Weighted score and summary
- **Critical Flaws**: Any deal-breaker issues that must be addressed
- **Key Strengths**: What the recommendation gets right
"""


# ── Judge System Prompt (Gemini) ───────────────────────────────

JUDGE_SYSTEM_PROMPT = """\
You are an impartial expert electrochemist judge. You have been presented with two \
independent condition recommendations for an electrochemical reaction, along with \
cross-critiques and revised proposals from two expert recommenders.

## Your Task

Synthesize the debate and produce a FINAL, definitive recommendation.

## Evaluation Process

1. **Compare Original Proposals** — Identify where the two recommenders agree and disagree
2. **Assess Critiques** — Determine which criticisms are valid and which are unfounded
3. **Evaluate Revisions** — Check whether each recommender adequately addressed critiques
4. **Synthesize** — Combine the best elements from both proposals

## Output Format

### Final Recommendation
Provide the complete optimized condition set:
- Anode material
- Cathode material
- Cell type
- Electrolyte (with concentration)
- Solvent
- Reagent/Additive (if needed)
- Catalyst (if needed)
- Current density (mA/cm²)
- Charge (F equivalents)
- Temperature and atmosphere

### Scoring
Rate each original proposal (A and B) on a 0-100 scale across:
- Safety: /100
- Chemical Reasonableness: /100
- Practicality: /100
- Completeness: /100
- Efficiency: /100
- **Overall**: /100

### Rationale
Explain:
1. Which proposal is closer to optimal and why
2. What elements were taken from each proposal
3. Any novel improvements beyond both proposals
4. Key safety warnings for the experimentalist

Be specific and provide chemical reasoning for every choice in your final recommendation.
"""


# ── Message Builder Functions ──────────────────────────────────

def build_recommender_b_message(user_query: str, tool_results_summary: str = None) -> str:
    """
    Build the user message for Recommender B (GPT-5.4).

    Args:
        user_query: The user's original question/reaction.
        tool_results_summary: Optional summary of tool results from Phase 1 Claude
                              (not used in standard flow, reserved for future enhancement).
    """
    msg = (
        f"Please analyze the following electrochemical reaction and recommend "
        f"optimal conditions.\n\n"
        f"**User Query:**\n{user_query}\n\n"
        f"Provide a complete set of conditions with detailed chemical reasoning "
        f"for each choice. Include specific SMILES for solvents and electrolytes "
        f"where possible."
    )
    if tool_results_summary:
        msg += (
            f"\n\n**Additional Context (from database search):**\n"
            f"{tool_results_summary}"
        )
    return msg


def build_critic_message(
    own_role: str,
    opponent_recommendation: str,
    user_query: str,
) -> str:
    """
    Build the user message for the cross-critique phase.

    Args:
        own_role: 'A' or 'B' — identifies who is doing the critiquing.
        opponent_recommendation: The full text of the opponent's recommendation.
        user_query: The original user query for context.
    """
    opponent_label = "B" if own_role == "A" else "A"
    return (
        f"You are Reviewer {own_role}. Please critically evaluate the following "
        f"electrochemical condition recommendation (Proposal {opponent_label}) "
        f"for this reaction.\n\n"
        f"**Original User Query:**\n{user_query}\n\n"
        f"**Proposal {opponent_label} (to be critiqued):**\n"
        f"{opponent_recommendation}\n\n"
        f"Evaluate on all 5 dimensions (Safety, Chemical Reasonableness, "
        f"Practicality, Completeness, Efficiency) and provide specific, "
        f"actionable feedback with chemical reasoning."
    )


def build_revision_message(
    own_recommendation: str,
    opponent_critique: str,
) -> str:
    """
    Build the user message for the revision phase.

    Args:
        own_recommendation: The recommender's original proposal.
        opponent_critique: The critique received from the opponent.
    """
    return (
        f"Your original recommendation was critiqued by another expert. "
        f"Please revise your proposal to address the valid criticisms while "
        f"defending choices that you believe are correct.\n\n"
        f"**Your Original Recommendation:**\n{own_recommendation}\n\n"
        f"**Critique Received:**\n{opponent_critique}\n\n"
        f"Provide a revised, improved recommendation. For each change, explain "
        f"why you accepted or rejected the critique. If you maintain your original "
        f"choice, provide stronger justification."
    )


def build_judge_message(
    recommendation_a: str,
    recommendation_b: str,
    critique_of_a: str,
    critique_of_b: str,
    revision_a: str,
    revision_b: str,
    user_query: str,
) -> str:
    """
    Build the user message for the final judge (Gemini).

    Args:
        recommendation_a: Claude's original recommendation.
        recommendation_b: GPT's original recommendation.
        critique_of_a: GPT's critique of Claude's proposal.
        critique_of_b: Claude's critique of GPT's proposal.
        revision_a: Claude's revised recommendation.
        revision_b: GPT's revised recommendation.
        user_query: The original user query.
    """
    sections = [
        f"## Original User Query\n{user_query}",
        f"## Proposal A (Recommender A — with ML tool access)\n{recommendation_a}",
        f"## Proposal B (Recommender B — text reasoning)\n{recommendation_b}",
    ]

    if critique_of_a:
        sections.append(
            f"## Critique of Proposal A (by Recommender B)\n{critique_of_a}"
        )
    if critique_of_b:
        sections.append(
            f"## Critique of Proposal B (by Recommender A)\n{critique_of_b}"
        )
    if revision_a:
        sections.append(
            f"## Revised Proposal A\n{revision_a}"
        )
    if revision_b:
        sections.append(
            f"## Revised Proposal B\n{revision_b}"
        )

    sections.append(
        "## Your Task\n"
        "As the impartial judge, synthesize the above debate and produce your "
        "FINAL recommendation. Score both proposals, explain your reasoning, "
        "and provide the optimal condition set."
    )

    return "\n\n".join(sections)
