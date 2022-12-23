# Qingxiang Guo
# {2022/5/17} {14:55}
#字符串的编码与解码
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'，GBK中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  #b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6',URF-8，一个中文三个字节

#解码，byte代表就是一个二进制数据
byte=s.encode(encoding='GBK')  #编码，b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'
print(byte.decode(encoding='GBK'))  #解码

byte=s.encode(encoding='UTF-8')   #编码
print(byte.decode(encoding='UTF-8'))   #解码，一定要用相同的方式