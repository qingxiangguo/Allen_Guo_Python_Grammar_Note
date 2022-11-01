# Qingxiang Guo
# {2022/6/30} {17:34}
nums=[11,22,33,44]  #是可迭代对象
print(type(nums))  #<class 'list'>
nums_iter=iter(nums)  #是迭代器
print(type(nums_iter))  #<class 'list_iterator'>  迭代器

for num in nums:  # for作用于可迭代对象会自动去找__iter__方法，获得迭代器
    print(num)

'''
11
22
33
44
'''

for num2 in nums_iter:  # 也可以你自己手动把迭代器提取出来，其实效果是一样的
    print(num2)

'''
11
22
33
44
'''