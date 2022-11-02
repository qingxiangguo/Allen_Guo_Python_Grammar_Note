# Qingxiang Guo
# {2022/5/11} {16:42}
#字典生成式
items=['fruit','books','others']
prices=[96,78,85]

d={i.upper():j for i,j in zip(items, prices)}  #i.upper()是利用方法，将其大写
# zip函数将可迭代对象作为参数，将对应元素打包成一个元组，然后返回由这些元组组成的列表
print(d)  #生成了新字典{'FRUIT': 96, 'BOOKS': 78, 'OTHERS': 85}

print(zip(items, prices)) #返回一个zip对象，因为节省内存

print(list(zip(items, prices)))  #使用list展开后，可以看到元组组成的列表，[('fruit', 96), ('books', 78), ('others', 85)]，list展开和range()有点像