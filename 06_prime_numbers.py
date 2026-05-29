# 列表推导式筛选质数（两种写法）
# 方法一：all() + 取余判断
# 方法二：0 not in + 列表推导式中的取余判断

import math  # 移到文件头部，确保 math.sqrt 可用

primes = [x for x in range(2, 101) if all(x % d != 0 for d in range(2, int(math.sqrt(x) + 1)))]
print(primes)

primes=[p for p in range(2,100) if 0 not in [p%d for d in range(2,int(math.sqrt(p))+1)]]
print(primes)
