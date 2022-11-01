# Qingxiang Guo
# {2022/5/9} {20:58}
#列表元素的添加操作，append,extend,insert,和利用切片操作元素，切片元素主要难点在索引
lst1=[10,20,30]
print('添加元素之前的lst1',lst1,id(lst1))
lst1.append(100)
print('添加元素之后的lst1',lst1,id(lst1))
lst2=['hello','world']
lst1.append(lst2)   #append只会添加一个元素，会将一个列表作为一个整体添加
print(lst1)
lst1.extend(lst2)
print(lst1)   #extend会将列表元素拆开，添加多个元素到末尾
#在任意位置上添加一个元素
lst1.insert(1,90)  #在索引1位添加90
print(lst1)
lst1.insert(1,'90')   #也可以添加字符串模式
print(lst1)
lst1.insert(1,lst2)  #在索引1位添加一整个列表，但是和append一样，只会将新列表作为一个整体加末尾
print(lst1)
#那么怎么在列表的任意位置上添加多个元素呢？使用切片操作！
lst3=[True,False,'haha']
#此时lst1为[10, ['hello', 'world'], '90', 90, 20, 30, 100, ['hello', 'world'], 'hello', 'world']
lst1[1:]=lst3   #将新的lst3，赋值到lst1的一个索引区间内，1:，相当于1:10:1的缩写,这个区间也是左闭右开的
print(lst1)
#最后结果为[10, True, False, 'haha']