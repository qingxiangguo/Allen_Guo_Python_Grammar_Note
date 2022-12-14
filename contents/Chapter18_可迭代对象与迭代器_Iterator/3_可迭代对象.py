# Qingxiang Guo
# {2022/6/30} {17:11}
#可迭代对象，只要是能使用for循环遍历的，都是
for x in [55,77]:
    print(x)

print('*'*3)

for x in 'abcdef':
    print(x)

print('*'*3)

for x in (33,44,55):
    print(x)

print('*'*3)

for x in {33:44, 55:66}:  #字典也可以，会取键
    print(x)

#for x in {33:44,{99:88}:66}:  #字典是可变对象，不能作为键，键只能是不可变对象
#    print(x)

#输出
'''
55
77
***
a
b
c
d
e
f
***
33
44
55
***
33
55
'''

'''
迭代器是一个可以记住遍历的位置的对象，迭代器对象从第一个元素开始访问，直到所有的元素访问结束。
可迭代对象的本质：在迭代过程中，有一个人去记录每次访问到了第几条数据，我们把这个人称为迭代器。
可迭代对象的本质，就是可以向我们提供这样一个中间人。
list,tuple等都是可迭代对象，可以用过iter()获取这些可迭代对象的迭代器。
然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。
'''