#!/usr/bin/env bash
# 重组被切分的大索引文件，并校验 md5。
# 在仓库根目录运行：  bash reassemble.sh
set -euo pipefail
cd "$(dirname "$0")/data"

echo ">> 重组 faiss_index.npy ..."
cat faiss_index.npy.part* > faiss_index.npy
echo ">> 重组 faiss_index_paper.npy ..."
cat faiss_index_paper.npy.part* > faiss_index_paper.npy

echo ">> 校验 md5 ..."
declare -A EXP=(
  [faiss_index.npy]=0935f15a3ffb96319bc1c7b03563dc32
  [faiss_index_paper.npy]=9fb7c7cd0e2d38a01a5a8b19c1ad56c8
)
ok=1
for f in faiss_index.npy faiss_index_paper.npy; do
  got=$(md5sum "$f" | awk '{print $1}')
  if [ "$got" = "${EXP[$f]}" ]; then
    echo "   OK  $f  $got"
  else
    echo "   ✗ 校验失败 $f  期望 ${EXP[$f]} 实得 $got"; ok=0
  fi
done
[ "$ok" = 1 ] || { echo "重组校验失败，请重新拉取分块"; exit 1; }

echo ">> 删除分块以省空间 ..."
rm -f faiss_index.npy.part* faiss_index_paper.npy.part*
echo "完成。索引就绪：$(pwd)/faiss_index.npy , faiss_index_paper.npy"
