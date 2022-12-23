# _*_ coding=utf-8 _*_
# 下面是一个输出指定载具类型的需求，如果不在list里面就会报错，默认是没有载具
# 里面被修饰的假property属性是kind，但是如果在类里面使用self.kind就会引发死循环而报错
# 所以可以看到实际操作都使用self._kind来避免，实际上只是为了换一个储存空间，避免触发自我调用
# 实际上你换一个名字也行，比如return self._ABCD也可以
class Vehicle(object):
    def __init__(self):
        self._kind = "No vehicle"
        self.kinds_list = ["tank", "car", "motorbike", "bike", "quad" ]

    @property
    def kind(self):
        return self._kind  #获取载具类型

    @kind.setter
    def kind(self, x):  # 设定载具类型
        if x in self.kinds_list:  # 如果在list里面
            self._kind = x  # 改变载具类型
        else:
            raise ValueError('{0} is an illegal kind of vehicle!'.format(x))

v = Vehicle()
print(v.kind) # No vehicle
v.kind = "tank"
print(v.kind)  # tank
# v.kind = "airplane" 会报错，ValueError: airplane is an illegal kind of vehicle!