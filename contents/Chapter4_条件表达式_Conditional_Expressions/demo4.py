# Qingxiang Guo
# {2022/5/6} {22:09}
#分支结构，嵌套if的使用
'''会员   >=200  8折
         >=100   9折
        其他不打折
        非会员    >=200  9.5折'''
answer=input('是会员吗y/n')
money=float(input('请输入您的购物金额:'))
#外层判断是否会员
if answer=='y':   #是会员
    if money>=200:
        print('打8折，付款金额为', money*0.8)
    elif money>=100:
        print('打9折，付款金额为', money*0.9)
    else:
        print('不打折，付款金额为', money)
else:   #非会员
    if money>=200:
        print('打9.5折，付款金额为', money*0.95)
    else:
        print('不打折，付款金额为', money)  #python强制缩进，要不然无法运行