# Qingxiang Guo
# {2022/7/17} {21:59}
#�پ�һ��װ���з���ֵ����������
import time

def timer(func):
    def deco(*args,**kwargs):
        start=time.time()  #��ǰʱ���
        res=func(*args,**kwargs)  #ִ��ԭ��������������ֵ��res
        stop=time.time()  #����ʱ��
        print(stop-start)
        return res #����ԭ�����ķ���ֵ
    return deco

@timer
def test():
    time.sleep(2)  #�ӳ�����
    print('test is running')
    return 'Returned value'

test()  #test=timer(test)

#test()�����deco��func������ԭtest
#������ԭtest
#��ͣ���룬��ӡtest is running
#����Returned value'����res���������
#Ȼ���ӡstop-start
#Ȼ�󷵻�res��Ҳ����Returned value
print('----------------')
print(test())

'''
test is running
2.010399580001831
----------------
test is running   #������Ϊʵ�������printʱ������������ٵ���һ��
2.019897699356079
Returned value
'''



