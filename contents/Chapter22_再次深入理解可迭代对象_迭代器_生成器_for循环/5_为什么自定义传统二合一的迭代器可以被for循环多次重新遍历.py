'''这里展示自定义的可迭代对象，与，迭代器是怎么联系起来的
传统的二合一迭代器指的是自己实现__iter__，__next__方法，并在__iter__中return self
的，【迭代器就是我自己】的类型
'''

class MyList(object):
    def __init__(self):
        self.items=[]   # [1,2,3,4,5]
        self.current = 0

    def add(self,val):
        self.items.append(val)  #定义一个方法，将参数输入MyList对象的items列表

    def __iter__(self):
        return self  #The iterator is the iterable oject itself

    def __next__(self):
        if self.current < len(self.items):
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

print(next(ml_iter))  # 1
print(next(ml_iter))  # 2
print(next(ml_iter))  # 3
print(next(ml_iter))  # 4

print('运行第一次for循环')

for num in ml_iter:  # 这里ml其实也一样，ml_iter，ml两者是一样的
    print(num)

print('运行第二次for循环')
for num in ml_iter:
    print(num)

print('运行第三次for循环')
for num in ml_iter:
    print(num)

'''
1
2   # 可以看见for循环取值是接着next取值的，如果前面五个next把迭代器取完了的话，接下来的
3   # 第一次for循环就会直接运行self.current = 0，raise StopIteration，又因为for循环
4   # 自带异常处理，所以会和平退出，self.current归零，下一次可以继续使用for循环
运行第一次for循环
5
运行第二次for循环
1
2
3
4
5
运行第三次for循环
1
2
3
4
5
'''

'''
for循环自动捕获并处理StopIteration异常,也就实现了遍历完所有数据就会结束，
并不会抛出这个异常。而next()函数则不一样，会一直前进，遇到StopIteration异常会直接中止
也就不能多次重新遍历了。总结：next()只能前进不能后退，for循环可以有意识的捕捉StopIteration，
保证对迭代器的多次重复遍历。其实for循环就是为监听StopIteration而设计的，只要数字取到头的时候
给个StopIteration，for循环就知道是正常结束的信号，就会和平退出，以后还可以再重新用

此外，能够多次用for循环还有一个重要的原因，就是我们手动设置了self.current = 0归零
从头到尾用的都是同一个迭代器，否则迭代器从头走到尾，是单向的，就不能回头聊。而且这里为了for循环能够多次
遍历，必须要这么做。因为for循环的时候，其逻辑是先调用__iter__，获取迭代器，然后针对同一个迭代器，不断next
期间迭代器由于并没有被储存在另一个类当中（也就是分离版本的迭代器），因此无法实现self.current的自动归零
因此必须要手动归零

如果你是分离版本的迭代器，则不用设置self.current = 0归零，因为与传统二合一迭代器不同，
for i in a:的时候，a的__iter__()会return B(self.lst)也就是每次都会重新将迭代器类B实例化一次，
因而指针也就自动归零，也就是self.index = 0
'''