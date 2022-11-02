# _*_ coding=utf-8 _*_
# 以植物大战僵尸为例子，向日葵每次增加阳光数必须是50，而不能是别的数字
# property的本质，也是属性拦截，方便对属性进行暗箱操作
class Zomebie(object):
    def __init__(self):
        self._sun = 0

    @property
    def sun(self):
        print('获取sun')
        return self._sun # 这个_sun在外面也是获取不了的

    @sun.setter
    def sun(self, value):
        print('设置sun')
        if value == 50:
            self._sun += value
        else:
            print("输入必须是50")

z = Zomebie()
print("*"*30)
print(z.sun)
print("*"*30)
z.sun += 50  # 因为相当于 z.sun = z.sun + 50，所以会先触发get，再触发set
print("*"*30)
print(z.sun)
print("*"*30)
z.sun += 100
print("*"*30)
print(z.sun)

'''
******************************
获取sun
0
******************************
获取sun
设置sun
******************************
获取sun
50
******************************
获取sun
设置sun
输入必须是50
******************************
获取sun
50
'''

