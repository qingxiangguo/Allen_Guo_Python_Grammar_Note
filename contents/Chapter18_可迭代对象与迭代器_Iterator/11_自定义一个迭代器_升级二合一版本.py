# Qingxiang Guo
# {2022/7/1} {15:36}
from collections.abc import Iterable  #用来判断一个对象是否是可迭代对象
from collections.abc import Iterator  #用来判断一个对象是否是可迭代器

'''这里展示自定义的可迭代对象，与，迭代器是怎么联系起来的'''
class MyList(object):
    '''自定义的一个可迭代对象'''
    def __init__(self):
        self.items=[]   # [1,2,3,4,5]
        self.current = 0

    def add(self,val):
        self.items.append(val)  #定义一个方法，将参数输入MyList对象的items列表

    def __iter__(self):
        #这个方法有两个功能
        #1，标记当前类创建出来的对象，一定是可迭代对象
        #2，到调用iter函数时，这个方法会被调用，返回相应的迭代器
        return self  #The iterator is the iterable oject itself
        #为什么返回自己呢？因为一般情况下，把可迭代对象和迭代器二合一了，省得再另外写一个单独实现nexr的迭代器类，所以这里的迭代器就是实例化对象自己

    def __next__(self):
        if self.current < len(self.items):  ##将上面那个可迭代对象的引用，与本迭代器的self.mylist属性连接，使得self.mylist.items可以访问上面的列表
            item = self.items[self.current]
            self.current += 1
            return item
        else:
            self.current = 0  #必须要这样，才能保证能够多次使用
            raise StopIteration #抛出异常，和平结束

#正式运行程序

ml = MyList()  #可迭代对象,ml
ml.add(1)
ml.add(2)
ml.add(3)
ml.add(4)
ml.add(5)

ml_iter = iter(ml)  #取出迭代器

print(ml_iter is ml)  # True 迭代器就是可迭代对象自己

print(next(ml_iter))  #开始手动迭代数值
print(next(ml_iter))
print(next(ml_iter))
print(next(ml_iter))
print(next(ml_iter))  # 当一个对象，即是可迭代对象对象，同时也是迭代器的时候，
# next可以同时作用于这个对象本身和其迭代器,因为这个时候，这个对象就是迭代器
#如果手动触发，最后一次self.current没有归零，所以下一次用for的时候，会直接运行else，结束循环

print("*"*30)

for num in ml_iter:   # 为什么这里输出的1，2，3，4，5会比遍历次数要少一次呢？见【深入理解可迭代对象_迭代器_生成器】
    print(num)

for num in ml_iter:
    print(num)

for num in ml_iter:
    print(num)

print("*"*30)

'''
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
1
2
3
4
5
******************************
True
True
'''

print(isinstance(ml,Iterable))  # True
print(isinstance(ml,Iterator))  # True, ml因为同时有__iter__和__next__方法，所以他同时自己也是迭代器，在__iter__里面返回的迭代器也就是自己