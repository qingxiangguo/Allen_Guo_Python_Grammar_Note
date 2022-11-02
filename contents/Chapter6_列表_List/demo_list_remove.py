# Qingxiang Guo
# {2022/5/10} {16:15}
#列表元素的删除操作
lst=[10,20,30,40,50,60,30]
lst.remove(30)  #从列表中移除一个元素，如果有重复元素只移除第一个元素，remove是按元素删除
print(lst)
# pop()根据索引移除元素
lst.pop(1)  #pop是根据位删除元素
print(lst)
lst.pop(0)  #如果不指定，将删除列表中的最后一个元素
print(lst)

'''删除原列表中的内容，使用的切片操作，将空列表替换回去，达到删除的效果'''
lst[1:3]=[]   #[40, 50, 60, 30]
print(lst)    #[40, 30]

'''清除列表中的所有元素'''
lst.clear()
print(lst)
'''也可以这样删除'''
lst=[]
print(lst)

'''del将列表对象删除'''
del lst
#print(lst)  再输出就报错