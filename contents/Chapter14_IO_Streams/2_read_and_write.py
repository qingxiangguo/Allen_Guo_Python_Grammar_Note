# Qingxiang Guo
# {2022/6/4} {19:02}
'''
文件的读写操作，写数据使用write，
可以完成向文件写入数据,注意:如果文件不存在那么创建，如果存在那么就先清空文件(覆盖)，然后写入数据到文件里.
'''

#下面介绍使用read读数据，num表示要从文件中读取的数据的字符数（而非字节数），如果没有传入num或者为负，那么就表示读取文件中所有的数据,read()将读取的数据以字符串的形式返回
file1=open('To_be_read.txt','r')  #新建文件,r只读
content=file1.read(3)  #表示读取3个字符
print('在file1中读取的内容是%s' % content)  #输出在file1中读取的内容是111，是字符串
file1.close()

#下面介绍readlines读数据
file3=open('To_be_read.txt','r')
print(file3.readlines())  #['111\n', '222\n', '333']，输出是列表

#下面介绍readline读数据
file4=open('To_be_read.txt','r')
print(file4.readline(),type(file4.readline()))  #输出111，每次只读一行，输出字符串

#下面介绍写数据，第一种
file2=open('To_be_written.txt','w')
file2.write('Hello, Im writing')   #原文件如果有内容会覆盖
file2.close()  #关闭文件

#下面介绍写数据，第二种
file5=open('To_be_written.txt','w')
s='''
Chaos isn't a pit
chao is a ladder
'''
file5.write(s)
file5.writelines(['rfffff\n', 'ssss\n', 'dddd\n'])  #writelines会插入多行，不覆盖
file5.close()

#如果不想覆盖原文件，使用a
file6=open('To_be_written.txt','a')
file6.write('Add')
file6.close()

'''
Chaos isn't a pit
chao is a ladder
rfffff
ssss
dddd
Add
'''



