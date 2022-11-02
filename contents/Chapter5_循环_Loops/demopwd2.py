# Qingxiang Guo
# {2022/5/8} {14:24}
'''流程控制语句，break，从键盘录入密码，最多3次，正确就结束'''
a=0
while a<3:
    '''条件执行体（循环体）'''
    pwd=input('请输入密码:')
    '''改变变量'''
    a += 1
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

