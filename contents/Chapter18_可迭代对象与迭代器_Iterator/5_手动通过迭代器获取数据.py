# Qingxiang Guo
# {2022/6/30} {17:36}
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
#4.执行for循环体的代码，print(num)
#5.接下来重复执行2-3-4步

