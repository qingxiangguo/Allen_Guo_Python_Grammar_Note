# Qingxiang Guo
# {2022/6/19} {20:16}
'''第一种，使用print输出内容'''
fp=open('test.txt','w')  #赋给句柄fp
print('hello',file=fp)  #print是可以直接输出的
fp.close()

'''第二种，使用上下文管理器，文件读写操作'''
with open('test1.txt','w') as file:
    file.write('hey')

'''第三种，使用列表输出'''
lst_name=['john','harry','potter','kate']
lst_mark=['AA','BB','CC','DD']
for i in range(4):
    print(lst_mark[i],lst_name[i])
#AA john
#BB harry
#CC potter
#DD kate

'''第四种，使用字典输出'''
d={'AAA':'john','BB':'harry','CC':'potter','DD':'kate'}
for key in d:
    print(key, d[key])
#AA john
#BB harry
#CC potter
#DD kate

'''第五种，使用zip函数输出'''
for s,name in zip(lst_mark,lst_name):  #使用zip函数，将两个列表合成一个迭代器对象
    print(s,name)
#AA john
#BB harry
#CC potter
#DD kate


