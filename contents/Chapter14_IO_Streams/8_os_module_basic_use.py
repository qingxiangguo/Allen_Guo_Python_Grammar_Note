# Qingxiang Guo
# {2022/6/7} {15:30}
'''
os模块，os模块在python中包含普遍的操作系统功能
os模块是Python标准库中的一个用于访问操作系统相关功能的模块
'''
import os
#os.system('notepad.exe')  #打开记事本
#os.system('calc.exe')  #打开计算器
#直接调用可执行文件
#os.startfile('E:\软件\QQ\Bin\QQScLauncher.exe')  #打开可执行文件

print(os.getcwd())  #返回当前的工作目录，输出E:\pythonProject\Chapter14_IO_Streams

lst=os.listdir('../Chapter14_IO_Streams')  #以列表的形式，输出指定路径下的所有文件和目录信息
print(lst)  #输出['1_open_function_basic_use.py', '2_read_and_write.py', '3_seek_and_tell_function.py', '4_flush_and_close_function.py', '5_with_and_context_manager.py', '6_context_manager_based_on_generator.py', '7__exit__and_context_manager.py', '8_os_module_basic_use.py', '9_os_path_basic_use_and_os_path_walk.py', 'out.txt', 'To_be_read.txt', 'To_be_written.txt']

#os.mkdir('newdir')  #创建新目录
#os.makedirs('A/B/C')   #递归创建多级目录
#os.rmdir('newdir')   #删除目录
#os.removedirs('A/B/C')   #递归删除多级目录
os.chdir('E:\pythonProject\chapter13')  #更改当前工作目录
print(os.getcwd())  #E:\pythonProject\chapter13