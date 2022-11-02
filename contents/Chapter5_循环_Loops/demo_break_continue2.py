# Qingxiang Guo
# {2022/5/9} {15:15}
#流程控制语句break与continue在二重循环中的使用
for i in range(5):   #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:  #下面这个print(j)和if是平级的，是针对for j循环下面的打印
            continue   #continue返回到最近的一个循环，本循环，也就是第二个for循环，起到的是一个跳过的作用
        print(j,end='\t')   #print变量，默认是带换行的，这里会输出1,3,5,7,9五次，因为偶数都被continue略过了
    print()