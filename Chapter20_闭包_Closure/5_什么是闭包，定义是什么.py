# Qingxiang Guo
# {2022/7/9} {11:52}
#1.什么是闭包。
#如果一个函数中又嵌套定义了另外一个函数，且内部这个函数用到了外部函数的局部变量或者形参
#那么这个内部函数，以及用到的外部函数之中的变量，称为闭包
#2.怎么定义闭包
#嵌套，内部这个函数用到了外部函数的局部变量或者形参，外部函数将内部函数的引用返回

def person(name):
    num=100
    def say(content):
        print('(%s):%s' % (name,content))
    return say

a=person('john')
a('hello')  #(john):hello
#a()就相当于say()