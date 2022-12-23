# Qingxiang Guo
# {2022/7/9} {12:35}
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

l1=line_conf(1,1)  #创建一个闭包，分别赋值给a,b
l2=line_conf(4,5)  #创建另一个闭包，分别赋值给a,b

print(l1(5))  #6
print(l2(5))  #25
#闭包有提高代码可用性的作用
