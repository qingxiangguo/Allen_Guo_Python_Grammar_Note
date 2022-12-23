# Qingxiang Guo
# {2022/5/8} {15:49}
#else语句可以与for搭配
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均输入错误')