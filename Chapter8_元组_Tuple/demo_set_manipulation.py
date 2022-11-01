# Qingxiang Guo
# {2022/5/12} {15:30}
#集合的数学操作，交集补集等
#交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)   #与上面的写法等价，结果为{40, 20, 30}
'''如果想求两个列表的交集呢？需要将两个列表先转换为集合'''
list1=[1,2,3]
list2=[3,4,5]
print(set(list1).intersection(list2))
print(set(list1) & set(list2))

#并集
print(s1.union(s2))
print(s1|s2)  #与上面的写法等价，结果为{40, 10, 50, 20, 60, 30}

#差集
print(s1.difference(s2))
print(s1-s2)  #与上面的写法等价，结果为{10}

#对称差集，为各自差集的补集
print(s1.symmetric_difference(s2))
print(s1^s2)   #与上面的写法等价，结果为{50, 10, 60}

