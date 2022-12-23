# Qingxiang Guo
# {2022/7/18} {21:43}
'''
一般装饰器都是由函数def来定义的，类也可以当做装饰器
那么类当做装饰器如何使用呢？
'''

class Test(object):
    def __init__(self,func):
        print('初始化')
        print('func name is %s' % func.__name__)
        self.__func=func
    def __call__(self, *args, **kwargs):
        print('下面执行原函数')
        self.__func()
        print('下面执行新功能')
        print('new function')

@Test  #相当于a=Test(a)，相当于Test(a)实例化了一个对象，由于这里有实例化操作，所以会执行__init__()
def a():
    print('----test------')

a()  #a()相当于，实例化对象()，会调用实例的__call__()方法，而__call__()方法已经被改写，包括了原函数和新功能

'''
初始化
func name is a
下面执行原函数
----test------
下面执行新功能
new function
'''

'''
执行逻辑如下,当程序运行到@Test时，就执行a=Test(a)
Test(a)相当于创建了一个实例化对象，这一点和函数不一样
由于创建了实例化对象，所以调用了类中的__init__函数
并将a引用赋值给了__init__中的func
并储存于私有属性self.__func，此时，a是一个实例化对象
a()，属于直接调用实例对象，会调用类的__call__方法，类装饰器巧妙的用这个方法
来执行原函数self.__func与新功能
总结：理解类装饰器的关键，在于了解Test()是创建实例对象，Test(a)是将a传入初始化方法__init__中
'''