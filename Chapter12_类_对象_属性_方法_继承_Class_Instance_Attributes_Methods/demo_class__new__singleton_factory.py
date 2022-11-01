# Qingxiang Guo
# {2022/5/31} {21:42}
'''
 __new__的定义：
 def __new__(cls,*args,**kwargs):
 pass
 参数说明：cls指当前正在实例化的类
__new__负责对象的创建，__init__负责对象的初始化，因此__new__的过程在__init__之前。
.init 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
new 通常用于控制生成一个新实例的过程。它是类级别的方法。
_init__方法做的事情是在对象创建好之后初始化变量。真正创建实例的是__new__方法。
'''

class Person(object):
    def __new__(cls, *args, **kwargs):  #cls指的就是Person本身，和self异曲同工
        print("in __new__")   #标记调用顺序
        #instance = object.__new__(cls)  #调用了父类object的__new__方法，将当前的cls实例化，传送创建一个实例instance。里面的cls是为了告诉该方法，是当前类cls请求的
        #instance = super().__new__(cls)  #也可以这么写，使用super()来调用父类，也就是object
        instance = super(Person,cls).__new__(cls)  #也可以这么写，代表的是cls类的MRO序列中，Person的父类，也还是object。
        #super()的用法比较绕人，他可以同时接收super(类，类)，以及super(类，对象)，都指的是后者MRO顺序中，前者的上一级，super()是缩写，所以经常比较绕
        return instance  #最后返回这个实例化的对象，以供后续的使用

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age

p1 = Person("Wang", 33)
p2 = Person("Wang", 33)
print(p1,p2)  #输出<__main__.Person object at 0x0000015B70963B80> <__main__.Person object at 0x0000015B70963B20>

#上面可以看到，类Person创造了两个不同内存空间的对象，这样实际操作中可能比较浪费内存
#所以有一种编程理念叫做单例模式（Singleton），指的是一个对象只允许被一次创建，一个类只能创建一个对象，并且提供一个全局访问点
#通俗的讲，就是创建的不同对象，其实都是一个对象，一个ID，__init__方法是没办法实现的，这个时候需要修改__new__
#当一个类需要提供比较通用的功能，且代码里有很多地方需要使用到它，则可以使用单例模式来避免创建多个重复的实例，节约系统资源。
#下面使用__new__来实现单例模式，其实现的逻辑是：判断系统是否已经有这个对象，如果有则返回，如果没有则创建。

class Singleton(object):
    _instance = None    #定义一个类的私有属性,_instance，可以通过类名+属性名来调用这个属性
    def __new__(cls, *args, **kwargs):   #实现单例模式，必须要在创建对象的层面来操作，也就是__new__
        if cls._instance is None:   #根据这个类的属性有无，来判断，只有当cls._instance，也就是没有创建过对象时，才执行创建操作
            cls._instance = object.__new__(cls)  #使用父类object的new函数，来创建当前类的一个实例对象，并传入cls._instance

        return cls._instance  #cls._instance有两个作用，一个是传出（return）实例化对象，一个是作为判断对象是否已经创建的标志，这里巧妙的把实例化对象本身，作为一个值，传给了属性

s1 = Singleton()
s2 = Singleton()
print(s1)  #输出<__main__.Singleton object at 0x000001B69D3739D0>
print(s2)  #输出<__main__.Singleton object at 0x000001B69D3739D0>，可见两者是同一个对象，实现了单例模式

#除了单例模式，python还可以利用__new__实现工厂模式
#什么是工厂模式？不暴露创建对象的具体逻辑，而是将将逻辑封装在一个函数中，那么这个函数就可以被视为一个工厂
#比如女娲造人，不可能亲自一个个的造，而是创建出一个工厂（八卦炉），让八卦炉自己一个个造出不同人种的人

class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass

class Apple(Fruit):  #本例子中，将Apple定义为Fruit的子类，没有什么意义，不影响结果
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")

class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")

class FruitFactory(object):  #这是一个水果工厂
    fruits = {"apple": Apple, "orange": Orange}  #创建一个字典，作为工厂类的公共属性，可以cls.fruits来调用这个字典

    def __new__(cls, name):   #准备实例化一个对象，此实例化对象可传入name参数，一般情况下是*args,**kargs的写法，但这里要用到具体的name，所以写法有变
        if name in cls.fruits.keys():  #获取字典的键，判断，如果实例对象传入的name（比如apple,orange），存在键中
            return cls.fruits[name]()  #那么，cls.fruits[name]，就取了字典中的值，也就是Apple或Orange，是类名，再加个括号，就是实例化了，相当于返回对应的实例化对象
        else:
            return Fruit()  #否则传回Fruit类的实例化对象

fruit1 = FruitFactory('apple')  #会返回Apple类的实例化对象,Apple()
fruit2 = FruitFactory('orange')  #会返回Orange类的实例化对象，Orange()

fruit1.print_color()   #输出apple is in red，相当于Apple().print_color()
fruit2.print_color()   #输出orange is in orange

#下面是另外一个工厂模式的例子，也是用到__new__，定义一个服装需求工厂，你需要什么，输入，自动返回对应的类的实例对象
#下面的需求工厂，相当于上面的FruitFactory

class Clot():

    def __init__(self, name):
        self.name = name

    def create(self):
        print(f"You will get a {self.name}")

class Adidas():

    def __init__(self, name):
        self.name = name

    def create(self):
        print(f"You will get a {self.name}")

class Nike():

    def __init__(self, name):
        self.name = name

    def create(self):
        print(f"You will get a {self.name}")

class Madness():

    def __init__(self, name):
        self.name = name

    def create(self):
        print(f"You will get a {self.name}")

class Hermes():
    def __init__(self, name):
        self.name = name

    def create(self):
        print(f"You will get a {self.name}")

class RequirementFactory:  #定义一个需求工厂
    def __new__(cls, need):
    #@staticmethod  #静态方法
    #def creatNeed(need):  #定义一个需求方法
        if need == "Nike":
            return Nike("Nike")
        elif need == "Adidas":
            return Adidas("Adidas")
        elif need == "Clot":
            return Clot("Clot")
        elif need == "Madness":
            return Madness("Madness")
        elif need == "Hermes":
            return Hermes("Hermes")

RequirementFactory("Clot").create()  #You will get a Clot,生成了一个实例，再调用这个实例的方法
RequirementFactory("Madness").create()  #You will get a Madness
RequirementFactory("Hermes").create()

