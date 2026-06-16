#!/bin/bash
# Hybrid GNN 训练流水线
#
# 使用方法:
#   ./run_hybrid_gnn.sh              # 完整流程
#   ./run_hybrid_gnn.sh --train-only # 仅训练
#   ./run_hybrid_gnn.sh --compute-xtb # 计算缺失的xTB特征

set -e

cd "$(dirname "$0")/.."
PROJECT_ROOT=$(pwd)

echo "========================================"
echo "Hybrid GNN 训练流水线"
echo "项目根目录: $PROJECT_ROOT"
echo "========================================"

# 检查CUDA
if python -c "import torch; print(torch.cuda.is_available())" | grep -q "True"; then
    DEVICE="cuda"
    echo "检测到 CUDA，使用 GPU 训练"
else
    DEVICE="cpu"
    echo "使用 CPU 训练"
fi

# 解析参数
COMPUTE_XTB=false
TRAIN_ONLY=false
PREPARE_DATA=true

for arg in "$@"; do
    case $arg in
        --compute-xtb)
            COMPUTE_XTB=true
            PREPARE_DATA=false
            shift
            ;;
        --train-only)
            TRAIN_ONLY=true
            PREPARE_DATA=false
            shift
            ;;
        *)
            shift
            ;;
    esac
done

# 步骤1: 计算缺失的xTB特征（可选）
if [ "$COMPUTE_XTB" = true ]; then
    echo ""
    echo "步骤1: 计算缺失的xTB特征..."
    python scripts/compute_missing_xtb.py \
        --train_data data/train.pt \
        --existing_csv data/xtb_reaction_molecules.csv \
        --output_csv data/xtb_reaction_molecules_extended.csv

    # 使用扩展后的CSV
    XTB_CSV="data/xtb_reaction_molecules_extended.csv"
else
    XTB_CSV="data/xtb_reaction_molecules.csv"
fi

# 步骤2: 准备数据
if [ "$PREPARE_DATA" = true ]; then
    echo ""
    echo "步骤2: 准备 Hybrid GNN 数据..."

    # 检查数据是否已存在
    if [ -f "data/train_hybrid.pt" ] && [ -f "data/val_hybrid.pt" ] && [ -f "data/test_hybrid.pt" ]; then
        echo "  数据文件已存在，跳过准备步骤"
        echo "  (如需重新准备，请删除 data/*_hybrid.pt)"
    else
        python scripts/prepare_data_hybrid.py \
            --input data/train.pt \
            --output_dir data \
            --xtb_csv "$XTB_CSV"
    fi
fi

# 步骤3: 训练模型
if [ "$TRAIN_ONLY" = true ] || [ "$PREPARE_DATA" = true ]; then
    echo ""
    echo "步骤3: 训练 Hybrid GNN 模型..."
    echo "目标: 超越 MLP 基线 (MAE 12.36)"
    echo ""

    python scripts/train_hybrid_gnn.py \
        --data_dir data \
        --output_dir checkpoints/hybrid_gnn \
        --batch_size 32 \
        --lr 5e-4 \
        --weight_decay 1e-4 \
        --epochs 150 \
        --patience 30 \
        --gnn_hidden 128 \
        --gnn_layers 4 \
        --gnn_heads 4 \
        --dropout 0.2 \
        --device $DEVICE
fi

echo ""
echo "========================================"
echo "完成!"
echo "========================================"
echo ""
echo "结果保存在: checkpoints/hybrid_gnn/"
echo "  - best_model.pt      : 最佳模型权重"
echo "  - results.json       : 训练结果和指标"
echo "  - test_predictions.json : 测试集预测"
