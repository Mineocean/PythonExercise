# 列表推导式实现矩阵转置：将 3x4 矩阵转置为 4x3
# 外层循环遍历列索引 i，内层循环遍历每一行取第 i 列元素

maxtir=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result=[[row[i] for row in maxtir] for i in range(4)]
print(result)
