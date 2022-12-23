# Qingxiang Guo
# {2022/7/1} {15:36}
'''这里展示自定义的可迭代对象，与，迭代器是怎么联系起来的
传统的二合一迭代器指的是自己实现__iter__，__next__方法，并在__iter__中return self
的，【迭代器就是我自己】的类型
'''

class MyList(object):
    '''自定义的一个可迭代对象'''
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

for num in ml_iter:
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

