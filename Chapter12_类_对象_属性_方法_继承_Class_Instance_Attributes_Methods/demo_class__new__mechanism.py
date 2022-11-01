# Qingxiang Guo
# {2022/6/1} {15:01}
'''
此部分主要讲__new__创建对象的机制，与__init__的区别，以及通过打印
各个对象的ID，来明白其中的参数是如何传递的
'''
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用了，他后面输入的cls的ID为{0}'.format(id(cls)))   #2226515474416
        instance=super().__new__(cls)  #这里是在Person子类中，调用父类object的new方法，创建了一个Person的实例对象,cls就是Person
        print('创建的实例对象instance的ID为{0}'.format(id(instance)))   #2226521979536
        return instance

    def __init__(self,obj_name,obj_age):
        print('__init__被调用了，后面输入的self的id值为{0}'.format(id(self)))  #2226521979536
        self.name=obj_name
        self.age=obj_age

print('父类Object的id为{0}'.format(id(object)))  #140708827412352
print('Person类的id为{0}'.format(id(Person)))   #2226515474416

#下面开始创建实例对象，看看他们ID的变化
p1=Person('John',30)
print('p1这个实例对象的id为{0}'.format(id(p1)))  #2226521979536

'''
总结，p1,self,instance的ID都是一样的，说明是同一个对象；Person,cls的ID一样，说明是同一个
实际的传参顺序是，在执行p1=Person('John',30)时，Person被传给最上面的cls
然后cls又被父类object的方法实例化，产生instance实例对象
instance实例对象，又被传给了后面init中的self
'''