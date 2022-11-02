# Qingxiang Guo
# {2022/5/9} {17:13}
#获取指定元素的指引
lst=['hello','world',98,'hello']  #索引分别为0,1,2,3,反过来是-1,-2
print(lst.index('hello'))  #如果列表中有相同元素，只返回第一个元素的索引
print(lst.index('hello',1,4))  #相当于在1,2,3索引里面，找hello的索引，左闭右开
print(lst.index('hello',-1))  #在倒数第一个位置，找hello