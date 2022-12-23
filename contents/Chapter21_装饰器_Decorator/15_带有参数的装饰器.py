# Qingxiang Guo
# {2022/7/18} {21:25}
import time

def call_out2(timeout=0):  #timeout是输入的参数，默认0，这个函数用来接收参数
    def call_out1(func):  #这里开始和普通的装饰器一样
        def call():
            print('-------1---------')
            time.sleep(timeout)  #使用接收的参数，暂停几秒
            ret=func()  #读取原函数的返回值
            print('-------2---------')
            return ret  #返回原函数的返回值
        return call
    return call_out1  #返回里面真正装饰的函数

@call_out2(2)   #等于@call_out1
def print_hello():
    print('hello world')
    return 'ok'

print(print_hello())
'''
-------1---------
hello world
-------2---------
ok
'''

'''
执行逻辑如下，@call_out2(2) ，先执行def call_out2(timeout=2): 
timeout赋值为2，然后返回call_out1，加在@的后面
这个时候就变为@call_out1，和普通装饰器一样
print_hello=call_out1(print_hello)
也就是print_hello=call
后面就和普通装饰器一样了
'''