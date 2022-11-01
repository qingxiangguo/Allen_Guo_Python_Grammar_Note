# Qingxiang Guo
# {2022/5/29} {16:23}
'''
子类继承了父类，那么子类就拥有了父类所有的类属性和类方法。通常情况下，子类会在此基础上，扩展一些新的类属性和类方法
但有的例外，即子类从父类继承得来的类方法中，大部分是适合子类使用的，但有个别的类方法，并不能直接照搬父类的，如果不对这部分类方法进行修改，子类对象无法使用。
super()函数返回父类所代表的对象，我们可以通过super().方法+你自己定义的新需求来实现对父类方法的重写
'''

#还是之前教师学生的例子

class Person(object):  #Person继承object类
    def __init__(self,obj_name,obj_age):
        self.name=obj_name
        self.age=obj_age
    def info(self):
        print(self.name,self.age)

class Student(Person):  #Student是Person的子类
    def __init__(self,obj_name,obj_age,obj_stu_no):   #Student自己的构造函数，多了一个obj_stu_no的属性
        super().__init__(obj_name,obj_age)  #使用super在子类中调用父类，意思是obj_name,obj_age这两个变量来自于父类的继承
        self.stu_no=obj_stu_no   #学号属性新赋值，而不是来自于继承

    def info(self):  #对父类的into方法进行了重写
        super().info()   #调用父类，保留父类
        print(self.stu_no)  #在此基础上，1输出学生学号


class Teacher(Person): #再另创造一个Persone的子类
    def __init__(self,obj_name,obj_age,obj_teach_year):  #Teacher自己的构造函数，多了一个obj_each_year的属性
        super().__init__(obj_name,obj_age)  #意思是obj_name,obj_age这两个变量来自于父类的继承
        self.teach_year=obj_teach_year   #教龄属性新赋值，而不是来自于继承

    def info(self):  #对父类的into方法进行了重写
        super().info()  #调用父类，保留父类
        print(self.teach_year)  # 在此基础上，输出教龄

stu1=Student('Jon',22,112099)
stu1.info()  #输出Jon 22 112099

teacher1=Teacher('Cassie',23,2)
teacher1.info()  #输出Cassie 23 2