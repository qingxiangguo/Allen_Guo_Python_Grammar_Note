# Qingxiang Guo
# {2022/5/6} {15:24}
#测试对象的布尔值，python一切皆对象
print(bool(False))  #False
print(bool(0))       #False
print(bool(0.0))     #False
print(bool(None))     #False
print(bool(''''''))   #长度为0的空字符串也是False
print(bool(''))
print(bool([]))   #空列表
print(bool(list()))   #空列表
print(bool(()))  #空元组
print(bool(tuple()))  #空元组
print(bool({}))  #空字典
print(bool(dict()))  #空字典
print(bool(set()))  #空集合

print('------------其他对象的布尔值均为True---------')
print(bool(18))
print(bool(True))
print(bool('Helloworld'))
