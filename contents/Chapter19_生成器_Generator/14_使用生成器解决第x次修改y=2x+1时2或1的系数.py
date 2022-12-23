# Qingxiang Guo
# {2022/7/5} {22:12}
'''回扣解决一开始的问题'''
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

#1.创建一个生成器
fib=create_point()

#2. 调用next来正常获取y=2x+1，以及x=y互换的值
print(next(fib))  #(0, 1)
print('---------')
print(next(fib))  #(1, 3)
print('---------')
print(fib.send((3, 2)))  #将k改成3，b改成2,注意整体是一个元组  输出(3, 11)  3*3+2=11
print('---------')
print(next(fib))  #输出(11,35)，系数永久改变了

#总结，print(next(fib)) 打印的永远是yield后面的返回值