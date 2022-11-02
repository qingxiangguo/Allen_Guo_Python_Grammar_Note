# Qingxiang Guo
# {2022/7/9} {17:17}
#思考_函数_匿名函数_闭包_对象_当做实参有什么区别
#先定义一个测试函数
def test(temp):
    pass

#再定一个函数
def a():
    pass

test(a)  #将函数a的引用传到test中，相当于是传功能（算法），而不是传数据

#定义一个匿名函数
b= lambda x:x+2

test(b)  #将函数a的引用传到test中，相当于是传功能（算法），而不是传数据

#定义一个闭包
def person(name):
    def say(content):
        print(name,content)
    return say

p=person('john') #建立一个闭包

test(p)  #将闭包p的引用传到test中，相当于是传功能（算法）+数据
#数据是外部函数中的那些局部变量，或者形参，而功能则是内部函数

#定义一个类对象

class Person(object):
    def __init__(self,name):
        self.name=name

p2=Person('mary')

test(p2)  #将实例对象p2的引用传到test中，相当于是传功能（算法）+数据


