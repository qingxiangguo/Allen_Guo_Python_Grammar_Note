# Qingxiang Guo
# {2022/7/5} {1:11}
'''
除了使用【next】函数可以启动生成器，还可以使用【send】函数启动
相同：都会让生成器继续往下运行
不同：send除了继续运行，还可以传值给xx = yield a中的xx
并且send用在第一次时，必须send（None）启动，
'''

def create_num(n):
    a, b = 0, 1
    i= 0
    while i < n:
        ret = yield a  # 就是说print(next())只会把yield a后面的内容打印出来
        print("ret的值为：{}".format(ret))
        a, b = b, a+b
        i += 1
    return "-----ok-----"

obj=create_num(10)
#print(obj.send(88877))  #第一次这样会报错，send不能作为开头，传非none值
#print(obj.send(None))   #强行想用send开头，而不是next开头的话，send里面传none，和next(obj)效果一样
print('---------')
print(next(obj))
print('---------')
print(next(obj))
print('---------')
print(next(obj))
print('---------')
print(next(obj))
print('---------')
print(obj.send(88888))
print('---------')
print(obj.send(99999))

'''
0
---------
ret的值为：None
1
---------
ret的值为：None
1
---------
ret的值为：None
2
---------
ret的值为：88888  #send只会把值传给xx =  yield a中的，xx
3
---------
ret的值为：99999
5
'''