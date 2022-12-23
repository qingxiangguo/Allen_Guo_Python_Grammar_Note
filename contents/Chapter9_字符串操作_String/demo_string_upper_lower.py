# Qingxiang Guo
# {2022/5/12} {21:48}
#字符串大小写转换方法
s='hello,python'
a=s.upper()  #转大写，会产生新对象
b=s.lower()  #转小写，会产生新对象
print(s,id(s),'\n',a,id(a), '\n', b,id(b))

s2='hello.Python'
print(s2.swapcase())  #HELLO.pYTHON，大小互换
print(s2.title())    #Hello.Python 单词首字母大写
print(s2.capitalize())   #字符串第一个大写