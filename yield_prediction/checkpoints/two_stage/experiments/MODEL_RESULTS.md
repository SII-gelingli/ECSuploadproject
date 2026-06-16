# 条件预测模型 Test 结果(分开报告)

**Test 集**: `data_audited_v3_clean/test.pt` = **2947 reactions**(paper+rxn 双零泄漏切分, 2025+ 论文)
**说明**: 两个模型评测口径不同,**不直接合表**,分开列出。

---

## A. 小模型 — `ConditionStage1HierSetV3` + SMI + FineE

- **ckpt**: `checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt`(epoch 51 / 80, val score 0.6495)
- **架构**: 6144D FP → (1024, 768, 512) → 多 head;参数量 ~10 M
- **输入**: 反应 SMILES → 6144 维 ECFP+条件指纹
- **输出**: 类别 ID(v3 分类设计的 ~170 个类) + set head(SMILES 集合)+ 4 个机制 tag
- **报告日期**: 2026-05-21([HIER_SET_V3_STRICT_NOLEAK_TEST_REPORT.md](HIER_SET_V3_STRICT_NOLEAK_TEST_REPORT.md))
- **原始结果**: [`hier_set_v3_smi_fineE_strict_noleak_test.json`](hier_set_v3_smi_fineE_strict_noleak_test.json)

### A.1 单类 head(softmax 多分类,报 top-1 / 3 / 5 准确率)

| 字段 | 类别数 | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| anode_material(材料家族) | 11 | **80.4%** | 95.7% | 98.0% |
| cathode_material(材料家族) | 11 | **55.5%** | 88.9% | 94.9% |
| cell_class_v3 | 3 | **75.9%** | 99.6% | — |
| anode_fine(细分写法) | 43 | 17.6% | 34.2% | 47.3% |
| cathode_fine(细分写法) | 49 | 30.2% | 53.8% | 61.7% |
| electrolyte_cation | 19 | 44.8% | 77.5% | 90.1% |
| electrolyte_anion | 23 | 27.8% | 55.8% | 74.5% |
| catalyst_class_v3 | 49 | **62.1%** | 80.0% | 85.1% |
| reagent_class_v3 | 103 | 31.1% | 46.1% | 51.1% |
| solvent_class_v3 | 23 | **42.8%** | 64.2% | 77.6% |
| ligand_class_v3 | 20 | **98.2%** | 99.4% | 99.4% |
| additive_class_v3 | 42 | **98.0%** | 98.5% | 98.5% |

**summary_single_avg7 = 0.687**(7 个主要单类 head 的 top-1 平均)

### A.2 具体 SMILES 单 head(ligand / additive 在词表上 softmax)

| 字段 | 词表大小 | top-1 | top-3 | top-5 |
|---|---:|---:|---:|---:|
| ligand(具体 SMILES) | 176 | **98.2%** | 98.6% | 98.6% |
| additive(具体 SMILES) | 104 | **98.0%** | 98.0% | 98.0% |

> 这两个字段绝大多数是 `ABSENT`,top-1 数值偏高主要是 absent 命中。

### A.3 Set head(SMILES 集合输出,catalyst / reagent / solvent 主体)

**架构**: K=4 slot,每 slot 输出 N+1 类(含 no_object),Hungarian matching 训练。
**口径**:
- **exact_set**(整库,严格): 模型 K=4 slot argmax 去重去 no_obj 得到的集合 == GT 集合
- **GT 非空 + exact**(真本事): 仅在 GT 集合去 `__ABSENT__` 后**非空**的反应上统计 — 排除 "GT=空,模型也空" 的白送命中
- **any (top-3)**: top-3 候选与 GT 至少 1 个重合(宽松参考)

| 字段 | exact_set (整库) | **GT 非空** | **set✓且 GT 非空** | **GT 非空命中率** | any (top-3) | F1 |
|---|---:|---:|---:|---:|---:|---:|
| catalyst_set | 58.26% | 1184 | **209** | **17.65%** | 70.14% | 58.5% |
| reagent_set | 25.72% | 2196 | **255** | **11.61%** | 42.04% | 27.2% |
| solvent_set | 19.38% | 2851 | **559** | **19.61%** | 70.89% | 40.2% |

### A.4 机制 tag(catalyst 上的正交多标签)

| Tag | Acc | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| mediator | 86.1% | 69.4% | 5.9% | 10.8% |
| photoredox | 99.6% | — | — | 0 |
| HAT | 99.9% | — | — | 0 |
| chiral | 99.5% | — | — | 0 |

> photoredox / HAT / chiral 在 EC test 集里基本零正样本,F1 = 0 是数据问题不是模型问题。

---

## B. 大模型 — Qwen3-8B + LoRA SFT

- **ckpt**: `checkpoints/qwen3_8b_clean_v1/`
- **架构**: Qwen3-8B + LoRA;输入反应 SMILES,直接生成 JSON 格式的条件描述
- **训练数据**: `data_qwen_sft_v3/`(同一份 19124 / 2234 / 2947 切分,JSONL 格式)
- **原始结果**: [`eval_results/qwen3_8b_clean_v1.json`](../../../../eval_results/qwen3_8b_clean_v1.json)
- **JSON 解析失败**: 1 / 2947(0.03%,可忽略)

### B.1 单字段(电极 / cell_type → 文本归一化后比类别)

| 字段 | 命中数 | 准确率 |
|---|---:|---:|
| anode | 947 / 2947 | **32.1%** |
| cathode | 1478 / 2947 | **50.2%** |
| cell_type | 2329 / 2947 | **79.0%** |

### B.2 多元素字段(SMILES 列表,canonical 化后比较)

- `_exact_set`(整库,严格): pred canonical 集合 == GT canonical 集合
- **GT 非空 + set✓**(真本事): 仅在 GT canonical 后**非空**的反应上统计
- `_any_overlap`: pred 与 GT 集合至少 1 个 SMILES 重合(宽松参考)
- `_first`: 第 1 个 SMILES 匹配(顺序敏感,仅供参考)

| 字段 | exact_set (整库) | **GT 非空** | **set✓且 GT 非空** | **GT 非空命中率** | any_overlap | (参考) first |
|---|---:|---:|---:|---:|---:|---:|
| catalysts | 55.14% | 1180 | **318** | **26.95%** | 55.65% | 55.62% |
| reagents | 22.84% | 2193 | **283** | **12.90%** | 25.59% | 24.74% |
| solvents | 16.19% | 2851 | **469** | **16.45%** | 56.63% | 42.89% |
| electrolytes | 19.34% | 2587 | **569** | **21.99%** | 19.38% | 19.34% |

---

## C. 评测口径差异说明(为什么分开报告)

| 维度 | 小模型 | 千问 |
|---|---|---|
| **输出空间** | 闭集(v3 分类的 ~170 个类 + 具体 SMILES 词表) | 开集(生成任意 JSON 文本) |
| **anode/cathode** | 11 类材料家族 + 43/49 类细分(双口径) | 文本输出后归一化映射 |
| **cell_type** | v3 设计 3 类 | 文本归一化 |
| **catalyst/reagent/solvent** | v3 抽象类(49/103/23) + set head 元素级 F1 + top-K recall | 具体 canonical SMILES `_first` / `_exact_set` |
| **electrolyte** | 拆 cation(19)× anion(23)双 head | 整体 SMILES `_first` / `_exact_set` |
| **ligand/additive** | 单 SMILES 词表 top-K(176 / 104 类) | (未单独报告,绝大多数 ABSENT) |
| **set 评测** | 元素级 P/R/F1 + top-K recall(粒度更细) | 整 set 是否完全相等(更严格的 0/1) |
| **机制 tag** | mediator / photoredox / HAT / chiral 多标签 | 不输出 |

直接合表比较会产生**口径不一致的误读**(同样叫 "catalyst" 准确率,小模型给的是 49 类 top-1,千问给的是具体 SMILES `_first`,数值不可直接比)。如需统一比较,需要写一层口径转换脚本(把千问输出用 `classifier_v3` 映射到类别;或把小模型 set head top-K 取出来算 `_exact_set`)。

---

## D. 各字段最强结果(信息密度版)

仅作单点参考,不构成跨模型对比:

| 字段 | 小模型最佳 | 千问最佳 |
|---|---|---|
| anode 材料 | 80.4% (top-1, 11 类) | 32.1% (开放文本) |
| cathode 材料 | 55.5% (top-1, 11 类) | 50.2% (开放文本) |
| cell_type | 75.9% (top-1, 3 类) | 79.0% (开放文本) |
| catalyst | 62.1% (v3 类 top-1) / set 58.3% / top-20 recall 83.6% | first 55.6% / set 55.1% |
| reagent | 31.1% (v3 类 top-1) / set 25.7% / top-20 recall 65.0% | first 24.7% / set 22.8% |
| solvent | 42.8% (v3 类 top-1) / set 19.4% / top-20 recall 96.0% | first 42.9% / set 16.2% |
| electrolyte | cation top-1 44.8% × anion top-1 27.8% | first 19.3% / set 19.3% |
| ligand | 98.2% | (未单报) |
| additive | 98.0% | (未单报) |

---

## E. 真本事口径对比(GT 非空 + set✓,排除 ABSENT 白送)

整库 `_exact_set` 数被 "GT=空,模型也猜空"的反应严重稀释(catalyst 一半反应 GT 是空,只要模型学会"先猜 ABSENT"就能拿到 50%+ 准确率)。真正想看哪个模型**敢/能预测出非空集合且整集合都对**,只能在 **GT 非空子集**上比:

| 字段 | GT 非空数 (小/千) | **小模型 set✓ 且 GT 非空** | **千问 set✓ 且 GT 非空** | 比较 |
|---|---:|---:|---:|---|
| catalyst | 1184 / 1180 | **209** (17.7%) | **318** (26.9%) | **千问领先 50%** |
| reagent | 2196 / 2193 | **255** (11.6%) | **283** (12.9%) | 接近,千问微胜 |
| solvent | 2851 / 2851 | **559** (19.6%) | **469** (16.5%) | **小模型领先 19%** |
| electrolyte | — / 2587 | (小模型未单评,拆 cation+anion 双 head) | **569** (22.0%) | — |

**直觉解释**:
- **catalyst**: EC 反应一半不需要金属催化剂(GT=空),小模型 64.7% top-1 命中里很大一部分是学会"先猜 ABSENT"。千问反而更敢真猜出 Co/Fe/Cu 等具体催化剂。
- **solvent**: 几乎所有反应都有溶剂(只 96 个空),所以差距没被 ABSENT 稀释,小模型闭集 vocab 在常用溶剂上确实占优。
- **reagent**: 两者接近,反映 reagent 长尾难度高 — 哪个都不容易。
