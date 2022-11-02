# Qingxiang Guo
# {2022/7/20} {16:43}
class Foo(object):
    def __init__(self,name):
        self.name=name

    def ord_func(self):
        print('实例方法')

    def __str__(self):
        return 'hihihi'

    @classmethod
    def class_func(cls):   #class_func = classmethod(class_func)
        print('类方法')

    @staticmethod
    def stat():
        print('静态方法')

f=Foo('haha')

f.ord_func()   #实例可以直接调用实例方法，相当于f.ord_func(f)，传实例self进去
Foo.ord_func(f)  #类想调用实例方法，要输入实例，传实例self进去

Foo.class_func()  #类可以直接调用类方法，相当于Foo.class_func(Foo)，传了类cls进去
f.class_func()  #实例对象也可以直接调用类方法，相当于f.class_func(f)，传了实例进去，也没关系，通过装饰器
#帮你完善，变成了传类cls进去
#类方法更复杂，你给他类对象，他直接传进去，你给他实例对象，他通过装饰器变成类对象，再穿进去

f.stat()
Foo.stat()

#总结：实例方法要传实例对象，类方法要传类对象（你传实例对象会帮你转成类对象），静态方法什么都不传
#这一章其实解答了，def ord_func(self): 定义实例方法时，为什么里面有个self。f.ord_func() =  f.ord_func(f)， f会被传给self
#类也是通过将不同实例传进去，将实例与实例之间给区分开来的

'''
其中，为什么实例化对象，也可以调用类方法呢，明明类方法需要传入cls，而我们传入的是self
实际上，
@classmethod
def class_func(cls):
就是一个装饰器，class_func=classmethod(class_func)
其中的机制如下，参照对有参数的函数进行装饰,classmethod的大概语法结构如下：
def classmethod(func):  #func是原classmethod函数
    def wrapped_func(temp_self):  #temp_self是传入的实例对象
        cls=temp_self.__class__   #实例的__class__属性可以取类
        func(cls)  #装饰器内部转换一下，将类对象，再传给类方法
    return wrapped_func
'''