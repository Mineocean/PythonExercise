"""import strip
list=['    banana','   loganberry','passion']
a=[w.strip() for w in list]
print(a)
from file input import filename

vec=[[1,2,3],[4,5,6],[7,8,9]]
for i in vec:
    for j in i:
      print(j,end=' ')
list=[j for i in vec for j in i]
print(list)

import os
[filename for filename in os.listdir('.') \
 if filename.endswith('.py ') and filename.startswith('s')]

maxtir=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list=[[row[i]for row in Maxtor] for i in range(4) ]
print(list)

def f(v):
    if v%2==0:
        v=v**2
    else:
        v=v+1
    return v
print([f(v)for v in [2,3,4,-1]if v>0])

primes = [x for x in range(2, 101) if all(x % d != 0 for d in range(2, int(math.sqrt(x) + 1))]
print(primes)
import math
primes=[p for p in range(2,100) if 0 not in [p%d for d in range(2,int(math.sqrt(p))+1)]]
print(primes)

import turtle
import math
triangle=[]
print('Positions(x,y):')
for i in range(3):
    while True:
        coord_input=input(f'the({i+1})point position:').strip()
        #First Check
        if ','not in coord_input:
            print('invalid input(Give me (x,y))')
            continue
        x_str,y_str=coord_input.split(',',1)
        #Second Check
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

pen=turtle.Turtle()
pen.speed(2)
pen.color('Blue')
pen.fillcolor('LightBlue')

d={1:'a',2:'b',3:'c',4:'d',5:'e'}
c=int(input('Enter a number:'))
print(d.get(c,'Not found'))
if c in d:
    print(d[c])
else:
    print('Not found')


import random
import string
x=string.ascii_letters+string.digits+string.punctuation
print(x)
y=[random.choice(x) for i in range(100)]
z=''.join(y)
d=dict()
for ch in z:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print((k,v),end=',')


student={
    'id':114514,
    'name':"先辈",
    'age':22,
    'score':{'math':99,'english':100,'computer':66},
    'course':['Python','Data']
}
print(f"{student['name']}")
print(f"{student['score']['math']}")
print(f"{student['course'][0]}")

student['course'].append('AI')
print(f"{student['course']}")


config={
    'input_path':'./data/input',
    'output_path':'./data/output',
    'log_level':'Error',
    'Max_treads':4,
    'timeout':30
}
print(f'input_path:{config["input_path"]}')
config['timeout']=90000
print(f'timeout:{config["timeout"]}')


text='Python is a powerful programming language'
char_count={}
for ch in text:
    char_count[ch]=char_count.get(ch,0)+1
for i,v in char_count.items():
    print(i,':',v)

#模拟登录系统
login_cache={}
def login(user_id,token):
    login_cache[user_id]=token
    print(f"User {user_id} login success,Cache updated")
def check_login(user_id,token):
    cache_token=login_cache.get(user_id,None)
    if cache_token==token:
        return True,"Login in OK"
    else:
        return False,"Login in Failed or Token Expired"
#模拟用户登录
login("Tom","0d000721")
print(check_login("Tom","0d000721"))
login("Jerry","0d000722")
print(check_login("Jerry","0d000722") )
#用户登出
del login_cache["Tom"]
print(check_login("Tom","0d000722"))



#配置多条件映射
#根据用户角色分配用户权限
role_permissions={
    'admin':['read','write','delete','create','manage'],
    'user':['read','write'],
    'viewer':['read']
}
def get_user_permissions(role):
    return role_permissions.get(role,[])
for role in ['admin', 'user', 'viewer', 'unknown']:
    print(f"{role.title()} Permissions", get_user_permissions(role))

import  random
x=[random.randint(1,100) for i in range(1000)]
s=set(x)
print(s)
for i in s:
    print(i,':',x.count(i))
"""
from re import search

#数据去重
