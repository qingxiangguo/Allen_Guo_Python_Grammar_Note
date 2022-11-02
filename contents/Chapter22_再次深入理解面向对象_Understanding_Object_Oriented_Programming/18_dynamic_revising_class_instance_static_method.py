# _*_ coding=utf8 _*_
# The example of the dynamic feature of python
import types

# Define a class
class Person(object):
    num = 0
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def say(self):
        print("hello")

# Define a instance method (only a function now)
def run(self, speed):
    print('the speed of %s is %d' % (self.name, speed))

# Define a class method (only a function now)
@classmethod
def test_class(cls):
    print('num = %d' % cls.num)
    cls.num = 100
    print('num = %d' % cls.num)

# Define a static method (only a function now)
@staticmethod
def test_static():
    print('static method')

# Build an instance method
p = Person('Allen', 18)
p.say()  # hello

# Bind the instance method, it is special, you have to use the types.MethodType
p.run = types.MethodType(run, p)
p.run(180)  # the speed of Allen is 180

# Bind the classmethod method
Person.test_class = test_class  # Binding a class method is much easier than instance method.
Person.test_class()

'''
the speed of Allen is 180
'''

# Bind the static method
Person.test_static = test_static
Person.test_static()  # static method

# You can also delete the attribute or method
# del p.run
# p.run(200) AttributeError: 'Person' object has no attribute 'run'

# delattr(p, "name")
# print(p.name)  AttributeError: 'Person' object has no attribute 'name'



