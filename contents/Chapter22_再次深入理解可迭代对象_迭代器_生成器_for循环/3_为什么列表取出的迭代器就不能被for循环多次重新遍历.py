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

'''
其实正常情况，同一个迭代器来说，是一个单向的容器，走到尾部之后，不会自动再回到开始位置
使用for循环之后，再一次for循环不会打印出任何结果
所以列表的迭代器已经被消耗完了，第二次及后续再for循环，自然打印不出来内容了
'''