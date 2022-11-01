# Qingxiang Guo
# {2022/7/4} {20:46}
class Faa(object):
    #斐波那契迭代器
    def __init__(self):
        #num1用来保存前前一个数，初始值为数列中的第一个数1
        #num2用来保存前一个数，初始值为数列中的第二个数
        self.num1 = 1
        self.num2 = 1

    def __next__(self):
        #被next()函数调用来获取下一个数
        temp_num = self.num1
        a=self.num1+self.num2
        self.num1, self.num2 = self.num2, a
        return temp_num

    def __iter__(self):
        #迭代器的__iter__返回自身即可
        return self

faa=Faa() #可迭代对象，又因为有__next__方法，所以也是迭代器
print(next(faa))
print(next(faa))
print(next(faa))
print(next(faa))
print(next(faa))  #1,1,2,3,5