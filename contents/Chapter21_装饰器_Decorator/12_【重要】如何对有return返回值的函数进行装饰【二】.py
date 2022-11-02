# Qingxiang Guo
# {2022/7/17} {21:52}
#关于装饰器修饰有返回的函数
#python 函数内部套另外一个函数的时候，内部函数如果结尾有return返回值，
#是不能自动继承到外部函数的，需要手动等号获取这个返回值，再在外部函数的结尾return出来。
#装饰器是一种特殊的闭包，下面我们以一个最简单的闭包作为例子

#反面教材
def fuc():  #定义一个用来调用的内部函数
    return 100

def person(name):
    def say(content):
        print('(%s):%s' % (name,content))
        fuc()  #fuc里面虽然有返回100，但是并不能自动继承到外部函数say()
    return say

a=person('john')  #创建一个闭包，a()=say()
print(a('hello'))
'''
(john):hello
None
fuc() return的100，并没有被捕获，所以打印整个函数的时候，会输出none
'''

#正面例子
def fuc():  #定义一个用来调用的内部函数
    return 100

def person(name):
    def say(content):
        print('(%s):%s' % (name,content))
        return_value=fuc()  #需要手动捕获fuc()的return
        return return_value  #然后再return一遍
    return say


a=person('john')  #创建了一个闭包a
print(a('hello'))  #这个时候,a()等于say()，除了打印(john):hello，还会返回100，打印出来

'''
(john):hello
100
'''

#正面例子
def fuc():  #定义一个用来调用的内部函数
    print('hello')
    return 100

def person(name):
    def say(content):
        print('(%s):%s' % (name,content))
        return fuc()  #也可以这样，等价于上面，会执行fuc函数，并返回fuc的返回值
    return say

a=person('john')
print(a('hello'))

'''
(john):hello
hello  
100
'''