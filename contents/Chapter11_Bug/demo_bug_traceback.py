# Qingxiang Guo
# {2022/5/23} {15:56}
#traceback模块可以打印出当前具体的异常信息，常用函数有
#traceback.format_exc()  以字符串返回异常信息
#traceback.print_exc()   直接打印出异常信息

import traceback
try:
    print('----------')
    print(1/0)
except:
    traceback.print_exc()
    traceback.print_exc(file=open('error.text', 'a'))  #a是没有的话就创建一个文件

