# Qingxiang Guo
# {2022/7/6} {23:48}
def create_point():
    x=0
    k=2  #设定初始值
    b=1
    while True:
        y=k*x+b
        temp = yield (x,y)  #生成器，产生一个元组，send只改变temp的值
        #也就是说，你不send，修改temp时，使用next，只取yield(x,y)中x,y的值，打印出来
        #但是如果你使用了send，就会修改k,b然后再打印的时候，打印的还是yield返回的x,y，只不过是修改计算过的
        if temp:  #如果使用了send，temp=True，那么会运行下面的代码
            k,b = temp  #这里会把接收到的元组，拆包赋值给k,b，改变系数
        x = y

fib1=create_point()
fib2=create_point()

print(next(fib1))
print(next(fib1))
print(next(fib1))

print('---------')
print(next(fib2))

'''
(0, 1)
(1, 3)
(3, 7)
---------
(0, 1)
'''

#总结：如果多次调用def代码块，实际是创建了多个生成器，且每个生成器之间没有关系，各用各的
