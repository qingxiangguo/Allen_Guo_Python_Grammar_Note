# Qingxiang Guo
# {2022/5/11} {16:16}
#字典的特点
d={'name':'张三','name':'李四'}  #key不允许重复，前面的张三会被替换掉
print(d)

d={'name':'张三','Nickname':'张三'}  #value可以重复
print(d)

lst=[10,20,30]   #列表是有序的
lst.insert(1,100)   #[10, 100, 20, 30]，指定位置插入元素
print(lst)
d={lst:100}   #以lst为键，100为值，创建一个新的字典，但是不行，因为键是不能变的
print(d)
