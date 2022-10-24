# Qingxiang Guo
# {2022/5/3} {23:54}
#布尔运算符，就是与或非
print('----------and并且------')
a,b=1,2
print(a==1 and b==2)  #True
print(a==1 and b<2) #False
print(a!=1 and b==2)  #False
print(a!=1 and b!=2)  #False

print('----------or或者------')
print(a==1 or b==2)  #True
print(a==1 or b<2)  #True
print(a!=1 or b==2)  #True
print(a!=1 or b!=2)  #False

print('----------not非------')
f=True
f2=False
print(not f)
print(not f2)

print('----------in与not in，存不存在------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)  #False
print('k' not in s)    #True