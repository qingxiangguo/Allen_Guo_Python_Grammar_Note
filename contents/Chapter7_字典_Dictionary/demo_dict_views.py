# Qingxiang Guo
# {2022/5/11} {14:43}
#获取字典视图
scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys)  #结果里面有个列表
print(type(keys))
print(list(keys))   #展开为一个列表，['张三', '李四', '王五']

#获取所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values))  #[100, 98, 45]

#获取所有的key-value对
items=scores.items()
print(items)
print(list(items))  #[('张三', 100), ('李四', 98), ('王五', 45)]，其中('张三', 100)是一个元组

print(list(scores))  #如果直接list整个字典，只输出key，效果和print(list(keys))一样

