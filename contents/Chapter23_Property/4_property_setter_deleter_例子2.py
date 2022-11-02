# _*_ coding=utf-8 _*_
class Timer(object):
    def __init__(self, value = 0.0):
        self._time = value
        self._unit = 's'

    @property
    def time(self):  #获取time假属性时会调用此方法
        return str(self._time) + '' + self._unit  #返回时间和单位

    @time.setter  #对属性进行设置
    def time(self, value):  #相当于对上面方法的一个补充方法
        if (value < 0):  # 实现对输入的数据的判断、控制和操作
            raise ValueError('Time cannot be negative')
        self._time = value

t = Timer()
a = t.time #会自动调用def time(self):
print(a)
t.time = 1.0  #会自动调用@time.setter
print(t.time)

'''
0.0s
1.0s
'''