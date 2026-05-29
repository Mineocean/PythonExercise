# 自定义函数 + 条件筛选的列表推导式
# f(v)：偶数平方，奇数加1；列表推导式中过滤掉 v<=0 的元素

def f(v):
    if v%2==0:
        v=v**2
    else:
        v=v+1
    return v

# 只对 v>0 的元素调用 f()，-1 被过滤
print([f(v)for v in [2,3,4,-1]if v>0])
