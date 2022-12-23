# _*_ coding=utf8 _*_
# __str__ will print the content when you print the instance object.
class Foo:
    def __str__(self):
        return "Allen"

    def __call__(self, *args, **kwargs):
        print ("This is __call__() method")

obj=Foo()
print(obj)
obj()  # Note the difference between __call__ and __str__

'''
Allen
This is __call__() method
'''