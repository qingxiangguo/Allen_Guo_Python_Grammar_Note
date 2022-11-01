# Qingxiang Guo
# {2022/7/4} {19:57}
#通过迭代器，下面要生成不确定个数的坐标
class PointXY(object):
    def __init__(self):
        self.x=0

    def __iter__(self):
        return self

    def __next__(self):
        temp_y = 2*self.x + 1
        temp_point_x_y=(self.x, temp_y)
        self.x= temp_y
        return temp_point_x_y

point_x_y=PointXY()  #创建一个可迭代对象
point_x_y_iter=iter(point_x_y)  #取出可迭代器

print(next(point_x_y_iter))  #(0, 1)

print(next(point_x_y_iter))  #(1, 3)
#这样可以想取多少取多少
#但是如果在未知次，可能要修改方程式k和b的系数值呢？