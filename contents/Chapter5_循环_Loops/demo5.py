# Qingxiang Guo
# {2022/5/7} {22:02}
'''输出100到999之间的水仙花数，比如
153=3*3*3+5*5*5+1*1*1
'''

for item in range(100,1000):
    ge=item%10   #个位数
    shi=item//10%10   #十位
    bai=item//100   #百位
    #print(bai,shi,ge)
    #判断
    if ge**3+shi**3+bai**3==item:
        print(item)