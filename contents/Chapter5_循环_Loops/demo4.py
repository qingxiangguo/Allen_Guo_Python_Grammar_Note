# Qingxiang Guo
# {2022/5/7} {21:38}
# for in 循环
for item in 'Python':  #第一次取出P，将P赋值给item，将item的值输出，Python字符串，属于可迭代对象
    print(item)

#range()也产生了一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环中不需要使用自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用python')

print('使用for循环，计算1到100之间的偶数和')

summary=0
for number in range(101):
    if not number%2:
        summary+=number
print('1到100之间的偶数和',summary)


