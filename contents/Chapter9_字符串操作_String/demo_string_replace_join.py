# Qingxiang Guo
# {2022/5/13} {16:51}
#字符串的常用操作，替换与合并
s='hello,Python'
print(s.replace('Python','Java'))

s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))  #换两次hello,Java,Java,Python

#下面是join方法，方法用于将序列中的元素以指定的字符连接生成一个新的字符串，其连接的对象是可迭代对象
#python里面可迭代对象有列表，元组，字典，集合，字符串，所以join对象也是这些
#下面是join列表的例子
lst=['hello','java','Python']
print('|'.join(lst))   #hello|java|Python
print(''.join(lst))  #hellojavaPython
#下面是join元组的例子
t=('hello','Java','Python')
print(''.join(t))
#下面是join字典的例子
d={'a':100,'b':100,'c':100}   #a|b|c，由于python3.6后，字典变为有序，因此不会出现下面join集合里面的情况
print('|'.join(d))
#下面是join集合的例子
s={'a','b','c'}
print('|'.join(s))  #但是由于集合是无序的，会随机输出b|a|c，a|c|b等
#下面是join字符串的例子
print('*'.join('Python'))  #P*y*t*h*o*n，会把字符串拆开当成序列来处理



