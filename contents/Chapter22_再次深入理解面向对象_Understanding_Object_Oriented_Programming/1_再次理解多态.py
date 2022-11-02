#多态，如果子类重写了父类方法，那么会调用子类的方法
#如果子类没有重写父类方法，那么会调用子类的方法

class MiniOS(object):
    #操作系统类
    def __init__(self, name):
        self.name=name
        self.apps = [] #

    def __str__(self):  #打印实例化对象的时候会输出的内容
        return "%s系统安装的软件为，%s" % (self.name, str(self.apps))

    def install_app(self, app):   #输入的app是一个实例化对象，也就是实例化对象也可以被传入

        if app.ppname in self.apps:  #如果实例化对象自己的名字属性
            print("已经安装了%s，无需再装" % app.ppname)

        else:
            app.install()
            self.apps.append(app.ppname)

class App(object):
    def __init__(self, ppname, version, desc):
        self.ppname = ppname
        self.version = version
        self.desc =desc

    def __str__(self):
        return "%s的当前版本是%s - %s" % (self.ppname, self.version, self.desc)

    def install(self):
        print("安装软件，%s %s" % (self.ppname, self.version))

class PyCharm(App):  #是App的子类，继承了一切属性和方法
    pass


class Chrome(App):
    def install(self):   #重写父类App的方法
        print("正在安装程序")
        super().install()

linux = MiniOS("Linux")  #实例化一个操作系统
print(linux)

pycharm = PyCharm("PyCharm", "1.0", "Python的IDE")
chrome = Chrome("C", "1.0", "CC")

linux.install_app(pycharm)  #触发App类的__str__函数
linux.install_app(chrome)

print(pycharm)
print(chrome)

'''
Linux系统安装的软件为，[]
安装软件，PyCharm 1.0
正在安装程序
安装软件，C 1.0
PyCharm的当前版本是1.0 - Python的IDE
C的当前版本是1.0 - CC
'''

