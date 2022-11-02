# Qingxiang Guo
# {2022/7/17} {21:46}
#被装饰的函数一旦return返回值后，就变麻烦
def xxx(func):  #这样xxx装饰器就是一个万能的，能接收不同个数参数的装饰器，而不用每个函数都写一个
    def yyy(*args,**kwargs):  #用来接收不确定个数的参数
        ret=func(*args,**kwargs)  #将接收到的参数进行拆包，然后传递到原函数中
        return ret #为了捕获100，需要手动捕获，并再次返回
    return yyy

@xxx
def a(num):
    print('--1--',num)
    return 100  #这里增加了返回值，如果想捕获这个返回值，就不能按原来的方式

print(a(100))
'''
会输出如下
--1-- 100
100
否则，会打印出none
'''