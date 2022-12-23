# _*_ coding=utf-8 _*_
class Goods(object):
    def __init__(self):
        self._price = 100  # 原价  反正这个名字不能和price一样
        self.discount = 0.8  # 折扣

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        print('get_price被调用')
        new_price = self._price * self.discount
        return new_price

    def set_price(self, value):
        print('set_price被调用')
        self._price = value
        # 千万不能self.price = value，要不然会赋值，引发set_price的反复调用从而引起死循环
        # 很多教程似乎都忽视了这一点,使用self._price，这个数据就会被储存到另一个空间，而不会触发死循环

    def del_price(self):
        del self._price  # 同样的道理，如果是self.price，而非self._price这里也会引起自己调用我自己，而进入死循环

    # 获取    设置     删除    描述文档
    price = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
print(obj.price)  # 获取真实商品价格，会调用get_price，然后打印价格80
obj.price = 200  # 修改商品原价，会调用set_price
print(obj.price) # 会调用get_price，然后打印价格200*0.8 = 160
print(Goods.price.__doc__)
del obj.price  # 删除商品原价
# print(obj.price) 这里会报错，因为price假属性已经被删除了

'''
get_price被调用
80.0
set_price被调用
get_price被调用
160.0
价格属性描述...
'''