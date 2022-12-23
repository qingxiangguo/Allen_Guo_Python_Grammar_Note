# Qingxiang Guo
# {2022/7/4} {21:39}
def fib_generator():
    num1=1
    num2=1
    while True:   #使代码有循环能力
        temp_num = num1
        num1,num2=num2,num1+num2
        yield temp_num

fib=fib_generator()  #生成一个迭代器
print(fib)  #<generator object fib_generator at 0x00000156BF5A9A10>

print(next(fib))  #因为fib是生成器，又因为生成器是迭代器，因此可以通过next函数取值  输出1

print(next(fib))  #1，next会返回yield后的值，可以供打印

print(next(fib))  #2

print(next(fib))  #3