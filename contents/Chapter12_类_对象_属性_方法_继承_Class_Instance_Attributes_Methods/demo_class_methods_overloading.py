# Qingxiang Guo
# {2022/5/31} {13:31}
'''
运算符重载：为运算符定义方法
所谓重载，就是赋予新的含义同一个运算符可以有不同的功能
'''

#首先学习一下python中+的用法
print(5+5)  #数字相加
a,b='foo','bar'  #各自赋值
print(a+b)  #foobar，字符串相加
a,b=['foo'],['bar']
print(a+b)  #f['foo', 'bar']，列表相加

#下面解析python中+的运算底层逻辑
a=20
b=100
c=a+b
print(c)  #120， 两个整数类型对象的相加操作
#底层如下，实际调用了内置方法__add__()
d=a.__add__(b)
print(d)  #一样输出120

#那么自定义的类对象可以执行加法操作吗？
class Student:
    def __init__(self,obj_name):
        self.name=obj_name   #每一个实例化对象中增加了name属性

    def __add__(self, other):  #self,other是add的固定用法，两个输入对象
        return self.name+other.name

    def __len__(self):
        return len(self.name)
stu1=Student('John')  #实例化两个对象出来
stu2=Student('Mary')

#print(stu1+stu2)  #会报错，显示unsupported operand type(s) for +
#这是因为+运算符不知道如何把两个类的对象相加，所以我们要使用特殊方法来实现运算符重载
#当我们调用+ 这个运算符时，Python 解释器调用了 add(self, other) 这个特殊方法。
#所以，在我们定义的类中重新手动实现 add() 方法，就可以支持+运算符。

print(stu1+stu2)  #输出JohnMary，实现了两个对象的加法运算，因为在Student类中，编写了__add__()特殊的方法

#下面介绍len()函数的用法，返回对象（字符、列表、元组等）长度或者项目个数
a='qingxiang'
print(len(a))  #输出9,，统计字符串的长度

car_list = ['honda','toyota','suzuki','mazda','subaru']
print(len(car_list))  #输出5

t=('a',20,33)
print(len(t))  #输出3

#除了len()函数外，python还内置了一个__len__()方法，可以达到一样的效果
print(t.__len__())  #3
print(car_list.__len__())  #5

#和上面一样的道理，不能直接len(stu1)，要通过修改__len__()来实现。也就是说你自己新定义的类，是没有现成的这些函数的
print(len(stu1))  #输出4，因为是John


