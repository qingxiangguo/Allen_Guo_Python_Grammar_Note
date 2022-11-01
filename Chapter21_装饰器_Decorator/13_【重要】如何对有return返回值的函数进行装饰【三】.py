# Qingxiang Guo
# {2022/7/17} {21:59}
#再举一个装饰有返回值函数的例子
import time

def timer(func):
    def deco(*args,**kwargs):
        start=time.time()  #当前时间戳
        res=func(*args,**kwargs)  #执行原函数，并将返回值给res
        stop=time.time()  #结束时间
        print(stop-start)
        return res #返回原函数的返回值
    return deco

@timer
def test():
    time.sleep(2)  #延迟两秒
    print('test is running')
    return 'Returned value'

test()  #test=timer(test)

#test()变成了deco，func保留了原test
#会运行原test
#暂停两秒，打印test is running
#返回Returned value'并给res，并不输出
#然后打印stop-start
#然后返回res，也就是Returned value
print('----------------')
print(test())

'''
test is running
2.010399580001831
----------------
test is running   #函数作为实参输入给print时，函数本身会再调用一遍
2.019897699356079
Returned value
'''



