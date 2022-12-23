from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

class get_province_population(object):
    def __init__(self,filename):
        self.filename=filename

    def __iter__(self):
        with open(self.filename) as f:
            for line in f:
                yield int(line)   #这里因为不存在边界，需要count的情况，所以不用考虑raise StopIteration之类的退出机制


gen = get_province_population('province_data.txt')

all_population = sum(gen)  #会遍历gen，并求和
print(all_population)  #7737179

for population in gen:  #gen不会被消耗了，会遍历gen，然后每一行除以总数
    print (population/all_population)

#看类型
print(isinstance(gen,Iterable))  #True  他当然是可迭代对象，因为有__iter__
print(isinstance(gen,Iterator))  #False，不是迭代器，也不是生成器，因为class下面一级，没有__next__，也没有yield
#yield只是在__iter__函数里面

fib_iter = iter(gen)  # 这里取出来的迭代器，是一个生成器，生成器就是特殊的迭代器
print(fib_iter)  # <generator object get_province_population.__iter__ at 0x00000267067C7140>, 取到了生成器
print(isinstance(fib_iter,Iterator))  # True, 生成器当然是迭代器

# 但是需要注意，这个写法有一个不好的地方，用next，需要额外调用一次iter()
# 因为有生成器的类的实例对象，本身只是可迭代，而不是迭代器，因为没有__next__方法，
# 而且yield也只是在__iter__函数里面而已，并不能让整个类变为迭代器
# next（）里面只能接迭代器（生成器）
# 所以需要手动取一下迭代器用,否则next(gen)会报错
# 这里使用上面取出来的fib_iter = iter(gen)

print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
# print(next(fib_iter)) 如果继续点话会报错StopIteration，这个迭代器（生成器）已经被消耗完了
# 如果想继续，需要手动再取一个迭代器出来

fib_iter2 = iter(gen)  # 再取一个出来
print(next(fib_iter2))  # 又从102200开头了

'''
7737179
0.013208948636188978
0.0015797747473594705
0.011061266645117038
0.0717327335970901
0.5083030908293579
0.3941141855448866
True
False
<generator object get_province_population.__iter__ at 0x000002062BCB6C00>
True
102200
12223
85583
555009
3932832
3049332
102200
'''



