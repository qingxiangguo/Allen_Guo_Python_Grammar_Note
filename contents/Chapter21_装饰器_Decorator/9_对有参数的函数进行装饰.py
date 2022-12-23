# Qingxiang Guo
# {2022/7/17} {21:24}
def timefun(func):
    print('------1---------')
    def wrapped_func(a,b):
        print(a,b)
        func(a,b)
        print('-------2--------')
    return wrapped_func

@timefun  #使用装饰器对foo函数进行装饰，此时foo=timefun(foo)，也就是wrapped_func
def foo(a,b):
    print('-------3--------')
    print(a+b)
    print('--------4-------')

foo(3,5)

'''
输出
------1---------
3 5
-------3--------
8
--------4-------
-------2--------
'''
#总结：1.如果被装饰的函数有两个参数，那么在定义闭包时，需要在内部函数中有对应的形参
#当调用函数时，实参会传递到闭包内部函数中有对应的形参，在内部函数执行时，将这些数据当做实参传递到原函数中