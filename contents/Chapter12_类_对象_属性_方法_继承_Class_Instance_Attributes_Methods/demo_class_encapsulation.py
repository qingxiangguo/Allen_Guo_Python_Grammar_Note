# Qingxiang Guo
# {2022/5/28} {21:00}
#封装是指隐藏对象的属性和实现细节，仅对外提供公共访问方式。
#高内聚：类的内部数据操作细节自己完成，不允许外部干涉。低耦合：仅对外暴露少量的方法用于使用。

class Car:
    def __init__(self,obj_brand):
        self.brand=obj_brand
    def start(self):
        print('汽车已启动')

car=Car('Benz')
car.start()
print(car.brand)

class Student:
    classname = 'jack'  #类属性
    def __init__(self,obj_name,obj_age):
        self.name=obj_name
        self.__age=obj_age   #不希望年龄被访问，加了两个__

    def show(self):
        print(self.name,self.__age)   #内部可以调用

stu1=Student('Sean',22)
print(Student.classname)  #调用类属性
stu1.show()   #但是可以通过调用调用了私密属性的公有方法，来输出私密属性Sean 22

print(dir(stu1))  #['_Student__age', '__class__', '__delattr__', '_  会输出一个包括可用元素的列表

print(stu1._Student__age)  #22,可以通过，对象._类名__年龄，来强行访问私密属性。实际工作中靠自觉