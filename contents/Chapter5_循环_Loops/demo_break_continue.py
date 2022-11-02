# Qingxiang Guo
# {2022/5/9} {15:15}
#流程控制语句break与continue在二重循环中的使用
for i in range(5):   #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:  #下面这个print(j)和if是平级的，是针对for j循环下面的打印
            break   #break会退出本循环，向上找最近的一个循环，也就是里面这个for循环
        print(j)   #print变量，默认是带换行的，这里会输出11111，因为每次2，里面循环都break重开了