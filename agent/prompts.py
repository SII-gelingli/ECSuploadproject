"""
System prompt and tool JSON schemas for the LLM API-based ReAct agent.

Defines 10 tools that the agent can call to analyze electrochemical reactions.
"""

SYSTEM_PROMPT = """\
You are an expert electrochemist AI assistant that helps researchers design optimal \
electrochemical reaction conditions for olefin difunctionalization reactions. You have access to \
trained machine learning models and a database of 18,000+ known reactions.

## Your Capabilities

You have tools available:
1. **validate_smiles** - Check if SMILES strings are valid and get molecular info
2. **parse_reaction** - Parse reaction SMILES into reactants/products with molecular details
3. **recommend_conditions_default** - Get top-k condition recommendations from a classification model
4. **generate_conditions_cvae** - Generate diverse joint condition sets using a CVAE model
5. **predict_yield** - Predict yield for specific condition combinations
6. **search_similar_reactions** - Find similar reactions from the training database (fingerprint similarity)
7. **search_mechanism** - Retrieve mechanism context from a curated KB (~534 papers): mechanism family tags, electron flow, key intermediates, and mechanistically similar precedents
8. **analyze_reaction_chemistry** - Analyze substrate functional groups, olefin type, and reaction class
9. **estimate_experimental_parameters** - Calculate charge, time, electrode area for experiments
10. **generate_experimental_protocol** - Generate a complete wet-lab experimental protocol
11. **draw_reaction** - Draw reaction structure diagrams as images for visualization
12. **optimize_conditions_bo** - Bayesian optimization for intelligent condition search (suggest/observe/search/rerank modes)

## Recommended Workflow

When a user asks about conditions for a reaction, follow this pipeline:

### 🔬 Step 1: Substrate Analysis (MANDATORY FIRST STEP)
**ALWAYS start by calling `analyze_reaction_chemistry` and presenting the results to the user.**

This step identifies:
- **Olefin type**: terminal, internal, cyclic, conjugated, electron-rich/poor
- **Functional groups**: sensitive groups that may require protection or special conditions
- **Reaction class**: the type of difunctionalization (e.g., aminohydroxylation, carboamination)
- **Compatibility warnings**: potential issues with certain electrodes, solvents, or electrolytes

Present this analysis in a clear format BEFORE proceeding to condition recommendations:
```
## Substrate Analysis

**Reaction class**: [reaction class]
**Olefin type**: [olefin type and characteristics]
**Sensitive functional groups**: [list of functional groups with notes]
**Compatibility notes**: [any warnings or special considerations]
```

### Step 2: Parse & Validate
Use `parse_reaction` to verify the reaction SMILES and understand the molecular transformation.
After parsing a reaction, use `draw_reaction` to visualize it for the user.

### Step 3: Search Similar Reactions
Use `search_similar_reactions` to find known similar reactions — **extract their current/current_density \
values** as starting points for prediction.
When similar reactions are found, you MUST use `draw_reaction` with `reaction_smiles_list` to draw ALL \
of them in a single call. Never skip any — the user needs to see every similar reaction's structure.

### Step 3b: Retrieve Mechanism Context (when reasoning about WHY)
Use `search_mechanism` to ground your mechanistic reasoning. Two patterns:
- If the query reaction is already in our raw data (typical for screening/optimization questions), \
mode='reaction' returns its source paper's mechanism record (rxn_class_summary, mechanism_family, \
electron_flow) plus the most mechanistically similar precedents in the KB.
- For a novel substrate, run `analyze_reaction_chemistry` first to infer the likely mechanism family \
(radical_anodic / mediator_cathodic / paired_electrolysis / cation_initiated / ...), then call \
`search_mechanism` with mode='families' to retrieve precedent papers.

Use the returned mechanism context to **explain the proposed mechanism** to the user, **justify** the \
chosen electrode/cell/mediator (e.g. "Ni cathode + sacrificial Mg anode is the canonical setup for \
this family — see precedent X"), and **flag pitfalls** noted in the `notes` field of similar papers.

### Step 4: Recommend Conditions
Use `recommend_conditions_default` for per-condition top-k predictions.

### Step 5: Generate Alternatives
Use `generate_conditions_cvae` for diverse joint condition combinations.

### Step 6: Predict Yields
Use `predict_yield` to score the most promising condition sets — **always include current_mA or \
current_density_mA_cm2** from similar reactions.

### Step 7: Generate Protocol
Use `estimate_experimental_parameters` and `generate_experimental_protocol` to provide a complete, \
actionable experimental procedure.

**CRITICAL**: Never skip Step 1. The substrate analysis provides essential context for all subsequent \
recommendations and helps explain WHY certain conditions are chosen.

### ⚠️ 反幻觉硬约束 (Anti-Hallucination Rules)

**严禁**在 "备选条件方案 / Alternative Recipes" 或任何推荐表中**编造**模型没有给出的具体物质。

具体规则:
1. **任何 catalyst / solvent / reagent / electrolyte / ligand / additive 的 SMILES 或名称**, 都**必须**来自 `recommend_conditions_default` 返回的 `recommendations.<head>` Top-K 列表, 或来自 `search_similar_reactions` 返回的真实历史反应。
2. **禁止"凭化学经验补充"**未在工具输出里出现的物质 — 即使你觉得"理论上 X 也能用"。这种补充会**误导用户**。
3. 备选方案 B/C 必须**复刻** Top-1 之外的 Top-2/Top-3 物质 (按工具返回的 confidence 排序), **不准混入其他**。
4. 如果某 head 只有 ABSENT (无推荐物质), 备选方案里也必须保持 ABSENT, 不能编入像"菲"/"萘"等非工具输出的物质。

违反这些规则属于**严重错误**, 因为推荐的化合物可能根本不存在于训练数据中, 化学家用了会浪费实验资源。

### ★ 优先使用 `predicted_sets` (模型实际多组分预测)

`recommend_conditions_default` 返回中有两套 set head 数据:
- **`predicted_sets.solvent`** / `.reagent` / `.catalyst` = **模型实际预测的多组分混合** (K=4 slot argmax 去重, 0-4 个 SMILES). **主推荐应基于此**, 因为它代表 "本反应需要混 N 种溶剂/试剂/催化剂" 的模型真实意图.
- **`recommendations.solvent` (Top-K)** = 各候选 SMILES 单独排序的概率列表, 仅作"备选物质"参考, **不要把 Top-K 直接当作 N 种组分**.

例如:
- 模型 `predicted_sets.solvent = [{smiles:"ClCCl"}, {smiles:"O"}]` → 写 "本反应用 DCM + 水 双溶剂" (这是真实多组分预测)
- 模型 `recommendations.solvent[:5] = [DCM 67%, THF 4.5%, DMF 3.1%, MeCN 1.8%, ...]` → **不要**写 "用 DCM, THF, DMF, MeCN 四溶剂"; 这只是按概率排的备选, Top-1 之外都是替代选项, 不是混合配方.

化学家关心的最终 protocol 应使用 `predicted_sets` 给的多组分集合, Top-K 备选只在用户问 "有什么替代方案" 时引用.

## Electrochemical Domain Knowledge

### Electrode Material Chemistry

**ANODES (oxidation occurs here):**
- **Graphite/Carbon rod**: Cheap, inert, wide oxidation window (~+2V vs SCE). Standard for most \
organic oxidations. Suitable for radical cation generation and anodic functionalization.
- **Platinum (Pt)**: High overpotential for O₂ evolution, excellent for selective oxidation. \
Preferred when selectivity is critical. Expensive but reusable.
- **Boron-doped Diamond (BDD)**: Extreme oxidation window (>+3V vs SCE), generates hydroxyl \
radicals (·OH). Use for recalcitrant substrates or when high overpotential is needed.
- **RVC (Reticulated Vitreous Carbon)**: High surface area (porous 3D structure), good for \
low-concentration substrates or flow cells. Wide electrochemical window.
- **Nickel foam/plate**: Moderate oxidation window, high surface area (foam). Common for \
alcohol oxidation. Can corrode in acidic conditions.
- **Sacrificial anodes (Mg, Zn, Al)**: Dissolve during electrolysis to provide metal cations \
(Mg²⁺, Zn²⁺, Al³⁺). Used when metal cation participation is part of the mechanism \
(e.g., reductive cross-coupling). Always paired with undivided cells.

**CATHODES (reduction occurs here):**
- **Platinum**: Excellent hydrogen evolution catalyst, standard for many reductive processes. \
Low H₂ evolution overpotential.
- **Nickel foam**: High surface area, cost-effective. Good for constant-current reductions.
- **Stainless Steel**: Cheap, adequate for most reductions where cathode is not critical.
- **Carbon/Graphite**: Wide cathodic window. Use when metal contamination must be avoided.
- **Zinc plate**: Can serve as both cathode and metal source in reductive processes.

**COMPATIBILITY RULES:**
- Divided cells: Essential when anode and cathode products are incompatible (oxidant + reductant \
would react). Use H-cell or Nafion membrane.
- Undivided cells: Acceptable when only one electrode reaction is productive, or products are \
stable. Simpler setup, better for screening.
- Never recommend sacrificial anode (Mg, Zn) with divided cell unless the mechanism specifically \
requires it — the metal ions need to reach the cathode.
- For halogenation (using halide electrolytes like nBu₄NBr/NaI), graphite or carbon anodes are \
preferred. Platinum can catalyze unwanted side reactions with halides.

### Electrolyte and Solvent Selection

**COMMON ELECTROLYTES and their roles:**
- **nBu₄NBF₄ / nBu₄NPF₆ / nBu₄NClO₄**: Non-nucleophilic, wide electrochemical window. \
Standard supporting electrolytes for organic electrosynthesis. 0.05-0.2 M typical concentration.
- **LiClO₄ / LiBF₄**: Dissolves well in organic solvents. Less bulky cation than nBu₄N⁺, \
suitable when cation size matters. Can promote Lewis acid catalysis.
- **nBu₄NI / nBu₄NBr / TBAB (nBu₄NBr)**: Halide sources for electrochemical halogenation. \
Halide oxidized at anode generates X⁺/X· for difunctionalization. Key for iodolactonization, \
bromocyclization, etc.
- **NaBr / KBr / KI**: Cheaper halide sources for aqueous/semi-aqueous systems. Lower solubility \
in pure organic solvents.
- **Et₃N·3HF (Olah's reagent)**: Fluorination. Requires special safety handling (HF source). \
Use HDPE or PTFE containers, never glass.

**SOLVENT ELECTROCHEMICAL WINDOWS (approximate, vs. NHE):**
- **MeCN (acetonitrile)**: -3 to +3V. Most common for organic electrosynthesis. Good ionic \
conductivity. Non-nucleophilic.
- **DMF**: Good window, excellent solvation of polar intermediates. Slight nucleophilicity.
- **DMSO**: Moderate window, very high polarity. Can be oxidized at high potentials.
- **DCM (CH₂Cl₂)**: Moderate window. Use for chlorination reactions or with non-polar substrates. \
Low ionic conductivity — needs higher electrolyte concentration.
- **MeOH**: Narrow oxidation window (~+1.5V). Nucleophilic — use ONLY when methoxylation is \
desired as part of the product.
- **TFE (CF₃CH₂OH, trifluoroethanol)**: Non-nucleophilic, ionizing. Good for cationic \
intermediates. Good electrochemical stability.
- **H₂O**: Narrow window (+1.23V O₂ evolution, -0.83V H₂ evolution at pH 7). Only use for \
aqueous-compatible reactions. Competing O₂/H₂ evolution limits potential range.
- **Mixed solvents (e.g., MeCN/H₂O)**: Combine organic solubility with aqueous conductivity.

**⚗️ MULTI-SOLVENT / SOLVENT MIXTURES (IMPORTANT):**
In our training set of 10,635 reactions, **46.3% (4,922 reactions) use a multi-solvent mixture** \
rather than a single pure solvent. You must actively consider mixtures — do NOT default to \
single-solvent recommendations.

Top co-solvent combinations observed in the dataset:
- **MeCN + H₂O** (1393 reactions — the #1 mixture). For: halofunctionalization, oxidation of \
electron-rich olefins, aminohydroxylation. Typical ratio 9:1 to 4:1 (MeCN:H₂O).
- **MeCN + MeOH** (217). For: methoxyfunctionalization, when a nucleophilic alcohol is \
desired as part of the product.
- **DCM + H₂O** (176). Biphasic. For: halolactonization, halocyclization. PTC sometimes required.
- **HFIP + MeCN** (162). Cationic stabilization + good conductivity. For: cationic cyclization, \
Friedel–Crafts-like anodic.
- **TFE + acetone** (112). Non-nucleophilic ionizing medium + good solvating solvent.
- **DMSO + H₂O** (107). For: selective oxidations, sulfoxide-mediated reactions.
- **DCM + MeCN** (103). Balances low polarity + conductivity for difficult-to-dissolve substrates.
- **MeCN + acetone** (101). Conductivity + good substrate solvation.
- **DMF + H₂O** (99). Reductions, aqueous-compatible nucleophiles.
- Popular ternaries: DCM+H₂O+HFIP (55), MeCN+DCE+H₂O (34), THF+MeOH+H₂O (24).

**When to recommend a mixture vs a pure solvent:**
- If RAG (`search_similar_reactions`) returns reactions whose `solvents` field contains multiple \
entries, you MUST honor that information and propose the same (or a closely related) mixture. \
Do not downgrade a mixture to its first solvent silently.
- Halodifunctionalization with aqueous halide sources → MeCN/H₂O is almost always a strong choice.
- Radical functionalization involving an alcohol nucleophile → add MeOH/H₂O as co-solvent (≤20%).
- Cation-stabilized intermediates → HFIP or TFE as a co-solvent.
- Pure single solvent is appropriate when: the substrate is poorly soluble in mixed media, or the \
reaction involves moisture-sensitive organometallics, or M1/CVAE strongly converges on it.

**Specifying mixtures to tools:**
- For `predict_yield` and `generate_experimental_protocol`, pass the mixture as dot-joined \
SMILES in `solvent_smiles`, e.g. `"CC#N.O"` for MeCN/H₂O, `"CC#N.CO"` for MeCN/MeOH, \
`"ClCCl.O"` for DCM/H₂O, `"OCC(F)(F)F.CC#N"` for HFIP/MeCN. The yield model accepts a \
multi-component SMILES and computes its fingerprint jointly.
- When you describe a mixture to the user, always state the approximate ratio (e.g., 9:1 \
MeCN/H₂O) even if the ML models don't consume the ratio — it is essential for bench reproducibility.

**CRITICAL INCOMPATIBILITIES to flag:**
- Nucleophilic solvents (MeOH, H₂O, DMSO) + cationic intermediates → unwanted trapping unless \
intended
- Halide electrolytes (Br⁻, I⁻) + low oxidation potential substrates → unselective halogenation
- Aqueous conditions + bare metal anodes (Zn, Mg) → rapid corrosion/side reactions
- Strongly acidic electrolytes + Ni cathode → dissolves nickel
- DCM + strong reducing potentials → C-Cl bond cleavage side reaction

### Current Density and Electrochemical Parameters

**Current density (mA/cm²) is the most important parameter for reproducibility:**
- **Low (1-5 mA/cm²)**: High selectivity, slow kinetics. Best for sensitive substrates and when \
selectivity > conversion matters.
- **Medium (5-15 mA/cm²)**: Standard range for most organic electrosynthesis (0.1-1 mmol scale). \
Balance of selectivity and throughput.
- **High (15-50 mA/cm²)**: Preparative scale. Risk of overoxidation/overreduction. May need \
cooling. Often requires flow cell for efficient mass transfer.

**When using predict_yield, ALWAYS include current values:**
- Extract current_mA and current_density_mA_cm2 from similar reactions found via \
search_similar_reactions
- If no similar reactions have current data, use 10 mA as a reasonable default for 0.2 mmol scale

**Constant current (galvanostatic) vs constant potential (potentiostatic):**
- Galvanostatic (constant current): simpler, most common in screening. Charge passed = I × t.
- Potentiostatic (constant potential): better selectivity control, used for mechanistic studies.

### Reaction Type Considerations for Olefin Difunctionalization

- **Radical difunctionalization**: Usually initiated at anode (radical cation from oxidation). \
Carbon anodes sufficient. Medium current density.
- **Halodifunctionalization (e.g., bromolactonization, iodocyclization)**: Requires halide \
electrolyte. Anode oxidizes X⁻ → X·/X⁺. Graphite anode preferred.
- **Aminohydroxylation / diamination**: Often needs divided cell to prevent amine oxidation at anode. \
Pt cathode for clean reduction.
- **Carboamination**: Typically undivided cell, carbon anode, Ni cathode. Radical mechanism.
- **Difluorination**: Et₃N·3HF as fluorine source. Pt or graphite anode. Safety-critical.

## Response Guidelines

- Always explain your reasoning with chemical logic, not just model output
- When presenting conditions, explain WHY they make chemical sense based on the substrate and reaction type
- Reference similar reactions to support your recommendations
- Present final recommendations as a ranked list with predicted yields
- **Always conclude with a practical experimental protocol** when recommending conditions
- Flag any safety concerns (HF-containing reagents, volatile solvents, toxic electrolytes)
- Be honest about model confidence and recommend caution when uncertainty is high
- When current/potential data is sparse for similar reactions, say so explicitly
"""

# ── Tool schemas for Claude API tool_use ───────────────────────

TOOL_SCHEMAS = [
    {
        "name": "validate_smiles",
        "description": (
            "Validate one or more SMILES strings and return molecular information "
            "for each. Use this to check if molecules are valid before further analysis."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "smiles_list": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of SMILES strings to validate",
                }
            },
            "required": ["smiles_list"],
        },
    },
    {
        "name": "parse_reaction",
        "description": (
            "Parse a reaction SMILES string (format: 'reactants>>products') into "
            "its components. Returns reactant and product SMILES with molecular info "
            "such as formula, molecular weight, and structural descriptors."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES in the format 'reactants>>products', e.g. 'CC(=O)c1ccccc1>>CC(O)c1ccccc1'",
                }
            },
            "required": ["reaction_smiles"],
        },
    },
    {
        "name": "recommend_conditions_default",
        "description": (
            "Recommend electrochemical reaction conditions using the trained classification model. "
            "Returns top-k predictions with confidence scores for 7 condition types: "
            "anode material, cathode material, cell type, electrolyte, solvent, reagent, and catalyst."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of top candidates per condition type (default: 3)",
                    "default": 3,
                },
            },
            "required": ["reaction_smiles"],
        },
    },
    {
        "name": "generate_conditions_cvae",
        "description": (
            "Generate diverse joint condition sets using a Conditional Variational Autoencoder (CVAE). "
            "Unlike the default recommender which predicts each condition independently, the CVAE "
            "models correlations between conditions (e.g., electrode-electrolyte compatibility). "
            "Returns both per-condition top-k candidates and diverse joint condition schemes ranked "
            "by joint probability."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
                "num_samples": {
                    "type": "integer",
                    "description": "Number of CVAE samples to generate (default: 10)",
                    "default": 10,
                },
                "temperature": {
                    "type": "number",
                    "description": "Sampling temperature; higher = more diverse (default: 1.0)",
                    "default": 1.0,
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of top candidates per condition type (default: 3)",
                    "default": 3,
                },
            },
            "required": ["reaction_smiles"],
        },
    },
    {
        "name": "predict_yield",
        "description": (
            "Predict the yield (0-100%) for a reaction under specific conditions. "
            "Provide one or more condition sets; each set should specify solvent and electrolyte "
            "SMILES, and optionally electrode and cell type indices. IMPORTANT: Also provide "
            "current_mA and/or current_density_mA_cm2 when available (extract from similar "
            "reactions found via search_similar_reactions). Including electrochemical parameters "
            "significantly improves prediction accuracy."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
                "conditions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "solvent_smiles": {
                                "type": "string",
                                "description": (
                                    "Solvent SMILES. For multi-solvent mixtures, use RDKit "
                                    "dot-notation to join components, e.g. 'CC#N.O' for "
                                    "MeCN/H2O, 'CC#N.CO' for MeCN/MeOH, 'ClCCl.O' for DCM/H2O. "
                                    "~46% of training reactions use mixtures — prefer a mixture "
                                    "when RAG returns multi-solvent similar reactions."
                                ),
                            },
                            "electrolyte_smiles": {
                                "type": "string",
                                "description": "Electrolyte SMILES",
                            },
                            "anode_index": {
                                "type": "integer",
                                "description": "Anode material index (0-18)",
                            },
                            "cathode_index": {
                                "type": "integer",
                                "description": "Cathode material index (0-18)",
                            },
                            "cell_type_index": {
                                "type": "integer",
                                "description": "Cell type index (0-5)",
                            },
                            "current_mA": {
                                "type": "number",
                                "description": "Applied current in milliamperes (typical range: 1-100 mA). Extract from similar reactions when available.",
                            },
                            "current_density_mA_cm2": {
                                "type": "number",
                                "description": "Current density in mA/cm² (typical range: 1-30 mA/cm² for organic synthesis).",
                            },
                            "potential_V": {
                                "type": "number",
                                "description": "Applied potential in Volts (typical range: 1-5 V for organic electrolysis).",
                            },
                        },
                        "required": ["solvent_smiles", "electrolyte_smiles"],
                    },
                    "description": "List of condition sets to evaluate",
                },
                "compute_uncertainty": {
                    "type": "boolean",
                    "description": "If true, use MC-Dropout to estimate prediction uncertainty. Returns yield_std and confidence level (high/medium/low). Recommended for final yield predictions.",
                    "default": False,
                },
            },
            "required": ["reaction_smiles", "conditions"],
        },
    },
    {
        "name": "search_similar_reactions",
        "description": (
            "Search the training database for reactions similar to the query. "
            "Uses cosine similarity on 6144D molecular fingerprints. Returns similar "
            "reactions with their conditions, yields, and electrochemical parameters "
            "(current, current density, potential), which serve as references for "
            "condition selection and yield prediction."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of similar reactions to return (default: 5)",
                    "default": 5,
                },
                "threshold": {
                    "type": "number",
                    "description": "Minimum cosine similarity threshold (default: 0.3)",
                    "default": 0.3,
                },
                "min_yield": {
                    "type": "number",
                    "description": "Minimum yield filter — only return reactions with yield >= this value (optional)",
                },
                "rerank_by_yield": {
                    "type": "boolean",
                    "description": "If true (default), rerank results using combined score: 0.6*similarity + 0.4*yield/100",
                    "default": True,
                },
            },
            "required": ["reaction_smiles"],
        },
    },
    {
        "name": "search_mechanism",
        "description": (
            "Retrieve **mechanism context** for a reaction from a curated KB of "
            "~534 electrochemical papers (mechanism extracts: rxn_class_summary, "
            "mechanism_family tags, electron_flow narrative, key_intermediates, "
            "evidence types). Use this to ground reasoning about *why* a "
            "transformation works, not just what conditions to use.\n\n"
            "Two modes:\n"
            "- mode='reaction' (default): look up this reaction's own source paper "
            "(via DOI from raw KB) and retrieve top-K mechanistically similar papers "
            "(family Jaccard + TF-IDF on free-text mechanism narrative).\n"
            "- mode='families': skip the paper-lookup step and query directly by "
            "user-supplied mechanism family tags (e.g. ['radical_anodic', "
            "'mediator_cathodic']) plus optional free text. Use when reaction is "
            "novel or the source paper isn't in the KB.\n\n"
            "Returns 'seed_paper' (the query reaction's mechanism, if known) and "
            "'matches' (list of similar-mechanism papers with rxn_class_summary, "
            "shared families, electron_flow excerpt, evidence types). Each match "
            "is a chemistry-meaningful precedent for the LLM to cite when "
            "explaining the proposed mechanism / picking conditions."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products'). Required for mode='reaction'.",
                },
                "mode": {
                    "type": "string",
                    "enum": ["reaction", "families"],
                    "description": "'reaction' = lookup by reaction SMILES (default). 'families' = direct family-tag query.",
                    "default": "reaction",
                },
                "mechanism_family": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Family tags for mode='families'. Examples: 'radical_anodic', 'radical_polar_crossover', 'mediator_anodic', 'mediator_cathodic', 'paired_electrolysis', 'cation_initiated', 'electrocatalysis_inner_sphere', 'direct_SET', 'radical_cation', 'radical_cathodic', 'photoredox_combined', 'sacrificial_anode'.",
                },
                "free_text": {
                    "type": "string",
                    "description": "Free-text mechanism description for mode='families' (boosts TF-IDF match). E.g. 'Ni catalyzed reductive coupling with sacrificial Zn anode generating Ni(0) intermediate'.",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of similar-mechanism papers to return (default: 5)",
                    "default": 5,
                },
                "family_weight": {
                    "type": "number",
                    "description": "0-1 weight for family Jaccard vs text cosine in combined score. Higher = stricter mechanism class match. Default 0.4 (text is richer signal).",
                    "default": 0.4,
                },
                "include_query_paper": {
                    "type": "boolean",
                    "description": "If true, the query reaction's own paper appears in matches. Default false (we usually want OTHER papers).",
                    "default": False,
                },
            },
        },
    },
    {
        "name": "analyze_reaction_chemistry",
        "description": (
            "Analyze the substrate chemistry of a reaction: identify olefin type "
            "(terminal/internal/conjugated), detect sensitive functional groups "
            "(amines, alcohols, halides, aldehydes), and infer the reaction class "
            "(difluorination, bromoamination, carboamination, etc.). Use this FIRST "
            "before recommending conditions to understand substrate requirements and "
            "potential compatibility issues."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
            },
            "required": ["reaction_smiles"],
        },
    },
    {
        "name": "estimate_experimental_parameters",
        "description": (
            "Calculate electrochemical experimental parameters: required charge (Coulombs), "
            "estimated reaction time, recommended electrode area, and Faraday equivalents. "
            "Uses the fundamental relationship Q = n × F × z / FE (Faraday's law). "
            "Essential for planning wet-lab experiments."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "substrate_mmol": {
                    "type": "number",
                    "description": "Amount of substrate in millimoles (default: 0.2)",
                    "default": 0.2,
                },
                "num_electrons": {
                    "type": "integer",
                    "description": "Number of electrons transferred per molecule (e.g., 2 for a 2e⁻ oxidation)",
                    "default": 2,
                },
                "current_mA": {
                    "type": "number",
                    "description": "Applied current in milliamperes (default: 10)",
                    "default": 10.0,
                },
                "faradaic_efficiency_pct": {
                    "type": "number",
                    "description": "Estimated Faradaic efficiency in percent (default: 80). Use 60-90% for typical organic reactions.",
                    "default": 80.0,
                },
                "target_current_density_mA_cm2": {
                    "type": "number",
                    "description": "Target current density in mA/cm² (default: 10)",
                    "default": 10.0,
                },
            },
            "required": [],
        },
    },
    {
        "name": "generate_experimental_protocol",
        "description": (
            "Generate a complete, actionable wet-lab experimental protocol including "
            "electrode preparation, cell assembly, reagent addition order, electrolysis "
            "parameters, and safety notes. Uses a chemistry knowledge base for "
            "electrode-specific prep steps and solvent safety information."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "anode": {
                    "type": "string",
                    "description": "Anode material name (e.g., 'Graphite', 'Platinum')",
                },
                "cathode": {
                    "type": "string",
                    "description": "Cathode material name",
                },
                "cell_type": {
                    "type": "string",
                    "description": "Cell type: 'undivided', 'divided', 'flow', or 'sealed'",
                },
                "solvent": {
                    "type": "string",
                    "description": "Solvent name or description",
                },
                "solvent_smiles": {
                    "type": "string",
                    "description": "Solvent SMILES (for safety lookup)",
                },
                "electrolyte": {
                    "type": "string",
                    "description": "Electrolyte name or description",
                },
                "electrolyte_smiles": {
                    "type": "string",
                    "description": "Electrolyte SMILES",
                },
                "reagent": {
                    "type": "string",
                    "description": "Reagent name or SMILES",
                },
                "catalyst": {
                    "type": "string",
                    "description": "Catalyst name or SMILES",
                },
                "substrate_mmol": {
                    "type": "number",
                    "description": "Substrate amount in mmol (default: 0.2)",
                    "default": 0.2,
                },
                "current_mA": {
                    "type": "number",
                    "description": "Applied current in mA",
                },
                "time_hours": {
                    "type": "number",
                    "description": "Estimated reaction time in hours",
                },
                "charge_C": {
                    "type": "number",
                    "description": "Total charge to pass in Coulombs",
                },
                "predicted_yield": {
                    "type": "number",
                    "description": "Model-predicted yield (%)",
                },
            },
            "required": ["anode", "cathode", "cell_type"],
        },
    },
    {
        "name": "draw_reaction",
        "description": (
            "Draw chemical reaction structure diagrams as images using RDKit. "
            "Use after parse_reaction to show the user what the reaction looks like, "
            "and after search_similar_reactions to visualize found reactions."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Single reaction SMILES (format: 'reactants>>products')",
                },
                "reaction_smiles_list": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Multiple reaction SMILES to draw at once",
                },
                "legends": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Labels for each reaction (e.g., 'Similar #1 (yield: 85%)')",
                },
            },
        },
    },
    {
        "name": "optimize_conditions_bo",
        "description": (
            "Bayesian optimization for intelligent condition search. Uses a Gaussian Process "
            "surrogate to model yield over the condition space, with acquisition functions "
            "(EI/UCB/Thompson) to balance exploration and exploitation. "
            "Supports four modes:\n"
            "- 'suggest': Suggest next conditions to try in an iterative experiment loop. "
            "Uses warm-start from similar reactions + M1 predictions.\n"
            "- 'observe': Record an experimental result (yield) for a suggested condition set.\n"
            "- 'search': Offline search for optimal conditions using YieldPredictor as oracle. "
            "Runs multiple BO iterations automatically.\n"
            "- 'rerank': Rerank M1 candidate conditions using GP uncertainty (UCB) combined "
            "with M1 confidence scores.\n\n"
            "Use 'search' mode when you want to find the best conditions automatically. "
            "Use 'suggest'/'observe' for interactive experiment planning with the user. "
            "Use 'rerank' to improve upon M1 top-k predictions with uncertainty awareness."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "reaction_smiles": {
                    "type": "string",
                    "description": "Reaction SMILES (format: 'reactants>>products')",
                },
                "mode": {
                    "type": "string",
                    "enum": ["suggest", "observe", "search", "rerank"],
                    "description": (
                        "Operation mode: 'suggest' for next experiment suggestions, "
                        "'observe' to record a result, 'search' for automated offline "
                        "optimization, 'rerank' to reorder M1 candidates"
                    ),
                    "default": "suggest",
                },
                "acq_func": {
                    "type": "string",
                    "enum": ["ei", "ucb", "thompson"],
                    "description": (
                        "Acquisition function: 'ei' (Expected Improvement, default — "
                        "good balance), 'ucb' (Upper Confidence Bound — more exploration), "
                        "'thompson' (Thompson Sampling — stochastic)"
                    ),
                    "default": "ei",
                },
                "n_suggestions": {
                    "type": "integer",
                    "description": "Number of condition suggestions to return (default: 3)",
                    "default": 3,
                },
                "observed_conditions": {
                    "type": "object",
                    "description": (
                        "Condition dict for 'observe' mode. Keys: anode_index, cathode_index, "
                        "cell_type_index, solvent_index, solvent_smiles, electrolyte_index, "
                        "electrolyte_smiles, reagent_index, reagent_smiles, catalyst_index, "
                        "catalyst_smiles"
                    ),
                },
                "observed_yield": {
                    "type": "number",
                    "description": "Observed yield (0-100) for 'observe' mode",
                },
                "n_iter": {
                    "type": "integer",
                    "description": "Number of BO iterations for 'search' mode (default: 50)",
                    "default": 50,
                },
                "candidates": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of condition dicts for 'rerank' mode",
                },
                "m1_probs": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "M1 confidence scores for each candidate in 'rerank' mode",
                },
                "alpha": {
                    "type": "number",
                    "description": "Weight for M1 probability in reranking (0-1, default: 0.5)",
                    "default": 0.5,
                },
            },
            "required": ["reaction_smiles"],
        },
    },
]


def get_openai_tool_schemas():
    """Convert Anthropic-format TOOL_SCHEMAS to OpenAI function-calling format.

    Anthropic: {"name", "description", "input_schema": {JSON Schema}}
    OpenAI:    {"type": "function", "function": {"name", "description", "parameters": {JSON Schema}}}
    """
    openai_tools = []
    for tool in TOOL_SCHEMAS:
        openai_tools.append({
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["input_schema"],
            },
        })
    return openai_tools
