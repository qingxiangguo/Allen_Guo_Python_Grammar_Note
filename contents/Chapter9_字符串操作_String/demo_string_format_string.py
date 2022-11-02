# Qingxiang Guo
# {2022/5/15} {12:08}
#字符串格式化的三种方式
#【一】第一种：旧版使用%为占位符，python3.6之前
'''
print() 函数使用以%开头的转换说明符对各种类型的数据进行格式化输出,
转换说明符（Conversion Specifier）只是一个占位符，它会被后面表达式（变量、常量、数字、字符串、加减乘除等各种形式）的值代替。
%d、%i	转换为带符号的十进制整数
%f、%F	转化为十进制浮点数
%s	使用 str() 函数将表达式转换为字符串
'''
#【1.1】旧版转字符
name='qingxiang'
print('hello %s' % name)  #hello qingxiang

#【1.2】旧版转多个字符与数字，格式化字符串中也可以包含多个转换说明符，这个时候也得提供多个表达式，用以替换对应的转换说明符；多个表达式必须使用小括号( )包围起来
name='qingxiang'
age=99
url='www.g.com'
print('%s is %d years old, his website is %s' % (name,age,url))   #后面的括号里面本质是一个元组

#【1.3】指定字符或整数的最小输出宽度（占多少位置）
n=1234567
print('%20d' % n)  #             1234567为结果，默认右对齐，一共占20字符，当数据的实际宽度足够时，指定的宽度就没有实际意义了

#【1.4】指定对齐方式以及小数精度，-指定左对齐，+表示加正负数，0表示宽度不足时补充0，而不是补充空格
f=140.5
print('%-+010.2f' % f)  #会输出+140.50，左对齐，正负数，补0失效，10个位置，两位小数
#注意，上面例子中，对于整数，指定左对齐时，在右边补 0 是没有效果的，因为这样会改变整数的值

a='hello'
print('%-+010s' % a)  #会输出hello，左对齐生效，正负失效，补0失效，占10个位置生效
#注意，上面例子中，对于字符串，只能使用-标志，因为其他符号对于字符串没有意义，而补 0 会改变字符串的值。

f=100.22
print('%+015.5f' % f)  #输出为+00000100.22000，正负生效，补0生效，小数5位生效

#【1.5】传统方法还支持字典输出，比如下面把abc重复
print("double abc is %(a)s%(b)s%(c)s" % {'a':'aa','b':'bb','c':'cc'})

#【二】第二种：使用format()方法，使用花括号以及数字作为占位符
name='qingxiang'
age=99
print('my name is {0},I am {1} years old'.format(name,age))  #my name is qingxiang,I am 99 years old

#再来一个例子，这里的{0}就按序号指代format里面的第一个元素，至于指定长度和精度的方法，和其他原理一样，但表达方法不太一样（在序号后面加冒号）
print('{0}'.format(3.1415926))  #3.1415926
print('{0:.3}'.format(3.1415926))  #3.14，表示一共三位，在0后面加冒号
print('{0:.3f}'.format(3.1415926))  #3.142,0:.3f表示三位小数
print('{:.3f}'.format(3.1415926))  #3.142，{0}中的0也可以省略不写
print('{:10.3f}'.format(3.1415926)) #输出为     3.142，指一共占10位

#format()使用>、^、<来表示右对齐、居中对齐、左对齐。在对齐符号（>、^、<）后面加上的数字，
#表示宽度，在对齐符号之前加上特定字符表示当输出的内容不足以占满宽度时，以特定字符填充。
#对于数字则可以使用与旧格式化一样的方法，字符串不行，一定要用>、^、<
name='qingxiang'
age=99
print('my name is {0:*<15},I am {1:+010} years old'.format(name,age))
#上面会输出，my name is qingxiang******,I am +000000099 years old
#这是因为{0:*<15}指定了15个*占位，左对齐，{1:+010}指定了正负，0填充，默认右对齐
print('my name is {0:*^15},I am {1:*>20,.3f} years old'.format(name,age))
#上面会输出my name is ***qingxiang***,I am **************99.000 years old
#这是因为{0:*^15}指定了15个*居中占位，{1:*>20,.3f}指定了20个*右对齐，3位浮点精度

#format()还支持变量赋值同时输出，这里其实已经有了一点f-string的风格
print('my name is {n}, I am {a} years old'.format(n='qingxiang',a=99)) #my name is qingxaing, I am 99 years old

#format()还支持字典方式输出，注意引用字典的时候，前面两个星号，由于字典无序，不用序号引用
dict={'name':'qingxiang','age':99}
print('my name is {name},I am {age} years old'.format(**dict)) #my name is qingxiang,I am 99 years old

#format()还支持列表方式输出
information=['qingxaing',99]
print('my name is {0[0]}, I am {0[1]} years old'.format(information)) #my name is qingxaing, I am 99 years old

#【三】第三种：最推荐的方法，f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串
#f-string 格式话字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
name='qingxiang'
print(f'hello {name}')  #hello qingxiang，替换变量

print(f'{1+2}')   #3，替换表达式

#f-string支持字典输出
d={'myname':'qingxiang','myage':99}
print(f'my name is {d["myname"]}, I am {d["myage"]} years old') #my name is qingxiang, I am 99 years old
#注意上面一定要双引号引用变量myname,myage，要不然会报错

#f-string支持列表输出
lst=['qingxiang',99]
print(f'my name is {lst[0]}, I am {lst[1]} years old')  #my name is qingxiang, I am 99 years old

#支持使用=拼接远算表达式与结果
x=1
print(f'{x+1}') #2
print(f'{x+1=}') #x+1=2

#此外f-string内不能出现\转义，如果确实需要 \，则应首先将包含 \ 的内容用一个变量表示，再在f-string大括号内填入变量名
#print(f'{ord('\n')}') 会报错
n=ord('\n')
print(f'{n}')  #会输出10



