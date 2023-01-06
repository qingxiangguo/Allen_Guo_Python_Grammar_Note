# Qingxiang Guo
# {2022/7/21} {22:06}
#验证能不能在一般的实例方法中，通过cls.属性，来调用类属性
class Singleton():
    instance = 'haha'  #定义一个类的公有属性

    def __new__(cls, *args, **kwargs):  #相当于重写了new方法
        print('这是__new__方法执行了')
        print(cls.instance)  #打印类属性
        return super().__new__(cls)  #在重写的new方法里面，借用父类的new方法，来基于cls（本类）来创建一个新对象

    def ord_func(self):  #定义一个实例方法
        print('This is instance method')
        print(self.instance)  #同时打印实例的属性
        print(Singleton.instance, '这是类属性')
        #print(cls.instance) 会报错

f = Singleton()
print('-------------')
f.ord_func()
#总结：cls.instance这种用法，只能在__new__方法，创建对象的时候使用，因为这时在封闭代码块内是定义了一个cls的变量
#名字来指代当前的这个类本身的。如果你在别的地方，比如说实例方法里面，使用cls.instance
#那么就会报错，说你没有指代cls变量名。