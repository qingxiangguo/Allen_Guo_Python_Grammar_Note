# _*_ coding=utf8 _*_
''''
Public members (generally methods declared in a class) are accessible from outside the class.
_Protected members of a class are accessible from within the class (instance) and are also available to its sub-classes (instance).
__Private members of the class are denied access from the environment outside the class. They can be handled only from within the class.
'''
class Person(object):  # The parent class
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age  # Protected attribute
        self.__taste = taste  # Private attribute

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def _work(self):
        print("My _work method")

    def __away(self):
        print("My __away method")

    def dowork(self):
        self._work()
        self.__away()

class _Bug(object):   # Protected class, it can be accessed by current file, not by from import
    @staticmethod
    def showbug():
        print('showbug')

class Student(Person): # The son class of Person
    def construction(self, name, age, taste):
        self.name = name
        self._age = age  # Protected attribute
        self.__taste = taste  # Private attribute

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()

# Then we start to test
p1 = Person("Allen", 18, "sweet")
print(p1.name) # Allen
print(p1._age) # 18, accessible from within the class and are also available to its sub-classes, but not from import
# print(p1.__taste) # AttributeError: 'Person' object has no attribute '__taste', the private can not be accessed outside the class

p1.showperson()  # It can access __taste, because the latter belongs to the same class
'''
Allen
18
sweet  # Private can be accessed by the class itself
'''

p1.dowork()
'''
Allen
18
sweet  # Private can be accessed by the class itself
'''

s1 = Student("Mikasa", 22, "spicy")
print(s1.name) # Mikasa
print(s1._age) # 22, protected attribute can be accessed by child
# print(s1.__taste) # Private can not be accessed outside

print("*"*20)

s1.construction("rose", 30, "bitter") # However, the "bitter" can not be stored

s1.showperson()
s1.showstudent()

print("*"*20)

s1.testbug()

print(p1._Person__taste)  # You can enforcely access the private attribute (not recommand)






