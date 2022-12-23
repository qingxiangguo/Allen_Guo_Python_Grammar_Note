class A(object):
    def __init__(self):
        self.a = 100
        self.b = 200
        self.c = "hello"

a = A()
print(A.__dict__) #{'__module__': '__main__', '__init__': <function A.__init__ at 0x000001A1CC6CEF80>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(a.__dict__) #{'a': 100, 'b': 200, 'c': 'hello'}

#Basically it contains all the attributes which describe the object in question. Ther are stored in dict.