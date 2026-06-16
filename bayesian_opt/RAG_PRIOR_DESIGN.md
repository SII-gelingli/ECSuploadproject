# RAG-mean Prior 设计方案

> 目标：用「历史相似反应 + 相似条件的 yield 均值」替换当前 `YieldSurrogate` 里的
> `yield_predictor_fn`（M3 YieldPredictor，R²≈0.39）作为 GP 的先验均值函数。
>
> 本文只描述**设计**与**接口规格**，不含可运行代码。实施时请作为 spec 参考。

---

## 1. 动机

### 1.1 当前设计的痛点

`bayesian_opt/surrogate.py` 中 GP 学残差：

```
y_observed = prior_mean(x) + GP_residual(x)
```

`prior_mean` 由 `yield_predictor_fn`（指向 M3 `YieldPredictor`）提供。已知问题：

- M3 平均预测 yield ≈ 98%+，真实均值只有 57.8%（`MODEL_ARCHITECTURES_CN.md:627`）。
- M3 与真实 yield 的 Spearman r ≈ 0.17，几乎无排序能力。
- 后果：GP 的 `y_residuals` 严重偏负（y_observed - 98 ≈ -40 左右），残差均值不零，破坏 GP 的常用假设（零均值先验），降低采集函数灵敏度。

### 1.2 为什么 RAG-mean 值得试

- **直接使用真实数据**：不经过回归模型压榨，不会"顶到天花板"。
- **同 domain 自然对齐**：FAISS 检索到的"相似反应"已经限定了化学语境。
- **零训练成本**：无需再拟合模型，加新数据立即生效。
- **可解释**：每次 `prior_mean(cond)` 返回值可以附带"来自哪几条历史 + 相似度权重"诊断。

---

## 2. 总体结构

### 2.1 两阶段检索

prior 接受的是**条件**（`dict`），但现有 `ReactionRetriever.search` 只按**反应指纹**检索。因此必须分两层：

```
┌─ Stage 1: Context pool build (一次性，init 阶段缓存) ─┐
│  reaction_smiles (本轮 BO 的目标反应)                  │
│       ↓  retriever.search(fp, top_k=N_ctx≈50,          │
│                            threshold=0.3)              │
│  → context pool: [(cond_i, yield_i, sim_rxn_i)] × N     │
└────────────────────────────────────────────────────────┘

┌─ Stage 2: Per-query condition k-NN (每次 predict 调用) ─┐
│  candidate cond_q                                        │
│       ↓  space.encode(cond_q) → vec_q ∈ ℝ^D              │
│       ↓  cosine(vec_q, R) → sim_cond_i                   │
│       ↓  select top-k=5 neighbors                        │
│       ↓  weighted mean of their yields                   │
│  → prior_mean(cond_q) ∈ [0, 100]                         │
└────────────────────────────────────────────────────────┘
```

### 2.2 两阶段的必要性

- 若直接**全库按条件检索**：等价于"同样的 Pd/MeCN 在所有反应里的平均 yield"，因为不同反应用同一条件产率差异巨大，平均后无信号。
- 若**只按反应检索、不再按条件筛**：回退到"与目标反应相似的反应的平均 yield"，候选池内所有 cond 得到同一个 prior → 等价于常数 prior，完全不区分候选好坏。
- 必须两阶段：先把语境收敛到"这类反应"，再在子集里按条件精排，才能给不同候选不同的 prior 值。

---

## 3. 接口规格

### 3.1 类声明（伪签名，非代码）

```
class RAGMeanPrior:
    def __init__(
        self,
        retriever: ReactionRetriever,
        space: ConditionSpace,
        reaction_smiles: str,
        model_manager,                  # 用于算 reaction fingerprint
        n_context: int = 50,
        k_neighbors: int = 5,
        rxn_sim_threshold: float = 0.3,
        cond_sim_threshold: float = 0.0,  # 0 → 不过滤
        fallback_mean: float = 57.8,      # 数据集全局 yield 均值
        shrinkage_alpha: Optional[float] = None,  # None → 不做 shrinkage
        cache_size: int = 4096,
    ): ...

    def __call__(self, cond: dict) -> float:
        """返回条件对应的 prior yield (0..100)。符合 YieldSurrogate.yield_predictor_fn 的签名。"""
        ...

    def diagnostics(self) -> dict:
        """返回调用统计：{total_calls, cache_hits, n_fallback, avg_n_neighbors, ...}"""
        ...
```

### 3.2 与 `YieldSurrogate` 的集成

**不需要改 `YieldSurrogate` 的 API**。`YieldSurrogate.__init__` 本来就接受 `yield_predictor_fn: Callable[[dict], float]`。只需：

```
prior = RAGMeanPrior(retriever, space, reaction_smiles, mm)
surrogate = YieldSurrogate(
    condition_space=space,
    yield_predictor_fn=prior,       # callable 替换
    use_prior_mean=True,
    ...
)
```

`RAGMeanPrior.__call__` 只实现 `(cond_dict) -> float` 即可，其余 GP 逻辑完全不变。

### 3.3 `BayesOptOptimizer` 的改动

`optimizer.py` 在 `initialize(reaction_smiles)` 时构造 surrogate。建议加一个开关：

```
optimizer = BayesOptOptimizer(
    ...,
    prior_mode: Literal["m3", "rag_mean", "none"] = "rag_mean",
)
```

- `"m3"`：沿用现有行为（兼容）。
- `"rag_mean"`：每次 `initialize(reaction_smiles)` 时 new 一个 `RAGMeanPrior` 实例注入 surrogate。
- `"none"`：`use_prior_mean=False`，GP 走 `normalize_y` 用经验均值。

---

## 4. 核心算法细节

### 4.1 Stage 1：Context pool 构造

伪流程：

```
def _build_context_pool(reaction_smiles):
    reactants, products = parse_reaction_smiles(reaction_smiles)
    fp = compute_reaction_fingerprint(reactants, products, mm.mol_extractor)

    raw_results = retriever.search(
        fp,
        top_k=n_context,
        threshold=rxn_sim_threshold,
        rerank_by_yield=False,       # 先不按 yield 加权，后面自己加权
    )

    pool = []
    for r in raw_results:
        y = r.get('yield')
        if y is None or y <= 0 or y > 100:
            continue                  # 脏数据过滤
        cond = extract_cond_from_result(r)  # 同 warm_start._extract_conditions_from_result
        vec = space.encode(cond)      # 一次性编码
        pool.append({
            'cond': cond,
            'yield': float(y),
            'sim_rxn': float(r['similarity']),
            'vec': vec,
        })

    # Pre-stack vectors for vectorized cosine
    self.R = np.stack([p['vec'] for p in pool], axis=0) if pool else None
    self.y_pool = np.array([p['yield'] for p in pool]) if pool else None
    self.sim_rxn = np.array([p['sim_rxn'] for p in pool]) if pool else None
    self.pool_size = len(pool)
```

**重要**：编码矩阵 `R ∈ ℝ^{N×D}` 在 init 时就构建好并 L2-normalize，Stage 2 的 cosine 直接用矩阵乘法，一次向量化得到所有 N 个相似度。

### 4.2 Stage 2：Per-query 计算

```
def __call__(self, cond):
    # Cache
    key = _hash_cond(cond)
    if key in cache:
        return cache[key]

    if self.pool_size == 0:
        val = self.fallback_mean
        _record_fallback()
        cache[key] = val
        return val

    q = space.encode(cond)
    q_norm = q / (np.linalg.norm(q) + 1e-12)
    R_norm = self.R / (np.linalg.norm(self.R, axis=1, keepdims=True) + 1e-12)
    sim_cond = R_norm @ q_norm           # shape (N,)

    # 合并相似度 → 权重
    w = self.sim_rxn * np.clip(sim_cond, 0.0, 1.0)

    # 条件相似度阈值
    if self.cond_sim_threshold > 0:
        mask = sim_cond >= self.cond_sim_threshold
        w = w * mask

    # Top-k 选择
    if w.sum() <= 0:
        # 所有邻居都被过滤 → 回退到参考池整体均值
        val = float(np.mean(self.y_pool))
    else:
        top_idx = np.argpartition(-w, min(self.k_neighbors, len(w)-1))[:self.k_neighbors]
        w_top = w[top_idx]
        y_top = self.y_pool[top_idx]
        if w_top.sum() > 0:
            val = float(np.sum(w_top * y_top) / w_top.sum())
        else:
            val = float(np.mean(y_top))

    # Shrinkage 可选
    if self.shrinkage_alpha is not None:
        val = self.shrinkage_alpha * val + (1 - self.shrinkage_alpha) * self.fallback_mean

    # Clip & cache
    val = float(np.clip(val, 0.0, 100.0))
    cache[key] = val
    return val
```

### 4.3 条件相似度的选型

当前设计用 **`space.encode` 向量的余弦**。理由：

1. 与 GP 同构 — 两边看同一个空间，prior 与 kernel 不会"各说各话"。
2. 代码零复用成本 — encode 已经存在。
3. 自动处理设备 one-hot + 分子 PCA 混合表示。

**潜在问题**：one-hot 维占 52 / 308，稀疏、量级差异；PCA 维是密集连续。余弦可能被密集维主导。

**缓解方案（可选）**：

| 方案 | 描述 |
|------|------|
| **分段加权余弦** | 设备段 cosine × w_dev + 分子段 cosine × w_mol，w_dev+w_mol=1，推荐初值 0.5/0.5 |
| **硬匹配 + 软匹配混合** | 设备字段要求完全相同（否则 sim=0）；分子字段用 PCA 余弦 |
| **Gower distance** | 离散 0/1、连续标准化欧氏，再合成。化学表格 BO 常用 |

**建议**：第一版用朴素 cosine，跑完对比实验再决定是否升级。

### 4.4 权重合成

默认 `w_i = sim_rxn_i × sim_cond_i`。替代：

| 合成方式 | 适用场景 |
|---------|---------|
| `w = sim_rxn × sim_cond` | 默认，两种相似度乘法 |
| `w = α·sim_rxn + (1-α)·sim_cond` | 想对某一维更敏感时 |
| `w = exp(sim / τ)` (softmax) | 只想取最像的一两个邻居，τ 小 → 尖锐 |
| `w = sim_rxn × sim_cond × (yield/100)` | 偏向"相似且高产"的邻居（类似 warm_start 的 `rerank_by_yield`）|

**警告**：最后一种会把 prior 拉高，可能重现 M3 的"高估"问题。不建议默认开启。

### 4.5 Shrinkage（可选）

当 `pool_size` 很小（< 5）或 top-k 相似度都很低时，局部均值方差很大。shrinkage 向全局均值收缩：

```
prior_final = α(n, sim) × local_mean + (1 - α(n, sim)) × fallback_mean
```

推荐 `α(n, sim) = min(1.0, n/10) × max(0.0, mean_top_sim)`：

- n < 10 时 shrinkage 强；
- mean_top_sim 低（邻居不够像）时也 shrinkage 强。

**默认**：关闭（`shrinkage_alpha=None`），先看 raw 版本效果；若方差过大再开启。

---

## 5. 边界情况处理

| 场景 | 预期行为 |
|------|---------|
| `retriever` 返回空（目标反应无相似项）| `fallback_mean` + 诊断记录 `n_empty_pool += 1` |
| Pool 非空但全部 `yield=None` / `<=0` | `fallback_mean` |
| `space.encode` 对某 cond 抛错 | 捕获 + 记录 warning，返回 `fallback_mean` |
| 候选 cond 的相似度全 < 阈值 | 回退到参考池整体 yield 均值（不含条件区分） |
| Cond 在 vocab 里不存在（`index=0`）| 正常 encode（index=0 的 embedding 会参与），不做特殊处理 |
| 同一 cond 多次调用 | cache 命中，O(1) |

---

## 6. 性能预算

假设单次 BO `suggest_next`：
- 候选池 ~200
- `predict` 调用 200 次 `prior_mean`
- Context pool N=50，向量维度 D≈308

单次 Stage 2 成本：
- encode: ~10 μs（主要是 lookup，不做 MorganFP 计算）
- cosine R_norm @ q_norm: 50 × 308 ≈ 15,400 乘加，~5 μs
- argpartition + 加权: <1 μs

**合计 ~20 μs/call × 200 call ≈ 4 ms 单次 suggest 的 prior 开销**，完全可忽略。

若没有 cache，BO 全流程（200 候选 × 20 iter）调用量约 4000 次，仍在 80 ms 量级。

---

## 7. 缓存策略

### 7.1 Key 设计

```
def _hash_cond(cond: dict) -> tuple:
    return (
        cond.get('anode_index', 0),
        cond.get('cathode_index', 0),
        cond.get('cell_type_index', 0),
        cond.get('solvent_index', 0),
        cond.get('solvent_smiles', ''),     # 多溶剂混合用 SMILES 区分
        cond.get('electrolyte_index', 0),
        cond.get('electrolyte_smiles', ''),
        cond.get('reagent_index', 0),
        cond.get('reagent_smiles', ''),
        cond.get('catalyst_index', 0),
        cond.get('catalyst_smiles', ''),
    )
```

注意 smiles 字段必须 hash —— 因为多溶剂混合在词表里都是 index=0，但实际 smiles 不同。

### 7.2 TTL / 失效

- **每次 `initialize(reaction_smiles)` 调用时清空 cache**（target reaction 变了，参考池变了，旧 prior 值失效）。
- `fit/update` 调用时**不需要**清 cache（RAG-mean prior 不依赖 GP 的观测，只依赖 retriever）。

### 7.3 容量

LRU cache，默认 `cache_size=4096`，覆盖大多数 BO 迭代场景。

---

## 8. 诊断输出

为了调试/评估，`RAGMeanPrior` 内部维护：

```
self.stats = {
    "total_calls": 0,
    "cache_hits": 0,
    "n_fallback_empty_pool": 0,
    "n_fallback_low_sim": 0,
    "pool_size": <int>,
    "mean_rxn_sim_in_pool": <float>,
    "yield_distribution_in_pool": (min, q25, median, q75, max),
    # For each call, optionally:
    "per_call_log": deque(maxlen=1000) of {
        "cond_hash": ...,
        "top_k_indices": [...],
        "top_k_weights": [...],
        "top_k_yields": [...],
        "returned": ...,
    }
}
```

`diagnostics()` 返回快照 dict。方便跑完 BO 后 dump 成 JSON 分析：

- `n_fallback / total` 高 → 参考池太稀疏或阈值太严
- `per_call_log` 里所有返回值聚集在几个数 → prior 没有区分力，等价常数 prior
- `pool_yield_distribution` 偏态 → 可能需要 shrinkage

---

## 9. 验证计划

### 9.1 离线诊断（不跑 BO）

**目标**：证明 RAG-mean 作为 yield 估计器比 M3 准。

**做法**：
1. 对训练数据做留一（leave-one-out）交叉验证。
2. 对每条被留出的 `(reaction, cond, y_true)`：
   - 算 `m3_pred = M3(reaction, cond)`
   - 算 `rag_pred = RAGMeanPrior(retriever_without_leave_out, space)(cond)`（retriever 必须剔除该条）
   - 算 `global_pred = 57.8` （常数基线）
3. 计算对 `y_true` 的：MAE、RMSE、Spearman、Pearson。

**期望结果**：

| Metric | M3 | RAG-mean | Global |
|--------|----|----|---------|
| MAE ↓   | ~25 | < 20 | ~22 |
| Spearman ↑ | ~0.17 | > 0.35 | 0 |
| Pearson ↑  | <0.2 | > 0.3 | 0 |

### 9.2 BO 回放对比

**目标**：证明换 prior 之后 BO 收敛更快或最终 yield 更高。

**做法**：
1. 选 10 条测试反应（无 leakage）。
2. 每条反应、每种 prior 配置（`m3`/`rag_mean`/`none`），相同 seed、相同采集函数（EI）、相同批次策略、`n_iter=20`。
3. 记录每轮的 best-so-far yield。
4. 画 regret curve：`y_oracle_max - y_best_so_far`。

**期望**：
- `rag_mean` 的 regret 曲线在早期（iter ≤ 5）明显低于 `m3` 和 `none`。
- 后期三者收敛（GP 数据够多时 prior 影响变小）。

### 9.3 Prior 区分力诊断

跑一次 BO（任一反应），dump `diagnostics()`，检查：

- `per_call_log` 里 prior 返回值的标准差（应 > 5，若 < 2 说明 prior 等价常数）。
- 多候选池上 prior 值的分布直方图（应覆盖 20-80 的主要区间，不应全挤在一处）。

---

## 10. 实施路线图

> 本节列步骤，供下次实现会话参照。

1. **新建 `bayesian_opt/priors.py`**（新文件，不改现有代码）
   - 定义 `RAGMeanPrior` 类，实现 Section 3-7 的所有逻辑。
   - 包含 `__call__`, `diagnostics`, `_build_context_pool`, `_hash_cond` 等。
2. **扩展 `BayesOptOptimizer.__init__`**（改 `optimizer.py`）
   - 新增 `prior_mode` 参数（`"m3" | "rag_mean" | "none"`，默认 `"m3"` 保兼容）。
3. **扩展 `BayesOptOptimizer.initialize`**
   - 根据 `prior_mode` 构造不同的 `yield_predictor_fn`：
     - `"m3"`：现有行为。
     - `"rag_mean"`：`RAGMeanPrior(retriever, space, reaction_smiles, mm)`。
     - `"none"`：`None` + 传 `use_prior_mean=False` 给 surrogate。
4. **扩展 `web_app.py` / `demo.py`**
   - 在界面/命令行上暴露 `prior_mode` 选项。
5. **写测试**（新文件 `tests/test_rag_prior.py`）
   - 单元：空池回退、cache 命中、向量化 cosine 一致性。
   - 集成：`YieldSurrogate(yield_predictor_fn=rag_prior).fit(...)` 流程不报错。
6. **写评估脚本**（新文件 `scripts/eval_prior.py`）
   - 实现 Section 9.1 的 LOO 交叉验证。
7. **BO 回放脚本**（新文件 `scripts/bo_replay.py`）
   - 实现 Section 9.2 的 10 反应 × 3 prior 对比。

---

## 11. 风险与回退

### 11.1 可能失败的情形

- **参考池普遍稀疏**：很多反应 FAISS 相似度 < 0.3，导致大量 fallback → RAG-mean 退化为常数 prior。
  - **监控**：`n_fallback_empty_pool / total_calls` > 20% 时报警。
  - **缓解**：降低 `rxn_sim_threshold` 到 0.2；或用 top-N without threshold。

- **参考池条件同质化**：相似反应普遍用同一套"惯例"条件 → Stage 2 的 cond sim 全部接近 1 → prior 值都接近 pool 平均 yield，区分力差。
  - **监控**：`per_call_log` 中 prior 值的 std < 3。
  - **缓解**：采用分段加权余弦，放大分子维度差异；或显式加一个"条件多样性惩罚"。

- **测试集泄漏**：若 retriever 的数据库包含 BO 评估目标反应本身，prior 会"作弊"看到答案。
  - **必做**：在 `scripts/bo_replay.py` 里构造 retriever 时**显式剔除目标反应**。
  - **已记录**：`Task #5 — Test leakage audit` 需要先完成。

### 11.2 回退路径

完全保留 `"m3"` 模式（默认值），用户配置 `prior_mode="m3"` 即回到当前行为。不破坏任何现有 API。

---

## 12. 开放问题

1. **`space.encode` 是否稳定**？不同 ConditionSpace 实例（不同 vocab）会得到不同 embedding。RAG-mean prior 的参考池编码与 BO 当次 encode 必须来自同一个 `ConditionSpace` 实例。**风险点**：持久化/反序列化时要保证一致。
2. **多溶剂混合在 encode 里的表达**：当前 `space.py` 对多溶剂 `solvent_index=0 + solvent_smiles="A.B"` 的编码路径需要审核 —— 若 fallback 到 `_smiles_to_morgan("A.B")`，RDKit 能正确处理；若只看 `solvent_index=0`，则所有多溶剂候选会共用同一个 PCA 向量，Stage 2 cosine 区分度下降。
3. **相似度阈值调参**：`rxn_sim_threshold` 在不同数据集上合理值不同。是否需要做一次 sweep（0.1 / 0.2 / 0.3 / 0.4），挑 LOO MAE 最低的？

---

## 13. 一句话总结

> 把 M3 的回归预测换成"相似反应池内条件 k-NN 的 yield 加权均值"，接口不变、代码新增一个类、成本毫秒级、效果等待离线 LOO + BO 回放实验证实。这条路的核心信念是：**真实数据的局部平均胜过一个 R²=0.39 的回归模型**。
