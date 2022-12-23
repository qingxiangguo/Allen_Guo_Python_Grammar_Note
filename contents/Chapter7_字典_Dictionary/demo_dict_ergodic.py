# Qingxiang Guo
# {2022/5/11} {14:54}
#字典元素的遍历
scores={'张三':100,'李四':98,'王五':45}
#字典元素的遍历
for a in scores:
    print(a, scores[a], scores.get(a))  #会输出，键，值，值，后面是获取值的两种方法
