'''
有时候会误认为，列表就是迭代器，实际上，列表可不是迭代器（iterator）。
要想成为迭代器，需要经过内置函数 iter 包装：
列表和迭代器的区别：
列表不论遍历多少次，表头位置始终是第一个元素
迭代器遍历结束后，不再指向原来的表头位置，而是为最后元素的下一个位置
'''

lst = [1,2,3,4]
print(type(lst))  # <class 'list'>
lst_iter = iter(lst)
print(type(lst_iter))  # <class 'list_iterator'>
# 可以看到列表和迭代器的类型是不同的

# print(next(lst))  # TypeError: 'list' object is not an iterator

for num2 in lst:  # 列表可以多次使用，因为每次都重新调用lst的__iter__，创建了新的迭代器
    print(num2)

for num2 in lst:
    print(num2)

for num in lst_iter:# 而迭代器只能被for遍历一次
    print(num)

for num in lst_iter:  # 再for一遍，迭代器也不能前进了
    print(num)

# print(next(lst_iter))  # Will cause an StopIteration error

'''
1
2
3
4
1
2
3
4
1
2
3
4
Traceback (most recent call last):
  File "E:\pythonProject\Chapter18_可迭代对象与迭代器_Iterator\test.py", line 14, in <module>
    print(next(lst_iter))
StopIteration

'''

'''
只有迭代器对象才能与内置函数 next 结合使用， next 一次，迭代器就前进一次，指向一个新的元素。
所以，要想迭代器 b 重新指向 a 的表头，需要重新创建一个新的迭代器。
'''