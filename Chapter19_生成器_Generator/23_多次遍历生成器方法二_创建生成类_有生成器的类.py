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
#创建一个实例化对象，对这个对象使用for，sum，iter等会遍历这个对象的函数时
#会调用这个对象的__iter__函数，而这个__iter__函数里面，会产生一个生成器
#一定要注意：所以gen本身，不是生成器对象！！！但是由于gen有__iter__方法
#所以gen是可迭代对象
#【重点！！！】真要说的话，yield只管自己一层，有yield语句的，就是生成器函数
#所以，在这个层面上，def __iter__(self):，是一个生成器函数。很巧妙的利用了对象
#被遍历时，会调用__iter__方法的特性，在调用时，返回一个内部生成器
all_population = sum(gen)  #会遍历gen，并求和
print(all_population)  #7737179

for population in gen:  #gen不会被消耗了，会遍历gen，然后每一行除以总数
    print (population/all_population)

for population in gen:  #gen不会被消耗了，会再次从头遍历gen，然后每一行除以总数
    print (population/all_population)

#看类型
print(isinstance(gen,Iterable))  #True  他当然是可迭代对象，因为有__iter__
print(isinstance(gen,Iterator))  #False，不是迭代器，也不是生成器，因为class下面一级，没有__next__，也没有yield
#yield只是在__iter__函数里面

fib_iter = iter(gen)
print(fib_iter)  # <generator object get_province_population.__iter__ at 0x00000267067C7140>, 取到了生成器
print(isinstance(fib_iter,Iterator))  # 生成器当然是迭代器

'''
成功输出
7737179
0.013208948636188978
0.0015797747473594705
0.011061266645117038
0.0717327335970901
0.5083030908293579
0.3941141855448866
'''

'''
可以看到，生成器类中的生成器，不会被消耗了，可以多次遍历
这是因为重写接口函数__iter__, 在__iter__里面创建生成器
这样每次遍历创建的实例化对象时，都会调用__iter__
从而创建一个新的yield生成器，达到一劳永逸的效果，相当于__iter__现在是生成器函数
通俗的理解，就是将yield降级，放在一个可反复触发的子类__iter__函数中
从而实现生成器的多次遍历
'''




