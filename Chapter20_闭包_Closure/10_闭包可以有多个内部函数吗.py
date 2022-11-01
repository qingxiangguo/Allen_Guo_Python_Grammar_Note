# Qingxiang Guo
# {2022/7/9} {16:25}
#闭包内部可以包括多个函数吗？可以，但没必要。
def line_conf(a,b):
    def line1(x):
        return a*x+b

    def line2(x):
        return 2*a*x+b

    return line1,line2  #返回的是一个元组

l=line_conf(1,2)  #l是一个元组。包括line1，line2函数的引用

print(l)  #输出(<function line_conf.<locals>.line1 at 0x00000264E23DEC20>, <function line_conf.<locals>.line2 at 0x00000264E23DECB0>)

print(l[0](5))  #7   元组取序号，调用的是line1
print(l[1](5))  #12  元组取序号，调用的是line2


