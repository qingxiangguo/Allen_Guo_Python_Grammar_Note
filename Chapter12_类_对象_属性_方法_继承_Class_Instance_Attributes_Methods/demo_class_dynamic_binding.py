# Qingxiang Guo
# {2022/5/27} {21:21}
#Python 动态绑定属性和方法， 动态语言与静态语言有很多不同，最大的特性之一就是可以实现动态的对类和实例进行修改，在Python中，我们创建了一个类后可以对实例和类绑定心的方法或者属性，实现动态绑定
class Student:
    def __init__(self,obj_name,obj_age):
        self.name=obj_name
        self.age=obj_age
    def eat(self):
        print(self.name,'is eating')


stu1=Student('Mary',19)
stu2=Student('Joe',22)

print('------------为stu1动态绑定性别属性，额外添加一个属性------------------')
stu1.gender='Female'
print(stu1.name,stu1.age,stu1.gender)  #多了一个gender属性
print(stu2.name,stu2.age)   #stu2仍然没有gender属性

print('------------为stu1动态绑定性一个新的方法------------------')

def drink():
    print('I am drinking')  #定义在类之外，称函数

stu1.drink=drink  #将drink函数赋值给stu1的新方法
stu1.drink()   #I am drinking
