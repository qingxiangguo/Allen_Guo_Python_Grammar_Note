# _*_ coding=utf8 _*_
# The example of the dynamic feature of python
import types


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def say(self):
        print("hello")

p = Person("Allen", 18)

print(p.name)
print(p.age)

# Let's give the instance a new attribute
p.address = "chicago"
print(p.address)  # You can add a new attribute while running

# We can also add a new attribute to the entire Class
Person.address = "Evanston"
p2 = Person("Mikasa", 22)

print(p2.address)  #Evanston

# Add an instance method to an instance: very important
def show_info(self):   # Define a funtion first, the self here is just a name
    print('----show info--------')

p2.show_info = types.MethodType(show_info, p2)
# The types.MethodType() function can bind the show_info function to the new method citation of p2
# namely, p2.show_info, and types.MethodType() function also bind the instance p2.
# So everytime you call p2.show_info(), it will be like p2.show_info(p2): the p2 instance is
# given to "self" in the def show_info(self):

p2.show_info()  # ----show info--------
print(type(p2.name))  # <class 'str'>
print(type(p2.show_info))  # <class 'method'>
print(type(p2.say))  # <class 'method'>
# From the above, you can see show_info is a new method.








