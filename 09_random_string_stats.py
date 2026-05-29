# random + string 生成随机字符串并统计字符出现频率
# 从字母、数字、标点中随机选 100 个字符，统计每个字符出现次数

import random
import string

# 构造字符池：大小写字母 + 数字 + 标点符号
x=string.ascii_letters+string.digits+string.punctuation
print(x)

# 随机选择 100 个字符拼接成字符串
y=[random.choice(x) for i in range(100)]
z=''.join(y)

# 统计每个字符的出现次数（利用 get() 设置默认值 0）
d=dict()
for ch in z:
    d[ch]=d.get(ch,0)+1

# 输出统计结果（每行一个，格式清晰）
for k,v in d.items():
    print(f'{k}: {v}')
