# Qingxiang Guo
# {2022/7/4} {20:10}
class PointXY(object):
    def __init__(self):
        self.x=0
        self.k=2
        self.b=1

    def __iter__(self):
        return self

    def __next__(self):  #一看就是迭代器
        temp_y = self.k * self.x + self.b
        temp_point_x_y=(self.x, temp_y)
        self.x= temp_y
        return temp_point_x_y

    def change_k_b(self, k, b):  #专门增加一个方法，来修改k或b的值
        self.k=k
        self.b=b

point_x_y=PointXY()  #创建一个可迭代对象
point_x_y_iter=iter(point_x_y)  #取出可迭代器

print(next(point_x_y_iter))  #(0, 1)

print(next(point_x_y_iter))  #(1, 3)

print(next(point_x_y_iter))   #(3, 7)

#调用point_x_y这个对象的change_k_b方法，来修改k，b的值
point_x_y.change_k_b(3,2)

print(next(point_x_y_iter))  #(7, 23)
#k和b就这样修改掉了，但是这种方法还是不够优雅，下面引入生成器的方式
