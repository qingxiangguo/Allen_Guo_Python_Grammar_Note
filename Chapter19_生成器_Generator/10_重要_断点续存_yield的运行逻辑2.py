# Qingxiang Guo
# {2022/7/5} {0:21}
def consumer():
    r = 0
    for i in range(3):
        print('--mark--')
        yield r  # 只要创建yield关键字后，自动加__iter__和__next__方法
        r = '200 OK'+ str(i)

c = consumer()

print(c)  #<generator object consumer at 0x0000028925AE9A10>，是一个生成器对象

print(next(c))  #0   结束的时候 i=0
print('************')
print(next(c))  #200 ok0   结束的时候 i=1
print('************')
print(next(c))  #200 ok1  结束的时候 i=2
print('************')
#print(next(c))  #i=3，不会进入循环，next找不到yield，从而保存

#输出如下
'''
--mark--
0
************
--mark--
200 OK0
************
--mark--
200 OK1
************

'''