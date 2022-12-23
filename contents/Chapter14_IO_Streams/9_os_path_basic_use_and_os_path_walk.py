# Qingxiang Guo
# {2022/6/7} {15:31}
import os.path
#获取文件或目录的绝对路径
print(os.path.abspath('2_read_and_write.py'))  #输出E:\pythonProject\Chapter14_IO_Streams\2_read_and_write.py

#用于判断文件或目录是否存在，如果存在返回True，如果不存在，返回False
print(os.path.exists('2_read_and_write.py'),os.path.exists('2_read_and_write.py'))   #True True

#将路径与文件名拼接起来
print(os.path.join('E:\pythonProject\Chapter14_IO_Streams','2_read_and_write.py'))  #输出E:\pythonProject\Chapter14_IO_Streams\2_read_and_write.py

#将路径与文件名分离
print(os.path.split('E:\pythonProject\Chapter14_IO_Streams\\2_read_and_write.py'))  #输出元组('E:\\pythonProject\\Chapter14_IO_Streams', '2_read_and_write.py')

#分离文件名与后缀
print(os.path.splitext('2_read_and_write.py'))  #输出元组('2_read_and_write', '.py')

#从一个路径中提取文件名
print(os.path.basename('E:\pythonProject\Chapter14_IO_Streams\\2_read_and_write.py'))  #输出2_read_and_write.py

#提取文件路径，不包括文件名
print(os.path.dirname('E:\pythonProject\Chapter14_IO_Streams\\2_read_and_write.py'))  #输出E:\pythonProject\Chapter14_IO_Streams

#用于判断是否是一个文件夹，返回True或False
print(os.path.isdir('E:\pythonProject\Chapter14_IO_Streams\\2_read_and_write.py'))  #False

#下面使用一个for循环，以及listdir方法，来获取后缀名为py的文件
import os
path=os.getcwd() #获取当前工作路径
lst=os.listdir(path)  #listdir方法，输出当前路径下的目录，以及文件列表
for filename in lst:
    if filename.endswith('.py'):  #这里用到了endswith方法
        print(filename)

'''
输出：1_open_function_basic_use.py
2_read_and_write.py
3_seek_and_tell_function.py
4_flush_and_close_function.py
5_with_and_context_manager.py
6_context_manager_based_on_generator.py
7__exit__and_context_manager.py
8_os_module_basic_use.py
9_os_path_basic_use_and_os_path_walk.py
'''


