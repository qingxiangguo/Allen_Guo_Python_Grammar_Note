# Qingxiang Guo
# {2022/5/7} {22:21}
'''流程控制语句，break，从键盘录入密码，最多3次，正确就结束'''
for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
