# Qingxiang Guo
# {2022/4/30} {16:47}
a=3.14159
print(a, type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)  #小数点会不精确，因为计算机是二进制处理的
print(n1+n3) #但是有的时候又没问题
from decimal import Decimal  #使用包来解决
print(Decimal('1.1')+Decimal('2.2'))