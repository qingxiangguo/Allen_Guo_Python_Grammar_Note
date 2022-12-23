'''
进一步理解__iter__方法，只要一个对象定义了__iter__()方法，那么它就是可迭代对象
__iter__()的作用是返回一个迭代器，虽然上面说过，只要实现了__iter__()方法就是可迭代对象，但是，没有实现功能（返回迭代器）总归是有问题的
__iter__()方法毕竟是一个特殊方法，不适合直接调用，所以Python提供了iter()方法。iter()是Python提供的一个内置方法
可以调用对象的__iter__（）方法，来取迭代器
'''

from collections.abc import Iterator

class A():  # 仅仅是可迭代对象，不是迭代器，迭代器需要用iter()调用，来取迭代器，也就是return B()
    def __iter__(self):
        print('A类的__iter__()方法被调用')
        return B()

class B():  #即是可迭代对象，又是迭代器，所以__iter__返回自己
    def __iter__(self):
        print('B类的__iter__()方法被调用')
        return self
    def __next__(self):
        pass
a = A()
print('对A类对象调用iter()方法前，a是迭代器吗：', isinstance(a, Iterator))
a1 = iter(a)
print('对A类对象调用iter()方法后，a1是迭代器吗：', isinstance(a1, Iterator))

b = B()
print('对B类对象调用iter()方法前，b是迭代器吗：', isinstance(b, Iterator))
b1 = iter(b)
print('对B类对象调用iter()方法后，b1是迭代器吗：', isinstance(b1, Iterator))

'''
对A类对象调用iter()方法前，a是迭代器吗： False
A类的__iter__()方法被调用
对A类对象调用iter()方法后，a1是迭代器吗： True
对B类对象调用iter()方法前，b是迭代器吗： True
B类的__iter__()方法被调用
对B类对象调用iter()方法后，b1是迭代器吗： True
'''

'''
对于B类，因为B类本身就是迭代器，所以可以直接返回B类的实例，也就是说self，当然，
你要是返回其他迭代器也没问题。

对于类A，它只是一个可迭代对象，__iter__()方法需要
返回一个迭代器，所以返回了B类的实例，如果返回的不是一个迭代器，调用iter()方法时
就会报以下错误：TypeError: iter() returned non-iterator of type 'A'
'''