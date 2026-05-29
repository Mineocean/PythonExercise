"""
V1 - 初始朴素版本
用户最初写的词频统计：逐行读取，用列表存储所有单词，逐个 count() 统计
问题：每个单词都调用 list.count()，时间复杂度 O(n^2)
"""

import time


def word_frequency_v1(filepath: str) -> list[tuple[str, int]]:
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.strip(".,;:!?\"'()-[]{}").lower()
                if word:
                    words.append(word)

    # 去重后逐个 count —— O(n²)
    result = []
    for w in set(words):
        result.append((w, words.count(w)))
    return sorted(result, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    start = time.perf_counter()
    top = word_frequency_v1("../hamlet.txt")[:20]
    elapsed = time.perf_counter() - start
    print(f"V1 耗时: {elapsed:.3f}s")
    for w, c in top:
        print(f"  {w}: {c}")
