# Qingxiang Guo
# {2022/6/23} {15:55}
'''写一个购买车票的程序'''
dict_ticket={'G156':['广州南-武汉南','11','22'],
            'G346':['广州武-汉南','33','44'],
            'G888':['广州南-武汉','55','66']}
print('车次\t\t起始站\t\t出发时间\t\t到达时间')
for train in dict_ticket:
    print(train,end='    ')  #都不换行
    for i in dict_ticket[train]:  #循环每个列车中，列表中的其他信息
        print(i, end='    ')
    print()  #一个列车的搞完后，手动换行

train_no=input('输入你买的车次')
persons=input('输入乘车人，多人分号隔开')
s=f'您已经够买了{train_no}车次'
s_info=dict_ticket[train_no]  #获取车次详细信息
s+=s_info[0]+'  '+s_info[1]+'开'  #这个车的起始站信息和开车时间
print(f'{s}请{persons}尽快进站')

'''
车次		起始站		出发时间		到达时间
G156    广州南-武汉南    11    22    
G346    广州武-汉南    33    44    
G888    广州南-武汉    55    66    
输入你买的车次G888
输入乘车人，多人分号隔开john;mary
您已经够买了G888车次广州南-武汉  55开请john;mary尽快进站
'''