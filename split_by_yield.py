#!/usr/bin/env python3
"""将武大烯烃双官能团反应.jsonl按产率分到不同的json文件中，格式与alkene_reactions_by_yield一致。"""

import json
import os
import re

INPUT = "/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/武大烯烃双官能团反应.jsonl"
OUTPUT_DIR = "/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/data/alkene_reactions_by_yield"

# 产率区间定义（与参考目录一致）
BINS = [
    ("yield_0.json",       lambda y: y == 0),
    ("yield_1-10.json",    lambda y: 1 <= y <= 10),
    ("yield_11-20.json",   lambda y: 11 <= y <= 20),
    ("yield_21-30.json",   lambda y: 21 <= y <= 30),
    ("yield_31-40.json",   lambda y: 31 <= y <= 40),
    ("yield_41-50.json",   lambda y: 41 <= y <= 50),
    ("yield_51-60.json",   lambda y: 51 <= y <= 60),
    ("yield_61-70.json",   lambda y: 61 <= y <= 70),
    ("yield_71-80.json",   lambda y: 71 <= y <= 80),
    ("yield_81-90.json",   lambda y: 81 <= y <= 90),
    ("yield_91-100.json",  lambda y: 91 <= y <= 100),
]

def parse_reference(prompt):
    """从prompt字段中解析文献信息：Title, Author, Citation。"""
    ref = {}
    m = re.search(r'\*\*Title\*\*:\s*(.+)', prompt)
    if m:
        ref["title"] = m.group(1).strip()
    m = re.search(r'\*\*Author\*\*:\s*(.+)', prompt)
    if m:
        ref["author"] = m.group(1).strip()
    m = re.search(r'\*\*Citation\*\*:\s*(.+)', prompt)
    if m:
        ref["citation"] = m.group(1).strip()
    return ref

def extract_reaction(line_obj):
    """从JSONL的一行中提取conversation_evaluation作为反应记录。"""
    ev = line_obj.get("evaluation", {})
    ce = ev.get("conversation_evaluation")
    if ce is None:
        return None

    # 跳过无效反应
    if ce.get("is_valid") != "true":
        return None

    # 从prompt中提取文献信息
    prompt = line_obj.get("prompt", "")
    ref = parse_reference(prompt)

    # 提取目标字段，与参考格式一致，并加入文献信息
    record = {
        "is_valid": ce.get("is_valid"),
        "cas_reaction_number": ce.get("cas_reaction_number"),
        "title": ref.get("title"),
        "author": ref.get("author"),
        "citation": ref.get("citation"),
        "reaction_smiles": ce.get("reaction_smiles"),
        "mapped_smiles": ce.get("mapped_smiles"),
        "electrochemistry_params": ce.get("electrochemistry_params"),
        "reactants": ce.get("reactants", []),
        "products": ce.get("products", []),
        "reagents": ce.get("reagents", []),
        "solvents": ce.get("solvents", []),
        "catalysts": ce.get("catalysts", []),
        "product_yield": ce.get("product_yield"),
    }
    return record

def parse_yield(val):
    """解析产率字符串为数值，返回 (numeric_yield, is_unknown)。"""
    if val is None or val == "" or val == "null":
        return None, True
    try:
        y = float(val)
        return y, False
    except (ValueError, TypeError):
        return None, True

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 初始化分桶
    buckets = {name: [] for name, _ in BINS}
    buckets["yield_unknown.json"] = []

    total = 0
    valid = 0
    skipped_invalid = 0

    with open(INPUT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            obj = json.loads(line)
            record = extract_reaction(obj)
            if record is None:
                skipped_invalid += 1
                continue
            valid += 1

            y_val, is_unknown = parse_yield(record["product_yield"])

            if is_unknown:
                buckets["yield_unknown.json"].append(record)
            else:
                y_int = int(round(y_val))
                placed = False
                for name, check in BINS:
                    if check(y_int):
                        buckets[name].append(record)
                        placed = True
                        break
                if not placed:
                    # 超出 0-100 范围的也归入 unknown
                    buckets["yield_unknown.json"].append(record)

    # 写出文件
    for name, records in buckets.items():
        out_path = os.path.join(OUTPUT_DIR, name)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    # 打印统计
    print(f"总行数: {total}")
    print(f"有效反应: {valid}")
    print(f"跳过(无效): {skipped_invalid}")
    print(f"\n按产率分布:")
    for name, _ in BINS:
        print(f"  {name:20s}: {len(buckets[name]):5d}")
    print(f"  {'yield_unknown.json':20s}: {len(buckets['yield_unknown.json']):5d}")
    print(f"  {'合计':20s}: {sum(len(v) for v in buckets.values()):5d}")

if __name__ == "__main__":
    main()
