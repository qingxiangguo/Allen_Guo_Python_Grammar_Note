# Qingxiang Guo
# {2022/5/13} {16:21}
#字符串的常用操作，字符串的劈分
s='hello world Python'
lst=s.split()  #默认分隔符是空格，输出列表，['hello', 'world', 'Python']
print(lst)

test='aaaxbbbxcccx1'
lst1=test.split(sep='x') #分隔符也可以是字母数字  ['aaa', 'bbb', 'ccc', '1']
print(lst1)

s1='hello|world|Python'
print(s1.split(sep='|'))   #['hello', 'world', 'Python']
print(s1.split(sep='|',maxsplit=1))   #['hello', 'world|Python']，maxsplit是最大分隔次数

#rsplit是从右侧开始劈分，主要区别体现在使用maxsplit命令时
print(s1.rsplit(sep='|',maxsplit=1))  #['hello|world', 'Python']