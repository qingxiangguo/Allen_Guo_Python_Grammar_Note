# Qingxiang Guo
# {2022/5/30} {21:53}
'''
所谓多态：
为了保留子类中某个和父类名称一样的函数功能，这时候，我们就用到了多态
可以帮助我们保留子类中的函数功能
'''

class Animal(object):
    def eat(self):
        print('Animal can eat')
class Dog(Animal):
    def eat(self):   #重写实例化方法
        print('Dog eats bones')
class Cat(Animal):
    def eat(self):   #重写方法
        print('Cat eats fish')

class Human:   #Human不是Animal类的子类
    def eat(self):   #名称一样的函数
        print('Human eats everything')

#定义一个函数
def func(obj):
    obj.eat()

#开始调用函数
func(Animal())   #这里Animal()相当于实例化一个对象，然后obj.eat()调用实例化方法，会输出Animal can eat，如果这里不带括号，会显示缺少实例对象所需的self
func(Cat())   #Cat eats fish
func(Dog())   #Dog eats bones
print('-------------')
func(Human())  #只要你有同名函数，就可以输出方法，不必要属于同一个父类

#上面是实例化例子，下面再举一个静态方法的例子
class Animal(object):
    @staticmethod
    def eat():
        print('Animal can eat')
class Dog(Animal):
    @staticmethod
    def eat():   #重写静态方法
        print('Dog eats bones')
class Cat(Animal):
    @staticmethod
    def eat():   #重写静态方法
        print('Cat eats fish')

class Human:   #Human不是Animal类的子类
    @staticmethod
    def eat():   #名称一样的函数
        print('Human eats everything')

#定义一个函数
def func(obj):
    obj.eat()

#开始调用函数
func(Animal)  #由于上面是静态方法，不需要输入实例化对象,也不需要self参数，是一个不变的静态方法，可以直接类名使用，所以这里不能有括号
func(Cat)   #Cat eats fish
func(Dog)   #Dog eats bones
print('-------------')
func(Human)  #只要你有同名函数，就可以输出方法，不必要属于同一个父类
