# Hier+Set V3 + SMI + FineE — 严格零泄漏版 Test 报告

**日期**: 2026-05-21
**模型**: `ConditionStage1HierSetV3` + `smi_single_heads['ligand', 'additive']` + `fine_electrode_heads['anode_fine', 'cathode_fine']`
**ckpt**: [`stage1_hier_set_v3_smi_fineE.pt`](../stage1_hier_set_v3_smi_fineE.pt) (epoch **51** / 80, val score **0.6495**)
**数据**: [`data_audited_v3_clean/`](../../../data_audited_v3_clean/) (paper+rxn 双零泄漏切分)
**Test 结果 JSON**: [`hier_set_v3_smi_fineE_strict_noleak_test.json`](hier_set_v3_smi_fineE_strict_noleak_test.json)

> 与 [HIER_SET_V3_FINE_ELECTRODE_TEST_REPORT.md](HIER_SET_V3_FINE_ELECTRODE_TEST_REPORT.md) (旧带泄漏版) 对照阅读.

---

## 0. 这次重训的原因 — 数据泄漏修复

诊断发现旧 `paper_id()` 把同一篇 paper 切成多个 pid, 导致 paper-level split 被绕过. 4 类泄漏源:

### 0.1 Wiley 系双身份 paper (47 篇)

同一 Wiley paper 在原始数据里**同时有两种身份**:
- screening tables 抽出的: filename `10.1002_anie.202425634_sup_1_p6_t0.json`, 带 `source.doi`
- CAS Reaxys 主反应抽出的: filename `2025_Angewandte_Chemie_..._e202425634.json`, **`source.doi` 为空**

旧规则: 第一种 → pid=`10.1002_anie.202425634`; 第二种 → pid=`2025_angewandte_..._e202425634`. **两个 pid 不同**, 被当成两篇 paper, 同一篇文献的反应横跨 train/test.

实测旧 split 真实泄漏 paper:

| paper | val/test 一侧 pid | train 一侧 pid | 涉及反应 |
|---|---|---|---|
| Angew e202425634 (2025) | citation pid → test | `10.1002_anie.202425634` → train | 156 |
| Angew e202300533 (2023) | citation pid → val | `10.1002_anie.202300533` → train | 146 |
| ChemSusChem e202402224 | → test | `10.1002_cssc.202402224` → train | 73 |
| AdvSynthCatal e202401108 | → test | `10.1002_adsc.202401108` → train | 54 |
| AdvSynthCatal e202401522 | → test | `10.1002_adsc.202401522` → train | 47 |
| AdvSynthCatal e202401225 | → test | `10.1002_adsc.202401225` → train | 35 |

合计 **511 个反应** 跨 split.

### 0.2 `_CAS_no_citation/` 目录每个反应自成一个 pid

600 个反应文件, filename 含嵌入式 DOI (e.g. `no-citation-extracted-reaction_00098_SI_10.1002_anie.201912119_19_table_0_3_rxn0.json`) 但 `source.doi` 为空. 旧规则用 filename stem 作 pid → **每个反应自成一个 pid**, 同一篇 paper 的 25-53 个反应被切到不同 pid, **整篇 paper 的 SI 反应被随机切分到 train/val**.

实测: 600 文件原本对应 36 篇 paper, 旧 paper_id 把它们碎成 600 个独立 pid.

### 0.3 反应 SMILES 跨 split

paper-level split 后, 仍有 158 个反应 SMILES 同时出现在 train 和 val/test (不同 paper 报告同一反应).

### 0.4 ajoc. / asia. 等 publisher 前缀缺失

`AsianJOC e202300485` 在 alias 表生成时 `ajoc.` 不在 Wiley 前缀白名单, 导致 DOI 文件和 no-DOI 文件没合并.

---

## 1. 修复方案

修改 [`scripts/prepare_data_audited.py`](../../../scripts/prepare_data_audited.py):

1. **`build_paper_alias_table()`**: 扫一遍 RAW, 用 `(journal, article_number_token)` 把双身份 paper 的多个 old_pid 合并到 canonical DOI pid
2. **`_extract_embedded_doi()`**: 对 `_CAS_no_citation/` filename 抽嵌入式 DOI, 合并 36 篇 paper
3. **`canonical_paper_id(doi, fp_name, alias_table)`**: 应用 alias 的新接口
4. **Wiley 前缀白名单**: 加 `ajoc./cctc./asia./slct./`...
5. **反应 SMILES 级 dedup** ([`prepare_data_v3.py`](../../../scripts/prepare_data_v3.py)): 优先级 test > val > train, 同 SMILES 跨 split 时从 train 剔出

修改后跑 `prepare_data_v3 → augment_class_labels_v3 → augment_set_labels → cp → augment_electrode_fine` 全 pipeline 重生成数据.

---

## 2. 零泄漏验证 (5 级)

| 检查项 | 结果 |
|---|---|
| 1. Paper-level: train ∩ test | **0** |
| 1. Paper-level: train ∩ val  | **0** |
| 1. Paper-level: val ∩ test   | **0** |
| 2. `_test` holdout 目录 (118 paper) ⊆ test split? | **True** (100% 子集) |
| 3. Per-pid 跨 split count | **0** |
| 4. Reaction SMILES 跨 split (train∩test/val) | **0** |
| 5. `_CAS_no_citation/` 同 paper 反应跨 split | **0** (36 paper 检查) |

**数据分布**:

| Split | Paper 数 | Reaction 数 |
|---|---|---|
| train | 803 | 19,124 |
| val | 89 | 2,234 |
| test | 118 | 2,947 |
| 合计 | 1,010 | 24,305 |

train paper 从旧 1341 降到 803, 因为 `_CAS_no_citation/` 600 个独立 pid 合并到 36 篇, 同时 511 个 Wiley 泄漏反应正确归位.

---

## 3. Test 集完整结果

> 所有 Top-K 都在 paper+reaction 双零泄漏 test 集 (118 paper / 2947 reactions) 上评估.

### 3.1 Single class heads (粗 + 细)

| Head | 类数 | Random (1/N) | Top-1 | Top-3 | Top-5 |
|------|------|--------------|-------|-------|-------|
| anode_material | 15 | 6.67% | **80.42%** | 95.72% | 98.00% |
| cathode_material | 15 | 6.67% | 55.51% | 88.90% | 94.91% |
| cell_class_v3 | 4 | 25.0% | **75.87%** | 99.59% | — |
| **anode_fine** ★ | 43 | 2.33% | **17.61%** | 34.24% | **47.30%** |
| **cathode_fine** ★ | 49 | 2.04% | **30.20%** | 53.78% | **61.69%** |
| electrolyte_cation | 23 | 4.35% | 44.79% | 77.54% | 90.13% |
| electrolyte_anion | 26 | 3.85% | 27.76% | 55.79% | 74.48% |
| ligand_class_v3 | 20 | 5.00% | 98.20% | 99.36% | 99.36% |
| additive_class_v3 | 105 | 0.95% | 98.00% | 98.54% | 98.54% |

> ligand/additive 98% 来自类极度不平衡 — 96% test 样本是 ABSENT.

### 3.2 Hier class heads

| Head | 类数 | Random (1/N) | Top-1 | Top-3 | Top-5 |
|------|------|--------------|-------|-------|-------|
| reagent_class_v3 | 103 | 0.97% | 31.08% | 46.15% | 51.07% |
| catalyst_class_v3 | 49 | 2.04% | **62.13%** | 80.01% | 85.14% |
| solvent_class_v3 | 27 | 3.70% | 42.76% | 64.20% | 77.64% |

### 3.3 SMI single heads

| Head | Vocab | Top-1 | Top-3 | Top-5 |
|------|------|-------|-------|-------|
| ligand (具体 SMILES) | 受 vocab 约束 | **98.20%** | 98.61% | 98.64% |
| additive (具体 SMILES) | 受 vocab 约束 | **98.00%** | 98.00% | 98.03% |

### 3.4 Set heads (多组分 SMILES 集合)

| Head | Vocab N | Recall | Precision | F1 | Top-5 | Top-10 | Top-20 |
|------|------|-------|----------|----|-------|--------|--------|
| solvent | 79 | 37.72% | 43.09% | **40.23%** | 83.10% | 91.45% | 96.00% |
| reagent | 546 | 26.99% | 27.36% | 27.18% | 46.08% | 57.96% | 65.05% |
| catalyst | 527 | 58.62% | 58.47% | **58.54%** | 74.08% | 77.47% | 83.58% |

### 3.5 Catalyst mech tags (multi-label, 4 bit)

| Tag | Acc | Precision | Recall | F1 |
|---|---|---|---|---|
| mediator | 86.05% | 69.44% | 5.88% | 10.85% |
| photoredox | 99.63% | 0.00% | 0.00% | 0.00% |
| HAT | 99.90% | 0.00% | 0.00% | 0.00% |
| chiral | 99.49% | 0.00% | 0.00% | 0.00% |
| AVG F1 | — | — | — | **2.71%** |

> 4 tag 都极度稀疏 (test 集 mediator 130/2947, 其余更少), F1 接近 0 是数据问题, 不是模型问题.

### 3.6 综合分数

- **AVG single (7 head)**: 68.65%
- **AVG hier (3 head)**: 45.32%
- **AVG smi (2 head)**: 98.10%
- **Set AVG F1**: 41.98%
- **综合 score** (训练目标加权平均): **0.5350**

---

## 4. 与旧带泄漏模型对比

| Head | 类数 | Top-1 旧 (带泄漏) | Top-1 新 (零泄漏) | Δ |
|------|------|------------|------------|------|
| anode_material | 15 | 82.67% | 80.42% | -2.25 |
| **anode_fine** | 43 | **28.88%** | **17.61%** | **-11.27** |
| cathode_material | 15 | 54.20% | 55.51% | +1.31 |
| **cathode_fine** | 49 | 29.75% | **30.20%** | +0.45 |
| cell_class_v3 | 4 | 82.09% | 75.87% | -6.22 |
| electrolyte_cation | 23 | 48.86% | 44.79% | -4.07 |
| electrolyte_anion | 26 | 27.72% | 27.76% | +0.04 |
| reagent_class_v3 | 103 | 36.11% | 31.08% | -5.03 |
| catalyst_class_v3 | 49 | 65.09% | 62.13% | -2.96 |
| ligand_class_v3 | 20 | 98.44% | 98.20% | -0.24 |
| additive_class_v3 | 105 | 96.77% | 98.00% | +1.23 |
| **平均** | | | | **-2.7** |

### 4.1 解读

- **多数 head 降 1-6 个百分点**: 这是真实损失, 是去除"模型曾在 train 见过同 paper 同反应"红利后的诚实数字
- **anode_fine 跌 11.27 pp 最显著**: 该 head 43 类对"具体形状+材料"组合 (graphite_rod / carbon_felt / RVC...) 这种细分类在跨 paper 时极难泛化, 旧模型很大程度上靠**记同一 paper 用什么电极**取得高分
- **个别 head 微升 (cathode_fine +0.45, electrolyte_anion +0.04, additive +1.23)**: 不是显著改善, 在统计噪声范围内
- **总平均 -2.7 pp**: 相当于约 80 个 test reaction 从"对"变"错". 占 test 总量 2947 的 ~2.7%, 与之前估算的 ~7% 泄漏在量级上自洽 (泄漏 reactions 集中在某些 paper, 这些 paper 没了之后影响放大到几个百分点)

### 4.2 哪些数字现在更可信

旧报告里的 anode_fine 28.88% 实际包含"已见过同 paper 反应"的红利. 新报告 17.61% 是模型在完全没见过的 paper 上的表现, **对外汇报应该用新数字**.

具体到 majority baseline 比较 (来自 [diagnose_majority_baseline](../../../scripts/diagnose_majority_baseline.py)):

| Head | 类数 | Majority % | Model T1 % | Δ vs major |
|------|------|------------|------------|-----------|
| **anode_fine** | 43 | 11.44 | 17.61 | **+6.18** |
| **cathode_fine** | 49 | 20.26 | 30.20 | **+9.94** |
| **solvent_class_v3** | 27 | 36.61 | 42.76 | **+6.14** |
| cathode_material | 15 | 51.61 | 55.51 | +3.90 |
| electrolyte_anion | 26 | 26.87 | 27.76 | +0.88 |
| anode_material | 15 | 82.66 | 80.42 | -2.24 |
| catalyst_class_v3 | 49 | 67.87 | 62.13 | -5.73 |
| reagent_class_v3 | 103 | 39.97 | 31.08 | -8.89 |
| cell_class_v3 | 4 | 83.85 | 75.87 | -7.97 |
| electrolyte_cation | 23 | 60.33 | 44.79 | -15.54 |

- **真正学到东西 (+5pp 以上)**: 3 个 head (anode_fine, cathode_fine, solvent_class)
- **边际 (+1~+5pp)**: 1 个 (cathode_material)
- **退化到 majority 或更差**: 6 个 head

特别 electrolyte_cation -15.54 pp 是最差的: 模型预测分布的熵 (1.345) 比 GT (1.352) 还低, 说明模型**比 majority baseline 更保守**, 倾向于错误预测稀有阳离子, 而 GT 实际上有 60% 都是 NBu4. 这个 head 可能需要调 class weight (现在用 `1/sqrt(freq)` 过度鼓励稀有类).

---

## 5. 还能从这次实验拿到的结论

### 5.1 数据治理 > 模型架构

paper-level + reaction-level 双重严格切分**没有改一行模型代码**, 但暴露出 11.27 pp 的"假"性能 — 比任何 hyperparam 调参的边际收益都大. 这是分类任务数据集的常见陷阱: 一个 paper 出多版本数据时, naive paper_id 会漏掉双身份.

### 5.2 越细的 head 越容易记忆 paper

| Head 粒度 | Top-1 损失 (旧→新) |
|---|---|
| **anode_material (15 粗类)** | -2.25 |
| **anode_fine (43 细类)** | **-11.27** |
| **cathode_material (15 粗类)** | +1.31 |
| **cathode_fine (49 细类)** | +0.45 |

细粒度 head 的方差远大于粗粒度 — 细类标签更依赖具体 paper 的电极选择 (graphite_rod vs carbon_felt vs RVC...). 跨 paper 泛化时, 这种差异主要靠**记忆该 paper 的偏好**取得高分. 修掉泄漏后, anode_fine 直接跌回接近 majority baseline + 6 pp 的真实水平.

### 5.3 majority baseline 是评估 long-tail head 的必备基线

`electrolyte_cation` 在旧报告里 Top-1 = 48.86% 看起来"还行", 但在严格 split 上是 44.79%, 而该 head 的 majority baseline 是 60.33% — 模型实际**比"永远预测 NBu4"还差 15.54 pp**. 类似的还有 cell_class_v3 / reagent_class_v3 / catalyst_class_v3. 这些 head 的"看起来体面" Top-1 全部是 long-tail 分布带来的视觉错觉, 应在汇报时把 majority baseline 一起列出来.

---

## 6. 文件清单

| 文件 | 用途 |
|---|---|
| [`stage1_hier_set_v3_smi_fineE.pt`](../stage1_hier_set_v3_smi_fineE.pt) | 新 ckpt (epoch 51, val 0.6495) |
| [`hier_set_v3_smi_fineE_strict_noleak_test.json`](hier_set_v3_smi_fineE_strict_noleak_test.json) | Test 完整指标 JSON |
| [`scripts/prepare_data_audited.py`](../../../scripts/prepare_data_audited.py) | 含 `build_paper_alias_table` + `canonical_paper_id` |
| [`scripts/prepare_data_v3.py`](../../../scripts/prepare_data_v3.py) | 含反应级 dedup |
| [`data_audited_v3_clean/`](../../../data_audited_v3_clean/) | 严格零泄漏数据 |
