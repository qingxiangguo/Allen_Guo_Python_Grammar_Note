# Qingxiang Guo
# {2022/6/8} {17:56}
'''
下面使用递归函数来实现遍历文件夹，也就是和os.walk一样的效果
'''

import os

def traverse_direct(path_name):  #定义函数名称，设定一个参数，以便传入路径,这里的path_name就是上一层的temp_path_name
    file_name=os.listdir(path_name)  #会列出当前路径下所有目录和文件的名字，存为列表，并放入一个变量file_name
    print(file_name)  #['1.txt', '2.txt', 'bb', 'cc']
    for name in file_name:  #['1.txt', '2.txt', 'bb', 'cc']
        temp_path_name=path_name + '/' + name  #  ./aa  + / + bb
        if os.path.isdir(temp_path_name):  #判断是否为目录，只有目录才执行下面操作, temp_path_name为./aa/bb
            print('%s is directory' % name)
            traverse_direct(temp_path_name)  #不能直接把name传过去，函数无法识别路径，要把包括上级路径信息的path_name加上去
        else:
            print('%s is file' % name)


traverse_direct("./aa")

'''
输出
['1.txt', '2.txt', 'bb', 'cc']
1.txt is file
2.txt is file
bb is directory  #发现b是目录以后，就去看b了
['33.txt', '44.txt', 'dd', 'ee']
33.txt is file
44.txt is file
dd is directory
[]
ee is directory
[]
cc is directory
[]

'''