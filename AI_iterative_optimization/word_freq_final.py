"""
V4 - 最终优化版
结合 AI 所有建议：编译正则、Counter、most_common()
"""

import re
import time
from collections import Counter

# 编译正则，只匹配英文字母，预处理阶段复用
WORD_RE = re.compile(r"[a-z]+")


def word_frequency_v4(filepath: str, top_n: int = 20) -> list[tuple[str, int]]:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = WORD_RE.findall(text)
    counter = Counter(words)
    return counter.most_common(top_n)


if __name__ == "__main__":
    start = time.perf_counter()
    top20 = word_frequency_v4("../hamlet.txt", 20)
    elapsed = time.perf_counter() - start

    print(f"V4 耗时: {elapsed:.4f}s")
    for i, (word, count) in enumerate(top20, 1):
        print(f"  {i:>2}. {word:<15} {count}")
