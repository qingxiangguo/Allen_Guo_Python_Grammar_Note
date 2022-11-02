# _*_ coding=utf-8 _*_
# 使用property还可以限定输入数据的特点类型，比如整数，字符串等等
class Money(object):
    def __init__(self):
        self._money = 0

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self._money = value
        else:
            print("error:ini不是整数")

a = Money()
a.money = 100
print(a.money)
a.money = 'hello'
print(a.money)

'''
100
error:ini不是整数
100
'''

