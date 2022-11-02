# Qingxiang Guo
# {2022/6/24} {16:32}
'''定义学生类录入5个学生信息储存到列表中'''
class Student(object):
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def show(self):  #定义一个显示函数
        print(self.name,self.age,self.gender,self.score)

if __name__ == '__main__':
    print('请输入五个学生信息，格式一定要是，姓名#年龄#性别#成绩')
    lst=[]  #建立一个空列表，用于加学生信息
    for i in range(0,5):
        s=input(f'请输人第{i+1}位学生的信息和成绩')  #依次输入学生信息
        s_lst=s.split('#')  #将信息，划开，放入一个s_lst列表
    #创建学生对象
        stu=Student(s_lst[0],int(s_lst[1]),s_lst[2],float(s_lst[3]))   #实例化一个对象
        lst.append(stu)  #都储存到lst列表中，注意，stu是一个个的实例化对象

#打印列表内容
    for item in lst:
        item.show()  #由于item是实例化对象，所以可以用show方法

'''
请输入五个学生信息，格式一定要是，姓名#年龄#性别#成绩
请输人第1位学生的信息和成绩张三#22#男#22
请输人第2位学生的信息和成绩张三#22#男#22
请输人第3位学生的信息和成绩张三#22#男#22
请输人第4位学生的信息和成绩张三#22#男#22
请输人第5位学生的信息和成绩张三#22#男#22
张三 22 男 22.0
张三 22 男 22.0
张三 22 男 22.0
张三 22 男 22.0
张三 22 男 22.0
'''