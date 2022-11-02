# Qingxiang Guo
# {2022/5/11} {11:43}
#字典元素的增删改操作
'''key的判断'''
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']  #删除指定键值对
print(scores)
scores.clear()
print(scores) #清空字典的元素
scores['陈六']=98  #新增元素，类似变量赋值
print(scores)

scores['陈六']=100  #修改元素
print(scores)