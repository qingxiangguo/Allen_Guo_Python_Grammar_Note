# _*_ coding=utf-8 _*_
'''
些特殊的字符，术语叫 metacharacters（元字符）
它们出现在正则表达式字符串中，不是表示直接匹配他们， 而是表达一些特别的含义
这些特殊的元字符包括下面这些：
. * + ? \ [ ] ^ $ { } | ( )
'''

# . 表示要匹配除了 换行符 之外的任何 单个 字符
content = '''苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的'''

import re
p = re.compile(r'.色')  # p是一个类对象
for one in p.findall(content):  # findall是类方法
    print(one)
