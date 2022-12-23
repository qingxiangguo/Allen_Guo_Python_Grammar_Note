# Qingxiang Guo
# {2022/6/6} {17:39}
'''
With语句与上下文管理器。对于系统资源，比如文件，数据库连接，socket
应用程序在打开这些资源并执行完毕后，必须要断开（关闭）资源。但系统允许的能打开的最大文件数量是有限的。
'''

#来看看如何正确关闭一个文件
#第一种，普通版
def m1():  #定义一个函数
    f=open('out.txt','w')
    f.write('helloworld')
    f.close()

#这样有一个潜在的问题，如果在调用f.write的过程中，出现了异常进而导致后续代码无法继续执行。close无法被正常调用
#因此资源就会一直被占用，那么如何改进代码呢？

#第二种，进阶版，使用抛异常来解决
def m2():
    f=open('out.txt','w')
    try:
        f.write('helloworld')
    except IOError:
        print('oops error')
    finally:
        f.close()

#第三种，高级版
#一种更加简洁优雅的方式，是使用with关键字。
#open方法的返回值赋值给变量f，当离开with代码的时候，系统会自动调用f.close()方法
#with语句之所以这么强大，背后是由上下文管理器做支撑的，上下文管理器可以使用with语句，那么什么是上下文管理器呢？
def m3():
    with open('out.txt','w') as f:
        f.write('helloworld')

#什么是上下文（context
#一篇文章，只给你摘录一段，没前没后，你是看不懂的，一段话说了什么，需要通过上下文来推断
#程序也有上下文，资源是如何申请，调用，以及最后关闭的，这就叫上下文

#什么是上下文管理器（context manager）呢？
#任何实现了__enter__() 和 __exit__() 方法的对象，都可以称为为上下文管理器。就拥有了使用with关键字的能力
#下面建立一个基于类的上下文管理器，FileManager()，来举例什么是上下文管理器，以及如何自定义创建一个上下文管理器

class FileManager():
    def __init__(self,file_name,file_mode):
        print('init is running')
        self.file_name=file_name
        self.file_mode=file_mode

    def __enter__(self):  #这就是上文方法
        print('Enter is running')
        self.file=open(self.file_name,self.file_mode)  #enter负责申请资源，封装了open这个操作，并赋值给self.file属性
        return self.file   #通过返回self.file属性，来返回打开的这个对象，enter方法返回的是，赋值给with语句中as后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):   #这就是下文方法，with语句执行完成会自动执行，即使出现异常也会执行该方法，里面的exc是处理异常的，另行讲解
        print('will close')
        self.file.close()   #要关闭资源

#f=FileManager()  #此时f指向的对象，就是一个上下文管理器，由于是类的实例化，所以这是一个基于类的上下文管理器

#FileManager()现在拥有了使用with的能力
with FileManager('out.txt','w') as f:   #里面的enter把返回的对象赋值给了f变量，注意这里不一定必须是f，f的命名是独立的
    print('writing')
    f.write('hello,python')

#会输出，init is running，Enter is running，writing，will close
#执行内部逻辑流程如下，第一，方法__init__()被调用，程序初始化对象FileManager，使得文件名是out.txt，文件模式是w
#方法__enter__()被调用，文件“out.txt”以写入的模式被打开，并且返回 FileManager 对象赋予变量 f
#'hello,python'被写入文件out.txt
#方法__exit__()被调用，负责关闭之前打开的文件流

'''
总结：Enter,exit都是魔法方法，with语句的本质，是用enter申请资源，with创建资源，exit释放资源，省略了open,close操作
或者说，with本质是一种封装，将open,enter,exit封装一个类，然后调用这个类，来节省操作
With语句后面不光可以接类的实例化对象（比如例子中的File()），还可以接函数(比如open())
'''