# Qingxiang Guo
# {2022/6/7} {12:26}
'''
之前介绍了基于类的上下文管理器，不过 Python 中的上下文管理器并不局限于此，除了基于类，它还可以基于生成器实现
比如可以使用装饰器 contextlib.contextmanager，来定义自己所需的基于生成器的上下文管理器，用以支持 with 语句
这个方式进一步简化了上下文管理器的实现方式
通过 yield 将函数分割成两部分，yield 上面的语句在 __enter__ 方法中执行，yield 下面的语句在 __exit__ 方法中执行，紧跟在 yield 后面的参数是函数的返回值。
上下文管理器中yield的作用：暂停代码的运行，将f返回到你调用的地方，有yield的地方称为“生成器”
'''

from contextlib import contextmanager

@contextmanager
def my_open(file_name,file_mode):  #定义一个函数，设置两个参数
    try:
        file=open(file_name,file_mode)  #yield关键字之前的代码可以认为是上文方法，负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        file.close()   #yield关键字后面的代码可以认为是下文方法，负责释放操作对象的资源
        print('over')

#普通函数是不能结合with语句使用
with my_open('out.txt','w') as g:
    g.write('hey')
