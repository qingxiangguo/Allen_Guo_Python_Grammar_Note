# Qingxiang Guo
# {2022/7/16} {18:05}
def check_login(func):
    def inner():
        #验证一
        if 'admin' != input('请输入用户名'):
            return '用户名不正确'  #不正确后，return会直接中断程序
        #验证二
        if '123456' != input('请输入密码'):
            return '密码不正确'
        #验证三
        if '7788' != input('请输入手机短信验证码'):
            return '验证码不正确'
        func()
    return inner


def f1():
    print('This is function one')

f1=check_login(f1)  #这就是装饰器的本质

f1()  #一样可以实现之前装饰器的效果