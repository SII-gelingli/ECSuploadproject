# Stage-1 + Stage-2 训练实验归档

各文件含义:
- `stage1_baseline.pt`: 不用 FG, 不用 cond decoding
- `stage1_fg.pt`: 仅 FG, 不用 cond decoding
- `stage1_cond.pt`: 不用 FG, 用 cond decoding
- `stage1_fg_cond.pt`: FG + cond decoding (Stage-1 val 65.25%)
- `stage2_baseline.pt`: 不用 FG (Stage-2 val 0.488)
- `stage2_fg.pt`: 用 FG (Stage-2 val 0.506)

eval_*.json: 对应组合在 2025+ test 上的指标
