# Qingxiang Guo
# {2022/7/17} {21:16}
from time import ctime,sleep

#定义一个闭包
def timefun(func):
    def wrapped_func():
        print('%s called at %s' % (func.__name__, ctime()))  #ctime()是现在的时间戳，__name__是函数名
        func()
    return wrapped_func

@timefun  #使用装饰器对foo函数进行装饰，此时foo=timefun(foo)
def foo():
    print('hello')

foo()
'''
foo called at Sun Jul 17 21:23:02 2022
hello
'''
sleep(2)  #过两秒再调用
foo()
'''
foo called at Sun Jul 17 21:23:04 2022
hello
'''