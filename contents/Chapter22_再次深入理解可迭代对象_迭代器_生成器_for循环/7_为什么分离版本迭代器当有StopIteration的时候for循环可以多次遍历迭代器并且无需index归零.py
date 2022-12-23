# _*_ coding=utf-8 _*_
'''
经常容易混淆的就是，有的时候for循环对于某些迭代器对象可以实现多次遍历
有的时候对迭代器对象只能一次性，到底是什么原因造成了这个差别呢？
其实，迭代器正常情况就是只能被遍历第一次的，是单向不能回头的，但是因为
有些时候，一些迭代器使用了特殊的技巧，实现了for循环可以多次遍历，比如：
(1）在传统二合一的迭代器中，使用了手动归零指针self.current = 0
(2) 在分离版本迭代器中， 巧妙的将可迭代对象类A，与迭代器类B分开，利用每一次循环A
的时候，都会调用A的__iter__函数，并重新实例化迭代器类B，从而实现指针自动归零
从而完成了for循环可以多次遍历


'''
class A():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        print('A.__iter__()方法被调用')
        return B(self.lst)  # 将B类实例化

class B():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        print('B.__iter__()方法被调用')
        return self  # B本身是一个迭代器

    def __next__(self):
        if self.index < len(self.lst):
            print('B.__next__()方法被调用')
            value = self.lst[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


        #except IndexError:
         #   raise StopIteration

# 接下来，我们用for循环遍历一下A类实例
a = A([1, 2, 3])

for i in a:
    print('for 循环取出的值', i)

print('-'*30)

for k in a:
    print('for 循环取出的值', k)

print('-'*30)

for n in a:
    print('for 循环取出的值', n)

'''

A.__iter__()方法被调用
B.__next__()方法被调用
for 循环取出的值 1
B.__next__()方法被调用
for 循环取出的值 2
B.__next__()方法被调用
for 循环取出的值 3
B.__next__()方法被调用
------------------------------
A.__iter__()方法被调用
B.__next__()方法被调用
for 循环取出的值 1
B.__next__()方法被调用
for 循环取出的值 2
B.__next__()方法被调用
for 循环取出的值 3
B.__next__()方法被调用
------------------------------
A.__iter__()方法被调用
B.__next__()方法被调用
for 循环取出的值 1
B.__next__()方法被调用
for 循环取出的值 2
B.__next__()方法被调用
for 循环取出的值 3
B.__next__()方法被调用

'''

'''
通过for循环对一个可迭代对象进行迭代时，for循环内部机制会自动通过调用iter()方法执行
可迭代对象内部定义的__iter__()方法来获取一个迭代器，然后一次又一次得迭代过程中通过
调用next()方法执行迭代器内部定义的__next__()方法获取下一个元素，当没有下一个元素时
，for循环自动捕获并处理StopIteration异常,也就实现了遍历完所有数据就会结束，
并不会抛出这个异常。而next()函数则不一样，会一直前进，遇到StopIteration异常会直接中止
也就不能多次重新遍历了。

总结：next()只能前进不能后退，for循环可以有意识的捕捉StopIteration，
保证对迭代器的多次重复遍历
'''

b = B([1, 2, 3])

print('-'*30)
for i in b:
    print('for 循环取出的b中值', i)  # 可以取出来

print('-'*30)

for i in b:
    print('for 循环取出的b中值', i)  #无法取出来

'''
此外，在传统二合一迭代器中，能够多次用for循环还有一个重要的原因，就是我们手动设置了self.current = 0归零
从头到尾用的都是同一个迭代器，否则迭代器从头走到尾，是单向的，就不能回头聊，但是在本例子中的
分离迭代器中，就算没有self.index = 0，也可以实现for来反复循环a，这是为什么呢？

这是因为与传统二合一迭代器不同，for i in a:的时候，a的__iter__()会return B(self.lst)
也就是每次都会重新将B实例化一次，因而指针也就自动归零，也就是self.index = 0

怎么验证这一点呢？我们直接对b进行实例化，然后用for来取b，由于没有每次都实例化的过程，指针无法借由归零
因此b就不能被for循环多次遍历了
'''

