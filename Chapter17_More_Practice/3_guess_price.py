# Qingxiang Guo
# {2022/6/21} {12:59}
#写一个猜价格的游戏
import random  #载入库，用来随机生成价格
price=random.randint(4000,6000)  #生成随机整数
print('今日竞猜商品价格为佳能数码相机，价格在4000到6000之间')
while True:
    try:
        guess=int(input('请输入您猜的价格'))
        if guess>price:
            print('大了')
            continue
        elif guess<price:
            print('小了')
            continue
        else:
            print('Bingo!')
    except:
        print('请输入正确的整数')

    answer=input('还要继续吗y/n')
    if answer=='Y' or answer=='y':
        continue
    else:
        print('游戏结束')
        break