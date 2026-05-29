"""
性能对比基准测试
运行 V1 朴素版 和 V4 最终版，展示效率提升
"""

import time
import sys
sys.path.insert(0, ".")

import v1_naive
import word_freq_final

FILEPATH = "../hamlet.txt"
TOP_N = 20

print("=" * 55)
print("  AI 迭代优化：词频统计性能对比")
print("=" * 55)

# --- V1 ---
print("\n[V1] 朴素版 (list.count, O(n^2))")
t1 = time.perf_counter()
r1 = v1_naive.word_frequency_v1(FILEPATH)[:TOP_N]
t1 = time.perf_counter() - t1

# --- V4 ---
print("\n[V4] AI优化版 (re + Counter, O(n))")
t4 = time.perf_counter()
r4 = word_freq_final.word_frequency_v4(FILEPATH, TOP_N)
t4 = time.perf_counter() - t4

# --- 对比 ---
print("\n" + "-" * 55)
print(f"{'版本':<12} {'耗时':>10}  {'提升':>12}")
print("-" * 55)
print(f"{'V1 朴素版':<12} {t1:>8.4f}s  {'—':>12}")
print(f"{'V4 优化版':<12} {t4:>8.4f}s  {t1/t4:>11.1f}x")
print("-" * 55)

# --- 验证结果一致性 ---
print(f"\n结果一致性: {'[一致]' if r1 == r4 else '[有差异]'} (取前{TOP_N}个高频词对比)")
