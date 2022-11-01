# Qingxiang Guo
# {2022/5/25} {21:37}
#关于类的实例方法（instance method），静态方法（static method），与类方法（class method）
class Student:   #Student为类的名称
    home_town='Newyork'   #直接写在类里的变量，称为类属性
    def __init__(self,obj_name,obj_age):
        self.name=obj_name   #self.name称为实例属性，进行了一个，将局部变量obj_name的值赋值给了实例属性self.name
        self.age=obj_age

    #实例方法
    def eat(self):
        print('I am eating')

    #静态方法
    @staticmethod
    def method():
        print('This is static method')

    #类方法
    @classmethod
    def cm(cls):
        print('This is class method')

#创建student类的对象，也称为实例化
stu1=Student('John',20)  #将John和20传给构造函数init中的obj_name,obj_age变量
stu1.eat()  #输出I am eating，对象名.方法名（）
print(stu1.name)   #输出John
print(stu1.age)    #输出age

print('---------------------')
Student.eat(stu1)   #与stu1.eat()代码功能相同，都是调用Student中的eat方法
                    #这里用的是类名.方法名（实例对象），stu1实际上就是方法定义处的self
                    #简单来说，一个是从类的方法运行，传入实例对象；一个是直接实例本身调用方法运行

#类属性的使用方式
print(Student.home_town)
stu2=Student('Rick',32)
stu3=Student('Bob',23)
print(stu2.home_town)  #Newyork
print(stu3.home_town)  #Newyork
Student.home_town='Evanston'
print(stu2.home_town)  #Evanston
print(stu3.home_town)  #Evanston
print('--------类方法使用方式-----------')
Student.cm()  #This is class method
print('--------静态方式的使用方式-----------')
Student.method()  #This is static method


