# Qingxiang Guo
# {2022/5/10} {16:43}
#列表元素的升序和降序操作
lst=[20,40,10,98,54]
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，从小到大排序，注意sort和sorted函数的区别
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键词参数，将列表中的元素降序
lst.sort(reverse=True)  #reverse=True，默认就是降序排序，reverse=False就是升序排序
print(lst)
lst.sort(reverse=False)
print(lst)

#使用内置函数sorted()，会产生一个新的列表对象
lst=[20,40,10,98,54]
print('原列表',lst)
#开始排序
new_list=sorted(lst)
print(lst)
print(new_list)
#同样也可以指定关键词参数，实现列表元素的降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)
