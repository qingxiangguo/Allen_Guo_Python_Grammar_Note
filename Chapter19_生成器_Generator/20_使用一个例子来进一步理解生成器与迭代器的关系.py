# Qingxiang Guo
# {2022/8/19} {13:41}
from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

def fib_generator():
    print('---1---')  #用来标识，便于检测运行顺序
    num1=1
    num2=1
    while True:   #使代码有循环能力
        print('---2---')
        temp_num = num1
        print('---3---')
        num1,num2=num2,num1+num2
        print('---4---')
        yield temp_num
        print('---5---')

fib=fib_generator()  #生成一个生成器对象

fib_ml=iter(fib)  #手动获取生成器对象fib的迭代器

#print(next(fib))

print(isinstance(fib,Iterable))  #结果是True，表示fib一定是可迭代对象
print(isinstance(fib,Iterator))  ##结果是True，表示fib一定是迭代器
print(isinstance(fib_ml,Iterable))  #结果是True，表示fib_ml一定是可迭代对象
print(isinstance(fib_ml,Iterator))  ##结果是True，表示fib_ml一定是迭代器

print(type(fib),id(fib))  #<class 'generator'> 1880167837568
print(type(fib_ml),id(fib_ml))  #<class 'generator'> 1880167837568，两者ID一致
#由于生成器就是特殊的迭代器，因此iter(fib)取到的fib_ml，实际上多此一举，就是fib本身
#函数里面有yield，自动创建了__iter__和__next__方法
#总结，生成器就是迭代器，对生成器手动取iter（）是没有意义的，只会取回自己
#next()作用对象只能是迭代器！！！直接对列表就不行