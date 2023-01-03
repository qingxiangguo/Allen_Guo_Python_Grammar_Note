# _*_ coding=utf-8 _*_

"""
re.search会在一个字符串中搜索匹配正则表达式的模式。如果找到模式，
则返回一个匹配对象，否则返回None。这个函数只会在字符串中查找第一个匹配的模式。

re.match与re.search类似，也是在字符串中查找模式匹配。
但是，它只会在字符串的开头进行匹配，如果字符串的开头不符合正则表达式的模式，则返回None。

"""
import re

# re.search example
text = "The cat is blue."
match = re.search(r"cat", text)
if match:
    print("Match found:", match.group())
else:
    print("Match not found.")

# Output: Match found: cat

# re.match example
text = "The cat is blue."
match = re.match(r"cat", text)
if match:
    print("Match found:", match.group())
else:
    print("Match not found.")

# Output: Match not found.

"""
在这个示例中，我们使用re.search在文本中搜索"cat"的模式，
并使用re.match在文本的开头匹配"cat"的模式。由于"cat"在文本中出现，
因此re.search返回一个匹配对象。但是，由于"cat"不在文本的开头，因此re.match返回None
"""

# 下面是更复杂的例子
print("更复杂例子")

import re

# re.search example
text = "The cat is blue. The dog is brown."
match = re.search(r"(\w+) (\w+) (\w+) (\w+)", text)
if match:
    print("Match found:", match.group())
    print("Match groups:", match.groups())
else:
    print("Match not found.")

# Output:
# Match found: cat is blue.
# Match groups: ('cat', 'is', 'blue', '.')

# re.match example
text = "The cat is blue. The dog is brown."
match = re.match(r"(\w+) (\w+) (\w+) (\w+)", text)
if match:
    print("Match found:", match.group())
    print("Match groups:", match.groups()) # 返回一个包含匹配的所有子组的元组
else:
    print("Match not found.")

# Output:
# Match found: The cat is blue.
# Match groups: ('The', 'cat', 'is', 'blue.')

