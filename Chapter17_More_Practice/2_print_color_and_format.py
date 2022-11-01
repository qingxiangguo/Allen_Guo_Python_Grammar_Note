# Qingxiang Guo
# {2022/6/21} {9:49}
'''这里练习颜色输出字符串和格式化输出字符串'''
#首先在终端输出颜色
print('\033[0;35;42mhello world')
#格式为\033+方括号，0是默认终端输出，35是前景色，42m是后景色

#其次是格式化输出字符串
height=170
weight=50.5
bmi=weight/(weight+height)
print('您的身高是'+str(height))  #您的身高是170
print('您的bmi是{0:0.2f}'.format(bmi))  #您的bmi是0.23

#预测未来子女身高
farther_height=int(input('fathers height'))
mother_height=int(input('mothers height'))
son_height=(farther_height+mother_height)*0.54
print('Sons height is {0}'.format(son_height))