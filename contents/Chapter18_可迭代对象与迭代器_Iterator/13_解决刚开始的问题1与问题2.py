# Qingxiang Guo
# {2022/7/1} {16:31}
class StuSystem(object):
    #学生管理系统
    def __init__(self):
        self.stus=[]
        self.current=0

    def add(self):  #添加新学生
        name=input('请输入学生姓名')
        tel=input('请输入学生电话')
        address=input('请输入学生住址')

        #建立一个字典，放入列表属性中
        new_stu=dict()
        new_stu['name']=name  #键值对配对
        new_stu['tel']=tel
        new_stu['address'] = address
        self.stus.append(new_stu)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.stus):  ##将上面那个可迭代对象的引用，与本迭代器的self.mylist属性连接，使得self.mylist.items可以访问上面的列表
            item = self.stus[self.current]
            self.current += 1
            return item
        else:
            self.current = 0  #必须要这样，才能保证能够多次使用
            raise StopIteration #抛出异常，和平结束

#问题1，怎么样才能实现for循环遍历系统中所有学生的信息呢
stu_sys = StuSystem()
stu_sys.add()
stu_sys.add()
stu_sys.add()

for temp in stu_sys:  #stu_sys是可迭代对象，当然你这里用iter()取迭代器后，再遍历迭代器也是一样的
    print(temp)

'''
{'name': '1', 'tel': '1', 'address': '1'}
{'name': '2', 'tel': '2', 'address': '2'}
{'name': '3', 'tel': '3', 'address': '3'}
'''

#问题2，stu_sys可不可以直接被列表推导式进行操作呢？
stu_list=[x for x in stu_sys]  #列表生成式中括号，没有list
print(stu_list,type(stu_list))  #[{'name': '1', 'tel': '1', 'address': '1'}, {'name': '2', 'tel': '2', 'address': '2'}, {'name': '3', 'tel': '3', 'address': '3'}]

stu_list2=list(stu_list)  #[{'name': '1', 'tel': '1', 'address': '1'}, {'name': '2', 'tel': '2', 'address': '2'}, {'name': '3', 'tel': '3', 'address': '3'}]
print(stu_list2,type(stu_list2))  #list需要加小括号

stu_list3=list(x for x in stu_sys)  #[{'name': '1', 'tel': '1', 'address': '1'}, {'name': '2', 'tel': '2', 'address': '2'}, {'name': '3', 'tel': '3', 'address': '3'}]
print(stu_list3, type(stu_list3))


stu_tuple=tuple(x for x in stu_sys)   #元组生成式
print(stu_tuple,type(stu_tuple))   #({'name': '1', 'tel': '1', 'address': '1'}, {'name': '2', 'tel': '2', 'address': '2'}, {'name': '3', 'tel': '3', 'address': '3'})