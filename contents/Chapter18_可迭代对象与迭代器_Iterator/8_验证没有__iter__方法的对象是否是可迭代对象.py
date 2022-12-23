# Qingxiang Guo
# {2022/6/30} {21:37}
'''
只要在类中，定义了__iter__方法，那么这个类创建出来的对象，一定是可迭代对象
通俗的说，一个具备了__iter__方法，那么这个类创建出来的对象一定是可迭代对象
'''
from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象

class MyList(object):
    def __init__(self):
        self.container = []

    def __iter__(self):
        pass

    def add(self,item):
        self.container.append(item)

mylist=MyList()  #实例化一个对象
mylist.add(11)
mylist.add(22)
mylist.add(33)

print(isinstance(mylist,Iterable))  #如果结果是True，则表示mylist一定是可迭代对象
#输出True
print(isinstance(mylist.container,Iterable))  # True

#小总结
#如果定义类时，有__iter__方法，那么
#这个类创建出来的对象一定是可迭代对象

for num in mylist.container:
    print(num)

'''
11
22
33
'''