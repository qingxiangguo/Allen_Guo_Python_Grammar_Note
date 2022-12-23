# Qingxiang Guo
# {2022/5/3} {15:02}

#赋值运算符，运算顺序从右往左

i=3+4
print(i)
a=b=c=20  #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('-----支持参数赋值----')
a=20
a+=30  #相当于a=a+30，单目运算符
print(a)
a-=10    #相当于a=a-10
print(a)
a*=2  #相当于a=a*2
print(a)
print(type(a))
a/=3
print(a)
print(type(a))  #到这里就变成float类型了
a//=2
print(a)  #所以这里是13.0，float类型
a%=3
print(a)
print('-------解包赋值------------')
a,b,c=20,30,40
print(a,b,c)
print('-----交换两个变量的值------')
a,b=10,20
print('交换之前：',a,b)
a,b=b,a
print('交换之后：',a,b)