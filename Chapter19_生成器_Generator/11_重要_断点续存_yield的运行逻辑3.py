# Qingxiang Guo
# {2022/7/5} {0:35}
def consumer():
    r = 0
    for i in range(3):
        xx=yield r
        print(str(r) +'\t'+ str(i))
        print(xx)


c = consumer()

print(c.send(None))  #输出0，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的
print('----')   #send(None)就相当于正常的next()
print(c.send(222))
print('----')
print(c.send(333))   #send只有xx = yield yy的时候生效，send（）的作用是使xx赋值为发送的值（send的参数）,然后让生成器执行到下个yield..
#send只立即生效一次，是临时传入

#以上结果为
'''
0    #首先r一直是0，第一次运行,yield r作为返回值，所以输出0
----
0	0  #第二次，接着运行，输出0	0，然后222是即时传入的，所以输出222，这里打断了原来的r。然后回到r，r还是0
222
0   #为什么这里会输出一个0呢，因为xx=yield r，产生r，而r就是0，会作为返回值
----
0	1  #第三次，接着运行，输出0	1，然后3是即时传入的，所以输出333，然后回到r，r还是0
333
0
'''