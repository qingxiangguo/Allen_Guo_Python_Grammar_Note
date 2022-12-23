# Qingxiang Guo
# {2022/5/13} {16:35}
#字符串的常用操作，字符串判断的相关方法
s='hello,python'
print('1.',s.isidentifier())  #判断是否是合法标识符，字母数字下划线
print('2.','hello'.isidentifier())  #True
print('3.','张三_'.isidentifier())  #True   汉字也是合法标识符
print('4.','张三_123'.isidentifier())  #True

print('5.','\t'.isspace())  #True，判断是否全部都是空白字符组成

print('6.','abc'.isalpha())  #True   是否全部是字母组成，汉字也算字母
print('7.','张三'.isalpha())  #True
print('8.','张三1'.isalpha())  #False

print('9.','123'.isdecimal())  #True   是否全部是十进制数字组成，汉字罗马不包括
print('10.','123四'.isdecimal())  #False
print('11.','ⅡⅡ'.isdecimal())  #False

print('12.','123'.isnumeric())  #True   判断是否纯数字组成，罗马汉字也包括
print('13.','123四'.isnumeric())  #True
print('14.','ⅡⅡ'.isnumeric())  #True

print('15.','abc1'.isalnum())  #True  判断是否全部是字母和数字组成，汉字也属于
print('16.','张三123'.isalnum())  #True
print('17.','abc!'.isalnum())  #False