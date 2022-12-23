class A(object):

    """This is a doc."""

    def __init__(self):
        self.a = 100
        self.b = 200
        self.c = "hello"

a = A()
print(A.__doc__)

'''
This is a doc.
'''

#Python objects have an attribute called __doc__ that provides a documentation of the object.
# For example, you simply call Dog.__doc__ on your class Dog to retrieve its documentation as a string.