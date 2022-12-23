# Qingxiang Guo
# {2022/6/28} {1:37}
'''用户登陆日志'''
import time
def show_info():
    print('输入提示数字，0，退出，1，查看登陆日志')

#记录日志
def write_logininfo(username):
    with open('log.txt','a') as file:  #time.time()返回当前时间的时间戳,time.localtime作用是格式化时间戳为本地的时间
        s=f'用户名{username},登录时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'  # strftime()函数可以把YYYY-MM-DD HH:MM:SS格式的日期字符串转换成其它形式的字符串
        file.write(s+'\n')

#读取日志
def read_logininfo():
    with open('log.txt','r') as file:
        while True:
            line=file.readline()
            if line=='':  #如果读到空
                break
            else:
                print(line)

if __name__=='__main__':
    username=input('请输入用户名')
    pwd=input('请输入密码')
    if 'admin'==username and 'admin'==pwd:
        print('登录成功')
        write_logininfo(username)  #写入日志
        show_info()  #提示要执行什么操作
        num=int(input('请输入操作数字'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_logininfo()  #读取日期
                num = int(input('请输入操作数字'))  #再问一下
            else:
                print('输入有误')
                show_info()
                num = int(input('请输入操作数字'))
    else:
        print('对不起，用户名密码不正确')


