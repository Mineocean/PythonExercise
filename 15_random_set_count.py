# random + set 去重与计数：生成大量随机数，用 set 去重后统计出现次数
# set 自动去重，count() 统计每个值在原列表中出现的次数

import  random

# 生成 1000 个 1-100 的随机整数
x=[random.randint(1,100) for i in range(1000)]

# set 自动去重
s=set(x)
print(s)

# 统计每个唯一值在原列表中出现的次数
for i in s:
    print(i,':',x.count(i))
