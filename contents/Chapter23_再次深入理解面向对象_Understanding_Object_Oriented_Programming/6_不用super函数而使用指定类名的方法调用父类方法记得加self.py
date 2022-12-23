# Qingxiang Guo
# {2022/7/21} {17:55}
#不用super函数而使用指定类名的方法调用父类方法记得加self
#比如super().__init__(name, *args, **kwargs)，与Son2.__init__(self, name, *args, **kwargs)

class Parent(object):
    def __init__(self,name,*args,**kwargs):
        print('parent的init开始被调用')
        self.name=name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        Son2.__init__(self, name, *args, **kwargs)   #这里原来是super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name, *args, **kwargs)   #这里原来是super().__init__(name, age, gender)
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):   #Grandson创建对象的时候，init调用逻辑，全部只遵循Grandson自己的mro顺序
    #Grandson的顺序为，Grandson, S1, S2, Parent, Object，所以里面层层调用super()，就会Grandson, S1, S2, Parent往上走
    def __init__(self, name, age,gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age, gender)  #这里原来是super().__init__(name, age, gender)
        print('Grandson的init结束被调用')

print(Grandson.__mro__)

gs = Grandson('john',12,'male')  #这一步开始运行的__init__
print('name',gs.name)
print('age',gs.age)
print('gender',gs.gender)

