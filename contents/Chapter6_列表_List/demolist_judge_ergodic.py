# Qingxiang Guo
# {2022/5/9} {18:21}
#列表元素的判断与遍历
print('p' in 'python') #True
print('k' not in 'python') #True

lst=[10,20,'python','hello']
print(10 in lst)  #数字存在，True
print('10' in lst)  #但是字符串不存在，True，所以list中的类型是有效的
print(100 in lst)  #False
print(10 not in lst)  #False
print(100 not in lst)  #True

print('------list的遍历-----------')
for item in lst:
    print(item)
    print(id(item))  #可以看到列表中每个元素有自己独立的id和type
    print(type(item))