# Condition Agent — 阿里云 ECS 部署包（全量 RAG 数据）

本仓库是 condition_agent 的**运行时最小包**：代码 + 全量反应检索索引（24,305 条，audited 全量）+ 模型 checkpoint，已剔除训练数据/优化器/qwen LoRA 等无关大文件。CPU 即可运行，无需 GPU。

## 一键部署

```bash
git clone https://github.com/SII-gelingli/ECSuploadproject.git
cd ECSuploadproject

export ANTHROPIC_API_KEY=sk-你的key            # 必填
# 下面两个可选，有默认值
# export ANTHROPIC_BASE_URL=https://api.boyuerichdata.opensphereai.com
# export ANTHROPIC_MODEL=claude-opus-4-6

bash setup_ecs.sh
```

`setup_ecs.sh` 会依次：① 装系统依赖 → ② 重组并校验大索引 → ③ 建 venv 装 Python 依赖 → ④ 启动 Gradio Web 服务（`0.0.0.0:7860`）。

启动后：
- **公网 IP 访问**：在阿里云安全组放行 TCP **7860**，浏览器开 `http://47.98.18.118:7860`
- **临时公网链接**：把启动命令改成 `python web_app.py --port 7860 --host 0.0.0.0 --share`

## 大文件说明

两个索引因超过 GitHub 单文件 100MB 限制被切分为 `data/*.npy.part*`：

| 文件 | 大小 | md5 |
|---|---|---|
| `data/faiss_index.npy`（全量反应 RAG，24,305 条） | 570M | `0935f15a3ffb96319bc1c7b03563dc32` |
| `data/faiss_index_paper.npy`（paper 级检索） | 576M | `9fb7c7cd0e2d38a01a5a8b19c1ad56c8` |

`reassemble.sh`（被 setup 自动调用）会 `cat *.part* > *.npy` 并校验 md5。

## 运行时不带 GPU / xtb

线上模型是 6144 维指纹版，不依赖 xtb 量化特征。检索走 numpy 暴力匹配（已装 faiss-cpu 也可，但本包只发 `.npy`，retriever 自动用 numpy 后端，24k 向量开销可忽略）。

## 手动启动（venv 已建好后）

```bash
source .venv/bin/activate
export ANTHROPIC_API_KEY=sk-...
python web_app.py --port 7860 --host 0.0.0.0
```
