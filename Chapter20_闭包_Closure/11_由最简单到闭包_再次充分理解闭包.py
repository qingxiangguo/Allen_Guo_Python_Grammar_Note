# Qingxiang Guo
# {2022/7/9} {16:33}
#这里举六个例子，来完成一个y=kx+b的功能，给出x，计算出y，由简单，到复杂
#例子一
x=1
k=1
b=2
y=k*x+b
print(x,y)  #输出1,3

#例子二，使用面向过程，函数编程
def line(k,b,x):
    print(x,k*x+b)

line(2,1,1)  #输出1,3

#例子二，使用面向过程，函数编程，但是全局变量
k=2
b=1
def line(x):
    print(x,k*x+b)

line(1)  #输出1,3

#例子四，缺省参数
def line(x,k=2,b=1):  #位置参数，在关键字参数前面
    print(x, k*x+b)

line(1)  #1,3

line(1,k=3,b=1)  #1,3

#例子五，对象
class Line1(object):
    def __init__(self,k,b):
        self.k=k
        self.b=b

    def __call__(self,x):  #这是个魔法方法，当输入，实例化对象名+()的时候，会自动调用
        print(x, x*self.k+self.b)

l=Line1(2,1)
l(1)  #这里输入x
#1,3

#例子六，使用闭包
def line_6(k,b):
    def create_y(x):
        print(x,k*x+b)
    return create_y

l=line_6(3,1)  #赋值k,b，3，1，l相当于create_y
l(1)  #输出1,4



