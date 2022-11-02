# Qingxiang Guo
# {2022/5/19} {7:49}
#函数的返回值
def fun(num):  #num为列表
    odd=[]  #存奇数
    even=[]    #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even  #要注意return会中止函数

#函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst))  #([29, 23, 53, 55], [10, 34, 44])，是元组

'''函数的返回值
（1）如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''

def fun1():
    print('hello')
    #return 可以省略
fun1()

def fun2():
    return 'hello'
res=fun2()   #比较灵活，先把对象传出来，再打印
print(res)

def fun3():
    return 'hello','world'  #只是返回对象，不打印到屏幕
print(fun3())    #多个结果，为元组
#在定义函数时，是否要设定返回值，视情况而定
