# Qingxiang Guo
# {2022/6/7} {12:57}
'''
上下文管理器中，__exit__()中的参数exc_type, exc_val, exc_tb，
分别表示 exception_type、exception_value和traceback。
当我们执行含有上下文管理器的with语句时，如果有异常抛出，异常的信息就会包含在这三个变量中，传入方法__exit__()。
因此，如果你需要处理可能发生的异常，可以在__exit__()添加相应的代码，比如下面这样来写：
'''

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
        if exc_type:    #如果有异常的话
            print(f'exc_type:{exc_type}')
            print(f'exc_value: {exc_val}')
            print(f'exc_traceback: {exc_tb}')
            print('exception handled')
        self.file.close()   #要关闭资源
        return True

with FileManager('out.txt','w') as obj:
    raise Exception('Exception raised')

'''
init is running
Enter is running
will close
exc_type:<class 'Exception'>
exc_value: Exception raised
exc_traceback: <traceback object at 0x000001DEC74717C0>
exception handled
'''

#这里使用raise主动抛异常了，raise的用法是，raise 异常名称(‘异常描述')，其中异常名称是固定的，描述可以自己写
#__exit__()方法中异常，被顺利捕捉并进行了处理。不过需要注意的是，如果方法__exit__()没有返回 True，异常会被抛出，程序会中断
# 因此，如果你确定异常已经被处理了，请在__exit__()的最后，加上“return True”这条语句，可以避免程序中断红字