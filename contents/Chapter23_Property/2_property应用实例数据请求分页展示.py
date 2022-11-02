# _*_ coding=utf-8 _*_
# 需求：每页展示的物品数量是固定的，现在需要根据请求的页码，来计算需要展示多少页到多少页

class Pager(object):
    def __init__(self, current_page):
        self.current_page = current_page  # 储存请求的页码
        self.per_items = 10  # 每页展示的商品数量

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(2)  #请求的页码
print('开始的值：', p.start)
print('结束的值：', p.end)

'''
开始的值： 10
结束的值： 20
'''

# propert属性，可以让返回值更灵活，更动态，调用属性可以自动调用方法，计算处理，再返回，更简洁