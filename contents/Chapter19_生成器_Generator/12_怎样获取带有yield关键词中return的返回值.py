# Qingxiang Guo
# {2022/7/5} {0:43}
def fib_generator():  #同时有三个yield
    num1=1
    num2=1
    temp_num=num1
    num1,num2=num2,num1+num2
    print('----1-----')
    yield temp_num

    temp_num = num1
    num1, num2 = num2, num1 + num2
    print('----2-----')
    yield temp_num

    temp_num = num1
    num1, num2 = num2, num1 + num2
    print('----3-----')
    yield temp_num

    print('没有代码了')
    return '已经生成了3个斐波那契数列'

fib=fib_generator()

print(next(fib))   #每一个next只能前进一个yield，整个def里面的内容需要三次next才能读完
print(next(fib))
print(next(fib))

'''
----1-----
1
----2-----   
1
----3-----
2
'''
#print(next(fib))
#如果强行第四个next的话，会报错：StopIteration: 已经生成了3个斐波那契数列
#1.如果在调用next的时候，从上一次暂停的位置，继续向下运行时，遇不到yield了，就会产生异常
#2.如果在调用next的时候，从上一次暂停的位置，继续向下运行时，遇不到yield了，而且下面还有个return
#那么，不光会产生异常，还会将return返回的数值，用异常储存起来（很奇怪的规定）

#那么怎么正确捕获yield代码块中return的返回值呢？使用try

try:
    print(next(fib))
except StopIteration as ret:
    print(ret.value)  #会输出  已经生成了3个斐波那契数列，并且程序不报异常
#总结：一般调用生成器，发现拿不到return语句的返回值，如果想拿到，必须
#捕获StopIteration错误，返回值包含在StopIteration的value中
