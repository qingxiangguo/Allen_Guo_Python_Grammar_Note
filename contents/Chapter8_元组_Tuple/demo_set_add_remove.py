# Qingxiang Guo
# {2022/5/12} {13:53}
#集合的相关操作
s={10,20,30,405,60}
'''集合元素的判断操作'''
print(10 in s)   #True
print(100 in s)   #False
print(10 not in s)    #False
print(100 not in s)   #True
'''集合元素的新增操作'''
s.add(80)   #注意，列表增加是append方法，都是往末尾加元素的，add一次添加一个元素
print(s)   #添加了80，但是是无序的，所以位置没什么意义
s.update({200,400,300})   #一次至少添加一个元素，可以以集合的方式加进去，列表中对应extend方法，实际上extend也可以以集合，元组。列表的方式，加入
s.update([100,99,8])   #可以以列表的方式，加入集合
s.update((78,64,56))   #可以以元组的方式，加入集合
print(s)

'''集合元素的删除操作'''
s.remove(100)
print(s)
s.discard(500)   #discard的好处是，就算没有，也不会报错
s.discard(300)
print(s)
s.pop()  #集合的pop()比较特殊，列表中pop()按位删除，比如list.pop(1)，但是集合无序，所以只能set.pop()，里面无参，否则报错
s.pop()
print(s)
s.clear()  #清空集合
print(s)
del s  #删除集合
