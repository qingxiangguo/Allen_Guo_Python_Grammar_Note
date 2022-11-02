# Qingxiang Guo
# {2022/7/9} {11:38}
#引用，python里面=大多都是引用，而不是赋值
#也就是修改原变量，新的也会变

#第一例子
a=[11,22,33]
b=a
a.append(44)
print(a)  #[11, 22, 33, 44]
print(b)  #[11, 22, 33, 44]

#第二例子
def xx(temp):
    print(temp)
    temp.append(44)
    print(temp)

nums=[100,200]
xx(nums)
'''
[100, 200]
[100, 200, 44]
'''

print(nums)
'''
[100, 200, 44]
'''

#下面例子对于理解闭包中的函数引用很重要
def test():
    print('---test func---')

#定义函数的本质为，定义了一个全局变量test，引用保存了一个代码块的地址
test() #这是调用引用
ret =test #目前ret也指向了ret代码块

#下面输出的2个地址结果是相同的
print(id(ret))  #2077108464672
print(id(test))  #2077108464672

