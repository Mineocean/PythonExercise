# 列表推导式 + strip() 去除字符串两端空白
# 对列表中每个元素调用 strip()，返回处理后的新列表

# str.strip 是字符串方法，无需额外导入
lst=['    banana','   loganberry','passion']
a=[w.strip() for w in lst]
print(a)
