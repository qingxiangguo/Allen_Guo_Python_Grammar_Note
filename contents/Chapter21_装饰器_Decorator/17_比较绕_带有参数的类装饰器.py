# Qingxiang Guo
# {2022/7/18} {22:12}
'''
当类装饰器含有参数的时候，其参数是通过init函数输入的
而装饰的过程，是通过桥梁函数的方法，作为中介实现的
也利用了类中的知识：当调用了：实例化对象（），或者实例化对象（参数），就会调用__call__方法
和不带参数的类装饰器的区别是：
不带参数的类装饰器：由于a=Test(a)，a等于实例对象本身，原函数传给__init__，a()是实例对象()，__call__函数调用原函数
带参数的类装饰器：实例对象=Test(100)，100参数传给__init__，a=实例对象(a)，a()等价于，实例对象(a)()。实例对象(a)调用了__call__
原函数传给__call__，返回一个桥梁函数，桥梁函数（）执行了原函数和新功能
'''
class Test(object):
    def __init__(self,num):
        print('初始化')
        self.__num=num

    def bridge_func(self):  #定义一个实例方法，可以通过self.bridge_func来取到
        print('下面执行原函数')
        self.__func()
        print('下面执行新功能')
        print('new function')

    def __call__(self, func):  #__call__，只要调用了：实例化对象（），或者实例化对象（参数），就会调用
        self.__func=func
        return self.bridge_func


@Test(100)  #要明白，Test(100)，也是实例化一个对象，只不过__init__中传了个参数100
def a():
    print('----test------')

a()   #因为a=实例化对象（a），所以a()等于【实例化对象（a）】().【实例化对象（a）】会调用__call__返回
#self.bridge_func，所以最后就变成了self.bridge_func()

'''
初始化
下面执行原函数
----test------
下面执行新功能
new function
'''

'''
运行逻辑如下，和不带参数的类装饰器不同，前者装饰时，是a=Test(a)，即直接实例化，且原函数的引用
传给了__init__中，保存了原函数。而带参数的类装饰器，首先执行@Test(100)，再将Test(100)的
返回值，加到@的前面。执行Test(100)的时候，由于是实例化了一个对象出来，100传给__init__中的num
接下来，这个实例对象，加到@的前面，也就是@实例化对象。然后开始装饰，即a=实例化对象（a）
那么直接调用实例化对象，且把a传入，这就调用了__call__函数，原函数传给了self.__func
又由于a=实例化对象（a），实例化对象（a）的返回结果就是self.bridge_func引用
所以a()，就是self.bridge_func()，其中self就是这个未命名的实例化对象，也就是调用实例化的bridge_func方法
因此会依次执行print('下面执行原函数')，self.__func()，print('下面执行新功能')，print('new function')
'''