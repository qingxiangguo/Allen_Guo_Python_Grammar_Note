# Qingxiang Guo
# {2022/6/30} {21:53}
from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

class MyList(object):
    '''自定义的一个可迭代对象'''
    def __init__(self):
        self.items=[]

    def add(self,val):
        self.items.append(val)  #定义一个方法，将参数输入MyList对象的items列表

    def __iter__(self):
        #这个方法有两个功能
        #1，标记当前类创建出来的对象，一定是可迭代对象
        #2，到调用iter函数时，这个方法会被调用，返回相应的迭代器
        return MyIterator(self)  #相当于把实例对象，传给MyIterator，然后再创建一个实例对象，也就是迭代器对象

class MyIterator(object):
    '''自定义的供上面可迭代对象调用的迭代器'''
    def __init__(self,other):  #多一个other，用于将可迭代对象和迭代器连接起来
        self.mylist=other  #将上面那个可迭代对象的引用，与本迭代器的self.mylist属性连接，使得self.mylist.items可以访问上面的列表

    def __next__(self):
        #这个方法有两个功能
        #1，标记当前类创建出来的对象（当然了，还有__iter__方法一起），一定是迭代器
        #2,当使用next函数，next迭代器时，这个方法会被自动调用，它返回一个数据
        print('haha')
        return 100

    def __iter__(self):
        pass

mylist=MyList()  #实例化一个可迭代对象
mylist_iter=iter(mylist)  #用iter函数获取可迭代对象的迭代器，它会自动调用mylist对象的__iter__方法
#iter(mylist)的结果，会调用mylist对象的__iter__方法，返回MyIterator(self)，self指代实例对象
#也就是将MyIterator(mylist)返回给mylist_iter
#而MyIterator(mylist)，相当于又创建了一个实例对象，所以会调用MyIterator类的__init__方法
#并同时将mylist传给MyIterator类的__init__方法中的other

print('mylist是否是可迭代对象',isinstance(mylist, Iterable))  # True
print('mylist是否是迭代器',isinstance(mylist, Iterator))   # False

print('mylist_iter是否是可迭代对象',isinstance(mylist_iter, Iterable))  # True
print('mylist_iter是否是迭代器',isinstance(mylist_iter, Iterator))  # True

'''
mylist是否是可迭代对象 True
mylist是否是迭代器 False  #调用了迭代器，单本身不一是迭代器
mylist_iter是否是可迭代对象 True
mylist_iter是否是迭代器 True  
'''

next(mylist_iter)
#输出haha,因为调用了__next__函数

print(next(mylist_iter))
#输出haha和100

#总结，iter函数，next函数，与__iter__方法，__next__方法的关系
#当对一个可迭代对象调用iter()函数时，它会自动调用这个可迭代对象的__iter__方法，这个方法返回对象当做迭代器
#当对一个迭代器对象调用next()函数时，它会自动调用这个迭代器的__next__方法，来返回下一个数据
#python要求迭代器本身也是可迭代的
#迭代器对象，一定是可迭代对象
#可迭代对象，不一定是迭代器