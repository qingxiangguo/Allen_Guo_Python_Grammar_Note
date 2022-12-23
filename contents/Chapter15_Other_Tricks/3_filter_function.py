# Qingxiang Guo
# {2022/6/10} {17:25}
'''
filter() 函数用于 过滤 可迭代对象中不符合条件的元素，返回由符合条件的元素组成的新的迭代器
filter的语法为filter(函数，可迭代对象)，前面需要输入一个函数
filter返回的是一个迭代器对象，所以输出的时候需要list展开。
'''

#传统方法，for循环来寻找偶数序列
a = [1, 2, 3, 4, 5]
b  = []
for i in a:
    if i % 2==0:
        b.append(i)
print(b) #输出[2, 4]

#那么使用filter的话，代码变得更简洁
a = [1, 2, 3, 4, 5]
#filter需要输入一个函数
def check(i):
    if i % 2==0:
        return i
b=list(filter(check,a))  #使用check函数，来筛选a中的元素
#由于filter返回的结果是一个迭代器，所以需要用list展开
print(b)  #输出[2, 4]


