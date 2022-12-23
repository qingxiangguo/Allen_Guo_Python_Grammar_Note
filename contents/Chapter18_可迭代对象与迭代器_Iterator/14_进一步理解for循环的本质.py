from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

class Ran(object):
    def __init__(self,b):
        self.a=0
        self.b=b
    def __iter__(self):
        return self
    def __next__(self):
            if self.a >= self.b:
                self.a = 0 #归零
                raise StopIteration
            self.a += 1
            return self.a

fib=Ran(5)
fib_iter=iter(fib)

#for num in fib:   #这里for会使用iter()来取fib的迭代器，再用next()来取值
#    print(num)

#print(next(fib_iter))  #由于归零，这里又可以重新开始计数了

for num in fib_iter:   #这里for是对于迭代器用的，fib_iter=iter(fib)。所以还是会执行iter()命令，返回迭代器
    #然后for再用next()进行取值
    print(num)

for num in fib_iter:   # 可以反复调用，从头开始
    print(num)

print(isinstance(fib,Iterable))  #True  fib即是可迭代对象，又是迭代器，只要iter返回的是自己，那么自己就是迭代器
print(isinstance(fib,Iterator))  # True
print(isinstance(fib_iter,Iterable))  # True
print(isinstance(fib_iter,Iterator))  #True

'''
1
2
3
4
5
1
2
3
4
5
'''

'''
我们接下来就看看，for循环的具体工作过程：
for循环在处理这些数据，会去取 __iter__() 方法，来获得迭代器，而迭代器刚好返回了自己，也就是他自己就是一个迭代器
然后调用迭代器的 __next__() 方法，一个个取值，并捕获StopIteration异常，
也就实现了遍历完所有数据就会结束，并不会抛出这个异常。
'''

