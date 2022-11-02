# Qingxiang Guo
# {2022/5/28} {22:14}
#继承允许我们定义继承另一个类的所有方法和属性的类，父类是继承的类，也称为基类，子类是从另一个类继承的类，也称为派生类。
#默认object是所有类的父类，平常省略了

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


class Teacher(Person): #再另创造一个Persone的子类
    def __init__(self,obj_name,obj_age,obj_teach_year):  #Teacher自己的构造函数，多了一个obj_each_year的属性
        super().__init__(obj_name,obj_age)  #意思是obj_name,obj_age这两个变量来自于父类的继承
        self.teach_year=obj_teach_year   #教龄属性新赋值，而不是来自于继承

stu1=Student('John',20,'129115')
teacher1=Teacher('Joey',39,10)

stu1.info()  #继承了父类中的info方法  输出John 20
teacher1.info()  #继承了父类中的info方法  输出Joey 39



