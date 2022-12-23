# _*_ coding=utf-8 _*_
from itertools import groupby
from collections.abc import Iterator
from collections.abc import Iterable
# 能够实现分类

# 例子一
cig_iter = groupby(["1","2","a","3","5","u"], lambda x: x.isdigit())

# 能够将后面的函数，映射到前面的列表，然后经过groupby函数输出一个迭代器cig_iter
# 然后这个迭代器，能够取出，key键值和组成内容digit_list，key和digit_list的对应关系类似，字典的键值对
for key, digit_list in cig_iter:
    print(key, list(digit_list))  # 会把1，2分为一组，直到遇到a，开始新的一组，然后再到3，又是一组

print('groupby的输出结果是可迭代对象吗：', isinstance(cig_iter, Iterable))
print('groupby的输出结果是迭代器吗：', isinstance(cig_iter, Iterator))

print('第二个内容digit_list是可迭代对象吗：', isinstance(digit_list, Iterable))
print('第二个内容digit_list是迭代器吗：', isinstance(digit_list, Iterator))
# 所以groupby的输出是迭代器，这个迭代器又可以取两个东西出来，一个键，一个又是关于内容的迭代器

"""
True ['1', '2']  # 因为是根据是否is.digit来判断，所以键值是True or False
False ['a']
True ['3', '5']
False ['u']
"""

# 例子二
for key, group in groupby([1,1,1,1,5,1,1,1,1,4]):
    print(key, list(group))

'''
1 [1, 1, 1, 1]  # 如果不设定判断标准，默认是根据不同值
5 [5]
1 [1, 1, 1, 1]
4 [4]
'''

# 例子三
it = groupby([1,1,1,1,5,1,1,1,1,4])
key1, group1 = next(it)  # 每次next可以取两个东西出来
print(key1, list(group1)) # 1 [1, 1, 1, 1]
key2, group2 = next(it)
print(key2, list(group2)) # 5 [5]
# 可以手动使用next对groupby输出的迭代器向前取，但由于迭代器是一次性的，group1（也是迭代器）后面将不复存在
print(key1, list(group1)) # 1 [] 不复存在

# 例子四，迭代器生成的迭代器，也可以手动next取值
it = groupby([1,1,1,1,5,1,1,1,1,4])
key1, group1 = next(it)  # 每次next可以取两个东西出来
# group1也是一个迭代器,可以列表化为[1,1,1,1]
print(next(group1)) # 1
print(next(group1)) # 1
print(next(group1)) # 1
print(next(group1))  # 1
# print(next(group1)) 会StopIteration



