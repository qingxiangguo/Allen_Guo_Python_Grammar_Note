# Qingxiang Guo
# {2022/5/8} {16:13}
#else语句可以与while搭配
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
        '''改变变量'''
    a+=1
else:
    print('对不起，三次密码均输入错误')