# 电化学条件智能体 — 模型架构说明

> 最后更新：2026-04-19
> 本文档基于 `condition_agent/config.py`、`bayesian_opt/` 与 `yield_prediction/models/` 的当前代码实际生成。

## 1. 系统功能概述

用户输入一个化学反应（SMILES 格式），系统自动推荐最佳电化学实验条件——阳极、阴极、溶剂、电解质、试剂、催化剂和电池类型，同时预测产率、提供不确定度、并生成完整的实验方案。

2026-04 起新增贝叶斯优化（BO）层：在三个 ML 模型与 FAISS 之上加一层 **GP + 采集函数** 主动学习闭环，可在迭代实验、离线搜索、以及对 M1 候选集重排三种模式下运行。

## 2. 体系总览：三个小模型 + 贝叶斯优化层 + 一个大模型

系统需要同时解决三个相互矛盾的问题：**准确性 vs. 多样性 vs. 可评估性**；加上 BO 层后还要解决 **利用 vs. 探索** 的权衡。单一模型无法兼顾，因此任务拆分为四层，由 Claude 大模型统筹。

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      用户查询（反应 SMILES）                              │
└────────────────────────────────┬─────────────────────────────────────────┘
                                 │
                                 ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                     Claude 大语言模型（中央控制器）                        │
│   ReAct 循环：思考 → 调用工具 → 观察 → 思考 …（最多 15 轮）                │
│                                                                          │
│   可调用 11 个工具：                                                       │
│   ┌────────────┐ ┌──────────────┐ ┌───────────────┐ ┌────────────────┐  │
│   │  化学分析  │ │  ML 推理     │ │   检索        │ │   输出生成     │  │
│   ├────────────┤ ├──────────────┤ ├───────────────┤ ├────────────────┤  │
│   │analyze_rxn │ │recommend_def │ │search_similar │ │estimate_params │  │
│   │validate    │ │generate_cvae │ │(FAISS,10635)  │ │gen_protocol    │  │
│   │parse       │ │predict_yield │ │               │ │draw_reaction   │  │
│   └────────────┘ └──────┬───────┘ └───────────────┘ └────────────────┘  │
│                         │                                                │
│                  ┌──────▼──────────────────────────┐                     │
│                  │   optimize_conditions_bo        │  ← 贝叶斯优化入口   │
│                  │   mode: suggest/observe/        │                     │
│                  │         search/rerank           │                     │
│                  └──────┬──────────────────────────┘                     │
└─────────────────────────┼────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                    贝叶斯优化层（BayesianConditionOptimizer）              │
│                                                                          │
│   GP 代理 (YieldSurrogate)  +  采集函数 (EI / UCB / Thompson)             │
│   ConditionSpace 编码（设备 one-hot 52D + PCA 分子指纹 4×64D ≈ 308D）    │
│   WarmStarter：FAISS 相似反应 + M1 top-k → 初始观测与候选池               │
└─────────────────────────┬────────────────────────────────────────────────┘
                          │ 调用
                          ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                       三个互补的机器学习模型                              │
│                                                                          │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────────┐ │
│  │  模型 ① (M1)     │ │  模型 ② (M2)     │ │     模型 ③ (M3)         │ │
│  │ ConditionRec-    │ │ CategoricalCVAE  │ │    YieldPredictor        │ │
│  │ ommenderXTB      │ │                  │ │                          │ │
│  │                  │ │                  │ │                          │ │
│  │ "每一类条件的    │ │ "哪些条件放在    │ │ "这套条件组合能跑出      │ │
│  │  最佳单项选择？" │ │  一起能协同？"   │ │  多少产率？"             │ │
│  │                  │ │                  │ │                          │ │
│  │ 精度优先         │ │ 多样性+兼容性    │ │ 打分、排序、BO 先验      │ │
│  └──────────────────┘ └──────────────────┘ └──────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

### 各组件角色

| 组件 | 回答什么问题 | 怎么做 |
|------|------------|--------|
| **M1** ConditionRecommenderXTB | "最好的阳极/溶剂/… 各自是什么？" | 7 个独立分类头，各自 top-k |
| **M2** CategoricalCVAE | "哪些条件组合起来兼容？" | 采样 z → 解码 7 条件联合分布 |
| **M3** YieldPredictor | "用这套具体组合，产率多少？" | 反应 + 条件 → 回归预测 |
| **FAISS** | "文献里相似反应用了什么条件？" | 余弦相似度检索 10,635 条已知反应 |
| **BO 层** | "下一步做什么实验信息量最大？" | GP 代理 + 采集函数，平衡利用与探索 |
| **Claude** | "综合所有证据，到底推荐什么？" | 工具输出 + 领域知识进行推理融合 |

**关键原则**：没有任何代码在硬编码融合规则——融合完全通过大模型推理实现。BO 层是 Claude 可选调用的工具，不是主路径。

---

## 3. 共享特征工程

三个 ML 模型共用同一套分子特征表示，由 `MolecularFeatureExtractor` 统一计算。BO 层另有独立的低维编码器（见第 7 节）。

### 3.1 Morgan 分子指纹（ECFP4）

```
SMILES → RDKit Mol → Morgan FP (radius=2, nBits=2048) → [2048D] 位向量
反应指纹 = [ 反应物指纹 | 产物指纹 | 差值指纹 ] = 6144D
diff_fp = product_fp - reactant_fp
```

### 3.2 xTB 量子化学描述符

> 实现：`yield_prediction/utils/xtb_features.py`（类 `XTBFeatureLookup`）

三级回退策略（`XTBFeatureLookup.get_features`）：

1. **查表优先**：优先从预计算 CSV `xtb_reaction_molecules.csv`（~14,513 个分子）中取 xTB QC 特征
2. **在线计算回退**：若分子不在 CSV 中，且 `XTB_BIN_PATH` 可执行，则实时调用 xTB：
   - RDKit 生成 3D 构象（`ETKDGv3`，maxIterations=500，失败则 `useRandomCoords`）
   - MMFF 力场优化（maxIterations=200）
   - 多片段 SMILES（盐类）→ 取最大片段 + 形式电荷
   - `subprocess` 调 xtb binary，`OMP_NUM_THREADS=1`、`MKL_NUM_THREADS=1`、超时 60 s
   - 正则从 stdout 解析 `TOTAL ENERGY / HOMO-LUMO GAP / HOMO / LUMO / molecular dipole / Gsolv`
   - 失败的 SMILES 会记录到 `_xtb_failed` 集合中，避免重复尝试
3. **兜底**：若 xTB 不可用或计算失败，xTB 特征填 0；RDKit 描述符仍可正常计算

每分子特征（11D）= 6 个 xTB QC 特征 + 5 个 RDKit 描述符：

| 类别 | 特征 |
|------|------|
| xTB（6D） | total_energy_Eh、homo_lumo_gap_eV、homo_eV、lumo_eV、dipole_total_Debye、gsolv_Eh |
| RDKit（5D，总是可用） | num_heavy_atoms、molecular_weight、num_rotatable_bonds、tpsa、logp |

反应级别：反应物(11D) + 产物(11D) + 差值(11D) = **33D**

### 3.2.1 xTB 相关环境变量（`config.py:112`）

```python
XTB_INSTALL_DIR = /inspire/hdd/global_user/gelingli-253114010248/xtb_install/xtb-dist
XTB_BIN         = $XTB_INSTALL_DIR/bin/xtb
XTBPATH         = $XTB_INSTALL_DIR/share/xtb
XTB_LIB         = $XTB_INSTALL_DIR/lib   # 追加到 LD_LIBRARY_PATH
XTB_TIMEOUT     = 60                     # 单次计算秒数上限
```

均可通过同名环境变量覆盖。首次调用时惰性检测 binary 是否存在与可执行，并打印一行日志。

### 3.3 条件标签编码（见 `config.py`）

| 条件 | 编码方式 | 类别数 | 说明 |
|------|---------|--------|------|
| 阳极 | 固定类别索引 | **23** | Carbon/Graphite/Pt/Glassy C/RVC/Ni/SS/Cu/Zn/Pb/Au/Ag/Fe/Mg/Al/Ti/Co/Pd/Sn/Nb/Hg/Pencil C/Unknown |
| 阴极 | 固定类别索引 | **23** | 与阳极相同类别表 |
| 电池类型 | 固定类别索引 | **6** | Undivided/Divided/Flow/Sealed/H-cell/Unknown |
| 电解质 | SMILES → 词表索引 | 101 | Top-100 + UNK |
| 溶剂 | SMILES → 词表索引 | 101 | Top-100 + UNK |
| 试剂 | SMILES → 词表索引 | 201 | Top-200 + UNK |
| 催化剂 | SMILES → 词表索引 | 101 | Top-100 + UNK |

推理时将 `UNKNOWN_INDICES` 对应的 logit 置 `-inf`（详见 `config.py:143`），避免推荐 "Unknown"。

> **注意**：模型类 `ConditionRecommenderXTB` 的构造器默认值仍写着 `num_anode=19`，但在线加载的权重和 config 约定的是 23 类——按 config.py 为准。

---

## 4. 模型 ① — ConditionRecommenderXTB（多头分类器）

> **文件**：`yield_prediction/models/condition_recommender.py`（类 `ConditionRecommenderXTB`）
> **权重**：`yield_prediction/checkpoints/condition_model/best_condition_model.pt`（由 `config.CONDITION_MODEL_PATH` 加载）
> **训练脚本**：`yield_prediction/scripts/train_condition_recommender.py`

### 4.1 功能

给定反应，独立预测 7 类条件中每一类的最佳选择。7 个头各自投票，共享隐层但彼此不协调。

### 4.2 网络结构

```
反应指纹 [B, 6144]                    xTB 特征 [B, 33]
         │                                      │
    fp_encoder                             xtb_encoder
    (6144→512→256)                         (33→64→64)
         │ [B, 256]                             │ [B, 64]
         └──────────── 拼接 ───────────────────┘
                         │ [B, 320]
                   fusion (320→256)
                         │ [B, 256]   （共享表示 h）
         ┌───────┬───────┬───────┬────────┬────────┬────────┬────────┐
       阳极    阴极    电池     电解     溶剂     试剂     催化
       (→23)   (→23)  (→6)     (→101)   (→101)   (→201)   (→101)
```

### 4.3 训练配置

| 项目 | 值 |
|------|---|
| 损失 | 7 个交叉熵之和 |
| 优化器 | AdamW (lr=1e-3, wd=1e-4) |
| 调度 | CosineAnnealingLR |
| 批大小 / 轮数 | 64 / 100（早停 20） |
| 选型标准 | 验证集 7 类平均 Top-1 |

### 4.4 性能（2026-04-19 生产权重 × test.pt，1064 条）

| 指标 | 值 |
|------|---|
| 平均 Top-1 | **0.677** |
| 平均 Top-3 | **0.852** |
| 平均 Top-5 | **0.890** |
| 平均 Top-10 | **0.931** |

逐条件、基线对比、ranking 联动指标详见第 14 节。

### 4.5 局限

7 个头彼此独立 → 可能产生不兼容组合（如 Pt + Br⁻）。这是引入 M2 和 BO 层的动因。

---

## 5. 模型 ② — CategoricalCVAE（联合条件生成）

> **文件**：`yield_prediction/models/condition_cvae.py`（类 `CategoricalCVAE`）
> **权重**：`yield_prediction/checkpoints/condition_model/best_cvae_condition_model.pt`（由 `config.CVAE_MODEL_PATH` 加载）

### 5.1 功能

生成完整的 7 条件**联合方案**并保证内部兼容性。采样不同潜变量 z 可产生多样化备选方案，每个方案附带联合概率分数。

### 5.2 网络结构

- **训练**：`[反应表示 | 条件 Embedding]` → VAE 编码器 → `μ, logvar` → 重参数化 → z → 解码器 → 7 个分类头重构
- **推理**：z ~ N(0, I) × temperature → `[repr | z]` → 解码器主干 → 7 个分类头 argmax
- 7 个头共享同一个 512D 解码主干输出，因此同一个 z 会同时"协调"7 个输出

潜变量维度 64D；反应编码器 `6144→512→256`；条件 Embedding 汇总 168D。

### 5.3 训练 / 性能

- 损失：`Σᵢ CEᵢ + β × KL`，β 在前 20 epoch 线性退火 0 → 0.1
- **test 集实测**（z=0）：平均 Top-1 = 0.458，Top-3 = 0.588；联合 7/7 精确匹配 = 0%，≥6/7 = 3.4%；生成多样性 0.991（详见第 14 节）
- 两种推理模式：`recommend()`（z=0 确定性）和 `generate(num_samples=10)`（采样生成）

---

## 6. 模型 ③ — YieldPredictor（MLP 回归器）

> **文件**：`yield_prediction/models/yield_predictor.py`（类 `YieldPredictor`）
> **权重**：`yield_prediction/checkpoints/best_model.pt`（由 `config.YIELD_MODEL_PATH` 加载，~65 MB）

### 6.1 功能

输入 = 反应 + 一套完整条件；输出 = 产率预测 (0–100%)。作为**候选方案评估器**，也作为 BO 层 GP 代理的**先验均值函数**。

### 6.2 结构

```
输入特征 [B, 10246]
├── 反应指纹            [6144D]
├── 溶剂指纹            [2048D]
├── 电解质指纹          [2048D]
└── 电化学参数            [6D]   (anode_idx, cathode_idx, current_mA,
                                  current_density, potential, cell_type_idx)

Linear(10246→512)+BN+ReLU+Drop(0.2)
Linear(512→256)+BN+ReLU+Drop(0.2)
Linear(256→128)+BN+ReLU+Drop(0.2)
Linear(128→1) → Sigmoid → ×100 → 产率
```

### 6.3 训练 / 性能

- 损失：MSE；优化器：AdamW；调度：CosineAnnealing w/ 5-epoch warmup
- test 集上用 M1_TOP1 预测条件喂入：预测产率均值 56.1%，真实均值 57.8%，Pearson 相关 0.725；在 M1 条件 7/7 全对的子集上，相关升至 0.859（详见第 14 节）

---

## 7. 贝叶斯优化层（`bayesian_opt/`）

> 目录：`condition_agent/bayesian_opt/`
> 工具入口：`optimize_conditions_bo`（`agent/tools.py:1074`）
> 暴露类：`BayesianConditionOptimizer`、`ConditionSpace`、`YieldSurrogate`、`AcquisitionOptimizer`、`WarmStarter`

### 7.1 为什么需要 BO 层

M1/M2/M3 都是**前馈推理**——没有"反馈闭环"。实际实验场景通常是：试一组条件 → 观察产率 → 更新认识 → 试下一组。这是 BO 的自然形态：
- 在少量观测下快速给出带不确定度的产率估计（**GP 代理**）
- 平衡"利用已知最优附近"与"探索未知空间"（**采集函数**）
- 不浪费已有的 M1/M3/FAISS 信息（**warm-start**）

### 7.2 ConditionSpace：条件编码

> `bayesian_opt/space.py`，总维度 ≈ 308D

| 段 | 编码 | 维度 |
|----|------|------|
| 阳极 | one-hot | 23 |
| 阴极 | one-hot | 23 |
| 电池类型 | one-hot | 6 |
| 溶剂 | Morgan FP → PCA | 64 |
| 电解质 | Morgan FP → PCA | 64 |
| 试剂 | Morgan FP → PCA | 64 |
| 催化剂 | Morgan FP → PCA | 64 |
| **合计** | | **308** |

- 每个分子类条件独立拟合一个 PCA（2048 → 64），基于词表全部 SMILES
- `decode` 用 PCA 空间余弦相似度最近邻将向量反映射回词表索引 + SMILES
- 提供 `sample_random`、`perturb`、`get_m1_candidates` 三种候选生成策略

### 7.3 YieldSurrogate：GP 代理（带先验均值）

> `bayesian_opt/surrogate.py`

**核心设计：残差学习**。GP 不是直接学产率绝对值，而是学 `观测 - YieldPredictor(cond)` 的残差。这样 M3 就变成了 GP 的**先验均值函数**，数据效率大大提高。

```
kernel = Constant × RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
alpha  = 1e-2      # 对角正则
normalize_y = True
n_restarts_optimizer = 3
MAX_OBSERVATIONS = 500   # 超过则保留最近 500 条
```

预测时：`predicted_yield = prior_mean(YieldPredictor) + gp_residual_mean`（裁剪到 [0, 100]）。

未拟合时返回 `(prior_mean, std=25)`——冷启动仍可用。

### 7.4 采集函数（`acquisition.py`）

| 名称 | 公式 | 用途 |
|------|------|------|
| **EI** | `(μ − y* − ξ) Φ(z) + σ φ(z)`, `z = (μ − y* − ξ)/σ` | 默认，ξ=0.01 |
| **UCB** | `μ + β σ` | β=2.0，探索偏重 |
| **Thompson** | 从 `N(μ, σ²)` 采样一次 | 简单多样化 |

`AcquisitionOptimizer.optimize` 对候选池计算采集值并按降序选 top-n。

### 7.5 WarmStarter：冷启动加速

> `bayesian_opt/warm_start.py`

避免"0 观测 0 候选"的冷启动：
1. **RAG 观测**：调用 `ReactionRetriever` 取 top-10 相似反应（阈值 0.3，按产率重排），把它们的 "条件 → 产率" 作为初始观测拟合 GP
2. **M1 候选**：调用 `ConditionRecommenderXTB` top-k，生成候选池（base = 全体 top-1；variants = 逐项换 top-2..k）
3. **常见溶剂混合物**：硬编码 9 种训练集高频混合溶剂（MeCN+H2O 等，占训练集 46.3%）作为额外候选

### 7.6 BayesianConditionOptimizer：三种使用模式

> `bayesian_opt/optimizer.py`

#### Mode 1 — 迭代实验（`suggest` / `observe`）

```python
opt.initialize(reaction_smiles)              # warm-start
next_conds = opt.suggest_next(n=3, acq_func='ei')
# 做实验…
opt.observe(conds_used, observed_yield)      # 更新 GP
next_conds = opt.suggest_next(...)           # 下一轮
```

候选池 = `M1 候选 + 随机采样填充到 pool_size + 最佳点的扰动`；去重后按采集函数排序。

#### Mode 2 — 离线自动搜索（`search`）

以 YieldPredictor 作为**虚拟 oracle**，全自动跑 n_iter 轮 BO。默认流程：
- Phase 1：评估 `n_initial_random=10` 个初始候选
- Phase 2：`n_iter=50` 轮迭代，每轮 suggest → M3 评估 → observe
- 返回按产率排序的前 10 条

#### Mode 3 — M1 候选重排（`rerank`）

不真正跑 BO，只用当前 GP 给 M1 候选打分：
```
combined = α × m1_prob + (1 − α) × normalized_UCB
```
默认 `α=0.5, β_UCB=1.5`。对快速推理场景很有用。

### 7.7 `optimize_conditions_bo` 工具参数

```python
{
  "reaction_smiles": "...",             # 必填
  "mode": "suggest" | "observe" | "search" | "rerank",
  "acq_func": "ei" | "ucb" | "thompson",  # 默认 ei
  "n_suggestions": 3,
  # mode=observe:
  "observed_conditions": {...}, "observed_yield": 85.0,
  # mode=search:
  "n_iter": 50,
  # mode=rerank:
  "candidates": [...], "m1_probs": [...], "alpha": 0.5,
}
```

BO 状态按 `reaction_smiles` 做键缓存在 `tools.py` 的 `_bo_states` 中，跨工具调用可持续化（通过 `get_state` / `load_state`）。

---

## 8. 检索模块 — FAISS 相似度搜索

> 文件：`rag/retriever.py`（类 `ReactionRetriever`）
> 索引：`data/faiss_index.bin`（~248 MB），`data/reaction_db.pkl`（~3.6 MB）
> 构建脚本：`build_index.py`

### 流程

```
查询反应 → 反应指纹 [6144D] → L2 归一化 → FAISS IndexFlatIP
   → 过滤相似度 > 0.3 → 可选产率感知重排（0.6×sim + 0.4×yield/100）
   → 返回 top-k 条件、产率、相似度
```

- 索引规模：**10,635** 条反应（2026-03 更新后，从 `alkene_reactions_by_yield` JSON 构建）
- 索引类型：`IndexFlatIP`（精确，无近似）
- 用途：条件查询工具本体 + BO 的 warm-start

---

## 9. 在线模型与权重汇总

| 模块 | 架构 / 类 | 权重 / 索引路径 | 配置常量 |
|------|----------|----------------|---------|
| M1 ConditionRecommenderXTB | 双编码器 + 7 头分类 | `yield_prediction/checkpoints/condition_model/best_condition_model.pt` | `CONDITION_MODEL_PATH` |
| M2 CategoricalCVAE | VAE + 7 头分类 | `yield_prediction/checkpoints/condition_model/best_cvae_condition_model.pt` | `CVAE_MODEL_PATH` |
| M3 YieldPredictor | 4 层 MLP | `yield_prediction/checkpoints/best_model.pt` | `YIELD_MODEL_PATH` |
| 多任务（可选） | 共享编码器 + 产率头 | `yield_prediction/checkpoints/multitask/best_model.pt` | `MULTITASK_MODEL_PATH` |
| ReactionRetriever | FAISS IndexFlatIP | `data/faiss_index.bin` + `data/reaction_db.pkl` | `FAISS_INDEX_PATH` / `REACTION_DB_PATH` |
| 词表 | JSON | `yield_prediction/data/vocab.json` | `VOCAB_PATH` |
| xTB 特征缓存 | CSV | `yield_prediction/data/xtb_reaction_molecules.csv` | `XTB_CSV_PATH` |
| BO ConditionSpace | PCA（每类分子独立拟合） | 在线拟合，不落盘 | — |
| BO YieldSurrogate | sklearn `GaussianProcessRegressor` (RBF + WhiteKernel) | 按 reaction_smiles 缓存在进程内 | — |

---

## 10. 实验性架构（已实现但未部署）

实验权重保存于 `yield_prediction/checkpoints/` 下，**不在 config.py 中引用**：

### 条件推荐变体
- `ConditionRecommender`（旧版，无 xTB）
- `DualTowerCondRec`（双塔 + 门控融合）
- `CompactCondRec`（PCA(FP)→128D + xTB）
- `ConditionVAE`（连续 VAE）
- `JointYieldCondModel`（条件+产率多任务）

### 产率预测变体
`ResNetPredictor` / `TransformerPredictor` / `AttentionMLP` / `DualTowerPredictor` / `DualTowerXTBPredictor` / `HighwayPredictor` / `CompactYieldPredictor` / `EnsemblePredictor` / `GINYieldPredictor` / `MoEYieldPredictor` / 聚类模型（K-Means per cluster） / 两阶段模型 / 对比学习

---

## 11. Claude Agent 工具总览（共 11 个）

> 源码：`agent/tools.py:65-78`

| # | 工具名 | 功能 |
|---|-------|------|
| 1 | `validate_smiles` | SMILES 合法性 / 结构校验 |
| 2 | `parse_reaction` | 反应 SMILES 拆分为反应物与产物 |
| 3 | `analyze_reaction_chemistry` | 烯烃、官能团、反应类型分析 |
| 4 | `recommend_conditions_default` | 调 **M1** 获得各类 top-k |
| 5 | `generate_conditions_cvae` | 调 **M2** 采样联合条件方案 |
| 6 | `predict_yield` | 调 **M3** 对具体组合打分 |
| 7 | `search_similar_reactions` | FAISS 检索相似反应 |
| 8 | `estimate_experimental_parameters` | 根据反应规模估算电流 / 电量 / 时间 |
| 9 | `generate_experimental_protocol` | 生成带安全注意事项的操作规程 |
| 10 | `draw_reaction` | RDKit 绘制反应图 |
| 11 | `optimize_conditions_bo` | **贝叶斯优化**（suggest/observe/search/rerank） |

---

## 12. 基础设施

| 项目 | 值 |
|------|---|
| GPU | 单块 CUDA GPU |
| 框架 | PyTorch 2.8+ |
| Python | 3.12 |
| 化学工具 | RDKit（指纹、描述符、可视化） |
| 检索 | FAISS |
| BO | scikit-learn GP + scipy.stats |
| 大模型 | Claude（`ANTHROPIC_BASE_URL` / 兼容 vLLM OpenAI 端点） |
| 默认模型 ID | `claude-opus-4-6`（通过 `ANTHROPIC_MODEL` 环境变量可改） |
| Web UI | Gradio（`web_app.py`） |
| 守护 | `run_daemon.sh` |

### AgentConfig 关键默认值（`config.py:162`）

```
max_tokens = 60000,    max_tool_rounds = 15
default_top_k = 3,     default_num_samples = 10
default_similarity_threshold = 0.3
bo_pca_dim = 64,       bo_default_acq_func = 'ei'
bo_default_n_similar = 10,   bo_default_m1_top_k = 5
```

---

## 13. 数据流水线与重训练

### 数据来源
- 主数据集：**10,635** 条电化学烯烃双官能化反应（`alkene_reactions_by_yield/`）
- 失败反应：**327** 条（产率=0，来自 `extracted_smiles.json`）
- 划分：80 / 10 / 10

### 完整重训练步骤

```bash
# 1. 原始 JSON → train/val/test.pt + vocab.json
python yield_prediction/scripts/prepare_data.py

# 2. 加 xTB 特征
python yield_prediction/scripts/prepare_data_xtb_enhanced.py

# 3. 加催化剂标签
python yield_prediction/scripts/add_catalyst_to_data.py

# 4. 训练 M1
python yield_prediction/scripts/train_condition_recommender.py --use_catalyst

# 5. 训练 M2
cd yield_prediction && python scripts/train_cvae_cat.py && cd ..

# 6. 训练 M3
cd yield_prediction && python scripts/train.py --model mlp

# 7. 重建 FAISS 索引
python build_index.py --no_train
```

BO 层**无需训练**——GP 在线拟合，PCA 根据词表即时拟合。

---

## 14. 测试集评测结果（2026-04-19）

> 权重：`yield_prediction/checkpoints/condition_model/{best_condition_model.pt, best_cvae_condition_model.pt}` + `checkpoints/best_model.pt`
> 数据：`yield_prediction/data/test.pt`（1064 条）
> 评测脚本：`yield_prediction/scripts/eval_condition_models.py` + `eval_yield_ranking.py`
> 结果目录：`yield_prediction/eval_results_20260419/`

### 14.1 数据划分与已知泄漏

- 划分：`prepare_data.py` 以 `random_state=42`、80/10/10 切分合并后的 alkene + extracted_smiles 数据 → train 8508 / val 1063 / test 1064
- 去重策略：`data_processor.py` 仅做 extracted_smiles vs alkene 跨源去重；**alkene 内部在 split 之前未去重**
- 实测泄漏：
  - test 与 train **完全重复条目**（反应 + 完整 7 条件 + 产率相同）：11 条
  - val 与 train 完全重复：8 条；test 与 val 完全重复：1 条
  - test 中 reactants+products 在 train 也出现过的条目：142 / 1064 ≈ **13.3%**（条件通常不同）
  - train 内部 (反应, 完整条件) 重复 >1 次的元组：45 个
- RAG 索引：`build_index.py --no_train` 从全量 alkene JSON 构建，**包含 test 反应**；评估 BO / Agent 召回类指标若用此索引会有检索级泄漏，需单独构 train-only 索引

### 14.2 M1 — ConditionRecommenderXTB

**Top-k（逐条件 + 平均）**

| Condition | Top-1 | Top-3 | Top-5 | Top-10 |
|-----------|-------|-------|-------|--------|
| anode | 0.660 | 0.882 | 0.934 | 0.987 |
| cathode | 0.818 | 0.932 | 0.963 | 0.996 |
| cell_type | 0.752 | 0.998 | 1.000 | 1.000 |
| electrolyte | 0.390 | 0.626 | 0.685 | 0.779 |
| solvent | 0.668 | 0.835 | 0.886 | 0.934 |
| reagent | 0.661 | 0.809 | 0.848 | 0.885 |
| catalyst | 0.790 | 0.882 | 0.911 | 0.935 |
| **AVERAGE** | **0.677** | **0.852** | **0.890** | **0.931** |

**基线对比（Top-1）**

`Random` = 1 / num_classes（均匀瞎猜）；`MostFreq` = 永远预测 train 中该条件最高频的类（准确率 = 该类在 test 中的占比）；`Lift` = Model − MostFreq。

| Condition | Random | MostFreq | Model | Lift |
|-----------|--------|----------|-------|------|
| anode | 0.043 | 0.332 | 0.660 | **+0.328** |
| cathode | 0.043 | 0.577 | 0.818 | +0.241 |
| cell_type | 0.167 | **0.885** | 0.752 | −0.133 |
| electrolyte | 0.002 | 0.162 | 0.390 | +0.228 |
| solvent | 0.009 | 0.438 | 0.668 | +0.230 |
| reagent | 0.002 | 0.467 | 0.661 | +0.194 |
| catalyst | 0.003 | 0.734 | 0.790 | +0.056 |

关键观察：
- **cell_type 输给 MostFreq**：该头仅 6 类且分布极不均，无脑猜 H-cell 就能拿 88.5%，M1 反而被"学习"拖累（Macro-F1=0.264 说明它在少数类上犯错换来了总错误率）
- **catalyst Lift 很低**（+0.056）：MostFreq 已 73.4%，说明标签极度倾斜，大多数反应都用同一催化剂
- **electrolyte 绝对值低**（0.390）但 Lift 仍显著（+0.228）：101 类长尾分布，模型相对基线进步很大

**F1 汇总**

| Condition | Macro-F1 | Weighted-F1 | 实际类别数 |
|---|---|---|---|
| anode | 0.508 | 0.645 | 16 |
| cathode | 0.435 | 0.803 | 18 |
| cell_type | 0.264 | 0.796 | 6 |
| electrolyte | 0.113 | 0.332 | 161 |
| solvent | 0.235 | 0.647 | 59 |
| reagent | 0.222 | 0.576 | 165 |
| catalyst | 0.188 | 0.744 | 102 |

Macro-F1 与 Weighted-F1 巨大差距（e.g. catalyst 0.188 vs 0.744）印证长尾分布下"尾部类几乎学不到"。

### 14.3 M2 — CategoricalCVAE

**Top-k（z=0，逐条件 + 平均）**

| Condition | Top-1 | Top-3 | Top-5 | Top-10 |
|-----------|-------|-------|-------|--------|
| anode | 0.330 | 0.586 | 0.712 | 0.865 |
| cathode | 0.579 | 0.756 | 0.828 | 0.974 |
| cell_type | 0.885 | 0.997 | 0.999 | 1.000 |
| electrolyte | 0.023 | 0.046 | 0.073 | 0.213 |
| solvent | 0.215 | 0.463 | 0.531 | 0.678 |
| reagent | 0.437 | 0.507 | 0.514 | 0.557 |
| catalyst | 0.734 | 0.760 | 0.768 | 0.784 |
| **AVERAGE** | **0.458** | **0.588** | **0.632** | **0.724** |

**联合匹配（所有 7 项同时命中）**

| 指标 | 值 |
|---|---|
| 7/7 精确匹配 | **0.0%** |
| ≥6/7 部分匹配 | 3.4% |
| ≥5/7 部分匹配 | 12.7% |
| 平均命中条件数 | 3.20 / 7 |
| 生成多样性（10 样本） | 0.991 |

**判读**：M2 在 test 集上每条件单独看弱于 M1（0.458 vs 0.677），且 7/7 完全命中为 0。生成多样性 0.991 说明采样空间很宽。所以 M2 真正的价值不在 Top-1 精度，而在作为 Agent 层 **B-方案生成器**：用它 sample N 个兼容的替代组合喂给 M3 / BO，而不是取代 M1。

### 14.4 M3 — YieldPredictor × Ranking 策略

M3 单独回归指标没做"真条件 → 真产率"的独立评估；下表是在 M1 推理产出的条件上评估 M3 作为 ranking 器的效果。

**Ranking 策略对比（1064 测试条，851 成功 featurize）**

| Strategy | AvgTop1 | Joint 7/7 | PredYld(%) | Correlation |
|---|---|---|---|---|
| **M1_TOP1（基线）** | **0.668** | **0.067** | 56.1 | **0.725 / 0.859(7/7 子集)** |
| M1_TOP3_PROB | 0.668 | 0.067 | N/A | — |
| M1_TOP3_YIELD | 0.344 | 0.000 | 98.3 | 0.171 |
| M1_TOP5_YIELD | 0.279 | 0.000 | 98.5 | 0.173 |
| M1_TOP3_COMBINED（0.5y+0.5p） | 0.668 | 0.067 | 97.8 | 0.190 / 0.375(7/7) |
| M1_TOP3_COMB_A03（0.3y+0.7p） | 0.668 | 0.067 | 97.8 | 0.190 / 0.375(7/7) |

**关键结论**

1. **单用 M3 对 M1 的候选 re-rank 会把 AvgTop1 从 0.668 拉到 0.344**（M1_TOP3_YIELD）。Per-condition 分解里 anode Δ=−0.546，cathode Δ=−0.666，cell_type Δ=−0.690 —— M3 倾向于把冷门高产率组合排到前面，偏离实验实际使用的条件。
2. **纯凭真值对比**：M3 预测产率平均 98%+（顶到天花板），而真实均值只有 57.8%；相关系数 0.17 表示 M3 在"任意 (反应, 条件)"上预测无偏排序能力很差。
3. **M1_TOP1 本身自带强 ranking 信号**：预测产率 56.1% vs 真 57.8%，相关 0.725；在 M1 7/7 全对的子集上甚至 0.859。说明 M1 挑选的条件本身就是高产率条件。
4. **Combined 策略 (0.5/0.5, 0.3/0.7)** 看起来数字不变，是因为 M1 给 Top-1 的概率一般远高于 Top-2/3，概率项 dominates ranking。
5. **设计启示**：M3 不应直接用于排序 M1 的 Top-k 备选，而应作为 **BO 层 GP 的先验均值**（空间足够大时 GP 残差拟合能补偿）、或仅用于最终候选的"产率数值估计"展示。

### 14.5 综合结论

| 模型 | 独立表现 | 建议用途 |
|------|---------|---------|
| M1 | AvgTop-1 0.677，Lift 6/7 显著为正 | Agent 默认条件推荐器 |
| M2 | AvgTop-1 0.458，7/7=0% | 兼容组合的备选生成器，不做主推 |
| M3 | 独立 ranking 比 M1 TOP1 差 0.32 | BO 先验 / 产率展示；不单独做候选排序 |

泄漏影响提示：
- 11 条 test 完全重复使得各表 Top-1 绝对值有约 **~1%** 乐观偏差（上限 11/1064）
- 反应级 13.3% 重叠使得 M1/M2 的反应指纹分支在这部分 test 上有"见过"效应
- 如果后续做 BO/RAG 评估，必须重建 train-only FAISS 索引，否则 warm-start 会把 test 真值直接带进 initial observations

---

*文档结束。若模型路径 / 类别数与代码出现不一致，以 `condition_agent/config.py` 和各模型 `.py` 文件为准。*
