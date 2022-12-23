'''
python的@property是python的一种装饰器，是用来修饰方法的
我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,
可以与所定义的属性配合使用，这样可以防止属性被修改。
使用场景：（1）修饰方法，是方法可以像属性一样访问；（2）与所定义的属性配合使用，这样可以防止属性被修改。
property属性通俗点理解是，虽然看上去是普通属性，或者给属性赋值，但实际上是调用了某个方法来获取数据或者设置数据
'''
# 一个简单的例子
class Foo(object):
    def func(self):
        print('func被调用')

    # 定义property属性
    @property
    def prop(self):
        print('prop被调用')

foo_obj = Foo() #实例化对象
foo_obj.func()
foo_obj.prop  # 实现了看上去调属性，实际上调方法

'''
func被调用
prop被调用
'''


