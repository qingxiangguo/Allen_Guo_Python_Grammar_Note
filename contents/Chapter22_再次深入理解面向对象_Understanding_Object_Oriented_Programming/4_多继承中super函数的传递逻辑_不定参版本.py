# Qingxiang Guo
# {2022/7/21} {17:55}
#面向对象的super()，主要用于多继承，有多个父类，避免父类方法被多次重复调用的问题
#这里用了不定参*args,**kwargs
class Parent(object):
    def __init__(self,name,*args,**kwargs):
        print('parent的init开始被调用')
        self.name=name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)   #不能想当然的认为这里super()会跳到Parent，实际上会调用Son2，因为是按照Grandson的mro顺序调用的
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):   #Grandson创建对象的时候，init调用逻辑，全部只遵循Grandson自己的mro顺序
    #Grandson的顺序为，Grandson, S1, S2, Parent, Object，所以里面层层调用super()，就会Grandson, S1, S2, Parent往上走
    def __init__(self, name, age,gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)

gs = Grandson('john',12,'male')  #这一步开始运行的__init__
print('name',gs.name)
print('age',gs.age)
print('gender',gs.gender)

print('---------------')
print(Son1.__mro__)  #(<class '__main__.Son1'>, <class '__main__.Parent'>, <class 'object'>)
s1 = Son1('harry', 18)
print('name', s1.name)
print('age', s1.age)