# Qingxiang Guo
# {2022/7/16} {17:33}
'''
学习装饰器，需要引用的知识，复习一下
'''
def foo():
    print('foo')

foo = lambda x:x+1 #会执行lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了
#另外一个匿名函数

ret = foo(11)
print(ret)  #输出12

#小结：如果定义了一个函数，而在接下来的代码中，又将这个函数名=xxx
#那么修改了原foo的指向，即foo()不一定就执行原来的函数功能
