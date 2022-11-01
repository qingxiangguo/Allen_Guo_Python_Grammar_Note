# Qingxiang Guo
# {2022/5/8} {17:15}
#输出99乘法表
for i in range(1,10):
    for j in range(1, i+1):
        print(i,'*',j,'=', i*j, end='\t')
    print()   #默认print，起到手动换行的作用