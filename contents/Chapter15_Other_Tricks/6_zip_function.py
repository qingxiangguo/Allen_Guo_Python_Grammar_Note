# Qingxiang Guo
# {2022/6/20} {20:25}
'''zip,也就是打包，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
python3中，zip()函数返回的是一对象（迭代器）。需要用 list()或tuple()把这个对象转成列表或元组
'''

#例子一
a = ['a', 'b', 'c', 'd']
b = ['1', '2', '3', '4']
print(zip(a,b))  #<zip object at 0x0000022FFDB80B40>，是一个迭代器
print(list(zip(a,b)))  #[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]，是一个个元组组成的列表

#例子二，你正在处理一些学生的成绩，有这样两个列表
#你想对它们进行排序，又不想破坏对应关系的话，就可以这样
names = ['John', 'Amy', 'Jack']
scores = [98, 100, 85]  # 分数和名字是一一对应的
data = list(zip(names, scores))
print(data)  #[('John', 98), ('Amy', 100), ('Jack', 85)]
data.sort()  #直接用了就排序了，属于sort方法
print(data)   #[('Amy', 100), ('Jack', 85), ('John', 98)]

a1, b1 = zip(*zip(a,b))  #与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(a1)  #('a', 'b', 'c', 'd'),zip总是返回元组
print(list(a1))  #['a', 'b', 'c', 'd']，转换为列表
print(b1)  #('1', '2', '3', '4'),zip总是返回元组
print(list(b1))  #['1', '2', '3', '4']，转换为列表
