# _*_ coding=utf8 _*_
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1  #python
        self.subject2 = 'cpp'

    def __getattribute__(self, item):  #The item is the name of instance attribute, like "subject1"
        print("__getattribute__ is working")
        #return self.subject1   # You can't access the self.XXX here, Because it will use the __getattribute__ again
        # and trigger an infinite recursion
        return object.__getattribute__(self, item)

s = Itcast("python")
print(s.subject1)

"""
__getattribute__ is working  # You can see that __getattribute__ is used before the attribute is printed
python
"""