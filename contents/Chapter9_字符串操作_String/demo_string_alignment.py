# Qingxiang Guo
# {2022/5/12} {22:04}
#字符串常用操作之内容对齐方法
s='hello,Python'
'''居中对齐'''
print(s.center(20,'*'))  #输出****hello,Python****，两个参数，总字符串长度，和填充用字符，默认空格

'''左对齐'''
print(s.ljust(20,'*')) #输出hello,Python********，其他同居中对齐
print(s.ljust(10))  #如果占位小于字符本身，就输出字符本身
print(s.ljust(20))  #输出hello,Python

'''右对齐'''
print(s.rjust(20,'*'))  #同上
print(s.rjust(20))
print(s.rjust(10))

'''也是右对齐，但是使用0进行填充，只有一个占位的参数'''
print(s.zfill(20))  #00000000hello,Python
print(s.zfill(10))
print('-8910'.zfill(8))  #会输出-0008910，加号减号比较特殊，0填充的时候，运算符会保证在前面