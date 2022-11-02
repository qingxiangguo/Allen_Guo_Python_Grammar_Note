# _*_ coding=utf8 _*_
from test import Person

obj = Person()
print(obj.__module__)  #test
print(obj.__class__)  #<class 'test.Person'>

# The __module__ property is intended for retrieving the module where the function was defined
# It will give you the class of the current instance

