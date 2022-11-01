# Qingxiang Guo
# {2022/5/29} {16:50}
'''
在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法，
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
'''

class Student:
    def __init__(self,obj_name,obj_age):  #构造函数init
        self.name=obj_name
        self.age=obj_age
    def __str__(self):
        return 'My name is {0}, I am {1} years old'.format(self.name,self.age)   #字符串格式化

stu=Student('John',20)
print(stu)  #输出My name is John, I am 20 years old，默认会调用__str__这样的方法
print(type(stu))   #<class '__main__.Student'>
