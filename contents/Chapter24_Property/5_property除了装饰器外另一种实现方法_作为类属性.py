# _*_ coding=utf-8 _*_
'''
property除了可以以装饰器的方式被调用外，也可以以给property()函数输入四个参数
的方式调用，property()函数前面三个参数分别对应于数据描述符的中的__get__，__set__，__del__方法
第四个是描述内容__doc__
property()被赋值给类属性
这种方法的可读性较装饰器方法可读性要差一点
'''

class Foo(object):
    def __init__(self, value):
        self.bar = value

    def get_bar(self):
            print('get_bar被调用')

    def set_bar(self, value):
            print('set_bar被调用并且新值被设置为', value )

    def del_bar(self):
            print('del_bar被调用,删除bar属性')

    bar = property(get_bar, set_bar, del_bar, "描述内容")  # 这里创建了类属性
    # 通过上面这个语句将一个方法伪装成为属性，并将对这个假属性操作的句柄分散在各个成员函数

obj = Foo(200)  # 建立一个实例，并将obj.bar属性设置为200
obj.bar  # 自动调用get_bar方法
obj.bar = "Allen"  # 自动调用set_bar方法
desc = Foo.bar.__doc__  # 自动获取第四个参数中的内容，注意这里只能是Foo.BAR.__doc__，而不是obj.BAR.__doc__

print(desc)
del obj.bar  # 自动调用del_bar方法

''''
set_bar被调用并且新值被设置为 200  #因为在建立实例的时候赋值了obj.bar，所以调用了set_bar
get_bar被调用  # obj.bar会调用get_bar
set_bar被调用并且新值被设置为 Allen  # obj.bar = "Allen"会调用set_bar
描述内容
del_bar被调用,删除bar属性  # 会调用del_bar方法
'''
