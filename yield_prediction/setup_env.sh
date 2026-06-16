#!/bin/bash
# 设置环境变量以使用本地包

export PYTHONPATH="/inspire/hdd/global_user/gelingli-253114010248/pip_packages:$PYTHONPATH"
export LD_LIBRARY_PATH="/inspire/hdd/global_user/gelingli-253114010248/pip_packages/rdkit.libs:$LD_LIBRARY_PATH"

echo "Environment configured."
echo "PYTHONPATH: $PYTHONPATH"
