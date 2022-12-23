# Qingxiang Guo
# {2022/5/31} {12:51}
'''这里讲一些python的特殊属性'''
class A:
    pass
class B:
    pass
class C(A,B):  #C是AB子类
    def __init__(self,obj_name,obj_age):
        self.name=obj_name
        self.age = obj_name
class D(A):
    pass

#下面创建C类的实例化对象，介绍__dict__内置属性
x=C('John',20)   #是C类的一个实例化对象
print(x.__dict__)  #输出{'name': 'John', 'age': 'John'}，输出实例对象，属性与值的字典
print(C.__dict__)  #{'__module__': '__main__', '__init__': <function C.__init__ at 0x000001C5F69DAA70>, '__doc__': None}，输出了类的属性和方法的各自字典

#下面介绍__class__内置属性
print(x.__class__)  #<class '__main__.C'>，表明是C类的

#__bases__内置属性
print(C.__bases__)  #类的所有父类构成元素（包含了一个由所有父类组成的元组，(<class '__main__.A'>, <class '__main__.B'>)

#__base__内置属性，返回MRO顺序中，最近的父类
print(C.__base__)  #<class '__main__.A'>

#__mro__属性，输出MRO顺序
print(C.__mro__)  #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#__subclassed__()方法
print(A.__subclasses__())  #[<class '__main__.C'>, <class '__main__.D'>]，会输出子类的列表


