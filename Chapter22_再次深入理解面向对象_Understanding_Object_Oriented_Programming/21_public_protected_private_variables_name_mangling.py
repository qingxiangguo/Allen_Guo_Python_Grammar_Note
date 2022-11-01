# _*_ coding=utf8 _*_
'''
To ensure that private variables cannot be accessed outside the class,
Python automatically replaces the name of the __spam private variable
inside the class with _classname__spam (note that classname is
preceded by an underscore, and spam is preceded by two underscores),
so that when the user accesses __spam externally, the corresponding variable
is not found
'''
class A(object):
    def __init__(self):
        self.__data = []  # Name mangling into self._A__data

    def add(self, item):
        self.__data.append(item)  # Name mangling into self._A__data.append(item)

    def printData(self):
        print(self.__data)

a = A()
a.add('hello')
a.add('python')
a.printData()

'''
['hello', 'python']  # The instance can access, but not from the outside calling.
'''