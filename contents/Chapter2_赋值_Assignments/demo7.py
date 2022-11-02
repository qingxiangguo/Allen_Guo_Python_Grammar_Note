# Qingxiang Guo
# {2022/4/30} {17:17}
str1='人生苦短，我用python'  #单引号和双引号的字符串必须在一行
str2="人生苦短，我用python"

str3="""人生苦短，  #三引号的字符串可以分布在多行，三引号可以是三个单引号，或者三个双引号
我用python"""

str4='''人生苦短，
我用python'''

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))