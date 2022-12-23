# Qingxiang Guo
# {2022/7/21} {18:19}
#面向对象的super()，主要用于多继承，有多个父类，避免父类方法被多次重复调用的问题
#下面这个例子，不是用不定参来统一解决传递报错的问题，而是明确指出每个函数中参数传递的情况
#这样可以帮助理解不同类之间的参数传递
#而且当数据结构，Son1和Son2没有一个公有的父类时，不用考虑super传参的问题，传参就简化了一些
#下面就是一个例子，把Parent类给去掉看看

class Son1():
    def __init__(self, name, age, gender):  #从Grandson接收name, age, gender三个参数
        print('Son1的init开始被调用')
        self.age = age  #三个参数，其中age用来创建属性
        super().__init__(name, gender)  #剩下的name, gender给Son2的构造函数，形参数量是匹配的
        print('Son1的init结束被调用')

class Son2():
    def __init__(self, name, gender):  #Son2从Son1接收name, gender两个实参
        print('Son2的init开始被调用')
        self.name=name
        self.gender =gender  #其中gender用来创建属
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):
    def __init__(self, name, age,gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age, gender)  #你要保证这一行的参数，都能够从Grandson得到，并且和MRO下一级调用的父类，也就是Son1的输入要匹配
        print('Grandson的init结束被调用')

print(Grandson.__mro__)  #(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class 'object'>)
print(Son1.__mro__)  #(<class '__main__.Son1'>, <class 'object'>)

gs = Grandson('john',12,'male')
print('name',gs.name)
print('age',gs.age)
print('gender',gs.gender)

'''
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class 'object'>)
Grandson的init开始被调用
Son1的init开始被调用
Son2的init开始被调用
Son2的init结束被调用
Son1的init结束被调用
Grandson的init结束被调用
name john
age 12
gender male
'''