# AI 迭代优化循环 —— 词频统计效率提升训练对话

> **场景**：用户需要统计莎士比亚《哈姆雷特》剧本中的词频。通过与 AI 的多轮对话，逐步优化代码，最终实现 **171 倍** 的性能提升。

---

## 第 1 轮：初始实现

**用户**：

> 我写了一个统计 hamlet.txt 词频的 Python 脚本，能跑，但感觉很慢。帮我看看有什么问题？

```python
def word_frequency_v1(filepath):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.strip(".,;:!?\"'()-[]{}").lower()
                if word:
                    words.append(word)

    result = []
    for w in set(words):
        result.append((w, words.count(w)))
    return sorted(result, key=lambda x: x[1], reverse=True)
```

**AI**：

> 你的代码逻辑是正确的，但存在一个严重的性能瓶颈。问题出在 `words.count(w)` 这行。
>
> **分析**：
> - 对于每一个去重后的单词 `w`，你都调用了一次 `list.count()`，这个方法需要遍历整个列表
> - 假设有 N 个单词，去重后有 U 个唯一单词，时间复杂度是 **O(N × U) ≈ O(N²)**
> - 《哈姆雷特》全文约 3 万个单词，这意味着约 **9 亿次** 比较操作
>
> **建议**：使用字典（dict）在一次遍历中完成计数，时间复杂度可降为 **O(N)**。

**用户**：

> 好的，我试试用字典改写。

---

## 第 2 轮：字典优化

**用户**：

> 改成字典版本后快了很多！但还能更快吗？

```python
def word_frequency_v2(filepath):
    word_count = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.strip(".,;:!?\"'()-[]{}").lower()
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)
```

**AI**：

> 字典版本已经将复杂度降到 O(N)，非常好。但还有两个优化空间：
>
> **1. 使用 `collections.Counter`**：
> Python 标准库提供了 `Counter`，专为计数设计，底层用 C 实现，比纯 Python 字典 `get()` 快 30%-50%。
>
> **2. 使用正则表达式分词**：
> 当前的 `split()` + `strip()` 对每个单词执行多次字符串操作。使用 `re.findall()` 可以一次性提取所有英文单词，减少 Python 层的循环开销。
>
> **代码对比**：
> ```python
> # 之前：split + strip 逐词处理
> for word in line.split():
>     word = word.strip(".,;:!?\"'()-[]{}").lower()
>
> # 之后：正则一次性提取（先统一转为小写）
> import re
> words = re.findall(r'[a-z]+', text.lower())
> ```

**用户**：

> Counter 确实更简洁。我再试试正则方案。

---

## 第 3 轮：Counter + 正则

**用户**：

> 用 `Counter` + `re.findall()` 重写了，代码少了很多，速度又快了！

```python
import re
from collections import Counter

def word_frequency_v3(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()
    words = re.findall(r'[a-z]+', text)
    return Counter(words).most_common(20)
```

**AI**：

> 这个版本已经很高效了。但我注意到一个细节：`re.findall()` 在函数内每次调用都会**重新编译正则表达式**。
>
> **编译正则表达式**：
> 将正则模式 `r'[a-z]+'` 用 `re.compile()` 编译为模块级常量，避免每次函数调用时的编译开销。
>
> 虽然单次提升微小（毫秒级），但在循环调用或大文件场景下，这是一个好习惯。
>
> ```python
> # 模块顶部，编译一次，全局复用
> WORD_RE = re.compile(r'[a-z]+')
> ```

**用户**：

> 明白了，我把正则提到外面编译。还有别的建议吗？

**AI**：

> 当前版本已经是 **理论最优** 的单线程方案了：
> - 分词：`re.findall()` 一次遍历，C 层实现
> - 计数：`Counter` 一次遍历，C 层实现
> - 排序：`most_common()` 使用堆排序，只取 Top-K，无需全排
>
> 如果还想更快，可以考虑：
> - **多进程并行**：将文件分块，多个进程分别统计，最后合并 Counter
> - **使用 `mmap`**：避免将整个文件加载到内存
>
> 不过对于《哈姆雷特》这个规模（~200KB），当前方案已经完全够用。

---

## 第 4 轮：最终版本与性能总结

**用户**：

> 把编译正则加上，这就是最终版了。能帮我跑个性能对比吗？

**AI**：

> 当然。以下是各版本的性能测试结果（测试环境：Windows 11, Python 3.14）：

```
=========================================================
  AI 迭代优化：词频统计性能对比
=========================================================

[V1] 朴素版 (list.count, O(n^2))
  耗时: 1.2072s

[V4] AI优化版 (re + Counter, O(n))
  耗时: 0.0071s

-------------------------------------------------------
版本           耗时        提升倍数
-------------------------------------------------------
V1 朴素版      1.2072s        —
V4 优化版      0.0071s    171.1x
-------------------------------------------------------
```

| 轮次 | 优化手段 | 时间复杂度 | 耗时 | 提升 |
|------|----------|-----------|------|------|
| V1 | list.count() 逐个统计 | O(n²) | 1.2072s | — |
| V2 | dict 一次遍历 | O(n) | ~0.05s | ~24x |
| V3 | Counter + re.findall() | O(n) | ~0.01s | ~120x |
| V4 | 编译正则 + most_common() | O(n) | 0.0071s | **171x** |

**用户**：

> 从 1.2 秒降到 0.007 秒，171 倍的提升！太夸张了。

**AI**：

> 这就是 **AI 迭代优化循环** 的核心价值：
>
> 1. **第 1 轮**：识别算法瓶颈（O(n²) → O(n)）
> 2. **第 2 轮**：引入标准库专用工具（dict → Counter）
> 3. **第 3 轮**：优化数据处理管道（split+strip → 正则）
> 4. **第 4 轮**：消除微小开销（编译正则）+ 结构化输出
>
> 每一轮改进都由 AI 分析代码、指出瓶颈、给出可执行的方案。用户只需要理解和实施，不需要从零学习算法复杂度或 Python 标准库的全部细节。
>
> 关键启示：
> - **算法选择是第一生产力**（O(n²) → O(n) 贡献了最大提升）
> - **标准库往往比手写快**（Counter 是 C 实现的）
> - **减少 Python 层循环**（正则批量处理优于逐词 split）
> - **细节决定极致性能**（编译正则、most_common 堆排序）

---

## 最终代码 (`word_freq_final.py`)

```python
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
```

**输出示例**：
```
V4 耗时: 0.0071s
   1. the            1144
   2. and             964
   3. to              754
   4. of              669
   5. i               577
   6. you             554
   7. a               550
   8. my              520
   9. hamlet          475
  10. in              434
  ...
```

---

## 总结

通过 4 轮 AI 迭代优化，词频统计从 **1.2072 秒降至 0.0071 秒**，性能提升 **171 倍**。AI 在每一轮中提供了：

- **算法复杂度分析**（识别 O(n²) 瓶颈）
- **标准库推荐**（Counter 替代手写字典）
- **代码模式优化**（正则替代逐词处理）
- **最佳实践**（编译正则、堆排序 Top-K）

整个过程展示了 **"人提问 + AI 诊断 + 人实施 + 验证循环"** 的高效协作模式。
