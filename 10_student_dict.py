# 嵌套字典：存储学生信息，包含嵌套的 score 字典和 course 列表
# 演示多层级键值访问以及列表的 append 操作

student={
    'id':114514,
    'name':"先辈",
    'age':22,
    'score':{'math':99,'english':100,'computer':66},  # 嵌套字典
    'course':['Python','Data']                          # 嵌套列表
}

# 访问各级数据
print(f"{student['name']}")           # 顶层键
print(f"{student['score']['math']}")  # 嵌套字典中的键
print(f"{student['course'][0]}")      # 嵌套列表中的索引

# 向 course 列表追加新课程
student['course'].append('AI')
print(f"{student['course']}")
