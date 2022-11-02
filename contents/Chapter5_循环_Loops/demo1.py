# Qingxiang Guo
# {2022/5/7} {15:52}
#range()内置函数的三种创建方式，range的优势是不论多长，你占的空间都一样，只有计算内容才占用更多
'''第一种创建方式，只有一个参数（小括号中只给了一个数）'''
r=range(10)   #默认从零开始，步长为1
print(r)  #range(0,10)，返回的是一个迭代器，不是具体的内容
print(list(r))   #所以需要用list()函数来展开这个迭代器，range()本质是创建了一个列表

'''第二种创建方式，给了两个参数'''
r=range(1,10)  #1到10，右边是开区间
print(list(r))   #[1, 2, 3, 4, 5, 6, 7, 8, 9]

'''第三种创建方式，给了三个参数'''
r=range(1,10,2)
print(list(r))  #[1, 3, 5, 7, 9]

'''判断指定的整数在序列中是否存在，使用in, not in'''
print(10 in r) #False，10不在当前的r的这个整数序列中
print(9 in r) #True，9在当前的r的这个整数序列中

print(10 not in r)  #True
print(9 not in r)   #False

print(range(1,20,1))   #占用空间一样
print(range(1,101,1))   #占用空间一样