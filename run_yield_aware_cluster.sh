#!/bin/bash
# 产率感知聚类实验脚本

cd /inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/yield_prediction

echo "=============================================="
echo "产率感知聚类 (Yield-Aware Clustering) 实验"
echo "=============================================="

# 方法1: 产率分层聚类 (推荐)
echo ""
echo ">>> 实验1: 产率分层聚类 (stratified) - 4层 x 2子聚类 = 8类"
python scripts/train_yield_aware_cluster.py \
    --cluster_method stratified \
    --n_yield_bins 4 \
    --n_subclusters 2 \
    --output_dir checkpoints/yield_aware_stratified_4x2 \
    2>&1 | tee ../yield_aware_stratified_4x2.log

echo ""
echo ">>> 实验2: 产率分层聚类 (stratified) - 5层 x 2子聚类 = 10类"
python scripts/train_yield_aware_cluster.py \
    --cluster_method stratified \
    --n_yield_bins 5 \
    --n_subclusters 2 \
    --output_dir checkpoints/yield_aware_stratified_5x2 \
    2>&1 | tee ../yield_aware_stratified_5x2.log

echo ""
echo ">>> 实验3: 产率分层聚类 (stratified) - 6层 x 1子聚类 = 6类 (纯产率分层)"
python scripts/train_yield_aware_cluster.py \
    --cluster_method stratified \
    --n_yield_bins 6 \
    --n_subclusters 1 \
    --output_dir checkpoints/yield_aware_stratified_6x1 \
    2>&1 | tee ../yield_aware_stratified_6x1.log

# 方法2: 联合特征聚类
echo ""
echo ">>> 实验4: 联合特征聚类 (joint) - yield_weight=0.3"
python scripts/train_yield_aware_cluster.py \
    --cluster_method joint \
    --n_yield_bins 4 \
    --n_subclusters 2 \
    --yield_weight 0.3 \
    --output_dir checkpoints/yield_aware_joint_w0.3 \
    2>&1 | tee ../yield_aware_joint_w0.3.log

echo ""
echo ">>> 实验5: 联合特征聚类 (joint) - yield_weight=0.5"
python scripts/train_yield_aware_cluster.py \
    --cluster_method joint \
    --n_yield_bins 4 \
    --n_subclusters 2 \
    --yield_weight 0.5 \
    --output_dir checkpoints/yield_aware_joint_w0.5 \
    2>&1 | tee ../yield_aware_joint_w0.5.log

# 方法3: 层次聚类
echo ""
echo ">>> 实验6: 层次聚类 (hierarchical) - 4层 x 2子聚类"
python scripts/train_yield_aware_cluster.py \
    --cluster_method hierarchical \
    --n_yield_bins 4 \
    --n_subclusters 2 \
    --output_dir checkpoints/yield_aware_hierarchical_4x2 \
    2>&1 | tee ../yield_aware_hierarchical_4x2.log

echo ""
echo "=============================================="
echo "所有实验完成！"
echo "=============================================="
