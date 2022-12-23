# Qingxiang Guo
# {2022/7/17} {21:37}
def xxx(func):  #这样xxx装饰器就是一个万能的，能接收不同个数参数的装饰器，而不用每个函数都写一个
    def yyy(*args,**kwargs):  #用来接收不确定个数的参数
        func(*args,**kwargs)  #将接收到的参数进行拆包，然后传递到原函数中
    return yyy

@xxx
def a(num):
    print('--1--',num)

a(100)
#输出  --1-- 100


@xxx
def b(num,num2,num3):
    print('--2--',num,num2,num3)

b(200,300,800)
#输出--2-- 200 300 800
