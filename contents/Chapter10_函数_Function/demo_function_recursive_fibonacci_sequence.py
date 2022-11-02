# Qingxiang Guo
# {2022/5/22} {17:02}
#利用递归，写一个函数，计算斐波那契数列第X位的数字
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        res=fib(n-1) + fib(n-2)
        return res

print(fib(7))  #8，第六位的数字

#如果依次输出前6位的数字

for i in range(1,7):
    print(fib(i), end='\t')

