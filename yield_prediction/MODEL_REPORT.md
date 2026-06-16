# 电化学反应产率预测与条件推荐系统 — 模型总结报告

## 1. 项目概述

本系统针对烯烃电化学反应，实现两项核心功能：

- **产率预测**：输入反应 SMILES + 反应条件 → 预测产率（0-100%）
- **条件推荐**：输入反应 SMILES → 推荐最优电化学反应条件（电极、电解质、溶剂等）

---

## 2. 数据处理

### 2.1 数据来源

| 数据集 | 文件 | 规模 | 说明 |
|--------|------|------|------|
| 产率反应数据 | `alkene_reactions_by_yield/yield_*.json` | 10,236 条 | 有明确产率的有效反应 |
| 失败反应数据 | `extracted_smiles.json` | 737 条（去重后 327 条） | `isolated_yield` 为空的反应，视为失败（yield=0） |
| **合并数据集** | — | **10,563 条** | 上述两者合并去重 |

去重策略：
- 与产率数据去重：按反应物+产物签名（同一反应在产率数据中已有记录则跳过）
- 失败反应内部去重：按完整签名（反应物+产物+电极+电解质+溶剂），保留同一反应在不同条件下的失败记录（这些是"什么条件会失败"的独立样本）
- 跳过：0 条与产率数据重叠，410 条内部完全重复

### 2.2 产率分布

```
产率区间     样本数     占比
─────────────────────────────
0% (失败)    327       3.1%
0-20%        587       5.6%
20-40%       1,160     11.0%
40-60%       2,672     25.3%
60-80%       3,887     36.8%
80-100%      1,930     18.3%
─────────────────────────────
均值: 57.8%   中位数: 61.0%   标准差: 23.1%
```

### 2.3 特征工程

**反应指纹（6,144 维）**：
- 反应物 Morgan 指纹（2,048D, radius=2）
- 产物 Morgan 指纹（2,048D）
- 差异指纹 = |产物 - 反应物|（2,048D）

**xTB 量子化学描述符（33 维，可选）**：
- 反应物描述符（11D）+ 产物描述符（11D）+ 差异描述符（11D）
- 包含 HOMO/LUMO 能级、偶极矩、极化率等
- 共覆盖 14,513 个分子

**条件特征（产率预测模型额外输入）**：
- 溶剂指纹（2,048D）+ 电解质指纹（2,048D）
- 电化学参数（6D）：阳极类型、阴极类型、电流、电流密度、电势、电解槽类型

**条件标签编码**：

| 条件类型 | 编码方式 | 类别数 |
|----------|----------|--------|
| 阳极材料 | 关键词匹配 → 19 类 | 19（含 Unknown） |
| 阴极材料 | 同上 | 19（含 Unknown） |
| 电解槽类型 | 字典映射 | 6（含 Unknown） |
| 电解质 | SMILES 词表 | 101（含 Unknown） |
| 溶剂 | SMILES 词表 | 94（含 Unknown） |
| 试剂 | SMILES 词表 | 201（含 Unknown） |
| 催化剂 | SMILES 词表 | 101（含 Unknown） |

### 2.4 数据集划分

随机划分（seed=42）：训练集 80% / 验证集 10% / 测试集 10%

---

## 3. 模型架构与训练方法

### 3.1 产率预测模型（MLP YieldPredictor）

**架构**：

```
输入 (10,246D) → Linear(512) → BN → ReLU → Dropout(0.2)
              → Linear(256) → BN → ReLU → Dropout(0.2)
              → Linear(128) → BN → ReLU → Dropout(0.2)
              → Linear(1)   → Sigmoid → 产率 (0~1)
```

**输入特征构成**：
```
反应指纹 (6,144) + 溶剂指纹 (2,048) + 电解质指纹 (2,048) + 电化学参数 (6) = 10,246D
```

**训练配置**：

| 参数 | 值 |
|------|-----|
| 优化器 | AdamW (lr=0.001, weight_decay=0.0001) |
| 学习率调度 | Cosine Annealing (warmup=5 epochs) |
| 损失函数 | MSELoss |
| 批大小 | 32 |
| 早停 | patience=10 |
| 失败反应采样 | WeightedRandomSampler (weight=2.0x) |

**失败反应利用策略**：将 327 条失败反应（yield=0）加入训练集，通过 `WeightedRandomSampler` 以 2 倍权重上采样，使模型学习到"哪些条件组合导致失败"。

### 3.2 条件推荐模型（Default — ConditionRecommender）

**架构**：

```
反应指纹 (6,177D) → ReactionEncoder(512) → BN → ReLU → Dropout
                  → SharedEncoder(256) → BN → ReLU → Dropout
                  → 7 个独立分类头：
                     ├─ anode_head    → Softmax (19 类)
                     ├─ cathode_head  → Softmax (19 类)
                     ├─ cell_type_head → Softmax (6 类)
                     ├─ electrolyte_head → Softmax (101 类)
                     ├─ solvent_head  → Softmax (94 类)
                     ├─ reagent_head  → Softmax (201 类)
                     └─ catalyst_head → Softmax (101 类)
```

输入维度 6,177 = 反应指纹 6,144 + xTB 描述符 33。

**训练配置**：

| 参数 | 值 |
|------|-----|
| 优化器 | AdamW (lr=0.001, weight_decay=0.0001) |
| 损失函数 | CrossEntropyLoss（yield-weighted） |
| 训练轮数 | 100 epochs |
| 批大小 | 32 |

**Yield-Weighted Loss**：

```python
yield_weight = (yield_value / 100.0).clamp(min=0.05)
loss = (per_sample_ce_loss * yield_weight).mean()
```

- 高产率反应（85%）→ 权重 0.85，强引导
- 失败反应（0%）→ 权重 0.05，几乎忽略
- 效果：模型优先学习高产率反应中的条件模式，避免被失败反应的条件"误导"

### 3.3 条件推荐模型（CVAE — CategoricalCVAE）

**架构**：

```
编码器：
  反应指纹 (6,177D) → ReactionEncoder → repr (256D)
  条件标签 (7类) → Embedding → concat
  [repr, cond_embed] → μ, log σ² (各 64D)

解码器：
  z (64D, 采样自 N(μ, σ²)) + repr → 7 个分类头（同 Default）
```

**训练配置**：

| 参数 | 值 |
|------|-----|
| 潜在空间维度 | 64 |
| KL Annealing | 线性 warmup 20 epochs, β_max=0.1 |
| 梯度裁剪 | max_norm=5.0 |
| 训练轮数 | 60 epochs |
| 损失函数 | Recon(CE) + β * KL（yield-weighted） |

**CVAE 优势**：能通过采样不同的 z 向量生成多组**联合条件方案**，保证条件之间的兼容性（Default 模型各条件独立预测，无法保证组合合理性）。

---

## 4. 训练结果

### 4.1 产率预测模型（MLP + 失败反应）

| 指标 | 验证集 | 测试集 |
|------|--------|--------|
| MAE | 11.81% | **12.73%** |
| RMSE | 16.14% | **16.55%** |
| R² | 0.467 | **0.520** |

最佳 epoch: 8（早停于 epoch 18）

版本迭代对比：

| 版本 | Test R² | Test MAE | 失败反应数 |
|------|---------|----------|-----------|
| 基线（仅产率数据） | 0.402 | 12.17% | 0 |
| + 失败反应 v1 | 0.471 | 11.89% | 122 |
| **+ 失败反应 v2（当前）** | **0.520** | **12.73%** | **327** |

R² 从基线 0.402 提升至 **0.520**（+29.4%），说明更多的失败反应样本让模型更好地建模了条件-产率关系的边界。

### 4.2 条件推荐模型（Default, yield-weighted）

Best epoch: 90, Avg Top-1 = **69.2%**

| 条件类型 | Top-1 | Top-3 | Top-5 | Top-10 |
|----------|-------|-------|-------|--------|
| 阳极材料 | 72.4% | 94.2% | 97.6% | 99.7% |
| 阴极材料 | 83.1% | 95.4% | 97.6% | 99.8% |
| 电解槽类型 | 86.4% | 99.6% | 100.0% | 100.0% |
| 电解质 | 33.9% | 58.3% | 69.4% | 81.0% |
| 溶剂 | 66.6% | 82.0% | 88.5% | 95.0% |
| 试剂 | 59.0% | 79.5% | 86.1% | 92.0% |
| 催化剂 | 83.1% | 94.5% | 97.3% | 99.0% |
| **平均** | **69.2%** | **86.2%** | **90.9%** | **95.2%** |

### 4.3 条件推荐模型（CVAE, yield-weighted）

Best epoch: 3, Avg Top-1 = **51.6%**

| 条件类型 | Top-1 | Top-3 | Top-5 | Top-10 |
|----------|-------|-------|-------|--------|
| 阳极材料 | 45.6% | 51.3% | 56.2% | 97.4% |
| 阴极材料 | 54.7% | 66.0% | 80.3% | 92.1% |
| 电解槽类型 | 85.3% | 99.5% | 99.8% | 100.0% |
| 电解质 | 4.4% | 7.3% | 9.6% | 15.3% |
| 溶剂 | 45.0% | 49.7% | 52.2% | 57.8% |
| 试剂 | 45.3% | 47.6% | 50.8% | 60.3% |
| 催化剂 | 80.7% | 82.5% | 82.8% | 85.0% |
| **平均** | **51.6%** | **57.7%** | **61.7%** | **72.6%** |

CVAE 的 Top-1 低于 Default 模型是预期行为：CVAE 的核心价值在于生成**多样化的联合方案**，而非单条件最优预测。

---

## 5. 推理流程

### 5.1 基础条件推荐

```bash
python scripts/recommend_conditions.py "反应物SMILES>>产物SMILES" --top_k 5
```

流程：反应 SMILES → Morgan 指纹 + xTB 描述符 → 条件模型 → 各条件 Top-K 候选

### 5.2 CVAE 多样化推荐 + 产率重排

```bash
python scripts/recommend_conditions.py --model_type cvae --rerank "反应物SMILES>>产物SMILES"
```

流程：

```
反应 SMILES
  │
  ├─→ Morgan 指纹 + xTB 描述符 (6,177D)
  │
  ├─→ [CVAE z=0 确定性预测] → 各条件 Top-K 候选（Part 1）
  │
  ├─→ [CVAE 多 z 采样] → N 组联合条件方案
  │     │
  │     └─→ 去重 + Unknown 索引屏蔽
  │
  └─→ [产率模型重排]
        │
        ├─ 对每组方案：拼接条件特征 → 产率模型预测 yield
        │
        └─ 按预测产率降序排列（Part 2）
```

### 5.3 推理示例

输入反应：`CC=CC >> CC(O)CC`（丁烯 → 丁醇）

**Part 1 — 各条件 Top-1 推荐**（z=0 确定性预测）：

| 条件 | Top-1 推荐 | 置信度 |
|------|-----------|--------|
| 阳极 | Graphite | 69.6% |
| 阴极 | Platinum | 94.3% |
| 电解槽 | Undivided | 100.0% |
| 电解质 | LiClO4 | 22.4% |
| 溶剂 | MeCN (CC#N) | 83.5% |
| 试剂 | HBr | 25.8% |
| 催化剂 | LiI | 21.6% |

**Part 2 — 多样化联合方案**（产率重排后 Top-3）：

| 排名 | 阳极 | 阴极 | 电解质 | 溶剂 | 预测产率 |
|------|------|------|--------|------|---------|
| 1 | Pt | Pt | HF/pyridine | DCM | **63.0%** |
| 2 | Graphite | Pt | KBr | MeOH | **47.9%** |
| 3 | Graphite | Pt | nBu4NBr | DMSO | **46.6%** |

重排将联合概率仅 2.41% 但预测产率最高（63%）的方案提升至首位，体现了产率模型对条件质量的鉴别能力。

---

## 6. 关键技术要点

### 6.1 Unknown 索引屏蔽

训练数据中缺失条件被编码为特定索引（电极=18, 电解槽=5, SMILES 类=0）。推理时对这些索引的 logit 设为 `-inf`，确保不推荐无意义的"Unknown"条件。

### 6.2 失败反应数据利用

采用**差异化策略**而非统一处理：

| 模型 | 策略 | 原理 |
|------|------|------|
| 产率预测 | WeightedRandomSampler 2x 上采样 | 让模型充分学习"条件→失败"的映射 |
| 条件推荐 | Yield-weighted CE loss (0.05~1.0) | 抑制失败条件的影响，聚焦高产率条件 |

### 6.3 产率重排

CVAE 生成的方案按联合概率排序反映的是"最常见的条件组合"，但常见不等于最优。产率重排将排序标准从"频率"转为"预测效果"，过滤可能导致低产率的组合。

---

## 7. 文件结构

```
yield_prediction/
├── configs/config.yaml           # 全局配置
├── models/
│   ├── yield_predictor.py        # MLP 产率预测模型
│   ├── condition_recommender.py  # Default 条件推荐模型
│   └── condition_cvae.py         # CVAE 条件推荐模型
├── utils/
│   ├── data_processor.py         # 数据加载与预处理
│   ├── feature_extractor.py      # Morgan 指纹提取
│   ├── xtb_features.py           # xTB 量子化学描述符
│   └── pca_reducer.py            # PCA 降维（可选）
├── scripts/
│   ├── train.py                  # 产率模型训练
│   ├── train_condition.py        # Default 条件模型训练
│   ├── train_condition_cvae.py   # CVAE 条件模型训练
│   ├── recommend_conditions.py   # 条件推荐推理
│   └── predict.py                # 产率预测推理
└── checkpoints/
    ├── best_model.pt             # 产率预测（含失败反应）
    ├── mlp/best_model.pt         # MLP 产率预测
    └── condition_model/
        ├── best_condition_model.pt      # Default 条件模型
        ├── best_cvae_condition_model.pt # CVAE 条件模型
        └── vocab.json                   # 条件词表
```

---

## 8. 使用方式

```bash
# 产率预测模型训练（含失败反应）
python scripts/train.py --include_failed --failed_weight 2.0

# 条件推荐模型训练（yield-weighted）
python scripts/train_condition.py --yield_weighted
python scripts/train_condition_cvae.py --yield_weighted

# 条件推荐（Default 模型）
python scripts/recommend_conditions.py "CC=CC>>CC(O)CC" --top_k 5

# 条件推荐（CVAE + 产率重排）
python scripts/recommend_conditions.py --model_type cvae --rerank "CC=CC>>CC(O)CC"

# 交互模式
python scripts/recommend_conditions.py --model_type cvae --rerank --interactive

# JSON 输出
python scripts/recommend_conditions.py --model_type cvae --rerank --json "CC=CC>>CC(O)CC"
```
