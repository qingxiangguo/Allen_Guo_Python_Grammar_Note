# Qingxiang Guo
# {2022/7/17} {21:01}
'''
装饰器也用到了闭包，那么他与普通闭包有什么区别呢?
'''
#下面是装饰器
def log(func):
    def call():
        ret=func()  #ret取原函数的返回值，也就是hello
        if ret and isinstance(ret,str):  #判断类型是字符串
            with open('log.txt','w') as f:  #那么就写入ret
                f.write(ret)
        return ret  #同时还返回ret，也就是hello
    return call

@log
def print_hello():
    return 'hello'

print(print_hello())

'''
会写入hello到文件
然后打印hello到屏幕
'''

#下面是闭包例子
def who(name):
    def do(content):
        print(name,content)
    return do

j=who('john')  #创建一个j闭包
j('hello')
#会输出：john hello
#总结:普遍闭包，内部函数将外部变量当做纯数据来用
#装饰器：内部函数将外部变量，当做可调用的对象，如函数，来使用