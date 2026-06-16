#!/usr/bin/env python3
import sys
LOCAL_PACKAGES = "/inspire/hdd/global_user/gelingli-253114010248/pip_packages"
sys.path.insert(0, LOCAL_PACKAGES)

import torch
from pathlib import Path

data_dir = Path(__file__).parent.parent / 'data'

print("=== Checking train_xtb_cat.pt ===")
data = torch.load(data_dir / 'train_xtb_cat.pt', weights_only=False)
print(f"Total samples: {len(data)}")
print("\nKeys in first sample:")
for k, v in data[0].items():
    if isinstance(v, list):
        print(f"  {k}: list, len={len(v)}")
    elif isinstance(v, torch.Tensor):
        print(f"  {k}: tensor, shape={v.shape}")
    else:
        print(f"  {k}: {type(v).__name__} = {v}")
