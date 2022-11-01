# Qingxiang Guo
# {2022/5/25} {17:51}
'''
这是一个类的结构
class Myclass:
    var1='类属性，也叫静态属性'
    __var2='类的私有属性'
    def __init__(self):
        self.var2='var2是实例的属性'
        self._var3='var2是实例的私有属性'
    var4='简单变量，非属性，作用域只在函数体内'
下面以一个人类的例子，来举例类的属性（公有属性，私有属性），类的方法（公有方法，私有方法）
特殊方法（魔法方法）
'''
#定义一个人类的类，拥有名字，性别，年龄，薪资等属性。其中薪资由于不能随便打听，是私有属性。
#同时，人类还有说话的功能（方法），有时说真话，也有撒谎的功能

class Human:
    '''This is the class Human'''   #自定义一个类的文档，后续可通过print(Human.__doc__)内置函数输出
    name='the default name'  #默认的类的属性，这些是可以公开访问的
    gender='male or female'
    age='0-100'
    __salary=8000    #类的私有属性，前面两个下划线表示，不能在类外面访问，只能在类内部传递用

    def __init__(self,obj_name,obj_gender,obj_age):  #init是魔法函数，用来初始化变量，self是默认必带的，代表传对象本身(因为你不知道会传什么名字进来)，另外还有name和age属性
        print('#'*50)   #用来测试这个初始化魔法函数是否运行
        self.name=obj_name  #将实例化时传入的name变量，赋值给对象的name属性，self.name为实例属性
        self.gender=obj_gender  #将实例化时传入的gender变量，赋值给对象的gender属性
        self.age=obj_age  #将实例化时传入的age变量，赋值给对象的age属性
        print('#'*50)   #用来测试

        '''关于上面变量名称，比较容易混淆，澄清如下：self指代你的传入的对象，即person1，
        obj_name，obj_gender，obj_age的名字可以随便定义，存储下面Human('John','male','19')中传入的属性数据，
        并将这些数据，传入到self对象的属性当中。所以左边的self.name，self.gender，self.age是不能变的（或者说是有意义的，代表了你的方法名称）
        其中的name，gender，age就是和类属性中的三个属性一致，相当于访问了这个对象的属性'''

    def __str__(self):  #也是另一个魔法方法
        msg= 'Hi I am the object of class Human!'  #会自动执行，不输出<__main__.Human object at 0x00000198A6D83C40>，而是自定义更人性化
        return msg

    def say(self):  #一个说话的功能（方法），会同时说真话，和假话
        print('my name is %s and I can earn %d' % (self.name,self.__salary))  #用到了字符串格式化，说真话，自己的姓名以及真实工资
        self.__lie()  #调用实例对象的私有的说假话方法

    def __lie(self):
        print("I can earn 9999 per month (It is a lie)")

#下面开始使用这个类
print(Human)   #输出<class '__main__.Human'>，这个类是可以直接打印的
print(Human.__doc__)  #会输出注释，This is the class Human
print(Human.name)  #输出the default name，类的公有属性也是可以直接访问的
#print(Human.__salary)  会报错，类的私有属性不能外面访问

person1=Human('John','male','19')  #实例化一个person1，并将各个属性赋值进去，初始化
#会输出，####################，可见init构造函数已经开始运行了

print(person1)  #会输出<__main__.Human object at 0x00000198A6D83C40>，表明person1是一个对象
print(person1.name, person1.age)  #可以访问刚刚定义的对象的属性，会输出John 19
person1.say() #会输出my name is John and I can earn 8000，I can earn 9999 per month (It is a lie)
#person1.__lie()  会报错，私有的方法（函数）无法访问
Human.say(person1)  #这样也可以，输出的结果和person1.say()是等价的，相当于将实例传送给类方法



