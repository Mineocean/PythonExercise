"""
#多继承
class bird():
    def fly(self):
        print("飞翔")
    def breathe(self):
        print("鸟儿呼吸")
class fish():
    def swim(self):
        print("游泳")
    def breathe(self):
        print("鱼儿呼吸")
class Volador(bird,fish):
    pass
volador=Volador()
volador.fly()
volador.swim()
volador.breathe()

#重写父类
class person():
    def say_hello(self):
        print("Hello")
class chinese(person):
    def say_hello(self):
        print("你好")
class american(person):
    def say_hello(self):
        print("Nice to meet you")
小明=chinese()
小明.say_hello()
Tom=american()
Tom.say_hello()

#即要又要，super
class animal():
    def __init__(self,leg_count):
        self.leg_count=leg_count
class Bird(animal):
    def __init__(self,leg_count):
     self.plume='白色'
     super(Bird,self).__init__(leg_count)
bird=Bird(2)
print('有一只鸟，它有%s条腿，羽毛有%s在树上唱歌'%(bird.leg_count,bird.plume))

#多态
class animal():
    def shout(self):
        print("动物叫声")
class dog(animal):
    def shout(self):
        print("汪汪")
class cat(animal):
    def shout(self):
        print("喵喵")
class cow(animal):
    def shout(self):
        print("哞哞")
def func(temp):
    temp.shout()
dog=dog()
func(dog)
cat=cat()
func(cat)
zhangsir=cow()
func(zhangsir)

#定义一个抽象的shape类，创建Circle类
class shape():
    def draw(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def draw(self):
        print("画一个半径为%s的圆"%(self.radius))
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def draw(self):
        print("画一个宽为%s，高为%s的矩形"%(self.width,self.height))

def draw_shape(shape):
    shape.draw()
circle1=circle(5)
circle1.draw()
rect1=rectangle(4,6)
rect1.draw()

#student类,第一个学生学号为1，每创建一个学号加1
#每个对象生成后需调用info方法输出姓名年龄和学号
class student():
    next_id = 1
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.id=student.next_id
        student.next_id += 1
        self.info()
    def info(self):
        print("姓名：%s，年龄：%s，学号：%s"%(self.name,self.age,self.id))
stu1=student('tom',18)
stu2=student('jim',22)
"""

