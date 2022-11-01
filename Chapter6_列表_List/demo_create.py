# Qingxiang Guo
# {2022/5/10} {17:03}
#列表生成式，利用循环，快速生成列表
lst=[i for i in range(1,10)]   #循环前面还要加一个i
print(lst)

'''生成一个自己乘自己的列表'''
lst2=[i*i for i in range(1,6)]
print(lst2)

'''生成一个2,4,6,8,10的列表'''
lst3=[i*2 for i in range(1,6)]
print(lst3)