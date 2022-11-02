# Qingxiang Guo
# {2022/5/6} {15:38}

#分支结构，单分支结构，条件表达式
money=1000 #余额
s=int(input('请输入取款金额'))
#判断余额是否充足
if money>=s:
    money-=s
    print('取款成功，您的余额为，',   money)

