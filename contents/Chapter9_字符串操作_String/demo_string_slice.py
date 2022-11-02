# Qingxiang Guo
# {2022/5/13} {21:20}
#字符串的切片操作
#Python中符合序列的有序序列都支持切片(slice)，列表,字符,元组，列表会不改变ID，字符，元组会改变ID
#元组比较特殊，能改变的前提是，里面第二层有能改变的类型，比如列表，否则可以切片，但是无法赋值改变内容
#字典和集合，无序，所以没法常规切片操作
s='hello,Python'
s1=s[:5]
s2=s[6:]
s3='!'

newstr=s1+s2+s3

print(s1,s2,newstr)  #hello Python helloPython!

#取偶数位置
print(s[::2])  #hloPto
#取奇数位置
print(s[1::2])  #el,yhn
#取出单个元素
print(s[1])  #e
#s[1]='XXX'  这样写不行，字符串不可修改
