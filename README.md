# Optimization of Electrocatalytic Olefin Difunctionalization Reactions

An AI-powered agent for designing optimal electrochemical reaction conditions, combining Claude LLM reasoning with pre-trained machine learning models and a reaction similarity database.

## Overview

This project provides an intelligent agent that helps researchers design electrochemical reaction conditions by:

1. **Recommending conditions** (anode, cathode, cell type, electrolyte, solvent, reagent, catalyst) using trained classification models
2. **Generating diverse condition combinations** using a Conditional Variational Autoencoder (CVAE)
3. **Predicting reaction yields** for specific condition sets
4. **Retrieving similar known reactions** from a database of 17,800+ reactions via fingerprint similarity search
5. **Reasoning about chemistry** using Claude as the orchestration engine (ReAct pattern)

## Project Structure

```
condition_agent/
├── main.py                  # CLI entry point (interactive / one-shot)
├── demo.py                  # Tool demo script (no API key needed)
├── build_index.py           # Build FAISS similarity search index
├── config.py                # Configuration and paths
├── requirements.txt         # Python dependencies
│
├── agent/                   # ReAct agent core
│   ├── loop.py              # ElectrochemAgent (Claude API + tool loop)
│   ├── prompts.py           # System prompt and 6 tool schemas
│   └── tools.py             # Tool implementations
│
├── models/                  # Model loading
│   └── loader.py            # Lazy-loading manager for 3 trained models
│
├── rag/                     # Retrieval-Augmented Generation
│   ├── retriever.py         # Cosine similarity search
│   └── index_builder.py     # Index construction from train.pt + JSON data
│
├── utils/                   # Utilities
│   ├── smiles_utils.py      # SMILES parsing and fingerprinting
│   └── display.py           # CLI formatting
│
├── data/                    # Reaction data
│   ├── extracted_smiles.json
│   └── alkene_reactions_by_yield/
│
└── yield_prediction/        # ML model definitions and training code
    ├── models/              # Model architectures
    ├── utils/               # Feature extraction
    ├── scripts/             # Training and inference scripts
    └── checkpoints/         # Trained model weights
```

## Installation

### Requirements

- Python 3.10+
- PyTorch >= 2.0
- RDKit
- Anthropic API key (for the full agent; not needed for `demo.py`)

### Setup

```bash
# Clone the repository
git clone https://github.com/SII-gelingli/Optimization-of-Electrocatalytic-Olefin-Difunctionalization-Reactions.git
cd Optimization-of-Electrocatalytic-Olefin-Difunctionalization-Reactions

# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-key-here"
```

### Build the Reaction Index

Before using the similarity search tool, build the FAISS index:

```bash
# Build index from training data + alkene reactions
python build_index.py

# Or skip alkene data
python build_index.py --no_alkene

# Specify custom data paths
python build_index.py --train_data /path/to/train.pt --alkene_data /path/to/alkene_dir
```

Note: `train.pt` (2GB) is not included in the repository due to size. Place it at `yield_prediction/data/train.pt` to include training data in the index.

## Usage

### Interactive Mode

```bash
python main.py
```

Then type your questions, e.g.:
```
> Recommend conditions for this reaction: C=Cc1ccccc1.O=C(Nc1cccc2cccnc12)c1ccccc1>>O=C1c2ccccc2CC(c2ccccc2)N1c1cccc2cccnc12
```

### One-Shot Mode

```bash
python main.py --reaction "CC(=O)c1ccccc1>>CC(O)c1ccccc1"
```

### Demo (No API Key Required)

Test all 6 tools locally without Claude:

```bash
python demo.py
python demo.py --device cuda
python demo.py --reaction "YOUR_REACTION_SMILES"
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--reaction` | Reaction SMILES for one-shot mode | — |
| `--query` | Custom query (with `--reaction`) | — |
| `--model` | Claude model to use | `claude-sonnet-4-20250514` |
| `--device` | Inference device | `cpu` |
| `--max_rounds` | Max tool call rounds | `15` |

## Agent Tools

| Tool | Description |
|------|-------------|
| `validate_smiles` | Validate SMILES strings and return molecular properties |
| `parse_reaction` | Parse reaction SMILES into reactant/product components |
| `recommend_conditions_default` | Top-k condition predictions (classification model) |
| `generate_conditions_cvae` | Diverse joint condition generation (CVAE model) |
| `predict_yield` | Yield prediction for specific condition combinations |
| `search_similar_reactions` | Find similar reactions from the database |

## Models

Three pre-trained models are included in `yield_prediction/checkpoints/`:

1. **ConditionRecommenderXTB+Catalyst** (`condition_recommender_cat/`) — Multi-head classifier for 7 condition types using fingerprint + xTB features. **80.4% Top-1 accuracy, 96.2% Top-3 accuracy**
2. **CategoricalCVAE** (`condition_model/`) — Conditional VAE for joint condition generation
3. **YieldPredictor** (`mlp/`) — MLP regression model for yield prediction. **R²=0.388** (trained with failed reactions)

### Model Performance (Updated March 2024)

| Task | Model | Metric | Value |
|------|-------|--------|-------|
| Condition Recommendation | ConditionRecommenderXTB+Catalyst | Top-1 Accuracy | 80.4% |
| | | Top-3 Accuracy | 96.2% |
| Yield Prediction | MLP | R² | 0.388 |
| | | MAE | 13.01% |
| Failure Detection | MultiTask Model | F1 Score | 0.525 |
| | | Recall | 72.2% |

## Data

- **Training data** (`yield_prediction/data/`): 10,812 electrochemical reactions including 206 failed reactions (yield=0)
- **Alkene reactions** (`data/alkene_reactions_by_yield/`): 10,800+ olefin difunctionalization reactions from CAS, organized by yield range (including yield_0.json for failed reactions)
- **Extracted SMILES** (`data/extracted_smiles.json`): Literature-extracted reaction SMILES
