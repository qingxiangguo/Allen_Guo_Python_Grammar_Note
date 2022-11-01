# Qingxiang Guo
# {2022/7/21} {18:05}
#面向对象的super()，主要用于多继承，有多个父类，避免父类方法被多次重复调用的问题
#下面这个例子，不是用不定参来统一解决传递报错的问题，而是明确指出每个函数中参数传递的情况
#这样可以帮助理解不同类之间的参数传递
#这里比较难理解的是，为什么class Son1(Parent):中的super()，不是等价于super(Son1,self)
#为什么最后不执行Son1的父类parent，而是去执行Son2
#因为最终实例化是在Grandson中完成的，他只是借用了上述的每一步方法，即super(类,self)
#传进去的值，永远是类Grandson，以及实例化对象g，所以一直是按照Grandson的mro顺序在执行

class Parent(object):
    def __init__(self,name):
        print('parent的init开始被调用')
        self.name=name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, gender):  #从Grandson接收name, age, gender三个参数
        print('Son1的init开始被调用')
        self.age = age  #三个参数，其中age用来创建属性
        super().__init__(name, gender)  #剩下的name, gender给Son2的构造函数，形参数量是匹配的
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender):  #Son2从Son1接收name, gender两个实参
        print('Son2的init开始被调用')
        self.gender = gender  #其中gender用来创建属
        super().__init__(name)  #剩下的name给Parent的构造函数，形参数量是匹配的，都是一个
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):
    def __init__(self, name, age,gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age, gender)  #你要保证这一行的参数，都能够从Grandson得到，并且和MRO下一级调用的父类，也就是Son1的输入要匹配
        print('Grandson的init结束被调用')

print(Grandson.__mro__)

gs = Grandson('john',12,'male')
print('name',gs.name)
print('age',gs.age)
print('gender',gs.gender)

'''
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
Grandson的init开始被调用
Son1的init开始被调用
Son2的init开始被调用
parent的init开始被调用
parent的init结束被调用
Son2的init结束被调用
Son1的init结束被调用
Grandson的init结束被调用
name john
age 12
gender male
'''