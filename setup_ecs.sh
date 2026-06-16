#!/usr/bin/env bash
# 一键在阿里云 ECS 上部署 condition_agent（CPU 版，全量 RAG 数据）。
# 用法：
#   export ANTHROPIC_API_KEY=sk-xxx          # 必填
#   export ANTHROPIC_BASE_URL=https://...    # 可选，默认见下
#   export ANTHROPIC_MODEL=claude-opus-4-6   # 可选
#   bash setup_ecs.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

PIP_MIRROR="${PIP_MIRROR:-https://mirrors.aliyun.com/pypi/simple/}"
: "${ANTHROPIC_API_KEY:?请先 export ANTHROPIC_API_KEY=...}"
export ANTHROPIC_BASE_URL="${ANTHROPIC_BASE_URL:-https://api.boyuerichdata.opensphereai.com}"
export ANTHROPIC_MODEL="${ANTHROPIC_MODEL:-claude-opus-4-6}"

echo "================ 1/4 系统依赖 ================"
if ! command -v python3 >/dev/null; then sudo dnf install -y python3 python3-pip; fi
python3 --version

echo "================ 2/4 重组索引 ================"
if [ ! -f data/faiss_index.npy ]; then bash reassemble.sh; else echo "索引已存在，跳过"; fi

echo "================ 3/4 Python 依赖 ================"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip -i "$PIP_MIRROR"
# CPU 版 torch（避免拉 CUDA 大包）
pip install -i "$PIP_MIRROR" torch --index-url https://download.pytorch.org/whl/cpu || \
  pip install -i "$PIP_MIRROR" torch
pip install -i "$PIP_MIRROR" \
  anthropic gradio httpx numpy openai pandas rdkit scipy scikit-learn tqdm faiss-cpu

echo "================ 4/4 启动 Web 服务 ================"
echo "ANTHROPIC_BASE_URL=$ANTHROPIC_BASE_URL  MODEL=$ANTHROPIC_MODEL"
echo "启动后访问 http://<ECS公网IP>:7860 （需在安全组放行 7860 端口）"
echo "或加 --share 生成临时公网链接。"
exec python web_app.py --port 7860 --host 0.0.0.0
