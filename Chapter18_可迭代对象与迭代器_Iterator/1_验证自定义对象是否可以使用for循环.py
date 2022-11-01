# Qingxiang Guo
# {2022/6/30} {14:39}
class StuSystem(object):
    #学生管理系统
    def __init__(self):
        self.stus=[]

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

#实例化对象
stu_sys=StuSystem()   #

#添加3个学生信息到系统中
stu_sys.add()
stu_sys.add()
stu_sys.add()

#问题1，怎么样才能实现for循环遍历系统中所有学生的信息呢，下面的方式能实现吗？目前不行，因为不是可迭代对象
#for temp in stu_sys:
#    print(temp)

#问题2. stu_sys可不可以直接被列表推导式进行操作呢？而不是下面的方式
for xx in stu_sys.stus:
    print(xx)

'''
{'name': '1', 'tel': '1', 'address': '1'}
{'name': '1', 'tel': '1', 'address': '1'}
{'name': '1', 'tel': '1', 'address': '1'}
'''