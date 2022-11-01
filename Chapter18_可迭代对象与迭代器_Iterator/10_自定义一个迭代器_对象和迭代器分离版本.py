from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

'''这里展示自定义的可迭代对象，与，迭代器是怎么联系起来的'''
class MyList(object):
    '''自定义的一个可迭代对象，想让他也有迭代器'''
    def __init__(self):
        self.items=[]   # [1,2,3,4,5]

    def add(self,val):
        self.items.append(val)  #定义一个方法，将参数输入MyList对象的items列表

    def __iter__(self):
        #这个方法有两个功能
        #1，标记当前类创建出来的对象，一定是可迭代对象
        #2，到调用iter函数时，这个方法会被调用，返回相应的迭代器
        return MyIterator(self)  #这里的self不能省略,因为是将MyList自己这个实例对象，传给MyIterator

class MyIterator(object):
    '''自定义的供上面可迭代对象调用的迭代器'''
    def __init__(self,other):  #迭代器需要传入一个other参数，other这里指代16行的self，self就可以理解为实例化对象
        self.mylist = other   #所以other.items就是一个列表，又由于other=self.mylist，所以self.mylist.items是一个列表
        self.current=0

    def __iter__(self):
        return self  # 迭代器的__iter__必须要返回自己，想让MyIterator(object)是个迭代器，所以这里必须要返回自己

    def __next__(self):
        if self.current < len(self.mylist.items):  ##将上面那个可迭代对象的引用，与本迭代器的self.mylist属性连接，使得self.mylist.items可以访问上面的列表
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            self.current=0 #必须要这样，归零，才能保证能够多次使用
            raise StopIteration #抛出异常，和平结束
            #为什么return none不行呢？for循环是一个已经实现的功能，它里面自带iter,next函数，并且自带异常判断


#正式运行程序
if __name__ == '__main__':
    ml = MyList()  #可迭代对象,ml
    ml.add(1)
    ml.add(2)
    ml.add(3)
    ml.add(4)
    ml.add(5)

    ml_iter = iter(ml)  #取出迭代器，会调用ml对象的__iter__方法，返回MyIterator(self)，也就是MyIterator(ml)
    #由于MyIterator是一个类，MyIterator(ml)会创建一个迭代器实例，并将原列表传入MyIterator的构造函数中
    print(next(ml_iter))  #开始手动迭代数值
    print(next(ml_iter))
    print(next(ml_iter))
    print(next(ml_iter))
    print(next(ml_iter))

print('*'*30)

for num in ml_iter:  # 迭代器因为在上面已经被next到底了，不能再用for遍历了
    print(num)

print('*'*30)

for num in ml: #
    print(num)

print('*'*30)

for num in ml: # for针对ml则没有问题，可以多次遍历
    print(num)

print(isinstance(ml,Iterable))  # True
print(isinstance(ml,Iterator))  # False, ml本身没有实现__next__方法，所以不是迭代器
print(isinstance(ml_iter,Iterable))  # True
print(isinstance(ml_iter,Iterator))  # True

'''
1
2
3
4
5
******************************
******************************
1
2
3
4
5
******************************
1
2
3
4
5
True
False
True
True
'''
