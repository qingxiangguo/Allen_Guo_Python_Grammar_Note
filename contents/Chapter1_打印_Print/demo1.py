# 下面写一个脚本，将文本输出到文本
fp=open('E:/pythonProject/test.txt',  'a+')
print('hello world', file=fp)  #’a+’就是文件有没有，没有就重新创建，有就追加
fp.close()  #关闭文件

# 不进行换行输出，输出内容在同一行中
print('hello', 'world', 'Python')
