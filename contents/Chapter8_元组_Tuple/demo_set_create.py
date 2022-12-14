# Qingxiang Guo
# {2022/5/12} {13:28}
#集合的创建方式
'''第一种创建方式使用{}'''
s={2,3,4,5,6,7,7}  #集合中的元素不可重复
print(s)
'''第二种创建方式使用set()'''
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,4,5,5,6,6])  #可以将列表转集合
print(s2,type(s2))

s3=set((1,2,4,4,5,65))  #集合中的元素是无序的，可以将元组转集合
print(s3,type(s3))

s4=set('python')   #可以将字符串，转为集合，会拆开字母
print(s4,type(s4))

s5=set({12,4,34,55,66,44,4})   #可以将列表转列表
print(s5,type(s5))

#如何定义一个空集合呢？
s6={}   #默认花括号会生成一个空字典，此方法不行
print(type(s6))

s7=set()   #要这样创建空集合
print(type(s7))

