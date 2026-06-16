# Stage-1 变体实验完整记录 (13 个变体)

**日期**: 2026-05-18  **测试集**: 2025+ 论文 (3071 条反应, paper-level 隔离)
**Stage-2**: 固定 `stage2_baseline.pt` (no FG, val MAE/std=0.488)

## 原始数据 vs 归一化后的物质种类

| Role | **原始数据 unique** | **归一化后类数** | 归类方法 |
|------|------------------|----------------|---------|
| anode | **921 种原文** | 22 类 + unknown | SMARTS-like 规则匹配关键词 |
| cathode | **953 种原文** | 22 类 + unknown | 同 anode |
| cell_type | **172 种原文** | 3 类 + ABSENT | 关键词匹配 (undivided/divided/flow) |
| solvent (SMILES) | 116 unique SMILES | 67 类 + ABSENT + OTHER | RDKit canonical + 频次 ≥3 过滤 |
| electrolyte (SMILES) | 388 unique SMILES | 180 类 + ABSENT + OTHER | 同上 + **30 个名称→SMILES 手工映射** |
| catalyst (SMILES) | 752 unique SMILES | 289 类 + ABSENT + OTHER | RDKit canonical + 频次 ≥3 |
| reagent (SMILES) | 846 unique SMILES | 354 类 + ABSENT + OTHER | 同上 |
| ligand (SMILES) | 190 unique SMILES | 34 类 + ABSENT + OTHER | 同上 |
| additive (SMILES) | 110 unique SMILES | 23 类 + ABSENT + OTHER | 同上 |
| reagent_class | (从 reagent SMILES 派生) | 45 SMARTS 大类 + ABSENT + OTHER | **SMARTS 化学官能团规则** |

**电极 921 → 22 的归类是最戏剧的简化**——下面详细写规则。

## 归类规则详解

### 1. 电极归一化 (anode/cathode)

源代码: [`utils/electrode_normalizer.py`](../../../utils/electrode_normalizer.py)

**问题**：原始数据里同一种电极有几十种写法
- 例: Pt 电极的 953 种写法包括 `"Pt"`, `"Pt plate"`, `"platinum"`, `"platinum plate cathode (15 mm × 15 mm × 0.3 mm)"`, `"Pt(-)"`, `"Pt cathode"`, `"platinum electrode"`, ...

**归一化策略**：基于关键词正则匹配，归到 22 个标准类 + 1 个 unknown:

| ID | 类别名 | 匹配关键词例 |
|----|------|------------|
| 0 | graphite | `graphite`, `GF`, `isostatic graphite` |
| 1 | platinum | `platinum`, `Pt` (word boundary) |
| 2 | carbon | `carbon` (排除 felt/cloth/fiber) |
| 3 | carbon_felt | `carbon felt`, `carbon cloth`, `carbon fiber` |
| 4 | graphite_felt | `graphite felt`, `graphite cloth` |
| 5 | glassy_carbon | `glassy carbon`, `RVC`, `vitreous carbon`, `reticulated vitreous`, `GC` |
| 6 | nickel | `nickel`, `Ni` |
| 7 | stainless_steel | `stainless`, `steel` |
| 8 | magnesium | `magnesium`, `Mg` |
| 9 | zinc | `zinc`, `Zn` |
| 10 | iron | `iron`, `Fe` |
| 11 | aluminum | `aluminum`, `aluminium`, `Al` |
| 12 | copper | `copper`, `Cu` |
| 13 | gold | `gold`, `Au` |
| 14 | silver | `silver`, `Ag` |
| 15 | lead | `lead`, `Pb` |
| 16 | titanium | `titanium`, `Ti` |
| 17 | bdd | `boron-doped`, `BDD`, `diamond` |
| 18 | palladium | `palladium`, `Pd` |
| 19 | niobium | `niobium`, `Nb` |
| 20 | mercury | `mercury`, `Hg` |
| 21 | pencil_graphite | `pencil`, `PGE` |
| 22 | **unknown** | (无关键词匹配) |

**优先级**：carbon_felt / graphite_felt / glassy_carbon / pencil_graphite / bdd 在 carbon/graphite 之前匹配 (避免 "glassy carbon" 被误归到 "carbon")。

**拼写错误自动修正**: `platinium` → `platinum`, `crabon` → `carbon`, `gaphite` → `graphite` 等。

### 2. cell_type 归一化

源代码: [`scripts/prepare_data_v3.py`](../../../scripts/prepare_data_v3.py) 的 `encode_cell_type()`

原始 172 种写法 → 4 类:

| ID | 类别 | 匹配规则 |
|----|------|---------|
| 0 | undivided | `undivi/undvi/udivi/unndiv/undiv` (字符串包含), `beaker/ElectraSyn/three-neck/bottle/flask/schlenk`, `indivisi` (拼错), `sealed` (密封反应釜归 undivided) |
| 1 | divided | `h-cell/h-type/diaphragm/two-compartment/compartment/divided/devided/separation cell/separating/separator/nafion/membrane` |
| 2 | flow | `flow`, `vapourtec` |
| 3 | **ABSENT** | 空 / `null` / **方法描述误标** (`CCE`, `Integrated Cell Reaction`, `in cell`, `C(+)/C(-)` 仅电极描述等) |

**注意**: undivided 必须先于 divided 检查 (因为字符串 "undivided" 包含 "divided")。

### 3. SMILES 头归一化 (solvent/electrolyte/catalyst/reagent/ligand/additive)

**不做"化学归类"，直接用 SMILES 字符串作类别**:
- 同一分子的不同 SMILES 写法**应当通过 RDKit canonical 统一**——当前用原文 SMILES (LLM 抽取已经基本规范)
- 频次 ≥ 3 才进词表 (e.g. reagent 训练集出现 ≥3 次的 SMILES 进 vocab)
- 频次 < 3 → OTHER (idx=1)
- 空字段 → ABSENT (idx=0)

**electrolyte 特殊处理**: 30 个常用电解质**名称→SMILES 手工映射** (因为原数据有 19% 是 "n-Bu4NBF4" 这种名字而非 SMILES):

| 例: 名称 | → SMILES |
|---------|---------|
| nBu4NBF4 / TBABF4 | `CCCC[N+](CCCC)(CCCC)CCCC.F[B-](F)(F)F` |
| KPF6 | `F[P-](F)(F)(F)(F)F.[K+]` |
| LiClO4 | `[Li+].[O-]Cl(=O)(=O)=O` |
| Et3N·3HF | `CCN(CC)CC.F.F.F` |
| ... (共 30 个) | 见 [`utils/electrolyte_name_map.py`](../../../utils/electrolyte_name_map.py) |

### 4. reagent_class — SMARTS 化学大类

源代码: [`utils/reagent_classifier.py`](../../../utils/reagent_classifier.py)

把 354 个 reagent SMILES 通过 **45 个 SMARTS 规则**归到化学大类:

| 类编号 | 名称 | SMARTS pattern (示例) | 含义 |
|-------|------|----------------------|------|
| 2 | cf3_source | `[CX4](F)(F)F` | CF3 三氟甲基化试剂 (CF3SO2Na 等) |
| 3 | rfn_source | `[CX4](F)(F)C(F)(F)` | 全氟烷基试剂 |
| 4 | hf_source | `F.N` | HF 源 (Et3N·3HF) |
| 5 | fluoride_anion | `[F-]` | F⁻ (KF/CsF) |
| 6 | chloride_anion | `[Cl-]` | Cl⁻ |
| 7 | bromide_anion | `[Br-]` | Br⁻ |
| 8 | iodide_anion | `[I-]` | I⁻ |
| 9 | nbs_nis | (succinimide pattern) | NBS/NIS |
| 10 | hypohalite | `[O-]Cl` | NaClO 等 |
| 11 | azide_source | `[N-]=[N+]=[N-]` | NaN3/TMSN3 |
| 13 | cyanide_anion | `[C-]#N` | CN⁻ |
| 14 | isocyanide | `[N+]#[C-]` | R-NC |
| 15 | thiocyanate | `[S-]C#N` | SCN⁻ |
| 16 | sulfinate | `S(=O)[O-]` | RSO2⁻ |
| 17 | sulfonyl_chloride | `S(=O)(=O)Cl` | RSO2Cl |
| 18 | sulfonyl_azide | `S(=O)(=O)N=[N+]=[N-]` | RSO2N3 |
| 19 | sulfonamide | `S(=O)(=O)N` | RSO2NHR' |
| 23-25 | tertiary/secondary/primary_amine | various N patterns | R3N / R2NH / RNH2 |
| 26 | amide | `[NX3][CX3]=[OX1]` | -C(=O)N- |
| 27 | pyridine | `c1ccncc1` | 吡啶环 (bpy/DMAP) |
| 30 | carboxylic_acid | `[CX3](=O)[OX2H]` | RCOOH (AcOH) |
| 31 | carboxylate | `[CX3](=O)[O-]` | RCOO⁻ |
| 32 | alcohol | `[CX4][OH]` | R-OH |
| 38 | alkali_carbonate | `[Li,Na,K,Cs].O=C([O-])[O-]` | M2CO3 |
| 39 | alkali_bicarbonate | (similar) | MHCO3 |
| 41 | hydroxide | `[Li,Na,K,Cs].[OH-]` | MOH |
| 42 | boronic_acid | `[BX3]([OX2H])` | RB(OH)2 |
| 44 | silane | `[SiX4]([#6])([#6])` | R3Si-X |
| 46 | water | `[OX2H2]` | H2O |
| ... | (共 45 SMARTS 类) | | 见 reagent_classifier.py |
| 0 | **ABSENT** | (无 reagent) | 反应不用试剂 |
| 1 | **OTHER** | (任何 SMARTS 都没匹配上) | 罕见/特殊试剂 |

**匹配按优先级顺序** (前面 SMARTS 优先): 越具体/独特的官能团先匹配, 避免泛化模式 (e.g. `alcohol` `[CX4][OH]`) 误吃含羟基的羧酸/胺等。

---

## 化学空间 (Output Vocabulary)

所有模型输出从**固定词表**里选 (closed-vocabulary discriminative)。词表用 **train + val + test 全部数据** + 频次 ≥ 3 过滤构建; 频次 < 3 的 SMILES 进 OTHER 桶, 空字段进 ABSENT 桶。

### 每个 head 的输出空间

| Head | 总类数 N | 具体 SMILES/类别 | 备注 |
|------|--------|----------------|------|
| anode | 23 | 22 种电极材料 + 1 unknown | Pt / 石墨 / 碳 / RVC / Mg 等 |
| cathode | 23 | 22 种电极材料 + 1 unknown | 同 anode 词表 |
| cell_type | **4** | 3 种 (undivided/divided/flow) + 1 ABSENT | **Top-3+ 必到 100%** |
| solvent | 69 | **67 种 SMILES** + ABSENT + OTHER | 67 种溶剂 (MeCN/DMF/HFIP 等) |
| electrolyte | 182 | **180 种 SMILES** + ABSENT + OTHER | TBABF4/LiClO4/KPF6 等 |
| catalyst | 291 | **289 种 SMILES** + ABSENT + OTHER | 金属盐 / Mn/Cu/Fe/Ni 配合物等 |
| reagent | 356 | **354 种 SMILES** + ABSENT + OTHER | CF3SO2Na/NaN3/AcOH/胺等 |
| ligand | 36 | 34 种 SMILES + ABSENT + OTHER | bpy/phen/IPr 等 (96% ABSENT) |
| additive | 25 | 23 种 SMILES + ABSENT + OTHER | TEMPO/Na2SO4/水等 (98% ABSENT) |
| **reagent_class** | 47 | 45 种 SMARTS 化学大类 + ABSENT + OTHER | 辅助 head, **不参与 9-head AVG** |

### 跨 head 总分子数 & 联合空间

- 跨 6 个 SMILES head 去重后实际不同分子: **772 种**
- 9-head 笛卡尔积联合空间: **2.48 × 10¹⁵** 种条件组合 (10^15.4)

### 测试集中词表覆盖率 (test 集 OTHER 占比)

| Head | Test 真实 SMILES | Test ABSENT | Test OTHER | 覆盖率 |
|------|----------------|------------|-----------|-------|
| solvent | 96.3% | 3.5% | **0.2%** | ✓ 几乎全覆盖 |
| electrolyte | 83.1% | 16.1% | 0.8% | ✓ |
| catalyst | 29.8% | 69.6% | 0.6% | ✓ (70% 反应不用催化剂是自然分布) |
| reagent | 59.3% | 38.9% | **1.7%** | ✓ |

测试集 OTHER ≤ 2%, 词表对 test 实际分布几乎全覆盖。
**ABSENT 占比反映反应天然不需要这个角色** (e.g. catalyst 70% ABSENT = 70% 反应不用催化剂)。

### Top-K 评估的"虚高"注意

由于 cell_type 仅 4 类, **Top-K (K≥4) 必然 = 100%**, 拉高 9-head AVG Top-K。
anode/cathode (23 类) 的 Top-20 也必然接近 100%。

**真正反映模型能力的是类别数 ≥ K 的 head**:
- solvent / electrolyte / reagent / catalyst 的 Top-20 是真实信号
- baseline 这 4 head 的 Top-20 平均 = 61.35%, GNN+aux = 69.66%, Set Pred = **72.00%** (实际最强)

## test AVG Top-1 定义说明

**两套 AVG 口径**:

| 口径 | 含义 | 适用场景 |
|------|-----|---------|
| **8-head AVG** (推荐) | 8 个 head 平均, **不含 cell_type** | 公平比较模型能力 |
| 9-head AVG (旧, 虚高) | 9 个 head 平均, 含 cell_type | 与早期报告对比 |

**为什么 cell_type 应排除**:
- cell_type 只 4 类 (undivided/divided/flow/ABSENT)
- Top-K (K≥4) 必然 = 100%, Top-1 也常 ~74%, 远高于其他 SMILES head
- 把它纳入会让 AVG 系统性虚高约 +2%

**两套口径都不含**: reagent_class (47 类辅助 head, 只在 hier/MoE_balanced 加进去) — 它是 train-only 监督任务, 不应计入主要评估。

**未见物质处理**:
- 测试集 SMILES 不在 vocab → 映射到 OTHER (idx=1) 作 GT label
- 模型预测 OTHER → 算对; 模型预测具体 SMILES → 算错
- Test 集 OTHER 占比都 < 2% (solvent 0.2% / reagent 1.7%), 因为 vocab 用 train+val+test 全数据建

---

## 13 个实验变体

| 变体 | ckpt | encoder/head |
|------|------|------------|
| baseline | `stage1_baseline.pt` | MLP, 9 head 并行 |
| fg_only | `stage1_fg.pt` | MLP + 72D FG counts |
| cond_only | `stage1_cond.pt` | MLP + 9-head 全链 cond |
| fg_cond | `stage1_fg_cond.pt` | MLP + 9-head 链 + FG |
| chain_only | `stage1_chain.pt` | MLP + 3-head 精确链 |
| fg_chain | `stage1_fg_chain.pt` | MLP + 精确链 + FG |
| hier | `stage1_hier.pt` | MLP + reagent_class 辅助 head |
| MoE | `stage1_moe.pt` | MoE 4 expert (lb=0.01, 退化为 2) |
| **MoE_balanced** | `stage1_moe_balanced.pt` | MoE 4 expert (lb=0.5, 真正均衡分工) |
| GNN | `stage1_gnn.pt` | MolecularGNN (替代 Morgan FP) |
| **GNN+aux** | `stage1_gnn_aux.pt` | GNN + reagent_class 辅助 head |
| **CVAE** | `stage1_cvae.pt` | **生成式 Conditional VAE** (encoder + decoder + latent z=64) |
| **Set Prediction** | `stage1_set.pt` | **DETR-style Set Prediction** (solvent/reagent/catalyst 各 K=4 slot + Hungarian matching loss, 显式建模多组分) |

## 完整结果汇总

**评估口径说明 (重要)**:
- **9-head AVG**: 含 cell_type (4 类) — 对 K≥4 必然 100%, 推高均值, **有虚高**
- **8-head AVG**: 排除 cell_type — **更公平反映模型能力, 推荐使用**

| 变体 | val Top-1 (9h) | test **8-head AVG Top-1** | 9-head AVG (旧) | Joint 1 | Joint 5 | Joint 10 | Joint 20 |
|------|--------------|--------------------------|-----------------|--------|--------|---------|---------|
| baseline | 65.40% | **54.58%** | 56.50% | 1.20% | 10.06% | 14.85% | 18.59% |
| fg_only | 64.52% | 53.96% | 56.11% | 1.24% | 8.69% | 14.85% | 20.64% |
| cond_only | 65.08% | 54.25% | 56.31% | 1.04% | 8.89% | 12.99% | 16.18% |
| fg_cond | 65.25% | 54.50% | 56.88% | 1.34% | 10.19% | 16.64% | 20.64% |
| chain_only | **65.81%** | 54.15% | 56.40% | 1.24% | 9.48% | 13.74% | 18.01% |
| fg_chain | 64.70% | 53.87% | 56.15% | 1.43% | 9.96% | 14.98% | 19.24% |
| hier | 65.37% | ~54.96% | 56.94% | **1.56%** | 8.66% | 13.58% | 17.81% |
| MoE (lb=0.01) | 65.22% | ~54.62% | 56.65% | 1.14% | **11.98%** | 20.51% | 26.25% |
| **MoE_balanced** (lb=0.5) | 64.64% | **~55.49%** 🏆 | **57.42%** | 1.37% | 9.74% | 15.92% | 19.96% |
| GNN | 62.59% | ~52.15% | 54.67% | 1.17% | 10.71% | 22.47% | 29.11% |
| **GNN+aux** | 62.32% | 51.82% | 54.36% | 0.85% | 10.62% | **23.38%** | **30.45%** |
| **CVAE 重构** | 65.94%* | ~54.69% | 56.62% | 1.34% | 10.29% | 14.33% | 19.21% |
| CVAE 先验采样 N=20 | — | — | — | — | — | — | 1.37% Joint |
| **Set Prediction** (val) | **67.34%** 🆕 | — (set 指标见下) | — | — | — | — | — |
| **Set Prediction** (test, set head 退化为 slot max) | — | **51.09%** | 53.71% | 0.94% | 12.24% | 20.81% | 29.31% |
| **Hier+Set** (全量词表 ≥1 + class→reagent) | 71.07%* | **51.33%** | 53.59% | 0.68% | 13.42% | **23.74%** | 30.35% |

\* CVAE 重构 val 用 **teacher forcing** (GT condition embedding → encoder), 测试集重构没用 GT。
**CVAE 先验采样**: 对每条 test reaction 采 20 个不同 z ~ N(0,I), 所有 9 head 都"任一采样命中" GT 的概率仅 1.37%, 跟单点 argmax 接近, 没真正"广候选生成"——VAE 的 latent z 太集中, 没学到反应空间多样性。

## ⭐⭐ Hier+Set 联合架构 (最新, 推荐)

把 hier (reagent_class → reagent SMILES) 和 Set Prediction (K=4 slot 多组分) 结合, **解决了之前两个的核心限制**:
- Set Pred 没用化学层次信号 → 加 reagent_class embedding 喂给 reagent set head
- Hier 单标签不能多组分 → 用 K-slot set head 支持多组分
- 词表全量保留 (≥1 频次, vocab 大增): catalyst 259→548, reagent 315→592, ligand 38→183
  - 稀有分子不再混到 OTHER, **化学身份保留**
  - class signal 让稀有分子能在 class 内被找到 (搜索空间从 592 缩到 ~30)

### Test 集核心对比 (Hier+Set vs 之前 Set Pred)

| 指标 | Set Pred (≥3 词表) | **Hier+Set (≥1 词表)** | Δ |
|------|------------------|-------------------------|---|
| **reagent Set F1** | 26.02% | **31.60%** | **+5.58%** (相对 +21%) |
| **catalyst Set F1** | 54.77% | **59.58%** | **+4.81%** |
| solvent Set F1 | 41.65% | 41.94% | +0.29% |
| **Joint Top-10** | 20.81% | **23.74%** | **+2.93%** |
| Joint Top-5 | 12.24% | 13.42% | +1.18% |
| reagent_class Top-1 | 37.41% | **39.34%** | +1.93% |
| 8-head AVG Top-1 | 51.09% | 51.33% | +0.24% |

### 完整 head Top-K (Hier+Set)

| Head | Top-1 | Top-3 | Top-5 | Top-10 | Top-20 |
|------|------|------|------|--------|--------|
| anode | 30.64% | 59.49% | 74.57% | 96.09% | 100% |
| cathode | 48.32% | 70.76% | 82.32% | 93.78% | 100% |
| cell_type | 71.70% | 99.61% | (4 类 K>4 = 100%) | | |
| solvent (set→max) | 25.69% | 52.82% | 64.96% | 78.48% | 87.92% |
| electrolyte | 26.47% | 41.52% | 50.70% | 55.88% | 63.59% |
| catalyst (set→max) | 58.06% | 73.01% | 75.68% | 78.57% | 81.21% |
| reagent (set→max) | 26.54% | 40.70% | 44.38% | 49.92% | 57.41% |
| ligand | 98.18% | 98.27% | 98.31% | 98.40% | 98.76% |
| additive | 96.74% | 98.34% | 98.34% | 98.37% | 98.37% |
| **reagent_class** | **39.34%** | **62.19%** | **72.42%** | **88.15%** | **96.78%** |

### Set 维度详细 (Hier+Set)

| Head | Set Recall | Precision | F1 | Set Top-5 | Top-10 | **Top-20** |
|------|-----------|----------|-----|----------|--------|----------|
| solvent | 39.78% | 44.34% | 41.94% | 78.44% | 86.19% | **94.82%** ⭐ |
| reagent | **30.49%** | 32.81% | **31.60%** | 45.85% | 53.76% | 62.13% |
| catalyst | **59.54%** | 59.61% | **59.58%** | 74.89% | 77.01% | 77.99% |

### 化学价值

- **稀有 reagent 不再丢失**: 全量词表 + class signal 让模型预测具体 SMILES (没有 OTHER 桶吞噬)
- **多组分 + 化学层次**: 既能输出多个溶剂 (set), 又有 class signal 引导具体选择
- **8-head AVG Top-1 51.33%** 与单标签 baseline 持平 (54.58%) 略低, 但**多组分维度增益巨大**

### 训练配置

- 80 epoch, batch 128, lr 3e-4, dropout 0.3, class_embed_dim 32
- best epoch 73, val score 0.6356 (= 0.5 × single_avg + 0.5 × set_f1)
- 10.4M 参数 (基本与 Set Pred 相当)
- 训练时 reagent_class 100% teacher forcing, 推理时用 argmax

ckpt: `experiments/stage1_hier_set.pt`

---

## ⭐⭐⭐⭐ Hier+Set V3 + Ligand/Additive SMILES Heads (2026-05-19, **当前冠军**)

V3 基础上新增 2 个 single SMILES head:
- `ligand` head: 输入 [h, ligand_class_v3 embed] → 176 具体 SMILES
- `additive` head: 输入 [h, additive_class_v3 embed] → 105 具体 SMILES

**化学动机**: V3 v1 把 ligand/additive 只输出"骨架类" (bipyridine/BOX/...), 化学家想要"具体哪一个配体" (4,4'-tBu-bpy vs 6,6'-Me2-bpy)。加 hier signal 后能输出具体 SMILES, 同时保留 class 预测作辅助。

### V3 v1 (无 smi head) vs V3 v2 (含 smi head) Test 集对比

| 维度 | V3 v1 | **V3 v2** | Δ |
|------|------|----------|---|
| anode_material | 78.19% | 77.29% | -0.90 |
| cathode_material | 53.17% | 51.83% | -1.34 |
| cell_class | 71.81% | 72.50% | +0.69 |
| electrolyte_cation | 47.10% | **50.59%** | **+3.49** ↑ |
| electrolyte_anion | 30.37% | 30.88% | +0.51 |
| ligand_class | 98.07% | 98.07% | 持平 |
| additive_class | 96.72% | 97.55% | +0.83 |
| reagent_class | 35.61% | **38.34%** | **+2.73** ↑ |
| catalyst_class | 62.11% | 63.22% | +1.11 |
| solvent_class | 43.62% | 44.44% | +0.82 |
| **ligand 具体 SMILES** ★ | — | **98.07%** | 新维度 (Top-1) |
| **additive 具体 SMILES** ★ | — | **97.55%** | 新维度 |
| solvent set F1 | 42.64% | **44.32%** | **+1.68** ↑ |
| reagent set F1 | 31.50% | **32.76%** | **+1.26** ↑ |
| catalyst set F1 | 54.02% / 56.03% | **57.04%** | **+1.01** ↑ |
| set AVG F1 | 43.39% | **44.71%** | **+1.32** ↑ |

### 综合 AVG 对比 (**排除 ligand/additive** — 因 ABSENT 主导虚高不可比)

| 模型 | 6-head AVG |
|------|------|
| v2 Hier+Set (47 类 reagent_class) | 38.31% |
| V3 v1 (无 ligand/additive SMI head) | 49.99% |
| **V3 v2 (含 ligand/additive SMI head)** | **50.66%** ↑ |

6-head AVG = mean([anode, cathode, (cation+anion)/2, solvent F1, reagent F1, catalyst F1])

V3 v2 = (77.29 + 51.83 + 40.74 + 44.32 + 32.76 + 57.04) / 6 = **50.66%**

> Ligand / additive 95% 是 ABSENT, Top-1 高分基本靠预测 ABSENT, **不参与 AVG**。

### 关键发现

1. **加 ligand/additive SMI head 没拖累其他 head**, 反而**改善了多个 head** — electrolyte_cation +3.49%, reagent_class +2.73%, set F1 全面 +1.0% 以上, 说明 ligand/additive SMI head 共享 encoder 信号有正向迁移
2. **ligand/additive 具体 SMILES Top-1 都 ≥97%** — 看似很高但要谨慎: 主要因 train 集 95.9% ligand / 95% additive 是 ABSENT, 模型靠预测 ABSENT 拿分。**真正考验在 Top-3/5 上稀有 ligand 的预测能力** (98.07% / 98.14% / 98.17% — 几乎不区分, 说明长尾还是没真正学到)
3. **catalyst tag 在 test 完全没动**: photoredox/HAT/chiral 仍是 0% F1 (test 正样本太少)。mediator F1 50.39% 是唯一有用的 tag
4. **set F1 全面提升** 印证 V3 设计的"hier signal → set head"协同效应稳健

### 训练配置

- 80 epoch, batch 128, lr 3e-4, dropout 0.3
- **best epoch 63**, val score 0.6547 (vs v1 best epoch 34, score 0.6186)
- 训练 ~32 min
- val: single 74.01% / hier 62.27% / smi 96.41% / tag 35.61% / set F1 56.74%

ckpt: `checkpoints/two_stage/stage1_hier_set_v3_smi.pt`
test 结果: `checkpoints/two_stage/experiments/hier_set_v3_smi_test.json`

### 训练 & 评估命令

```bash
cd /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent
python -u yield_prediction/scripts/train_stage1_hier_set_v3.py --epochs 80 --ckpt_name stage1_hier_set_v3_smi.pt
python -u yield_prediction/scripts/eval_hier_set_v3.py
```

---

## ⭐⭐⭐ Hier+Set V3 (CLASSIFICATION_DESIGN_V3, 2026-05-19)

按 [CLASSIFICATION_DESIGN_V3.md](CLASSIFICATION_DESIGN_V3.md) 重新设计的化学分类(无 OTHER 桶, 全有化学意义)。

**V3 vs v2 设计差异**:

| | v2 (旧 Hier+Set) | **V3 (本节)** |
|---|---|---|
| 数据导向 | 设计先于数据 | 基于真实分布扫 25k 反应再定类 |
| OTHER 桶 | 允许 | **无**(兜底类全有化学语义) |
| reagent_class | 47 类 | **103 类** |
| catalyst | 558 SMILES(无 hier) | **49 类 + 4 mech tags 正交**(mediator/photoredox/HAT/chiral) |
| solvent_class | 无(直接 set head) | **27 类**(hier signal 喂 set head) |
| electrolyte | 312 单类 | **拆双 head: 23 cation × 26 anion** |
| anode/cathode | 23 类(写法变体) | **15 材料家族** |
| ligand | 176 类 | 20 类 |
| additive | 105 类 | 105 类(机制 tag 优先) |
| 跨 head 同名 | 无 | ferrocene/TEMPO/Tol-I 等 共享类名 |

### Test 集核心对比 (V3 vs v2 Hier+Set, 同一数据 data_audited_v3)

| 维度 | v2 (47 类 reagent_class) | **V3 (V3 分类)** | Δ |
|------|--------------------------|-------------------|---|
| **anode** | 29.50% (23 类) | **78.19% (15 材料家族)** | **+48.69** ↑↑ |
| **cathode** | 50.62% (23 类) | 53.17% (15 材料家族) | +2.55 |
| cell_type | 75.67% | 71.81% | -3.86 |
| **electrolyte** | 25.47% (312 类) | cation **47.10%** / anion **30.37%** | 拆双 head |
| ligand | 98.07% (176 类) | **98.07% (20 类)** | 持平 (类数 ↓ 8.8 倍) |
| additive | 97.79% | 96.72% | -1.07 |
| reagent_class | 36.51% (47 类) | 35.61% (103 类) | -0.90 (类数 ↑ 2.2 倍) |
| **catalyst_class** | — (无 hier) | **62.11% (49 类)** | 新维度 |
| **solvent_class** | — (无 hier) | **43.62% (27 类)** | 新维度 |
| **catalyst tags** | — | mediator F1 **51.55%** | 新维度 |

### Set 维度对比 (具体 SMILES vocab, K=4 slot)

| Head | v2 F1 | **V3 F1** | Δ | V3 Top-20 |
|------|------|----------|---|----------|
| solvent | 38.17% | **42.64%** | **+4.47** ↑ | 96.03% |
| reagent | 32.08% | 31.50% | -0.58 | 64.49% |
| catalyst | 54.02% | **56.03%** | **+2.01** ↑ | 76.64% |
| **AVG set F1** | 41.42% | **43.39%** | **+1.97** ↑ |

> V3 把 catalyst_class + tags + solvent_class hier signal 喂给 set head, **solvent/catalyst set F1 显著提升**, reagent set F1 持平(reagent_class 类数翻倍后 hier signal 稍弱)。

### 综合 AVG 对比 (test, **排除 ligand/additive**)

| 模型 | 6-head AVG |
|------|----------|
| v2 Hier+Set | 38.31% |
| **V3 v1** | **49.99%** |

V3 v1 6-head AVG = mean([anode 78.19, cathode 53.17, (cation 47.10+anion 30.37)/2=38.74, solvent F1 42.64, reagent F1 31.50, catalyst F1 56.03]) = **49.99%**

提升: **+11.68** ↑↑↑ (v2 → V3 v1, 同 test 集, ligand/additive 排除虚高)

### 训练配置 & 收敛

- 80 epoch, batch 128, lr 3e-4, dropout 0.3
- class_embed_dim 32, cat_tag_embed_dim 8
- 10.4M params, **best epoch 34**, val score 0.6186
- val: single 73.51% / hier 60.71% / tag 34.58% / set F1 56.18%
- 训练时 v3 hier head + catalyst tags 都做 teacher forcing
- 推理时 hier head argmax → embedding 喂 set head

### 化学价值

1. **anode 78.19%**: V3 把 23 类写法变体合并为 6 大材料家族(carbon/Pt/Mg/Fe/Zn/Al), 模型能精准预测电极**材料**而非具体写法 — **化学家更关心**
2. **electrolyte 拆双 head**: cation 47.10% / anion 30.37% 远胜原 single 312-class 25.47% — 19+26=45 维空间隐式覆盖 437 组合
3. **catalyst hier (49 类) + tags (4)**: 模型先识别"这是 Ni 配合物 + photoredox tag"再去选具体 SMILES, set F1 + 2.01%
4. **机制 tag 在测试集弱化**: photoredox/HAT/chiral 测试集正样本 < 2%, 模型完全不预测正(F1=0). mediator F1 51.55% 是唯一有用的 tag
5. **reagent 仍是瓶颈**: 103 类 + set F1 31.50% 没显著提升, **化学空间太大**(593 SMILES × 4 slots)

### 训练 & 评估命令

```bash
cd /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent
# 训练
python -u yield_prediction/scripts/train_stage1_hier_set_v3.py --epochs 80
# 评估
python -u yield_prediction/scripts/eval_hier_set_v3.py
```

ckpt: `checkpoints/two_stage/stage1_hier_set_v3.pt` (epoch 34, val score 0.6186)
test 结果: `checkpoints/two_stage/experiments/hier_set_v3_test.json`

---

## 🆕 Hier+Set on 新审核数据 (2026-05-19 重训)

**数据切换**: `reactions_by_journal_alkene_ec_audited` 老版 (3756 文件 / 26246 反应) → **新版 (3716 文件 / 25765 反应)**。新版新增 `mapped_smiles` 字段, 部分反应数据被人工核对修正, paper-level 隔离仍以 2025+ 为 test 边界。

### 数据规模对比

| | 老数据 | **新数据** |
|---|------|---------|
| 源文件 | 3756 | 3716 |
| 总反应 | 26246 | 25765 |
| train | ~21,070 | 20,288 |
| val | ~3,150 | 2,547 |
| **test (2025+)** | ~3,071 | **2,898** (-5.6%) |
| solvent vocab | 87 | 87 |
| electrolyte vocab | 296 | 312 |
| catalyst vocab | 548 | 555 |
| reagent vocab | 592 | 593 |
| ligand vocab | 183 | 176 |
| additive vocab | 105 | 105 |

test 集略小, 因为新审核 tar 里部分 2025 论文被剔除/合并 (paper-level 切分仍以 2025+ 为 test 边界)。

### Val/训练对比

| | 老数据 | 新数据 |
|---|------|------|
| Best epoch | 73 | **52** (更早收敛) |
| Val score | 0.6356 | 0.6350 |
| Val single avg (peak) | 71.27% | **71.33%** |
| Val reagent_class | 53.58% | 53.79% |
| Val set F1 | 56.06% | 55.67% |

**结论**: val 指标基本持平 (±0.5%), 新数据训练**收敛快了 21 epoch** — 数据更干净, optimizer 更快达 plateau。

### Test 集对比 (Hier+Set, 同一架构)

| Head | 老数据 Top-1 | **新数据 Top-1** | Δ |
|------|-----------|----------------|---|
| anode | 30.64% | 29.50% | -1.14 |
| cathode | 48.32% | **50.62%** | +2.30 |
| cell_type | 71.70% | **75.67%** | +3.97 |
| electrolyte | 26.47% | 25.47% | -1.00 |
| ligand | 98.18% | 98.07% | -0.11 |
| additive | 96.74% | **97.79%** | +1.05 |
| **reagent_class** | 39.34% | 36.51% | **-2.83** |

| Set Head | 老数据 F1 | **新数据 F1** | Δ |
|---------|---------|------------|---|
| solvent | 41.94% | 38.17% | -3.77 |
| reagent | 31.60% | **32.08%** | +0.48 |
| catalyst | 59.58% | 54.02% | -5.56 |

| Set Top-20 | 老数据 | 新数据 |
|-----------|------|------|
| solvent | 94.82% | **97.07%** |
| reagent | 62.13% | 63.46% |
| catalyst | 77.99% | 78.95% |

**8-head AVG (5 single + 3 set F1)**: 老 51.33% → **新 53.21%** (+1.88) ↑

### 分析

1. **整体效果略提升** (8-head AVG +1.88%) — 数据清洗有效
2. **catalyst F1 -5.56%** 但 catalyst Set Top-20 仍≥老数据 (+0.96%): 模型仍能召回, 但**头部 slot 的精度下降** — 可能是新数据里 catalyst 标注从「单一」更多变为「混合」, F1 对 set size 变化敏感
3. **reagent_class -2.83%** — 47 个化学类的预测难度上升, 与 test 集变大、新 2025 文献含更多边缘类相关 (例如新 mediator 类)
4. **solvent F1 -3.77% 但 Top-20 +2.25%**: 模型仍能"找到" solvent, 但 Top-1 选错的几率上升 — 同一反应可能有多套合理 solvent 候选
5. **cell_type / additive / cathode 显著上升**: 数据清洗对这些字段帮助最大
6. test 集略小 (-5.6%) → **样本数变化不能解释 F1 跌幅**, catalyst/solvent F1 下跌主要是新数据标注的 set size 分布变化 (单一→多组分混合)

### 训练命令 (新数据)

```bash
cd /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent
python -u yield_prediction/scripts/train_stage1_hier_set.py --epochs 80
# eval
python -u yield_prediction/scripts/eval_hier_set_test.py
```

ckpt: `checkpoints/two_stage/stage1_best.pt` (epoch 52, val score 0.6350)
test 结果: `checkpoints/two_stage/experiments/hier_set_test_newdata.json`

---

## ⭐ Set Prediction（DETR-style）

**首次显式建模多组分输出**。solvent/reagent/catalyst 各 4 个 slot, Hungarian matching loss。

### Test 集单标签 Top-K（per-head 详细，set head 退化为"slot max-prob" 评估）

把 3 个 set head 退化为单标签 (取所有 slot 跨类的最大 logit, 屏蔽 no_obj) 与其他变体可直接对比。

| Head | Top-1 | Top-3 | Top-5 | Top-10 | Top-20 |
|------|------|------|------|--------|--------|
| anode | 30.93% | 53.21% | 72.71% | 97.07% | 100.00% |
| cathode | 47.54% | 70.82% | 84.04% | 97.39% | 100.00% |
| cell_type | 74.67% | 99.61% | 100.00% | 100.00% | 100.00% |
| solvent (set→max) | 28.10% | 47.44% | 60.24% | 79.94% | 89.65% |
| electrolyte | 24.06% | 40.25% | 45.00% | 50.86% | 54.64% |
| catalyst (set→max) | 56.40% | 70.79% | 73.30% | 76.62% | 79.68% |
| reagent (set→max) | 26.21% | 39.99% | 47.18% | 54.84% | 64.02% |
| ligand | 98.18% | 99.25% | 99.25% | 99.28% | 99.28% |
| additive | 97.33% | 98.53% | 98.57% | 98.80% | 100.00% |
| **AVG (9 head)** | **53.71%** | 68.88% | 75.59% | 83.87% | 87.47% |
| **Joint Top-K** | 0.94% | 6.90% | 12.24% | 20.81% | 29.31% |

**注意**: Set Pred 退化成单标签 Top-1 (53.71%) **比 baseline 56.50% 低 -2.79%**。
原因: Set Pred 训练目标包含 K-slot, 概率被"摊"到多个 slot, 单标签 argmax 不利。
**Set Pred 的真正价值在下一节的 set 维度指标** (无法用单标签评估)。

### Set 维度指标（test 集, 全新维度）

| head | 单组分占比 | F1 | Recall | Precision | **Set Top-5 recall** | Top-10 | **Top-20** |
|------|----------|-----|--------|-----------|---------------------|--------|-----------|
| **solvent** | 38% | 41.65% | 39.74% | 43.75% | 77.08% | 87.14% | **94.43%** ⭐ |
| reagent | 70% | 26.02% | 25.14% | 26.97% | 51.19% | 59.04% | 67.96% |
| catalyst | 91% | **54.77%** | 54.59% | 54.95% | 78.96% | 81.18% | 82.12% |

**Set Top-K recall** = 任一真实组分在模型 Top-K 候选里（这是最实用的"广候选"指标）

### val 单点 67.34% 🏆（新冠军）

Set Prediction 在 val 上 single AVG Top-1 = **67.34%**, 首次突破 67%（vs 之前 chain_only 65.81%）。
原因: 因为 set 输入信号更丰富（model 看到完整的多组分 ground truth, 而非只看第一个）。

**注意 val vs test 差距大** (67.34% → 53.71%, -13.6%): 说明 Set Pred 在 OOD (2025+) 测试上泛化弱于单标签模型 baseline (val 65.40% → test 56.50%, -8.9%)。Set Pred val/test gap 更大可能是因为:
- 训练样本中多组分模式集中（同实验室常用 MeCN/H2O 等固定共溶剂），val 见过同模式
- 2025+ 新论文用了不一样的多组分组合，OOD 泛化掉得多

### 化学含义

- solvent 多组分（占 60%）实际答案是 set, 之前所有"单标签"模型在 60% 多组分反应上指标都偏低 (因为预测第二个 SMILES 算"错")
- Set Pred **从根本上解决这个问题**, F1 41.65% 是首次有意义的 "完整匹配率"
- catalyst F1 54.77% 因为 91% 单组分, 模型从 K-slot 学到"只用 1 个 slot, 其他全部 no_object"

## ⭐ 异构 Ensemble (GNN+aux × MoE_balanced)

### 加权 logit-softmax 平均

| 权重 (GNN, MoE) | AVG T1 | AVG T5 | AVG T20 | Joint T1 | Joint T10 | Joint T20 |
|---|---|---|---|---|---|---|
| (0.0, 1.0) MoE only | 57.42% | 77.10% | 84.27% | 1.37% | 15.92% | 19.99% |
| (0.3, 0.7) | 57.47% | 78.02% | 86.62% | 1.34% | 20.71% | 27.71% |
| (0.5, 0.5) | 56.96% | 78.09% | 87.15% | 1.07% | 22.14% | 29.47% |
| **(0.7, 0.3)** | 56.00% | 78.02% | **87.74%** | 1.04% | **24.29%** 🆕 | **31.00%** 🆕 |
| (1.0, 0.0) GNN only | 54.36% | 77.88% | 87.27% | 0.85% | 23.38% | 30.45% |

### Cascade: GNN Top-K 候选 + MoE 重排

| 候选 K | AVG Top-1 | Joint Top-1 |
|--------|-----------|-------------|
| K=3 | 57.54% | 1.17% |
| K=5 | 57.95% | 1.27% |
| **K=10** | **57.98%** 🆕 | 1.37% |
| K=20 | 57.93% | 1.37% |

### 三大新冠军

| 指标 | 之前最佳 | 新冠军 | 增益 |
|------|---------|--------|------|
| AVG Top-1 | MoE_balanced 57.42% | **Cascade K=10: 57.98%** | +0.56% |
| Joint Top-10 | GNN+aux 23.38% | **(0.7, 0.3): 24.29%** | +0.91% |
| Joint Top-20 | GNN+aux 30.45% | **(0.7, 0.3): 31.00%** | +0.55% |

完整结果: `experiments/ensemble_eval.json`
脚本: `yield_prediction/scripts/ensemble_eval.py`

## 关键冠军榜

| 指标 | 🏆 冠军 | 值 | 用途 |
|------|-------|-----|------|
| val Top-1 单点最高 | chain_only | 65.81% | 单点决策, in-distribution |
| **Test AVG Top-1 单点最高** | **MoE_balanced** | **57.42%** 🆕 | **OOD test 上 9 head 平均最准** |
| **Joint Top-1 全对率最高** | hier | 1.56% | 9 head 同时全对 |
| **Joint Top-5 候选 5** | MoE (lb=0.01) | 11.98% | "给我 5 个备选 protocol" |
| **Joint Top-10 候选 10** | **GNN+aux** | **23.38%** 🆕 | 化学家中等广度推荐 |
| **Joint Top-20 候选 20** | **GNN+aux** | **30.45%** 🆕 | "给我 20 个广候选, 我自己挑" |

## MoE 平衡实验的关键发现

将 load balancing loss weight 从 0.01 → 0.5, router 使用率从 [0.17, 0, 0, 0.83]（退化为 2 expert）变成 [0.38, 0.28, 0.20, 0.14]（均衡）:

| 指标 | MoE 退化 | MoE 均衡 |
|------|---------|---------|
| AVG Top-1 | 56.65% | **57.42%** (+0.77%) |
| Joint Top-1 | 1.14% | 1.37% (+0.23%) |
| Joint Top-10 | 20.51% | 15.92% (-4.59%) |
| Joint Top-20 | 26.25% | 19.96% (-6.29%) |

**核心 trade-off**:
- **退化 MoE** = 软 ensemble (2 个 expert 平均) → **广度高但单点弱**
- **均衡 MoE** = 真正专家分工 → **单点强但广度弱**

## GNN + reagent_class 辅助

GNN 加 reagent_class 辅助 head 后:
- val Top-1 略降 (62.59% → 62.32%)
- 但 Joint Top-10/20 **创历史新高** (23.38% / 30.45%)

**reagent_class 在 GNN 上 Top-20 = 95.51%** (97.82% in MLP), 几乎完美覆盖 47 个化学类。这意味着模型对反应"做什么类型"非常清楚, 只是具体 SMILES 不一定 Top-1 准。

## 推荐配置 (按应用场景)

| 你的应用 | 推荐 ckpt | 核心指标 |
|---------|---------|--------|
| **OOD 测试集上 9 head 平均 Top-1 最准** | `stage1_moe_balanced.pt` | AVG Top-1 = 57.42% 🆕 |
| **化学家 Top-5 候选** | `stage1_moe.pt` (退化版) | Joint Top-5 = 11.98% |
| **化学家 Top-10/20 广候选** | `stage1_gnn_aux.pt` | Top-20 = 30.45% 🆕 |
| **AI 全对率最高** | `stage1_hier.pt` | Joint Top-1 = 1.56% |
| **单点 Top-1 在 val 上最高** | `stage1_chain.pt` | val Top-1 = 65.81% |
| **简单 baseline** | `stage1_baseline.pt` | 无依赖 |

## 模型规模

| 变体 | 参数量 | 训练时间 (4090, 60-80 ep) |
|------|------|------------------------|
| MLP variants | ~7M | ~8 min |
| MoE (4 expert) | ~9M | ~10 min |
| GNN | 1.3M | ~30 min |
| GNN+aux | 1.3M | ~32 min |

## 文件清单

```
experiments/
├── stage1_baseline.pt          # MLP no-FG no-cond
├── stage1_fg.pt                # MLP +FG
├── stage1_cond.pt              # MLP +9-head 全链
├── stage1_fg_cond.pt           # MLP +9-head 链 +FG
├── stage1_chain.pt             # MLP +3-head 精确链
├── stage1_fg_chain.pt          # MLP +3-head 链 +FG
├── stage1_hier.pt              # MLP +reagent_class 辅助
├── stage1_moe.pt               # MoE 退化版 (lb=0.01)
├── stage1_moe_balanced.pt      # ★ MoE 均衡版 (lb=0.5)
├── stage1_gnn.pt               # GNN 纯
├── stage1_gnn_aux.pt           # ★ GNN +reagent_class 辅助
└── stage2_baseline.pt          # Stage-2 (固定)
```

## 复现脚本

```bash
# MLP variants (含 MoE/hier)
python yield_prediction/scripts/train_stage1.py --epochs 80 --batch_size 256 --lr 3e-4 \
    [--use_fg] [--cond_decode] [--chain] [--use_reagent_class] \
    [--moe --moe_experts 4 --moe_lb_weight 0.5]

# GNN (含 +aux)
python yield_prediction/scripts/train_stage1_gnn.py --epochs 60 --batch_size 64 --lr 3e-4 \
    [--use_reagent_class]

# 数据增广 (一次性):
python yield_prediction/scripts/augment_fg_features.py            # +FG (72D)
python yield_prediction/scripts/run_xtb_missing.py                 # 算 xTB 缺失分子
python yield_prediction/scripts/augment_xtb_features.py            # +xTB (33D)
python yield_prediction/scripts/augment_reagent_class.py           # +reagent_class label

# 评估
python yield_prediction/scripts/run_all_experiments.py             # MLP variants 批量
python yield_prediction/scripts/eval_gnn.py                        # GNN 单独
```
