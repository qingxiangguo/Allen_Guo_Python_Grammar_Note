# Qingxiang Guo
# {2022/6/30} {21:32}
#1，定义一个列表
nums=[11,22,33,44]  #可迭代对象

#2，取列表这个可迭代对象的迭代器
nums_iter=iter(nums)

#3，循环的方式，调用next取，迭代器中的数据
while True:
    try:
        number=next(nums_iter)  #提取迭代器的下一个数据
        print(number)
    except StopIteration as ret:
        print(ret)
        break
'''
11
22
33
44
'''