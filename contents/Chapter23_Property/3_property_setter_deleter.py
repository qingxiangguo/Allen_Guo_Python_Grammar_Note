# _*_ coding=utf-8 _*_
class Goods(object):
    @property  # 获取price属性的时候会自动调用此方法
    def price(self):
        print('@property')

    @price.setter  #price属性赋值的时候会自动调用此方法
    def price(self, value):
        print("@price.setter")

    @price.deleter  #删除price属性的时候会自动调用此方法
    def price(self):
        print("@price.deleter")

obj = Goods()
obj.price
obj.price = 100
del obj.price

'''
@property
@price.setter
@price.deleter
'''

'''
注意点：在Good类中，想使用@price.setter和@price.deleter功能的话，
@propery一定要在最前面。并且@XXX.deleter中的XXX要与被装饰的函数名一致
这个用法的意义是，给予了赋值并返回值的过程中，一些可以操作的空间
'''

