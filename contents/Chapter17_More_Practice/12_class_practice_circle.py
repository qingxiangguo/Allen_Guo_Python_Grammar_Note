# Qingxiang Guo
# {2022/6/24} {16:02}
'''写一个类，计算圆的周长与面积'''
import math

class Circle(object):
    def __init__(self, r):
        self.r=r

    def get_area(self):
        return math.pi*math.pow(self.r,2)  #圆的面积
    def get_perimeter(self):
        return 2*math.pi*self.r  #圆的周长

if __name__ == '__main__':
    r=int(input('请输入圆的半径'))
    c=Circle(r)  #实例化一个对象c
    print('面积为{:.2f}'.format(c.get_area()))
    print('周长为{:.2f}'.format(c.get_perimeter()))

'''
请输入圆的半径5
面积为78.54
周长为31.42
'''