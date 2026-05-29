# 嵌套循环与列表推导式：将二维列表展开为一维
# 先用传统 for 循环逐元素打印，再用列表推导式收集所有元素

vec=[[1,2,3],[4,5,6],[7,8,9]]
# 传统嵌套循环
for i in vec:
    for j in i:
      print(j,end=' ')
# 等价的列表推导式（展开二维列表）
list=[j for i in vec for j in i]
print(list)
