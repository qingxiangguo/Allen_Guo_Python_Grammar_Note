# Qingxiang Guo
# {2022/7/9} {12:46}
'''
在闭包中修改外部函数的变量，是不行的，必须要用nonlocal来声明
但是有一种例外，就是这个外部变量本身，是可变的
比如是列表，那么修改列表的值，是ok的，因为没有更改引用
对数字、字符串、元组等不可变类型来说，只能读取，不能更新。如果尝试重新绑定，例如count=count+1
属于是修改可变对象，建立了一个新的引用
其实会隐式创建局部变量count。这样，count就不是自由变量了，因此不会保存在闭包中。
为了解决这个问题，Python3引入了nonlocal声明。
它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。
如果为nonlocal声明的变量赋予新值，闭包中保存的绑定会更新
'''
#下面以一个计算器为例子
def counter(start=0):
    def add_one():
        nonlocal start
        start+=1
        return start
    return add_one  #一定不能写成add_one()

c1=counter(5)  #创建一个闭包，start起始值为5
print(c1())  #6  c1()相当于add_one()
print(c1())  #7

c2=counter(50)  #创建另外一个闭包，start起始值为50
print(c2())  #51
#说明可以创建多个闭包，每个闭包之间没有关系