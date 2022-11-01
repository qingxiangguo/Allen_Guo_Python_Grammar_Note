# Qingxiang Guo
# {2022/7/16} {18:06}
def check_login(func):
    print('-----1-------')
    def inner():
        print('------2-----')
        func()
        print('-------3------')

    print()
    return inner

print('-----4-----')
@check_login
def f1():
    print('-----5-------')
    print('This is function one')

f1()

'''
-----4-----
-----1-------

------2-----
-----5-------
This is function one
-------3------
'''
#说明：@check_login这个装饰器对f1的修饰时间，不是因为f1()的调用，而是遇到@，就会执行装饰器内部函数
