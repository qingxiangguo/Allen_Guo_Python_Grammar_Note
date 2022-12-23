# Qingxiang Guo
# {2022/5/12} {21:27}
#字符串的查询操作
s='hello,hello'
print(s.index('lo'))  #3，在第三位
print(s.find('lo'))   #3，和index的区别是，find不会报错
print(s.rindex('lo'))  #9，这个方法是倒着找出现的位置
print(s.rfind('lo'))   #9，这个方法是倒着找出现的位置，和rindex区别是rfind不会报错