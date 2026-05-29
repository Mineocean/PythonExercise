# 字典 get() 方法：安全取值，键不存在时返回默认值而非抛出异常
# 同时对比传统的 if/else 键存在性检查方式

d={1:'a',2:'b',3:'c',4:'d',5:'e'}

# 循环获取有效输入，防止非数字输入导致 ValueError
while True:
    try:
        c=int(input('Enter a number:'))
        break
    except ValueError:
        print('Invalid input, please enter an integer')

# get() 方法：键不存在时返回 'Not found'，不会报错
print(d.get(c,'Not found'))

# 传统写法：先判断键是否存在，存在则取值
if c in d:
    print(d[c])
else:
    print('Not found')
