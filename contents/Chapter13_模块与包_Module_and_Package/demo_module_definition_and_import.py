# Qingxiang Guo
# {2022/6/2} {15:06}
'''
Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python对象和Python定义语句。
模块能定义函数，类和变量，模块里也能包含可执行的代码。
'''
#下面示范模块的导入
import math #导入一个关于数学运算的模块
print(id(math))  #1905745258240
print(type(math))   #<class 'module'>
print(math)  #<module 'math' (built-in)>
print(math.pi)  #导入模块math中的pi函数

print(dir(math))  #查看math可用的方法
print(math.pow(2,3),type(math.pow(2,3)))  #8.0 <class 'float'>。2的3次方
print(math.ceil(9.001))  #向上取整  10
print(math.floor(9.999))  #向下取整  9

#还可以从模块中调用函数
from math import pi
print(pi)  #3.141592653589793，就可以直接调用了

#你还可以导入自定义模块，首先建立一个python文件，clac.py
import calc
print(calc.add(2,3))  #5，注意这里不能直接add(2,3)，因为只是调用了模块，不能直接用里面的函数
print(calc.div(10,2))  #5.0