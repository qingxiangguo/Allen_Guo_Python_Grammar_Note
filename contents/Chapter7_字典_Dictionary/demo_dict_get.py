# Qingxiang Guo
# {2022/5/11} {11:29}
#字典元素的获取，这些方法都只能同时获得一个键的值
scores={'张三':100,'李四':98,'王五':45}
'''第一种获取方式'''
print(scores['张三'])  #输出100

'''第二种方式，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六'))  #None，get()不会报错，而中括号方法会报错

