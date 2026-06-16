# Electrochemical Condition Agent — Model Architectures

## 1. What This System Does

A user provides a chemical reaction (as a SMILES string). The system recommends optimal electrochemical conditions — anode, cathode, solvent, electrolyte, reagent, catalyst, and cell type — along with predicted yield and a complete experimental protocol.

## 2. Why Three Small Models + One Large Model

The system faces a fundamental tradeoff: **accuracy vs. diversity vs. evaluability**. No single model handles all three well, so we decompose the problem into three complementary sub-tasks, each handled by a specialized small model, with a large language model (Claude) orchestrating and reasoning over their outputs.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        User Query (Reaction SMILES)                      │
└────────────────────────────────┬─────────────────────────────────────────┘
                                 │
                                 ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                     Claude LLM  (Central Controller)                     │
│                                                                          │
│   ReAct Loop: Think → Call Tool → Observe → Think → ... (up to 15 rounds)│
│   180-line system prompt with electrochemistry domain knowledge          │
│   Makes the FINAL decision — no hardcoded fusion logic                   │
│                                                                          │
│   Calls 10 tools:                                                        │
│   ┌────────────┐ ┌──────────────┐ ┌───────────────┐ ┌────────────────┐  │
│   │ Chemistry  │ │ ML Inference │ │   Retrieval   │ │    Output      │  │
│   │ Analysis   │ │              │ │               │ │  Generation    │  │
│   ├────────────┤ ├──────────────┤ ├───────────────┤ ├────────────────┤  │
│   │analyze_rxn │ │recommend_cond│ │search_similar │ │estimate_params │  │
│   │validate    │ │generate_cvae │ │(FAISS,10572)  │ │gen_protocol    │  │
│   │parse       │ │predict_yield │ │               │ │draw_reaction   │  │
│   └────────────┘ └──────┬───────┘ └───────────────┘ └────────────────┘  │
└─────────────────────────┼────────────────────────────────────────────────┘
                          │ calls
                          ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                     Three Complementary ML Models                        │
│                                                                          │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────────┐ │
│  │    Model ①       │ │    Model ②       │ │       Model ③            │ │
│  │ ConditionRec-    │ │ CategoricalCVAE  │ │    YieldPredictor        │ │
│  │ ommenderXTB      │ │                  │ │                          │ │
│  │                  │ │                  │ │                          │ │
│  │ "What is the     │ │ "What conditions │ │ "How well does this      │ │
│  │  best choice     │ │  work well       │ │  combination actually    │ │
│  │  for EACH        │ │  TOGETHER?"      │ │  perform?"               │ │
│  │  condition?"     │ │                  │ │                          │ │
│  │                  │ │                  │ │                          │ │
│  │ Top-1: 80.4%     │ │ Top-1: 65.9%     │ │ R²=0.404, MAE=13.21%    │ │
│  │ Top-3: 96.0%     │ │ Top-3: 87.7%     │ │                          │ │
│  │ ACCURACY-FIRST   │ │ DIVERSITY+COMPAT │ │ SCORING & RANKING        │ │
│  └──────────┬───────┘ └────────┬─────────┘ └────────────┬─────────────┘ │
│             │ per-condition     │ joint schemes          │               │
│             │ top-k             │                        │               │
│             └──────────┬────────┘                        │               │
│                        │ candidate schemes               │               │
│                        └────────────────►────────────────┘               │
│                                          yield scoring                   │
│                                              │                           │
│                                              ▼                           │
│                                   Ranked Candidate Schemes               │
│                                              │                           │
└──────────────────────────────────────────────┼───────────────────────────┘
                                               │
                                               ▼
                                     LLM Final Reasoning
                                   (synthesize all evidence
                                    + domain knowledge)
                                               │
                                               ▼
                              Recommendations + Reasoning + Protocol
```

### Role of Each Component

| Component | Question It Answers | How |
|-----------|-------------------|-----|
| **Model ①** ConditionRecommenderXTB | "What is the single best anode? Best solvent? ..." | 7 independent classification heads, each picks top-k from its vocabulary |
| **Model ②** CategoricalCVAE | "What sets of conditions work well together?" | Samples latent variable z → decoder outputs all 7 conditions jointly |
| **Model ③** YieldPredictor | "If I use this specific combination, what yield do I get?" | Takes reaction + complete conditions as input → regresses yield |
| **FAISS Retrieval** | "What worked for similar reactions in the literature?" | Cosine similarity search over 10,572 known reactions |
| **Claude LLM** | "Given all evidence, what should I actually recommend?" | Synthesizes model outputs + retrieval results + domain knowledge |

### Why the LLM Is Essential

The three small models provide statistical predictions, but they cannot:
- Detect chemical incompatibilities (e.g., "Pt anode + Br⁻ electrolyte causes unwanted halide reactions")
- Explain *why* a condition is appropriate in chemical terms
- Resolve conflicts when models disagree with literature precedents
- Generate experimental protocols with safety warnings

The LLM reads all tool outputs as JSON, reasons about them using its chemistry knowledge, and produces the final recommendation. **No code combines the model outputs** — the fusion happens entirely through LLM reasoning.

---

## 3. Shared Feature Engineering

All three models share the same molecular feature representations, computed by `MolecularFeatureExtractor`.

### 3.1 Morgan Fingerprint (ECFP4)

```
SMILES → RDKit Mol → Morgan FP (radius=2, nBits=2048) → [2048D] bit vector
```

Reaction fingerprint (used by all models):
```
reaction_fp = [ reactant_fp (2048D) | product_fp (2048D) | diff_fp (2048D) ] = 6144D

diff_fp = product_fp - reactant_fp    (encodes structural changes)
```

### 3.2 xTB Quantum Chemical Descriptors

**Pre-computed** for 14,513 molecules in `xtb_reaction_molecules.csv`. Looked up at runtime, not computed on the fly. If a molecule is missing from the cache, xTB features are zero-filled and only RDKit descriptors are used.

Each molecule → 11D features:

| Feature | Dim | Source | Meaning |
|---------|-----|--------|---------|
| total_energy_Eh | 1 | xTB | Total energy (Hartree) |
| homo_lumo_gap_eV | 1 | xTB | HOMO-LUMO gap |
| homo_eV | 1 | xTB | HOMO energy level |
| lumo_eV | 1 | xTB | LUMO energy level |
| dipole_total_Debye | 1 | xTB | Dipole moment |
| gsolv_Eh | 1 | xTB | Solvation free energy |
| num_heavy_atoms | 1 | RDKit | Heavy atom count |
| molecular_weight | 1 | RDKit | Molecular weight |
| num_rotatable_bonds | 1 | RDKit | Rotatable bond count |
| tpsa | 1 | RDKit | Topological polar surface area |
| logp | 1 | RDKit | Partition coefficient |

Reaction-level: reactant(11D) + product(11D) + diff(11D) = **33D**

### 3.3 Condition Label Encoding

| Condition | Encoding | Classes | Notes |
|-----------|----------|---------|-------|
| Anode | Fixed category index | 19 | Carbon, Pt, Graphite, GC, Ni, SS, ... |
| Cathode | Fixed category index | 19 | Same as anode |
| Cell type | Fixed category index | 6 | Undivided, Divided, Flow, Sealed, H-cell, Unknown |
| Electrolyte | SMILES → vocab index | 101 | Top-100 by frequency + UNK (index=0) |
| Solvent | SMILES → vocab index | 101 | Top-100 + UNK |
| Reagent | SMILES → vocab index | 201 | Top-200 + UNK |
| Catalyst | SMILES → vocab index | 101 | Top-100 + UNK |

UNK indices are masked to `-inf` during inference to prevent recommending "Unknown".

### 3.4 Feature Dimensions Summary

| Feature Set | Dimensions | Used By |
|-------------|-----------|---------|
| Reaction fingerprint | 6,144 | All three models + FAISS |
| xTB descriptors | 33 | Models ① and ② |
| Solvent fingerprint | 2,048 | Model ③ only |
| Electrolyte fingerprint | 2,048 | Model ③ only |
| Electrochemical params | 6 | Model ③ only (anode_idx, cathode_idx, current, current_density, potential, cell_type_idx) |

---

## 4. Model ① — ConditionRecommenderXTB (Multi-Head Classifier)

> **File**: `yield_prediction/models/condition_recommender.py` (class `ConditionRecommenderXTB`)
> **Checkpoint**: `checkpoints/condition_recommender_cat/best_model.pt`
> **Training script**: `yield_prediction/scripts/train_condition_recommender.py`

### 4.1 What It Does

Given a reaction, independently predicts the best choice for each of the 7 condition types. Each classification head votes on its own — they share the same hidden representation but do not coordinate with each other.

### 4.2 Architecture

```
Reaction Fingerprint [B, 6144]          xTB Features [B, 33]
         │                                      │
         ▼                                      ▼
   FP Encoder                             xTB Encoder
   Linear(6144→512)+BN+ReLU+Drop(0.3)    Linear(33→64)+BN+ReLU+Drop(0.3)
   Linear(512→256)+BN+ReLU               Linear(64→64)+BN+ReLU
         │ [B, 256]                             │ [B, 64]
         └──────────── Concat ──────────────────┘
                         │ [B, 320]
                         ▼
                   Fusion Layer
                   Linear(320→256)+BN+ReLU+Drop(0.3)
                         │ [B, 256]   (shared representation)
                         ▼
         ┌───────┬───────┬───────┬────────┬────────┬────────┬────────┐
         ▼       ▼       ▼       ▼        ▼        ▼        ▼
      anode   cathode  cell   electro-  solvent  reagent  catalyst
      head    head     type   lyte      head     head     head
      (→19)   (→19)   head    head     (→101)   (→201)   (→101)
                       (→6)   (→101)
```

### 4.3 Training

| Item | Value |
|------|-------|
| **Loss** | Sum of 7 cross-entropy losses: `L = Σᵢ CE(logitsᵢ, labelᵢ)` |
| **Optimizer** | AdamW (lr=1e-3, weight_decay=1e-4) |
| **Scheduler** | CosineAnnealingLR (T_max=epochs, eta_min=1e-6) |
| **Batch size** | 64 |
| **Epochs** | 100, early stopping patience=20 |
| **Selection** | Best average Top-1 accuracy across 7 conditions on validation set |

### 4.4 Performance

| Condition | Top-1 | Top-3 |
|-----------|-------|-------|
| Catalyst | 88.9% | 99.3% |
| Cell Type | 87.2% | 100.0% |
| Anode | 86.3% | 98.5% |
| Cathode | 84.1% | 99.2% |
| Reagent | 82.5% | 95.0% |
| Solvent | 80.1% | 95.7% |
| Electrolyte | 53.6% | 86.0% |
| **Average** | **80.4%** | **96.0%** |

### 4.5 Limitation

The 7 heads are independent — each picks the globally most likely option for its condition type without considering what the other heads chose. This can produce chemically incompatible combinations (e.g., Pt anode + Br⁻ electrolyte). This limitation motivates Model ②.

---

## 5. Model ② — CategoricalCVAE (Joint Condition Generation)

> **File**: `yield_prediction/models/condition_cvae.py` (class `CategoricalCVAE`)
> **Checkpoint**: `checkpoints/cvae_cat/best_model.pt`
> **Training script**: `yield_prediction/scripts/train_cvae_cat.py`

### 5.1 What It Does

Generates **complete sets of 7 conditions** that are internally compatible. By sampling different latent variables z, it produces diverse alternative schemes. Each scheme comes with a joint probability score indicating how coherent the combination is.

### 5.2 Architecture

**Training phase** (learns to compress condition combinations into latent space):

```
Reaction FP [B, 6144]                       7 True Condition Labels
        │                                            │
        ▼                                            ▼
  Reaction Encoder                            7 Embedding Layers
  Linear(6144→512)+BN+ReLU+Drop              anode_emb(19,16)
  Linear(512→256)+BN+ReLU+Drop               cathode_emb(19,16)
        │                                    cell_type_emb(6,8)
        │ repr [B, 256]                      electrolyte_emb(101,32)
        │                                    solvent_emb(101,32)
        │                                    reagent_emb(201,32)
        │                                    catalyst_emb(101,32)
        │                                            │
        │                                    cond_emb [B, 168]
        │                                            │
        └────────────── Concat ─────────────────────┘
                          │ [B, 424]
                          ▼
                    VAE Encoder
                    Linear(424→512)+BN+ReLU+Drop
                    Linear(512→256)+BN+ReLU+Drop
                          │
                    ┌─────┴─────┐
                 fc_mu       fc_logvar
                 [B,64]       [B,64]
                    │            │
                    └─ Reparameterize: z = μ + ε·σ,  ε ~ N(0,I)
                          │
                          z [B, 64]
                          │
        repr [B, 256] ────┘
                │ [B, 320]
                ▼
          Decoder Trunk
          Linear(320→512)+BN+ReLU+Drop
          Linear(512→512)+BN+ReLU+Drop
                │ [B, 512]
                ▼
        7 Classification Heads (reconstruct condition labels)
```

**Inference phase** (no true conditions available — sample z from prior):

```
Reaction FP [B, 6144]
        │
        ▼
  Reaction Encoder → repr [B, 256]

  Sample z ~ N(0, I) × temperature        ← random, not matched to reaction
        │ [B, 64]
        │
  [repr | z] = [B, 320]
        │
  Decoder Trunk → [B, 512]
        │
  7 Classification Heads → argmax each → one complete condition scheme
  Compute joint probability: log P = Σᵢ log softmax(logitsᵢ)[argmaxᵢ]

  Repeat N times with different z → N schemes → deduplicate → sort by joint probability
```

### 5.3 Key Mechanism: How z Coordinates 7 Conditions

The 7 classification heads share the same 512D decoder trunk output, which is determined by `(repr + z)`. The same z value simultaneously influences all 7 outputs through this shared hidden layer. During training, the decoder learned that certain z regions correspond to chemically coherent condition combinations, so each sampled z naturally produces a compatible set.

**Important limitation**: The prior p(z) = N(0,I) is fixed and independent of the reaction. Ideally, different reactions should sample from different z distributions (conditional prior), but the current design uses a universal prior. This is compensated by: (1) the decoder interpreting z differently based on repr, and (2) ranking schemes by joint probability to filter out poor samples.

### 5.4 Training

| Item | Value |
|------|-------|
| **Loss** | `L = Σᵢ CEᵢ + β × KL(q(z\|x,c) ‖ N(0,I))` |
| **KL Annealing** | β: 0 → 0.1 linearly over first 20 epochs (prevents posterior collapse) |
| **Optimizer** | AdamW |
| **Gradient clip** | max_norm = 5.0 |
| **Epochs** | 100, best at epoch 92 |
| **Selection** | Best average Top-1 accuracy at z=0 on validation set |

### 5.5 Performance

| Metric | Value |
|--------|-------|
| Avg Top-1 (z=0) | 65.9% |
| Avg Top-3 (z=0) | 87.7% |

Lower accuracy than Model ① because joint modeling is harder, but provides diverse, compatible schemes that Model ① cannot.

### 5.6 Two Inference Modes

| Mode | Method | Use Case |
|------|--------|----------|
| **Deterministic** | `model.recommend(fp)` — z fixed at 0 | Compatible with Model ① API, single best prediction |
| **Generative** | `model.generate(fp, num_samples=10, temperature=1.0)` — sample multiple z | Diverse joint schemes ranked by joint probability |

---

## 6. Model ③ — YieldPredictor (MLP Regressor)

> **File**: `yield_prediction/models/yield_predictor.py` (class `YieldPredictor`)
> **Checkpoint**: `yield_prediction/checkpoints/best_model.pt`
> **Training script**: `yield_prediction/scripts/train.py`

### 6.1 What It Does

Given a reaction AND a complete set of conditions, predicts the expected yield (0–100%). Unlike Models ① and ②, which only take the reaction as input and output conditions, this model takes both reaction and conditions as input and outputs a score. It serves as the **evaluator** for candidate schemes proposed by the other two models.

### 6.2 Architecture

```
Input Features [B, 10246]
│
├── Reaction FP         [6144D]   ← shared with Models ① and ②
├── Solvent FP          [2048D]   ← Morgan FP of the chosen solvent
├── Electrolyte FP      [2048D]   ← Morgan FP of the chosen electrolyte
└── Electrochemical params  [6D]  ← anode_idx, cathode_idx, current_mA,
                                     current_density, potential, cell_type_idx

        │ [B, 10246]
        ▼
  Linear(10246→512) + BatchNorm + ReLU + Dropout(0.2)
        │
  Linear(512→256) + BatchNorm + ReLU + Dropout(0.2)
        │
  Linear(256→128) + BatchNorm + ReLU + Dropout(0.2)
        │
  Linear(128→1) → Sigmoid → ×100 → Yield (0–100%)
```

### 6.3 Training

| Item | Value |
|------|-------|
| **Loss** | MSELoss (regression) |
| **Optimizer** | AdamW (lr=1e-3, weight_decay=1e-4) |
| **Scheduler** | CosineAnnealingLR with 5-epoch warmup |
| **Batch size** | 64 |
| **Epochs** | 100, early stopping patience=10 |
| **Selection** | Best validation loss (MSE) |
| **Optional** | WeightedRandomSampler for failed reactions (yield=0) at 2× weight |

### 6.4 Performance

| Metric | Value |
|--------|-------|
| R² | 0.404 |
| MAE | 13.21% |
| RMSE | 17.70% |

---

## 7. Retrieval Module — FAISS Similarity Search

> **File**: `rag/retriever.py` (class `ReactionRetriever`)
> **Index**: `data/faiss_index.bin` (248 MB), `data/reaction_db.pkl` (3.6 MB)
> **Build script**: `build_index.py`

### 7.1 What It Does

Finds known reactions from the literature that are structurally similar to the query reaction. Returns their conditions and yields as empirical reference for the LLM.

### 7.2 Method

```
Query reaction SMILES
    │
    ▼
Compute reaction fingerprint [6144D]
    │
    ▼
L2 normalize → unit vector
    │
    ▼
FAISS IndexFlatIP (inner product = cosine similarity)
    │
    ▼
Filter: similarity > threshold (default 0.3)
    │
    ▼
Optional yield-aware reranking:
    score = 0.6 × similarity + 0.4 × yield/100
    │
    ▼
Return: top-k similar reactions with conditions, yields, similarity scores,
        aggregated condition statistics, current parameters
```

### 7.3 Index Details

- **10,572** unique reaction-condition pairs (deduplicated from 10,812 raw reactions)
- Built from `alkene_reactions_by_yield/` JSON files only (not from train.pt, to avoid duplication)
- Index type: `IndexFlatIP` (exact search, no approximation)
- Dimension: 6,144

---

## 8. Data Pipeline

### 8.1 Data Source

- **10,812** electrochemical alkene difunctionalization reactions from CAS database
- **327** failed reactions (yield = 0) from `extracted_smiles.json`
- Train / Val / Test split: 8,649 / 1,081 / 1,082 (80/10/10)

### 8.2 Full Retraining Pipeline

```bash
# Step 1: Raw JSON → train.pt / val.pt / test.pt + vocab.json
python yield_prediction/scripts/prepare_data.py

# Step 2: Add xTB features → train_xtb.pt
python yield_prediction/scripts/prepare_data_xtb_enhanced.py

# Step 3: Add catalyst labels → train_xtb_cat.pt
python yield_prediction/scripts/add_catalyst_to_data.py

# Step 4: Train Model ①
python yield_prediction/scripts/train_condition_recommender.py --use_catalyst

# Step 5: Train Model ②
cd yield_prediction && python scripts/train_cvae_cat.py && cd ..

# Step 6: Train Model ③
cd /path/to/yield_prediction && python scripts/train.py --model mlp

# Step 7: Rebuild FAISS index
python build_index.py --no_train
```

---

## 9. Online Model Summary

| Model | Architecture | Input | Output | Params | Key Metric |
|-------|-------------|-------|--------|--------|------------|
| ConditionRecommenderXTB | Dual Encoder + 7-Head Classifier | 6177D (FP+xTB) | 7 × top-k logits | ~3.5M | Top-1: 80.4% |
| CategoricalCVAE | VAE + 7-Head Classifier | 6144D (FP) | Joint condition schemes | ~4.4M | Top-1: 65.9% |
| YieldPredictor | 4-layer MLP | 10246D (FP+Cond) | yield ∈ [0,100]% | ~6M | MAE: 13.21% |
| ReactionRetriever | FAISS IndexFlatIP | 6144D (FP) | Top-k similar reactions | N/A | 10,572 indexed |

---

## 10. Experimental Architectures (Not Deployed)

The following models were implemented and evaluated but not adopted for production.

### 10.1 Condition Recommendation Variants

| Model | Architecture | Notes |
|-------|-------------|-------|
| ConditionRecommender | FP(6144)→512→512→7 heads | Legacy, no xTB. Replaced by XTB version |
| DualTowerCondRec | FP tower + xTB tower + gate fusion → 7 heads | Learnable gate weights for feature fusion |
| CompactCondRec | PCA(FP→128D) + xTB(33D) = 161D → 256 → 7 heads | 10× fewer parameters via PCA compression |
| ConditionVAE | Continuous VAE on condition vectors | Replaced by discrete CategoricalCVAE |
| JointYieldCondModel | Shared encoder → condition heads + yield head | Multi-task: conditions + yield jointly |

### 10.2 Yield Prediction Variants

| Model | Architecture | Params | Idea |
|-------|-------------|--------|------|
| ResNetPredictor | MLP + 4 residual blocks | ~5M | Skip connections for deeper networks |
| TransformerPredictor | Features → 16 tokens → 4-layer Transformer → pool | ~8M | Self-attention over feature segments |
| AttentionMLP | MLP with multi-head self-attention | ~4M | Learn feature importance weights |
| DualTowerPredictor | Reaction tower + Condition tower + cross-attention | ~4M | Separate encoding + cross-modal interaction |
| DualTowerXTBPredictor | FP tower + xTB tower + gate fusion | ~4M | Gate fusion for heterogeneous features |
| HighwayPredictor | 6 highway layers with adaptive gating | ~4M | `t·transform(x) + (1-t)·x` adaptive depth |
| CompactYieldPredictor | PCA + solvent/electrolyte embeddings → small MLP | ~0.5M | Dimensionality reduction: 10301D → 253D |
| EnsemblePredictor | MLP + ResNet + Highway → learned weights | ~12M | Ensemble with learnable combination weights |
| GINYieldPredictor | Molecular graph → GIN layers → pool + xTB → MLP | ~3M | Graph neural network, no fingerprints needed |
| MoEYieldPredictor | 8 expert MLPs + gating network | ~6M | Mixture of Experts with load balancing |
| Clustered Models | K-Means clustering → per-cluster MLP | ~3M×8 | Different models for different reaction types |
| Two-Stage Model | Classify yield range → range-specific regressor | ~4M | Coarse-to-fine prediction |
| Contrastive Learning | Contrastive repr learning + regression head | ~3M | Pull similar-yield reactions closer in repr space |

---

## 11. Infrastructure

### Hardware & Software

| Item | Value |
|------|-------|
| GPU | Single CUDA GPU |
| Framework | PyTorch 2.8+ (NGC container) |
| Python | 3.12 |
| Chemistry | RDKit (fingerprints, descriptors, visualization) |
| Search | FAISS (similarity retrieval) |
| LLM | Claude via Anthropic API |
| Web UI | Gradio |
| Deployment | Alibaba Cloud ECS (47.98.18.118:7860) |

### Common Training Hyperparameters

```yaml
batch_size: 32-64
learning_rate: 0.001
weight_decay: 0.0001
epochs: 60-100
early_stopping_patience: 10-20
scheduler: CosineAnnealing with warmup
gradient_clip: 5.0 (CVAE only)
random_seed: 42
```

---

*Last updated: 2026-03-22*
