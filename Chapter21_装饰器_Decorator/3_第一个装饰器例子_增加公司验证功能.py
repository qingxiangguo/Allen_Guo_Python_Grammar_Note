# Qingxiang Guo
# {2022/7/16} {17:43}
'''
假设有这样一个需求，公司每个部门，调用者公司提供的四个基础功能，f1(),f2(),f3(),f4()
但是开发人员在过去没有注意验证权限相关问题，平台基础功能可以被任何人随意调用
现在需要对平台重构，在每个基础功能中增加验证
写代码要遵循开放封闭原则，它规定已经实现的功能的代码不允许被修改，但是可以被扩展，这个时候
就可以使用装饰器，在不修改原函数的情况下，调用原函数，并增加新的功能
装饰器属于语法糖的一种，代表好用的小技巧
'''
def check_login(func):
    def inner():
        #验证一
        if 'admin' != input('请输入用户名'):
            print('用户名不正确')   #不正确后，return会直接中断程序
            return
        #验证二
        if '123456' != input('请输入密码'):
            print('密码不正确')
            return
        #验证三
        if '7788' != input('请输入手机短信验证码'):
            print('验证码不正确')
            return
        func()
    return inner

@check_login
def f1():
    print('This is function one')

#f1内容已经变了，指向inner了
f1()  #等于调用inner()

#当python解释器遇到@check_login的时候时，它会将check_login当做可执行的对象来执行
#即check_login()，并且下面的f1函数的引用，当做实参进行传递，此时变成了check_login(f1)
#将check_login(f1)的返回值，当做新的f1的值，f1=check_login(f1)，也就是说
#f1的指向变成了check_login(f1)的返回值，inner

'''
验证一
验证二
This is function one   #即实现了验证，又保留了原功能
'''
