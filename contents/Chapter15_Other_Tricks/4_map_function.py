# Qingxiang Guo
# {2022/6/10} {17:25}
'''
map()函数会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
map的语法为map(函数，可迭代对象)，前面需要输入一个函数
map返回的是一个迭代器对象，所以输出的时候需要list展开。
'''

#map需要输入一个函数
def square(x):  #计算平方数
    return x**2

a=map(square,[1,2,3,4,5])
print(list(a))  #[1, 4, 9, 16, 25]

#下面看一下有多个可迭代对象（iterable）的情况
def add(x,y,z):
    return x + y + z

list1=[1,2,3]
list2=[1,2,3]
list3=[1,2,3]
res=map(add,list1,list2,list3)
print(list(res))  #输出[3, 6, 9]，第一位，第二位，第三位会分别全部相加

#有人可能会问，如果三个列表长度不一样怎么办？
#在我们看下另一个例子你就明白了

def add(x,y,z):
    return x,y,z

list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = [1,2,3,4,5]
res = map(add, list1, list2, list3)
print(list(res))  #输出[(1, 1, 1), (2, 2, 2), (3, 3, 3)]