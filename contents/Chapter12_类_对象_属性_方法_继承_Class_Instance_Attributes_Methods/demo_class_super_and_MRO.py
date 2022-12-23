# Qingxiang Guo
# {2022/5/30} {11:13}
'''
在这里详细解释super()的用法，以及方法解析顺序(Method Resolution Order - MRO)
一个类可以有多个父类,  在类的多继承中,如果继承多个父类方法,调用父类方法时(父类名.方法),
会造成父类方法中某些数据被重复调用,所以建议使用super()方法,那么,
多继承在python解释器中时怎样调用它的各个父类方法呢?在python类中,
有一个内置方法__mro__,它返回一个元祖,保存父类的调用顺序,能够保证每个父类都会被调用,而且只被调用一次.

如果简单粗暴的理解,super()就是执行父类的方法，经常看到的super().__init__(obj_name,obj_age)，其实就是调用了父类的init方法
但实际上，super()不是直接调用父类，super本身就是一个类，super()是这个类的实例化对象，
实际上用法是super(类名，对象名)，他接收两个参数，返回对象的MRO顺序中，类的父类。
比如super(C,d)，返回的是d的MRO中，C的上一个父类
'''
print('-----------例子一-----------------')
class A:
    def p(self):
        print('A')
class B:
    def p(self):
        print('B')
class C(A,B):   #C的多父类
    def p(self):
        print('C')
class D(C):    #D的单父类
    def p(self):
        print('D')

a=A()  #实例化出a,b,c,d
b = B()
c = C()
d = D()

print(D.__mro__)  #查看D的MRO顺序，是D,C,A,B,Obj
#(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

super(C,d).p()  #super调用了d的MRO，为D,C,A,B,Obj，其中C的上一级父类是A，所以会输出A的p方法，打印A，所以super只会执行一次


print('-----------例子二-----------------')
class A:
    def p(self):
        print('A')
class B(A):
    def p(self):
        super().p()   #这里会调用A
        print('B')
class C(B):
    def p(self):
        print('C')
class D(C):
    def p(self):
        super().p()   #这里会调用C
        print('D')

d = D()
d.p()   #执行d的p方法，会先执行super().p()，调用C的p方法，然后最后打印D。其中，C的p方法，会打印C，和AB没关系。因此最终输出C,D

print('-----------例子三-----------------')
class A:
    def p(self):
        print('A')
class B(A):
    def p(self):
        super().p()
        print('B')
class C(B):
    def p(self):
        super().p()
        print('C')
class D(C):
    def p(self):
        super().p()
        print('D')
d = D()
d.p()

'''执行d的p方法，会先执行super().p()，调用C的p方法，然后整个程序最后打印D。
其中，C的p方法，会先调用B的p方法，再打印C。B的p方法，会调用A的p方法。再打印B。
其中，A的p方法，打印A。
所以最后由外到内，访问到A，再由内向外，打印出A,B,C,D
一层层迭代，相当于执行下面的逻辑
class D(C):
   def p(self):
      def p(self):
            def p(self):
                def p(self):
                    print('A')
                print('B')
            print('C')
        print('D')
'''

print('-----------例子四-----------------')

class A:
    def __init__(self):   #本质上，构造方法，和其他自定义的方法一样，都是方法
        print('A')
class B:
    def __init__(self):
        print('B')
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
        print('C')
class D(B,A):
    def __init__(self):
        super(B,self).__init__()
        print('D')

print(C.__mro__)  #首先确定了C的MRO，是CABO
print(D.__mro__)  #确定了D的MRO，是DBAO

print('init C:')
c = C()   #调用C的构造方法，输出A,C
#分析：C中会先执行构造方法，super(C,self).__init__()，其中super(C,self)，是指self【也就是C】的
#MRO顺序中，C的上一级，也就是A，A的构造方法，会打印A，所以先打印A，后打印C

print('init D:')
d = D()   #调用D的构造方法，输出A,D
#分析：D中会先执行构造方法，super(B,self).__init__()，其中super(B,self)，是指self【也就是D】的
#MRO顺序中，B的上一级，也还是A。A的构造方法，会打印A，所以先打印A，后打印D
#总之就是要看MRO顺序，并且super只会执行一次

print('-----------例子五-----------------')
class A:
    def __init__(self):   #本质上，构造方法，和其他自定义的方法一样，都是方法
        print('A')
class B:
    def __init__(self):
        print('B')
class C(A,B):
    def __init__(self):
        super(C,self).__init__()
        print('C')
class D(B,A):
    def __init__(self):
        super().__init__()  #其他和例子四一样，如果把这里修改一下
        print('D')

print('init D:')
d = D()   #输出B,D
#分析：D中会先执行构造方法，super().__init__()，缺省状态下，会选最优先的一个父类调用
#也就是B，所以先打印B,最后打印D。

print('-----------例子六-----------------')
class A(object):
    def __init__(self):
        self.n = 10

    def minus(self, m):
        self.n -= m


class B(A):
    def __init__(self):
        self.n = 7

    def minus(self, m):
        super(B, self).minus(m)  #B的上一位是C，会跳到C
        self.n -= 2


class C(A):
    def __init__(self):
        self.n = 12

    def minus(self, m):
        super(C, self).minus(m)   #C的上一位是A，会跳到A
        self.n -= 6


class D(B, C):
    def __init__(self):
        self.n = 15

    def minus(self, m):
        super(D, self).minus(m)  # 最后结果是5   D的上一位是B会跳到B
        print(self.n)
        self.n -= 2


d = D()  # 初始化，调用 class D的__init__方法，只是赋值self.n并没有输出
print(D.__mro__)  #D类的MRO顺序为：DBCAO，所以执行顺序为DBCA
d.minus(2)  #输出5
#分析：首先是D的构造方法，self.n，也就是D.n为15，从始至终，这个self.n指的都是D，因为只有他实例化，初始化了
#其他类没有初始化。然后D的minus方法，从这里扩展开来，其中m=2，相当于执行
#D的上一个父类【最优先的】，B().minus(2)，self.n -= 2，15-2=13
#然后执行另一个父类C，self.n -= 6，13-6=7
#最后执行父类A，self.n -= m，7-2=5，所以最终为5
#也就是说,super是一种定位传送的方式，整个是由外向内定位到DBCA，然后再由A，从内向外，执行到CBD。
print(d.n)   #输出的结果是3
#分析：由于上一行，运行了d.minus(2)。self.n，也就是d.n在上面运行完后，是5，最后再运行self.n -= 2。
#如果不允许d.minus(2)，删除这一步，则d.n为构造方法中，产生的15


print('-----------例子七-----------------')


class A(object):
    def __init__(self):
        self.n = 10
        super(A, self).__init__()

    def minus(self, m):
        self.n -= m


class B(A):
    def __init__(self):
        self.n = 7
        super(B, self).__init__()  #调用C的构造函数

    def minus(self, m):
        super(B, self).minus(m)
        self.n -= 2


class C(A):
    def __init__(self):
        self.n = 12
        print('11111')
        super(C, self).__init__()  #调用A的构造函数

    def minus(self, m):
        super(C, self).minus(m)
        self.n -= 5


class D(B, C):
    def __init__(self):
        self.n = 15
        print('ssssss')
        super(D, self).__init__()   #调用B的构造函数

    def minus(self, m):
        print(self.n)
        self.n -= 2


d = D()  #依次调用DBCA的构造函数，输出sssss,11111
print(D.__mro__)  #顺序为DBCAO
d.minus(2)
#分析：d.minus(2)，在D的minus中是要打印self.n，在D的构造函数中，self.n初始为15
#但是调用了B的构造函数，self.n被重新赋值为7；又接着调用了C的构造函数
#self.n被重新赋值为12；最后又调用了A的构造函数，于是self.n，也就是d.n最终为10，print(self.n)也就是输出10
print(d.n)  # 由于运行了d.minus(2)，所以输出最后的结果是 10-2=8
#如果去掉上面的d.minus(2)，那么d.n将始终为10


print('-----------例子八-----------------')


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)  #将调用父类的bar方法，其中message是你赋值的HelloWorld
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    # 分析：fooChild = FooChild()，将FooChild实例化了，将调用FooChild的构造函数
    #FooChild的构造函数中，将调用FooParent的构造函数，将输出Parent，最后再输出FooChild的构造函数中的Child
    fooChild.bar('HelloWorld')
    #fooChild.bar方法，message等于传入的'HelloWorld'
    #super(FooChild, self).bar(message)，将调用父类的bar方法
    #父类的bar方法中，将输出HelloWorld from Parent
    #接着回到子类bar方法内，输出：print('Child bar fuction')
    #最后输出self.parent，由于FooChild实例化的过程中，调用了FooParent的构造函数，因此self.parent被赋值为，I'm the parent，打印输出

print(FooChild.__mro__)  #mro顺序为child,parent,object
print(fooChild.parent) #会输出I'm the parent，因为在实例化调用构造函数中，最后在父类中赋予了self.parent属性
                    #这里的self.parent，就是fooChild.parent
'''
最后总结：super()经常起的是在内部之间跳跃调用的作用
'''