#!/usr/bin/env python3
"""从OpenAlex批量检索每篇文章的DOI，写回yield JSON文件。"""

import json
import glob
import os
import time
import urllib.request
import urllib.parse
import re

DATA_DIR = "/inspire/hdd/global_user/gelingli-253114010248/WDproject2/condition_agent/data/alkene_reactions_by_yield"
CACHE_FILE = os.path.join(DATA_DIR, "doi_cache.json")
MAILTO = "gelingli@example.com"  # OpenAlex polite pool


def normalize_title(title):
    """标准化标题用于匹配：小写、去掉多余空白和标点。"""
    t = title.lower().strip()
    t = re.sub(r'\s+', ' ', t)
    return t


def search_openalex(title):
    """用标题在OpenAlex中搜索，返回 (doi, openalex_id) 或 (None, None)。"""
    url = (
        "https://api.openalex.org/works?search="
        + urllib.parse.quote(title)
        + f"&per_page=3&mailto={MAILTO}"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DOI-Fetcher/1.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read())
    except Exception as e:
        print(f"    [ERROR] API请求失败: {e}")
        return None, None

    if not data.get("results"):
        return None, None

    # 在前3个结果中找标题最匹配的
    norm_query = normalize_title(title)
    for w in data["results"]:
        w_title = w.get("title") or ""
        if normalize_title(w_title) == norm_query:
            doi = w.get("doi")  # 格式: https://doi.org/10.xxx
            oa_id = w.get("id")
            return doi, oa_id

    # 没有精确匹配，取第一个结果（如果标题相似度足够高）
    first = data["results"][0]
    first_title = normalize_title(first.get("title") or "")
    # 简单相似度：共同单词比例
    words_q = set(norm_query.split())
    words_f = set(first_title.split())
    if len(words_q) > 0:
        overlap = len(words_q & words_f) / max(len(words_q), len(words_f))
        if overlap >= 0.75:
            return first.get("doi"), first.get("id")

    return None, None


def main():
    # 加载缓存（避免重复查询）
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)
        print(f"已加载缓存: {len(cache)} 条")
    else:
        cache = {}

    # 收集所有唯一标题
    all_files = sorted(glob.glob(os.path.join(DATA_DIR, "yield_*.json")))
    titles = set()
    for fp in all_files:
        data = json.load(open(fp, "r", encoding="utf-8"))
        for r in data:
            t = r.get("title")
            if t:
                titles.add(t)

    print(f"唯一文章数: {len(titles)}")
    to_query = [t for t in titles if t not in cache]
    print(f"需要查询: {len(to_query)} (已缓存: {len(titles) - len(to_query)})")

    # 批量查询
    for i, title in enumerate(to_query):
        doi, oa_id = search_openalex(title)
        cache[title] = {"doi": doi, "openalex_id": oa_id}

        status = doi if doi else "NOT FOUND"
        print(f"  [{i+1}/{len(to_query)}] {status}  <- {title[:70]}")

        # 每50条保存一次缓存
        if (i + 1) % 50 == 0:
            with open(CACHE_FILE, "w") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

        # OpenAlex polite pool: ~10 req/s 足够，稍微加延迟防封
        time.sleep(0.15)

    # 最终保存缓存
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    # 统计
    found = sum(1 for v in cache.values() if v.get("doi"))
    print(f"\nDOI检索结果: {found}/{len(titles)} ({100*found/len(titles):.1f}%)")

    # 写回yield文件
    total_updated = 0
    for fp in all_files:
        data = json.load(open(fp, "r", encoding="utf-8"))
        changed = False
        for r in data:
            t = r.get("title")
            if t and t in cache:
                info = cache[t]
                if info.get("doi"):
                    r["doi"] = info["doi"]
                    total_updated += 1
                    changed = True
                else:
                    r["doi"] = None
                    changed = True
        if changed:
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已更新 {total_updated} 条反应记录的DOI")


if __name__ == "__main__":
    main()
