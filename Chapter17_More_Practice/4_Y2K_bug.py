# Qingxiang Guo
# {2022/6/22} {11:25}
'''千年虫，指的是1989,89可以直接加19，但是00会被识别为0，所以2000就会有问题'''
year=[82,83,87,00,92,81]
print('原列表',year)
for index,value in enumerate(year):  #会将列表中的序号和值对应起来
    print(index,value)    #index，value只是两个值，修改value不能修改原列表
    if str(value)!='0':  #如果字符串化的值不等于0
        year[index]=int('19'+str(value))  #如果尾号其他，前面加19，修改的时候，一定要在原列表修改
    else:
        year[index]=int('200'+str(value))  #如果尾号是00，会被识别为0，所以前面要加200

print('修改之后的列表',year)
year.sort()
print('排序之后的列表',year)

'''
输出结果为：
原列表 [82, 83, 87, 0, 92, 81]
0 82
1 83
2 87
3 0
4 92
5 81
修改之后的列表 [1982, 1983, 1987, 2000, 1992, 1981]
排序之后的列表 [1981, 1982, 1983, 1987, 1992, 2000]
'''


