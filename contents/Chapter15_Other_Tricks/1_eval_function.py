# Qingxiang Guo
# {2022/6/9} {21:14}
'''
这里介绍内置函数eval()的作用
eval()函数用来执行一个字符串表达式，并返回表达式的值。还可以把字符串转化为l列表，元组，字典
'''

#字符串转换成列表
a='[1,2,3,4,5]'
print(a,type(a))  #[1,2,3,4,5] <class 'str'>
b=eval(a)
print(b,type(b)) #[1, 2, 3, 4, 5] <class 'list'>

# 字符串转换成字典
a="{'name':'guo','age':25}"
print(a,type(a))   #{'name':'guo','age':25} <class 'str'>
b=eval(a)
print(b,type(b))   #{'name': 'guo', 'age': 25} <class 'dict'>

#字符串转换为元组
a="(1,2,3,4,5)"
eval(a)

#返回表达式的值
x=4
print(eval('3*x'))  #12

#返回表达式的值
n=81
print(eval('n+6')) #87