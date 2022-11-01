# _*_ coding=utf8 _*_
'''
The special attribute __slots__ allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results:

faster attribute access.
space savings in memory.

You need to control the number of attributes you want to add
'''

class Person(object):
    __slots__ = ("name", "age")

p = Person()
p.name = "Allen"
p.age = 18
# p.address = Chicago  # You can add attribut which is not defined in __slots__

class Person2(Person):
    pass
p2 = Person2()
p2.phone_num = "911"  # The __slots__ will not affect the child class

