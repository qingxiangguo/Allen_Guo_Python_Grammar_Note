# _*_ coding=utf-8 _*_
'''
由于python进行属性的定义时，没办法设置私有属性，
因此要通过@property的方法来进行设置。这样可以隐藏属性名，
让用户进行使用的时候无法随意修改。
'''

class DataSet(object):
    def __init__(self):
        self._images = 1
        self._labels = 2 #定义属性的名称
    @property
    def images(self): #方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images
    @property
    def labels(self):
        return self._labels
l = DataSet()
#用户进行属性调用的时候，直接调用images即可，而不用知道属性名_images，因此用户无法更改属性，从而保护了类的属性。
print(l.images)
# l.images = 8 AttributeError: can't set attribute 'images'
# 因为没有定义set函数，所以无法修改这个属性
print(l.labels)

'''
1
2
'''