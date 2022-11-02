# Qingxiang Guo
# {2022/5/8} {16:41}
'''输出一个三行四列的矩形'''

for i in range(1,4):  #行表，执行三次，一次是一行
    for j in range(1,5):
        print('*', end='\t')   #print默认是打印一行，结尾加换行。end='\t'意思是末尾不换行，加\t。
    print('\n') #不换行的循环完了后，来一个手动换行的