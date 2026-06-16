# 电化学反应产率预测与条件推荐系统

基于深度学习的电化学反应产率预测和最优反应条件推荐系统。

## 项目结构

```
yield_prediction/
├── configs/
│   └── config.yaml          # 配置文件
├── models/
│   ├── yield_predictor.py   # 产率预测模型
│   └── condition_recommender.py  # 条件推荐模型
├── utils/
│   ├── data_processor.py    # 数据处理
│   └── feature_extractor.py # 分子特征提取
├── scripts/
│   ├── train.py             # 产率模型训练
│   ├── train_condition.py   # 条件模型训练
│   └── predict.py           # 预测脚本
├── run.py                   # 主入口
└── requirements.txt         # 依赖
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 数据说明

- **alkene_reactions_by_yield/**: 按产率分类的电化学反应数据
- **extracted_smiles.json**: 提取的SMILES反应数据

数据包含:
- 反应物/产物 SMILES
- 电化学参数 (阳极、阴极、电解质、电流等)
- 反应产率

## 使用方法

### 1. 训练产率预测模型

```bash
python run.py train-yield --config configs/config.yaml
```

### 2. 训练条件推荐模型

```bash
python run.py train-condition --config configs/config.yaml
```

### 3. 运行预测

```bash
# 演示模式
python run.py predict --demo

# 批量预测
python run.py predict --input reactions.json --output results.json
```

## 模型说明

### 产率预测模型 (YieldPredictor)

- 输入: 反应物指纹 + 产物指纹 + 差异指纹 + 溶剂指纹 + 电解质指纹 + 电化学参数
- 输出: 预测产率 (0-100%)
- 架构: MLP with BatchNorm and Dropout

### 条件推荐模型 (ConditionRecommender)

- 输入: 反应指纹 (反应物 + 产物)
- 输出:
  - 阳极材料 (分类)
  - 阴极材料 (分类)
  - 电解池类型 (分类)
  - 电解质 (分类)
  - 溶剂 (分类)
  - 电流 (回归)
  - 电流密度 (回归)

## 配置说明

见 `configs/config.yaml`:

- `data`: 数据路径和划分比例
- `model`: 模型架构参数
- `training`: 训练超参数
- `output`: 输出路径

## 评估指标

- **MAE**: 平均绝对误差 (%)
- **RMSE**: 均方根误差 (%)
- **R²**: 决定系数

## 特征工程

1. **分子指纹**: Morgan/ECFP指纹 (2048位)
2. **反应指纹**: [反应物FP | 产物FP | 差异FP]
3. **电化学参数**: 电极编码 + 电流 + 电流密度 + 电解池类型
