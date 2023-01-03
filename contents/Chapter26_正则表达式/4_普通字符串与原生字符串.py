# _*_ coding=utf-8 _*_

# 在Python中，有两种字符串：普通字符串和原生字符串。普通字符串中的特殊字符（如换行符、制表符、反斜杠等）会被转义，而原生字符串则不会。
# 例如，下面是一个普通字符串的例子：

string = "This is a string.\nIt has a newline character."
print(string)

# 输出：
# This is a string.
# It has a newline character.
# 这里的反斜杠和换行符会被转义，所以字符串会被换行。

# 而使用原生字符串，反斜杠和换行符不会被转义，字符串中的换行符会被保留：

string = r"This is a string.\nIt has a newline character."
print(string)

# 输出：This is a string.\nIt has a newline character.
# 原生字符串通常用于正则表达式，因为正则表达式中经常会包含反斜杠和其他特殊字符，使用原生字符串可以避免转义带来的麻烦。

# 例如，下面是一个使用正则表达式的例子：

import re

pattern = r'([a-zA-Z0-9._%+-]+)@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
result = re.match(pattern, 'someone@example.com')
if result:
    print("Match found:", result.group())  # Match found: someone@example.com
    print(result.group(1))  # someone
else:
    print("Not find")

"""
r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
它的含义是：
[a-zA-Z0-9._%+-]+：匹配一个或多个字母、数字、点、下划线、百分号、加号或减号。
@：匹配一个@符号。
[a-zA-Z0-9.-]+：匹配一个或多个字母、数字、点或减号。
\.：匹配一个点，因为点是正则表达式中的特殊字符，所以需要转义。
[a-zA-Z]{2,4}：匹配两到四个字母。
"""
