# Qingxiang Guo
# {2022/6/10} {17:25}
'''
这里介绍了reduce()函数的用法，会对对参数序列中元素进行累积
比如元组，列表。reduce有两个参数，会对
传入的第 1、2 个元素进行操作，得到的结果再与第三个数据用你指定的函数运算，最后得到一个结果
'''
from functools import reduce

def add(x,y):  #定义一个函数给reduce用
    return x+y

sum1=reduce(add,[1,2,3,4,5])
print(sum1)  #输出15，本质是1+2，结果再+3，结果再+4，实现累加

def multi(x,y):  #定义一个乘法函数，输入给reduce，可以实现阶乘
    return x*y
multi1=reduce(multi,[1,2,3,4,5])
print(multi1)  #输出120，实现了阶乘

def show(x,y):
    return x,y  #这样可以更清楚地看清楚reduce内部机制

show1=reduce(show,[1,2,3,4,5])
print(show1,type(show1))  #((((1, 2), 3), 4), 5) <class 'tuple'>，一个嵌套元组

def lst(x,y):
    return [x,y]  #这样可以更清楚地看清楚reduce内部机制

list1=reduce(lst,[1,2,3,4,5])
print(list1,type(list1))  #输出一个嵌套列表，[[[[1, 2], 3], 4], 5] <class 'list'>
