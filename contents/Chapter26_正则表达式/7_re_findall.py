# _*_ coding=utf-8 _*_
import re

text = "The cat is blue. The dog is brown."
match = re.findall(r"(\w+) (\w+) (\w+) (\w+)", text)
if match:
    print("Match found:", match)
    print("Match first element in list:", match[0])
    print("Match first element in the tuple and list:", match[0][0])
else:
    print("Match not found.")