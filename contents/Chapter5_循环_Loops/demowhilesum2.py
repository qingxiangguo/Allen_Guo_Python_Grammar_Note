# Qingxiang Guo
# {2022/5/7} {17:10}
#计算1到100之间的偶数和

'''sum=0
a=0
while a<=100:
    sum+=a
    a+=2

print('1到100之间的偶数和为'+str(sum))'''

#还有一种做法
sum=0
a=1
while a<=100:
    if not a%2:
        sum+=a
    a+=1
print('1-100之间偶数和',sum)


