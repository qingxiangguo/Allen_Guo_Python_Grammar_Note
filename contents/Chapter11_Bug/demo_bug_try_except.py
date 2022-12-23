# Qingxiang Guo
# {2022/5/23} {14:01}
#python异常语句
try:    #一个try至少对应一个except
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为:',result)
except ZeroDivisionError:  #这些except能避免直接报错，能够保证正常结束
    print('除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')