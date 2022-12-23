# Qingxiang Guo
# {2022/6/4} {15:54}
#这里介绍了一些常见的模块
import sys  #与Python解释器及其环境操作相关的标准库
import time  #提供与时间相关的各自函数的标准库
import os  #提供了访问操作系统服务功能的标准库
import calendar #提供了与日期相关的各自函数的标准库
import urllib.request  #一定要导入到urllib包中的request模块，用于读取来自网上的数据标准库
import json  #用于使用JSON序列化和反序列化对象
import re  #用于在字符串中执行正则表达式匹配和替换
import math  #提供标准算数运算函数的标准库
import decimal  #用于进行精确控制运算精度，有效位数和四舍五入操作的十进制运算
import logging  #提供了灵活的记录事件，错误，警告和调试信息等日志信息的功能

print(sys.getsizeof(24))   #输出28,24占了28个字节
print(sys.getsizeof(True))  #输出28，True占了28个字节

print(time.time())  #输出秒，返回当前时间的时间戳(1970纪元后经过的浮点秒数)。
print(time.localtime(time.time()))  #time.struct_time(tm_year=2022, tm_mon=6, tm_mday=4, tm_hour=15, tm_min=58, tm_sec=1, tm_wday=5, tm_yday=155, tm_isdst=0)
#上面是作用是格式化时间戳为本地的时间

print(urllib.request.urlopen('https://github.com/qingxiangguo/').read())  #同时用了打开方法，再输入给读取方法
#urllib.request 请求模块，爬取一个网站的时候会用

