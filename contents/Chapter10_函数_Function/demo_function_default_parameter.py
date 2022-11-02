# Qingxiang Guo
# {2022/5/19} {8:35}
#函数参数定义，默认值参数
def fun(a,b=10):   #b称为默认值参数
    print(a,b)

#函数的调用
fun(100)   #100,10,如果只有一个参数，b就默认
fun(20,30)   #如果两个参数，默认的10就被替代

print('hello',end='\t')    #这就是个例子，end默认值是'\n',现在替换为'\t'
print('world')