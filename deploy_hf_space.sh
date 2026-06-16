#!/bin/bash
# 部署 Electrochemical Condition Agent 到 Hugging Face Space
# 使用方法: cd /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent && bash deploy_hf_space.sh

set -e

HF_SPACE="https://huggingface.co/spaces/SII-gelingli/ElectrochemicalConditionAgent"
DEPLOY_DIR="/inspire/hdd/global_user/gelingli-253114010248/hf-echem-agent"
SOURCE_DIR="/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent"

echo "=============================================="
echo "部署 Electrochemical Condition Agent"
echo "=============================================="

# 1. 克隆 Space
echo "Step 1: 克隆 HF Space..."
rm -rf "$DEPLOY_DIR"
git clone "$HF_SPACE" "$DEPLOY_DIR"
cd "$DEPLOY_DIR"

# 2. 清理旧文件 (保留 .git)
echo "Step 2: 清理旧文件..."
find . -maxdepth 1 ! -name '.git' ! -name '.' -exec rm -rf {} +

# 3. 复制项目文件
echo "Step 3: 复制项目文件..."

# 创建目录结构
mkdir -p agent data models rag utils
mkdir -p yield_prediction/models yield_prediction/utils

# 主文件
cp "$SOURCE_DIR/config.py" .
cp "$SOURCE_DIR/web_app.py" app.py  # HF Space 入口必须是 app.py

# Agent 模块
cp "$SOURCE_DIR/agent/__init__.py" agent/
cp "$SOURCE_DIR/agent/prompts.py" agent/
cp "$SOURCE_DIR/agent/tools.py" agent/
cp "$SOURCE_DIR/agent/loop.py" agent/

# Models 模块
cp "$SOURCE_DIR/models/__init__.py" models/
cp "$SOURCE_DIR/models/loader.py" models/

# RAG 模块
cp "$SOURCE_DIR/rag/__init__.py" rag/
cp "$SOURCE_DIR/rag/retriever.py" rag/
cp "$SOURCE_DIR/rag/index_builder.py" rag/

# Utils 模块
cp "$SOURCE_DIR/utils/__init__.py" utils/
cp "$SOURCE_DIR/utils/smiles_utils.py" utils/
cp "$SOURCE_DIR/utils/echem_utils.py" utils/
cp "$SOURCE_DIR/utils/display.py" utils/ 2>/dev/null || touch utils/display.py

# Yield prediction 模块
touch yield_prediction/__init__.py
cp "$SOURCE_DIR/yield_prediction/models/__init__.py" yield_prediction/models/
cp "$SOURCE_DIR/yield_prediction/models/condition_recommender.py" yield_prediction/models/
cp "$SOURCE_DIR/yield_prediction/models/condition_cvae.py" yield_prediction/models/
cp "$SOURCE_DIR/yield_prediction/models/yield_predictor.py" yield_prediction/models/ 2>/dev/null || true
touch yield_prediction/utils/__init__.py
cp "$SOURCE_DIR/yield_prediction/utils/feature_extractor.py" yield_prediction/utils/
cp "$SOURCE_DIR/yield_prediction/utils/xtb_features.py" yield_prediction/utils/ 2>/dev/null || true

# 数据文件
cp "$SOURCE_DIR/data/chemistry_kb.json" data/

# 4. 复制模型权重 (大文件)
echo "Step 4: 复制模型文件..."
mkdir -p models_trained

# 检查并复制模型
if [ -d "$SOURCE_DIR/models_trained" ]; then
    cp -r "$SOURCE_DIR/models_trained/"* models_trained/ 2>/dev/null || true
fi

# 5. 复制 FAISS 索引
echo "Step 5: 复制 FAISS 索引..."
cp "$SOURCE_DIR/data/reaction_index.faiss" data/ 2>/dev/null || echo "No FAISS index found"
cp "$SOURCE_DIR/data/reaction_metadata.pkl" data/ 2>/dev/null || echo "No metadata found"

# 6. 创建 requirements.txt
echo "Step 6: 创建 requirements.txt..."
cat > requirements.txt << 'EOF'
torch>=2.0.0
numpy>=1.24.0
pandas>=2.0.0
rdkit>=2023.3.1
faiss-cpu>=1.7.4
anthropic>=0.18.0
gradio>=4.0.0
scikit-learn>=1.3.0
EOF

# 7. 创建 README.md
echo "Step 7: 创建 README.md..."
cat > README.md << 'EOF'
---
title: Electrochemical Condition Agent
emoji: ⚡
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
---

# Electrochemical Condition Agent ⚡

An intelligent AI assistant for electrochemical olefin difunctionalization reaction condition recommendation.

## Features

- **Substrate Analysis**: Analyze olefin type, functional groups, and reaction class
- **Condition Recommendation**: ML-based prediction of optimal electrochemical conditions (80.4% accuracy)
- **Similar Reaction Search**: Find similar reactions from 10,000+ database
- **Yield Prediction**: Predict reaction yield under specific conditions
- **Experimental Protocol**: Generate actionable wet-lab procedures with safety notes

## Models

| Model | Performance |
|-------|-------------|
| ConditionRecommender (XTB+Catalyst) | 80.4% top-1 accuracy |
| CategoricalCVAE (Catalyst) | 64.4% joint accuracy |

## Database

- 10,572 unique reaction-condition pairs
- Electrochemical parameters: current, current density, potential

## Usage

1. Enter your reaction SMILES: `reactants>>products`
2. **Chat tab**: Intelligent conversation with the agent
3. **Tools tab**: Direct access to individual tools

## Example

```
Input: CC(=O)OC=C>>CC(=O)OC(F)CF
Output:
- Reaction type: difluorination
- Recommended: Pt anode, Et₃N·3HF electrolyte, undivided cell
- Predicted yield: 72%
```
EOF

# 8. 配置 Git LFS
echo "Step 8: 配置 Git LFS..."
git lfs install
cat > .gitattributes << 'EOF'
*.pt filter=lfs diff=lfs merge=lfs -text
*.pth filter=lfs diff=lfs merge=lfs -text
*.faiss filter=lfs diff=lfs merge=lfs -text
*.pkl filter=lfs diff=lfs merge=lfs -text
*.bin filter=lfs diff=lfs merge=lfs -text
EOF

# 9. 提交
echo "Step 9: 提交更改..."
git add .
git status
git commit -m "Deploy Electrochemical Condition Agent v2.0

Features:
- Substrate analysis with olefin type detection
- 9 agent tools including experimental protocol generation
- Enhanced chemistry knowledge base
- 10,572 reaction-condition pairs in database"

# 10. 推送
echo "Step 10: 推送到 Hugging Face..."
git push origin main

echo ""
echo "=============================================="
echo "部署完成!"
echo "=============================================="
echo "访问: https://huggingface.co/spaces/SII-gelingli/ElectrochemicalConditionAgent"
