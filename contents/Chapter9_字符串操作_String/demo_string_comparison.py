# Qingxiang Guo
# {2022/5/13} {21:08}
#字符串的比较操作

print('apple' > 'app')   #True，字符串比较时，符一般都是以ASCII码值的大小作为字符比较的标准
print(ord('a'),ord('b'))  #a为97，b为98，ord函数可以将字符转化为你所需要的ASCII码
print(ord('郭'))
print(chr(37101))  #chr函数可以将0-255中的任一整数转化为你所需要的字符

'''==与is的区别
==比较的是value
is比较的是id是否相等
'''
a=b='Python'
c='Python'
print(a==b)  #True
print(b==c)  #True
print(a is b)  #True
print(a is c)  #True,pyCharm做了优化，涉及到字符串驻留机制