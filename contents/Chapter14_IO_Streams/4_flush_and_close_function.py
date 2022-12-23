# Qingxiang Guo
# {2022/6/5} {18:29}
'''
这里主要介绍flush()和close()的用法，以及两者的区别
向文件中写入数据的时候，python并不会立刻写入，而是会写到缓冲区，等待清空的时候写入文件
到缓冲区，然后用flush或close真正的写入文件
如果open后不close，可能的坏处有：（1）数据丢失，缓冲区没有满之前不会写入文件中。（close有保存的作用，将缓冲区中的内容真正写入文件）
（2）文件句柄被占用，多线程或者进程情况下 会造成文件写入错乱，造成脏数据（3）对象未解除引用，垃圾回收无法回收此对象占用
所以每次写入数据后可以加上flush(),对写入的数据进行保存，这样即使最后没有close()，也不会导致之前的数据未保存
简单粗暴的理解，flush()是手动临时存档，而close()是最终正式存档，之后整个文件句柄将不能访问
'''

file=open('To_be_written.txt','a')   #以追加方式打开
file.write('hello')
file.flush()  #手动将数据从缓冲区，立即写入文件中
file.write('world')
file.close()  #如果close()在flush前面，文件句柄就不能访问

#输出如下
'''
Chaos isn't a pit
chao is a ladder
rfffff
ssss
dddd
Addhelloworld
'''