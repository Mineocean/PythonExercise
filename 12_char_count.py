# 使用字典统计字符串中每个字符的出现次数
# 利用 get() 方法为首次出现的字符初始化计数为 0

text='Python is a powerful programming language'
char_count={}
for ch in text:
    # get(ch,0)：键不存在时返回 0，实现首次计数
    char_count[ch]=char_count.get(ch,0)+1

# 输出每个字符及其出现次数
for i,v in char_count.items():
    print(i,':',v)
