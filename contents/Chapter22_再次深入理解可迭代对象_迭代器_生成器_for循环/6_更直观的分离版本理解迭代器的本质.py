class A():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        print('A.__iter__()方法被调用')
        return B(self.lst)  # 将B类实例化

class B():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        print('B.__iter__()方法被调用')
        return self  # B本身是一个迭代器

    def __next__(self):
        try:
            print('B.__next__()方法被调用')
            value = self.lst[self.index]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration

a = A([1, 2, 3])
a1 = iter(a)  # A.__iter__()方法被调用,返回B的实例，B就是迭代器，其实就是 a1 = B([1,2,3])
print(next(a1)) # B.__next__()方法被调用，其实就是next(B的实例对象)
print(next(a1)) # B.__next__()方法被调用，其实就是next(B的实例对象)
print(next(a1)) # B.__next__()方法被调用，其实就是next(B的实例对象)
#print(next(a1)) # 会报错

'''
A类实例化出来的实例a只是可迭代对象，不是迭代器，调用iter()方法后，返回了一个B类的实例a1，
每次对a1调用next()方法，都用调用B类的__next__()方法。
'''