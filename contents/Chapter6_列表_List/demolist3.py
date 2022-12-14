# Qingxiang Guo
# {2022/5/9} {17:53}
#获取列表中的多个元素，进行切片操作
lst=[10,20,30,40,50,60,70,80]
print(lst[1:6:1])  #开始为1,stop为6，步长为1，输出为[20, 30, 40, 50, 60]，区间左闭右开
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))  #说明切片出来的是新列表
print('---切片的一些省略写法和默认---')
print(lst[1:6])  #默认步长为1
print(lst[1:6:]) #默认步长为1
print(lst[1:6:2])  #[20, 40, 60]
print(lst[:6:2])  #[10, 30, 50]，左边默认为0
print(lst[1::2])  #[20, 40, 60, 80]，右边默认为到结束
print('---------步长为负数的情况-------')
print('原列表',lst)
print(lst[7::-1])  #start=7,stop省略，step=-1,[80, 70, 60, 50, 40, 30, 20, 10]，是逆序列的一种方式
print(lst[::-1])   #省略开始和结束，也是逆序列
print(lst[6:0:-2])   #从70到10，步长为-2，[70, 50, 30]，因为左闭右开，所以那个索引0是不包括的
