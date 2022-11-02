# Qingxiang Guo
# {2022/6/24} {12:01}
'''写一个迷你计算器'''
def calc(a,b,op):
    if op=='+':
        return add(a,b)
    elif op=='-':
        return sub(a,b)
    elif op=='*':
        return mul(a,b)
    elif op=='/':
        if b!=0:
            return div(a,b)
        else:
            print('除数不能为0')

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__=='__main__':
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    op=input('运算符')
    print(calc(a,b,op))  #除数为01，上面只是打印，没有返回值，所以这个print会打印出none

'''
请输入第一个整数10
请输入第二个整数0
运算符/
除数不能为0
None
'''