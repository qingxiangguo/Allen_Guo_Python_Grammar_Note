# Qingxiang Guo
# {2022/5/3} {23:32}
# 比较运算符的结果为Bool类型
a,b=10,20
print('a>b吗?', a>b)  # False
print('a<b吗?', a<b)  # True

print('a<=b吗?', a<=b)  # True
print('a>=b吗?', a>=b)  # False
print('a==b吗?', a==b)  # False
print('a=!b吗?', a!=b)  # True

'''一个=为赋值运算符，==称为比较运算符
一个变量由三部分组成，标识，类型，值，==比较的是值还是标识呢？答案是值
比较对象的标识是is
'''
a=10
b=10
print(a==b)  #True，说明a与b的value相等
print(a is b)  #True，说明a与b的id标识也相等，电脑为了节省内存，既然都是10，就使用同一个标识
#以下代码没学过，后面会跟大家讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)  #value, True
print(lst1 is lst2)  #id, False  #所以列表和变量id分配的机制还不太一样，因为列表是可变的
print(id(lst1), id(lst2))
print(a is not b)  #False
print(lst1 is not lst2) #True



