# _*_ coding=utf8 _*_
# This allows the instance to be manipulated like a dict.
class Foo():
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)

obj = Foo()

result = obj['k1']   # Will active __getitem__
obj['k2'] = 'Allen'   # Will activate __setitem__
del obj['k1'] # Will activate __delitem__

'''
__getitem__ k1
__setitem__ k2 Allen
__delitem__ k1
'''