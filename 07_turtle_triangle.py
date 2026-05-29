# turtle 库绘制三角形：用户输入三个顶点坐标，程序计算边长与周长
# 包含输入验证（逗号分隔、整数检查）、边长计算、周长计算

import turtle
import math

# 获取三个顶点坐标，带输入验证
triangle=[]
print('Positions(x,y):')
for i in range(3):
    while True:
        coord_input=input(f'the({i+1})point position:').strip()
        #First Check：必须包含逗号
        if ','not in coord_input:
            print('invalid input(Give me (x,y))')
            continue
        x_str,y_str=coord_input.split(',',1)
        #Second Check：坐标值必须为整数
        try:
            x=int(x_str)
            y=int(y_str)
            triangle.append([x,y])
            break
        except ValueError:
            print('invalid input(Give me Valid(x,y))')
            continue

#计算三角形的三条边长
p1,p2,p3=triangle
side1=math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)  #p1-p2的边长
side2=math.sqrt((p3[0]-p2[0])**2+(p3[1]-p2[1])**2)  #p2-p3的边长
side3=math.sqrt((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)  #p3-p1的边长
side_length=[side1,side2,side3]
perimeter=sum(side_length)
print('======Angle======')
print(f'顶点坐标：{triangle}')
print(f'三边长：{[round(s,2) for s in side_length]}')
print(f'周长：{round(perimeter,2)}')

# 初始化 turtle 画笔（未完成绘制逻辑）
pen=turtle.Turtle()
pen.speed(2)
pen.color('Blue')
pen.fillcolor('LightBlue')
