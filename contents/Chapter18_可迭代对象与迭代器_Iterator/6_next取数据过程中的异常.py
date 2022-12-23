# Qingxiang Guo
# {2022/6/30} {21:24}
nums=[11,22,33,44]  #是可迭代对象
nums_iter=iter(nums)  #是迭代器

num1=next(nums_iter)
print(num1)

num2=next(nums_iter)
print(num2)

num3=next(nums_iter)
print(num3)

num4=next(nums_iter)
print(num4)

try:
    num5=next(nums_iter)
    print(num5)
except StopIteration as ret: #主动捕获异常来停止迭代
    print(ret)

print('-'*30)

for num in nums:
    print(num)

'''
11
22
33
44
------------------------------
11
22
33
44
'''

#小总结：
#for循环的过程，可以手动通过上面的iter()和next()函数来实现
#也就是说
#1.先调用iter()，将nums当做实参，得到nums这个可迭代对象的迭代器
#2.调用next()，将上一步得到的迭代器，进行取值
#3.将上一步取出来的值，赋值给num这个变量
#4.执行for循环体重的代码，print(num)
#5.接下来重复执行2-3-4步，当nums中的所有数据都获取完毕之后，会在下一次调用next时，产生StopIteration异常
#只不过for循环中自带了异常处理，当它遇到StopIteration异常的时候，会自动结束for循环