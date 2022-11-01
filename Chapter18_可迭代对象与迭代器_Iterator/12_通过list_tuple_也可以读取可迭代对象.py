# Qingxiang Guo
# {2022/7/1} {16:28}
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
        return self  #

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

nums=list(ml)  #list在创建一个新列表的时候，只要是可迭代对象，就可以放到list中当实参
print(nums)  #[1, 2, 3, 4, 5]

nums2=tuple(ml)
print(nums2)  #(1, 2, 3, 4, 5)

aa = iter(ml)
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))  # raise StopIteration #抛出异常，和平结束

'''
1
2
3   当一个对象，即是可迭代对象对象，同时也是迭代器的时候，next可以同时作用于这个对象本身和其迭代器
因为这个时候，这个对象就是迭代器
'''
