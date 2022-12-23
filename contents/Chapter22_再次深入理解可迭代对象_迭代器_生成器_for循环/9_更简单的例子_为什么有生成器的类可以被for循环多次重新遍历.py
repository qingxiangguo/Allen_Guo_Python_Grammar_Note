from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

class A():
    def __init__(self, lst):
        self.lst = lst
        self.count = 0

    def __iter__(self):
        print('A.__iter__()方法被调用')
        for i in self.lst:
            yield i  #每次调用__iter__时候，都会使用一个yield关键字从而产生一个新的生成器

a = A([1, 2, 3]) #首先将A实例化
a_iter = iter(a)  #取出a的迭代器
print(a_iter)  # <generator object A.__iter__ at 0x0000022136B06C70>,并且不仅仅是
# 迭代器，还是一个生成器

print(isinstance(a,Iterable))  # True  他当然是可迭代对象，因为有__iter__
print(isinstance(a,Iterator))  # False 一定要记得，实现生成器的类，本身的实例并不是迭代器，因为没有__next__方法

# 下面开始实验，for循环可不可以多次遍历，答案是成功的，a并不会被消耗了
for k in a:  #这里用a还是a_iter差别不大，反正for都会尝试用iter去取迭代器，如果是a_iter，就是会返回迭代器自己（这里是yield的底层实现，你看不见）
    print(k)

print('*'*30)

for n in a:
    print(n)

print('*'*30)

for n in a:
    print(n)

'''
在这个方法中，__iter__函数，就是生成器函数，之后重复使用这个类的实例就行了，因为诸如sum（）、
for in 循环等函数都是调用了对象内置的__iter__方法来获得迭代器的
'''