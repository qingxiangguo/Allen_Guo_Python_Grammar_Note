# Qingxiang Guo
# {2022/6/8} {21:43}
'''
这里设计一个学生信息管理系统，可以增删改等，由几大模块构成
'''
import os
#下面是用来保存的文件名
filename='student.txt'

#下面是程序主函数，注意这里只是定义，而非运行主函数
def main():
    while True:  #可以进行无限的循环，配合适当地方的break来在你想要的地方退出
        menu()  #首先先打印主界面
        choice=int(input('请输入您想选择的功能'))
        if choice in [0,1,2,3,4,5,6,7]:  #如果输入数字是其中
            if choice==0:  #如果选择退出系统
                answer=input('您确定要退出系统吗？y/n')  #再确认一次
                if answer=='y' or answer=='Y': #如果确定要退出
                    print('谢谢您的使用，退出！')
                    break  #中断循环，退出系统
                else:   #如果在再一次的确认中反悔了
                    continue  #那么继续回到最近一次的循环，也就是while True
            elif choice==1:
                insert()  #调用insert函数，录入学生信息，insert函数是你在主函数之外自己定义的
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()


#下面是定义菜单界面的函数，供前面调用
def menu():
    print('=====================学生信息管理系统================================')
    print('------------------------功能菜单-----------------------------------')
    print('\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t0.退出系统')

#下面定义录入学生信息的函数，供前面调用
def insert():
    student_list=[]  #用于存储录入的学生，每一个学生是一个字典
    while True:   #循环录入学生，录了一个，还会问你下一个
        id=input('请输入学生ID，如1001')
        if not id:
            continue   #如果id为空的话，回到最近的循环，就是while True
        name=input('请输入姓名')
        if not name:
            continue
        #成绩由于是整数，复杂一点，要try一下，做好异常管理
        try:
            english=int(input('请输入英语成绩'))
            math = int(input('请输入数学成绩'))
            bio = int(input('请输入生物成绩'))
        except:  #如果输入有问题
            print('输入成绩无效，请输入整数')
            continue  #抛异常完了，要继续立即返回while true，重新录入
        #将录入的学生信息报错到字典中
        student={'id':id,'name':name,'english':english,'math':math,'bio':bio}
        student_list.append(student)  #将字典添加进入列表中
        #开始准备询问是否继续输入
        answer=input('是否继续添加学生信息?y/n')
        if answer=='y' or answer=='Y':
            continue   #立即返回while true，重新录入
        else:
            break  #中断循环

    #在insert函数内，while循环外，开始保存信息到文件中
    save(student_list)   #之前所有信息都存到列表中了
    print('学生信息已写入文件',filename)

def save(lst): #定义一个save函数，用于insert中将学生信息保存到文件中，需要传入参数lst，是一个包括了很多字典的列表
    stu_txt=open(filename,'a+',encoding='utf-8')  #新建一个文件，将句柄交给stu.txt
    #下面将列表中的元素，分别循环写入文件
    for item in lst:
        stu_txt.write(str(item)+'\n')  #每一个元组字符串化，然后加一个换行符
    stu_txt.close()

def search():  #查找学校信息
    student_query=[] #空列表，用于储存查询到的学生信息
    while True:
        if os.path.exists(filename):
            id=''
            name=''
            mode=input('按ID查找请输入1，按姓名输入2')
            if mode=='1':
                id=input('请输入要查询的学生ID')
            elif mode=='2':
                name=input('请输入要查询的学生姓名')
            else:
                print('输入有误，重新输入')
                continue
            with open(filename, 'r', encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=eval(item)
                    if id!='':  #如果ID不等于空，也就是上面程序输入了1
                        if d['id']==id:  #如果这就是你要查询的学生
                            student_query.append(d)  #把这个学生字典放入student_query列表
                    elif name!='':
                        if d['name'] == name:
                            student_query.append(d)
            #下面开始显示查询结果，专门定义一个函数格式化输出
            show_student(student_query)
            #清空列表，每一此查询一个，然后要清空
            student_query.clear()
            answer=input('是否要继续查询?y/n')
            if answer=='y':
                continue  #从search while true重新开始
            else:
                break  #退出search循环
        else:
            print('暂未保存学生信息')

def show_student(lst):  #用来显示查询结果
    if len(lst)==0:
        print('没有查询到学生信息')
        return  #退出函数
    #定义标题的，格式化输出
    format_title='{0:^6}\t{1:^12}\t{2:^8}\t{3:^10}\t{4:^10}\t{5:^8}'   #format的格式化，^表示居中，占几个字符
    print(format_title.format('ID','姓名','英语成绩','数学成绩','生物成绩','总成绩'))  #输出标题
    #定义内容的显示格式
    format_data = '{0:^6}\t{1:^12}\t{2:^8}\t{3:^10}\t{4:^10}\t{5:^8}'
    for item in lst:  #列表中是一个个字典，存入时并没有字符串化，可以直接用
        print(format_data.format(item.get('id'),item.get('name'),item.get('english'),item.get('math'),item.get('bio'),int(item.get('english'))+int(item.get('math'))+int(item.get('bio'))))  #get是获取值

def delete():  #输入学号，删除信息，主要是通过把其他学生重新写一遍实现
    while True:
        student_id=input('请输入要删除的学生的ID') #你输入的目标ID
        if student_id:  #如果student_id确实有输入，有内容
            if os.path.exists(filename):  #如果输出文件夹确实有内容，也就是已经录入了学生信息了
                with open(filename,'r',encoding='utf-8') as file:  #以with语句，打开之前的输出文件
                    student_old=file.readlines()  #将所有内容，也就是一行行长得像字典的字符串，输入到student_old，student_old是一个列表
            else:
                student_old=[]  #如果之前没有录入过学生，定义为空列表，便于后面判断

            flag=False   #用于标记是否删除,在遍历中遇到你想要的删除ID，可以改变

            #下面针对上面的输出结果student_old列表，进行操作，如果student_old存在，执行删除的操作；如果student_old不存在，输出提示【还没有录入】
            if student_old:   #如果已经录入了文件
                with open(filename,'w',encoding='utf-8') as wfile: #准备开始重写文件
                    for item in student_old:  #列表中遍历，取出来的是一个个字符串
                        d=eval(item) #将这一个个字符串，转为字典，便于判断ID
                        if d['id']!=student_id:  #如果不相等，则写入
                            wfile.write(str(d)+'\n')   #将整个字典又字符串化放回去
                        else:
                            flag=True   #这样可以通过后面来检查flag的值，来判断是否完成了某种操作

                    if flag:  #如果完成了删除
                        print(f'ID为{student_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:  #如果student_old是一个空列表，没有录入学生信息
                print('尚未录入学生信息')
                break  #退出while true循环，中止delete()函数循环，但是由于外面还有主程序的while true循环，所以会回到主界面
            show()   #删除之后，要重新显示所有学生信息

            answer=input('是否要继续删除？y/n')
            if answer=='y':
                continue   #回到开头的delete()函数中的while True
            else:
                break  #会退出delete()函数循环，但是由于外面还有主程序的while true循环，所以会回到主界面

def modify():  #修改学生信息
    while True:   #这里不能通过递归函数调用自己modify()的方式，否则再次输入学生信息的时候，没反应，可能涉及到读写以及释放资源的问题
        show()  #首先展示学生的全部信息
        if os.path.exists(filename):  #如果输出文件夹确实有内容，也就是已经录入了学生信息了
            with open(filename,'r',encoding='utf-8') as rfile:
                student_old=rfile.readlines()  #将所有内容，也就是一行行长得像字典的字符串，输入到student_old，student_old是一个列表
        else:  #如果不存在文件
            print('尚未录入学生信息')
            return
        student_id = input('请输入要修改的学生的ID')  # 你输入的目标ID
        with open(filename, 'w',encoding='utf-8') as wfile:
            id_list=[]  #构建一个空列表，用于后面判断输入的ID是否存在
            for item in student_old:  #列表中遍历，取出来的是一个个字符串
                d=eval(item)  #将这一个个字符串，转为字典，便于判断ID
                id_list.append(d['id'])  #将每一个ID加入列表，循环结束后会获得一个包括所有ID的列表
                if d['id']==student_id:
                    print('找到学生信息，可以修改他的相关信息了')
                    while True:
                        try:
                            d['name']=input('请输入姓名')
                            d['english'] = int(input('请输入英语成绩'))
                            d['math'] = int(input('请输入数学成绩'))
                            d['bio'] = int(input('请输入生物成绩'))
                        except:
                            print('输入有误，请重新输入')
                        else:
                            break
                    wfile.write(str(d)+'\n')
                    print('修改成功！')
                else:
                    wfile.write(str(d) + '\n')

            if student_id not in id_list:
                print('您输入的学号不存在本数据库中')

            answer=input('是否继续修改其他学生信息y/n?')
            if answer=='y':
                continue  #回到开头的modify()函数中的while True
            else:
                break


def sort():
    show()  #首先展示一下结果
    if os.path.exists(filename):  #看文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list=rfile.readlines()   #全部读入文件，放入一个列表
        student_new=[]  #建一个新列表，用来储存，以及排序
        for item in student_list:
            d=eval(item)
            student_new.append(d)  #将一个个字典，放入列表

    else:
        return  #结束函数

    asc_or_desc=input('请选择，0，升序，1，降序')
    if asc_or_desc=='0':
        asc_or_desc_bool=False  #用于后面sort函数排序
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()  #如果有错，再重新执行一次函数
    mode=input('请选择排序方式，1.按英语成绩排序，2.按数学成绩排序，3.按生物成绩排序，0.按总成绩排序')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
        #x表示列表student_new中的每一个元素，也就是一个字典，这里表示以english的值的整数，来排序
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['math']), reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x: int(x['bio']), reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x: int(x['english'])+int(x['bio'])+int(x['math']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)  #最后再显示一下


def total():  #统计文件里有多少人
    if os.path.exists(filename):  #看文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:  #如果确读到了内容
                print(f'一共有{len(students)}名学生')  #直接对列表使用len函数
            else:
                print('还没有录入学生信息')
    else:
        print('还没有录入学生信息')

def show():  #显示所有学生信息
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            format_title = '{0:^6}\t{1:^12}\t{2:^8}\t{3:^10}\t{4:^10}\t{5:^8}'
            print(format_title.format('ID', '姓名', '英语成绩', '数学成绩', '生物成绩', '总成绩'))
            format_data = '{0:^6}\t{1:^12}\t{2:^8}\t{3:^10}\t{4:^10}\t{5:^8}'
            for item in student:
                d=eval(item)  #列表中的字符串元素转为字典
                print(format_data.format(d.get('id'),d.get('name'),d.get('english'),d.get('math'),d.get('bio'),int(d.get('english'))+int(d.get('math'))+int(d.get('bio'))))


#下面运行主函数
if __name__ == '__main__':  #保证本文件是主程序入口，下面内容只有在运行本程序的时候才会运行
    main()
