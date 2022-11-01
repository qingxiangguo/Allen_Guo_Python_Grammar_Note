from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

class Ran(object):
    def __init__(self,b):
        self.a=0
        self.b=b

    def __iter__(self):  #为什么yield在__iter__中呢？而不是__next__中呢
        #因为__iter__是一个非常重要的基础声明，for第一个调用的也是iter
        #在iter里面加入yield,next相当于就自动创建了
        try:
            while True:
                if self.a >= self.b:
                    self.a = 0
                    raise StopIteration  # 这里人为激发产生异常，如果不使用后面的try。。。except，就会报错直接退出。那么就不能继续遍历生成器了
                self.a += 1
                yield self.a  #因为这里有yield,相当于__iter__现在是生成器函数，降级，但整个类的实例化对象不是生成器对象
            #并且每一次后面的for使用next，都会使得yield后面的代码继续运行
        except StopIteration:  #保证报错的时候，平缓退出，要不然遇到下面第一个for循环就直接退出了
            pass

if __name__ == '__main__':        #在iter里面加入yield,next相当于就自动创建了
    fib=Ran(5)

fib_iter = iter(fib) #取fib的迭代器
print(fib_iter)  # <generator object Ran.__iter__ at 0x00000280C3149A10>, 把__iter__里面的生成器给取出来了

print(isinstance(fib,Iterable))  #True, 有__iter__，是可迭代对象
print(isinstance(fib,Iterator)) #False，整个fib并不是迭代器

print(isinstance(fib_iter,Iterable))  #True, fib_iter是生成器，所以是可迭代对象
print(isinstance(fib_iter,Iterator)) #True，fib_iter是生成器，所以是可迭代对象

'''
实例化的fib首先是可迭代对象，因为有__iter__函数，
'''

for i in fib:
    print(i, end='  ')

for i in fib:
    print(i, end='  ')

for i in fib:
    print(i, end='  ')

#输出1  2  3  4  5  1  2  3  4  5  1  2  3  4  5
#类的生成器，在__iter__中，使用yield，使得生成器可以被多次从头遍历了
'''
这里的代码运行逻辑是，整个过程看起来就是不断地 执行->中断->执行->中断 的过程
一开始调用fib=Ran(5）。由于里面有yield，因此不需要你指定iter,next
fib就已经是一个生成器，也是一个可迭代对象了，并且拥有迭代器（当然，迭代器可以用iter(fib)取出来）
然后for循环的时候，for第一反应是使用iter函数，调用fib的iter函数，看是不是可迭代对象，来取里面的迭代器
然后就开始执行while True语句，由于里面有yield语句，fib也拥有迭代器（生成器）
接着执行yield self.a，然后暂停回到for循环
for循环会使用next函数，对fib的迭代器进行取值，由于next触发了yield继续运行，因此
会接着运行self.a +=1的语句，然后在while True里面开始循环执行

当我们使用 yield 时，它帮我们自动创建了__iter__() 和 next() 方法，而且在没有数据时，也会抛出 StopIteration 异常，
也就是我们不费吹灰之力就获得了一个迭代器，非常简洁和高效。
带有 yield 的函数执行过程比较特别：

调用该函数的时候不会立即执行代码，而是返回了一个生成器对象；
当使用 next() (在 for 循环中会自动调用 next() ) 作用于返回的生成器对象时，函数 开始执行，在遇到 yield 的时候会『暂停』，并返回当前的迭代值；
当再次使用 next() 的时候，函数会从原来『暂停』的地方继续执行，直到遇到 yield语 句，如果没有 yield 语句，则抛出异常；
整个过程看起来就是不断地 执行->中断->执行->中断 的过程。一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；
然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，要注意的是，
此刻会记住中断的位置和所有的变量值，也就是执行时的上下文环境被保留起来；当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield ，
如果没有 yield ，则抛出异常。简而言之，就是 next 使函数执行， yield 使函数暂停。
'''