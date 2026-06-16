# condition_agent —— 电化学烯烃双官能化反应条件智能体

> 项目说明（目的 + 现状进展）
> 生成日期：2026-05-30
> 依据：`README.md`、`config.py`、`MODEL_ARCHITECTURES_CN.md`、`yield_prediction/MODEL_REPORT.md`、`yield_prediction/eval_results/EVALUATION_REPORT.md`、`eval_results/llm_ablation_sonnet46_full/REPORT.md` 以及 `agent/`、`rag/`、`bayesian_opt/` 等源码与评测结果。

---

## 1. 项目目的（这个项目要解决什么）

给定一个**化学反应（SMILES 格式）**，自动推荐一整套最优的**电化学实验条件**，并给出可执行的实验方案。具体要预测 7（~9）类条件：

- 阳极 (anode)、阴极 (cathode)、电池类型 (cell_type)
- 电解质 (electrolyte)、溶剂 (solvent)、试剂 (reagent)、催化剂 (catalyst)
- （新数据中还扩展了 ligand 配体、additive 添加剂）

聚焦的化学领域是**烯烃（olefin/alkene）的电化学双官能化反应**。除了推荐条件，系统还能：

1. **预测产率**（给定一套条件估计产率 0–100%）
2. **生成多样化的候选条件组合**（CVAE）
3. **检索文献中相似的已知反应**（FAISS 相似度搜索）
4. **贝叶斯优化**：在"试一组→看产率→再试"的迭代实验场景里做主动学习
5. **化学推理与方案合成**：用 Claude 大模型把上述工具的输出融合成最终建议 + 实验规程（含安全提示）

核心设计哲学：**三个互补的小 ML 模型 + 检索库 + 贝叶斯优化层 + 一个大模型（Claude）做中央编排**。融合逻辑不写死在代码里，而是由 LLM 通过 ReAct（思考→调工具→观察→再思考，最多 15 轮）推理完成。

---

## 2. 系统架构总览

```
用户查询（反应 SMILES）
        │
        ▼
Claude 大语言模型（中央控制器，ReAct 循环，可调用 11 个工具）
   ├── 化学分析：validate_smiles / parse_reaction / analyze_reaction_chemistry
   ├── ML 推理：recommend_conditions_default(M1) / generate_conditions_cvae(M2) / predict_yield(M3)
   ├── 检索：search_similar_reactions（FAISS）
   ├── 输出：estimate_experimental_parameters / generate_experimental_protocol / draw_reaction
   └── 优化：optimize_conditions_bo（贝叶斯优化，suggest/observe/search/rerank 四模式）
        │
        ▼
贝叶斯优化层（BayesianConditionOptimizer：GP 代理 + 采集函数 + warm-start）
        │
        ▼
三个互补 ML 模型 + FAISS 检索库
```

### 四类核心组件的分工

| 组件 | 回答什么问题 | 实现 |
|------|------------|------|
| **M1** ConditionRecommenderXTB | "各类条件各自的最佳选择？" | 双编码器(指纹6144 + xTB 33) → 7 个独立分类头，各自 top-k（精度优先）|
| **M2** CategoricalCVAE | "哪些条件组合在一起兼容？" | 采样潜变量 z → 解码 7 条件联合分布（多样性 / 兼容性）|
| **M3** YieldPredictor | "这套组合能跑多少产率？" | 4 层 MLP 回归（打分 / 排序 / 作 BO 先验）|
| **FAISS RAG** | "文献里相似反应用了什么条件？" | 6144 维反应指纹余弦相似度检索 |
| **BO 层** | "下一步做哪个实验信息量最大？" | sklearn GP（残差学习）+ EI/UCB/Thompson 采集函数 |
| **Claude** | "综合所有证据到底推荐什么？" | 工具输出 + 领域知识推理融合，并做化学兼容性校验 |

### 共享特征工程
- **Morgan 指纹 (ECFP4, radius=2, 2048 位)**：反应指纹 = [反应物 | 产物 | 差值] = 6144 维
- **xTB 量子化学描述符 (33 维)**：每分子 6 个 xTB 量子特征（HOMO/LUMO/gap/能量/偶极/Gsolv）+ 5 个 RDKit 描述符；三级回退策略（查预计算 CSV → 在线调 xTB binary → 填 0）

---

## 3. 目录结构（关键部分）

```
condition_agent/
├── main.py / demo.py           # CLI 入口（交互 / 一次性）/ 免 API key 的工具演示
├── web_app.py                  # Gradio Web UI
├── run_daemon.sh               # 后台守护
├── config.py                   # 全局配置、模型路径、标签映射、AgentConfig
├── build_index.py              # 构建 FAISS 索引
│
├── agent/                      # ReAct 智能体核心
│   ├── loop.py                 # ElectrochemAgent（LLM + 工具循环）
│   ├── tools.py                # 11 个工具实现（含 BO 入口）
│   ├── prompts.py              # 系统提示 + 工具 schema
│   └── debate_*.py             # "辩论模式"（多智能体辩论，2026-03 加入）
│
├── rag/                        # 检索增强
│   ├── retriever.py            # 反应相似度检索（ReactionRetriever）
│   ├── mechanism_retriever.py  # 机理库检索（2026-05 新增）
│   └── index_builder*.py       # 索引构建（v3 / paper 级零泄漏版）
│
├── bayesian_opt/               # 贝叶斯优化层（2026-04 新增）
│   ├── optimizer.py / surrogate.py / acquisition.py
│   ├── space.py / warm_start.py / priors.py
│   └── RAG_PRIOR_DESIGN.md
│
├── yield_prediction/           # ML 模型定义、训练、特征提取、评测
│   ├── models/                 # M1/M2/M3 + 大量实验性变体（见 §6）
│   ├── utils/                  # 特征提取、xTB、电极/试剂分类器等
│   ├── scripts/                # 数据准备、训练、评测、LLM ablation 脚本
│   ├── checkpoints/            # 训练好的权重
│   ├── data_audited_v3_clean/  # 严格零泄漏的审计后数据集（当前主用）
│   └── eval_results/           # 评测产物
│
├── eval_results/               # LLM ablation 等顶层评测（2026-05）
└── data/                       # 反应数据、FAISS 索引、机理 KB
```

---

## 4. 已实现的能力（功能进展）

- ✅ **完整的 ReAct 智能体**：11 个工具，支持交互式 CLI / 一次性模式 / Gradio Web UI / 后台守护
- ✅ **三个 ML 模型上线**（M1/M2/M3）并配 lazy-loading 管理
- ✅ **FAISS 检索库**：从全量烯烃反应 JSON 构建（精确 IndexFlatIP）
- ✅ **贝叶斯优化层**（2026-04）：GP 残差学习 + 三种使用模式（迭代实验 / 离线自动搜索 / M1 候选重排），无需训练、在线拟合
- ✅ **辩论模式**（2026-03）：多智能体辩论编排
- ✅ **机理知识库 + 机理检索**（2026-05）：534 篇论文由 LLM 离线预读全文提取机理 JSON（机理家族、电子流、限速步、关键中间体、证据类型等）
- ✅ **LLM 后端可切换**：Anthropic 或 OpenAI 兼容端点（vLLM）；默认模型 `claude-opus-4-6`
- ✅ **系统化评测体系**：条件推荐 top-k、基线对比、F1、联合匹配、产率排序、消融实验、LLM ablation

---

## 5. 模型与实验结果（性能进展）

### 5.1 数据集演进
- 早期：`alkene_reactions_by_yield`（10,635 条有效反应）+ extracted_smiles 失败反应，80/10/10 划分（test 1064 条）。**已知存在数据泄漏**：11 条 test 与 train 完全重复，反应级重叠约 13.3%。
- 当前主用：**`data_audited_v3_clean`** —— 严格的 **paper + SMILES 双零泄漏切分**（按论文划分，2025+ 论文做 test，DOI 大小写归一化），118 test paper / 2947 test 反应。
- 检索/机理底库：`reactions_by_journal_alkene_ec_audited`，**24,564 反应 / 2,617 paper**；机理库 534 paper。

### 5.2 三个模型的实测表现（2026-04-19，旧 test.pt 1064 条）

| 模型 | 关键指标 | 结论 / 定位 |
|------|---------|------------|
| **M1** ConditionRecommenderXTB | 平均 Top-1 **0.677** / Top-3 0.852 / Top-5 0.890；7 项里 6 项显著超过"最频类"基线 | Agent 默认条件推荐器（骨干）|
| **M2** CategoricalCVAE | 平均 Top-1 0.458；联合 7/7 精确匹配 **0%**；生成多样性 0.991 | 仅做兼容组合的 B-方案生成器，不做主推；可被裁剪 |
| **M3** YieldPredictor | 用 M1 条件喂入时预测产率 56.1% vs 真值 57.8%，相关 0.725（7/7 子集 0.859）| **只作产率估计器 / BO 先验**，不能单独给 M1 候选排序（会把准确率从 0.668 砸到 0.344）|

关键发现（来自评测报告）：
- **长尾问题严重**：electrolyte/reagent/catalyst 类别极多且分布倾斜，Macro-F1 远低于 Weighted-F1，尾部类几乎学不到 → 这正是 RAG / 机理库要补的地方。
- **cell_type 头打不过"无脑猜 undivided"基线**（−0.133），可用简单规则替代。
- **消融结论**：RAG 是最有价值的模块（RAG_ONLY 0.701 ≈ FULL 0.696，M1+RAG 0.703 最优）；CVAE 贡献边际（oracle 仅 +2.63%），YieldPredictor 对 top-1 选择零贡献、价值在排序/估值。

### 5.3 V3 两阶段模型（2026-05-21，当前最佳条件模型）
- 架构：Hier+Set（层次化 + 集合预测）+ Ligand/Additive SMILES 头 + 精细电极分类，权重 `checkpoints/two_stage/stage1_hier_set_v3_smi_fineE.pt`。
- 严格零泄漏数据上：Stage-1 综合 score **0.5350**，平均单项 **68.65%**，catalyst 集合 F1 **58.54%**。

### 5.4 LLM Ablation 实验（2026-05-26，最新里程碑）
在 **全量 2947 条零泄漏 test 反应**上，用 Claude Sonnet 4.6（温度 0）量化"反应库 / 机理库"对大模型条件预测的实际帮助，分三组：
- **A** 纯 LLM 内置知识（只给反应 SMILES）
- **B** A + 反应库 top-5 相似反应及其条件
- **C** B + 机理库（seed 机理 + 机理相似 paper top-3）

| 组别 | 平均单项命中率 | 净增益 |
|------|:---:|:---:|
| A 纯 LLM | 0.361 | — |
| B +反应库 | 0.407 | **+4.6 pp** |
| C +机理库 | 0.433 | 全量 +2.6 pp |

- **反应库**增益最大的恰是 M1 最弱的长尾项：reagent +9.9、solvent +8.9、cathode +8.6、electrolyte +6.4。
- **机理库**：全量口径只覆盖 46.8% 反应（机理库尚不全），但在**真正拿到机理的 1380 条子集上净增益 +5.4 pp**（每项都正增益），且能把 B 组被相似反应噪声带偏的 cell_type/catalyst 修回来。
- A→C 整体单项 0.361→0.433，**相对提升约 +20%**。
- 产物：`eval_results/llm_ablation_sonnet46_full/`（raw_results.json、aggregate.json、2947 条逐反应 md、6 张图表、REPORT.md）。

---

## 6. 实验性 / 未部署的工作
`yield_prediction/checkpoints/` 下有大量已实现但**未在 config.py 启用**的变体：
- 条件推荐：ConditionRecommender(旧)、DualTowerCondRec、CompactCondRec、ConditionVAE、JointYieldCondModel
- 产率预测：ResNet / Transformer / AttentionMLP / DualTower(±xTB) / Highway / Ensemble / GIN / MoE / 聚类(K-Means per cluster) / 两阶段 / 对比学习
- Qwen3-8B SFT 数据集（`data_qwen_sft_v3/`）与训练日志 —— 探索过用开源 LLM 微调做条件预测

---

## 7. 基础设施
- PyTorch 2.8+ / Python 3.12 / 单 CUDA GPU
- RDKit（指纹、描述符、可视化）、FAISS（检索）、scikit-learn GP + scipy（BO）、xTB（量子描述符）
- Gradio Web UI、后台守护脚本、pytest 测试（`tests/`、`bayesian_opt` 自带测试）

---

## 8. 当前结论与下一步方向

**已经验证的核心论点**：
1. 多模型 + 检索 + LLM 编排的范式有效；**RAG（反应库）是最关键的增益来源**，尤其对长尾条件。
2. **机理库正交且有效**，扩库后潜力更大（当前覆盖率 46.8%，机理 KB 仅 534 paper）。
3. M1 是可靠骨干；M2(CVAE) 可裁剪；M3 只能做估值不能做选择。
4. 严格的**零泄漏数据切分**是可信评测的前提，旧数据集存在 ~13% 反应级泄漏。

**可见的下一步**（基于报告中的明确建议）：
- 把机理知识库从 534 paper 扩到全库，提升机理覆盖率与整体增益。
- 推进 V3 两阶段 / 集合预测模型，替换旧 M1+M2。
- 做严格 train-only FAISS 索引下的 BO / Agent 端到端召回评测。
- 简化系统：以 M1+RAG+置信度路由为主路径，按需调用 BO 与 LLM 推理。

---

> ⚠️ 说明：仓库内多数 `.py` 源文件与部分 `.md`（如 `main.py`、`MODEL_ARCHITECTURES_CN.md` 中后段）被大量重复占位注释（"# ── Project paths ──"、"（自动补充内容）"等）污染，建议后续清理。本文档的事实依据来自未被污染的配置、评测 JSON/REPORT 与文档前段实际内容。
</content>
</invoke>

result
The file /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/PROJECT_OVERVIEW.md is created successfully.
<system-reminder>
Warning: this is the last turn before the context window runs out. Reply briefly. Respond to the user, but you will not be able to make any more tool calls.