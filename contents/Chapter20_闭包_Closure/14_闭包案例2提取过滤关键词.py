# Qingxiang Guo
# {2022/7/10} {9:06}
#下面是对某些文本进行分析，提取出这些特殊行
#例如，需要取得result.txt文件中，含有163.com的关键字，使用闭包
def filter_163(keep):  #用来创建一个闭包并读取你要提取的关键字
    def inner_filter(file_name):   #输入读取的文件名
        file=open(file_name)  #创建句柄
        lines=file.readlines()  #将文件内容读到一个列表lines中
        file.close()
        extract=[i for i in lines if keep in i]   #遍历lines每一行，如果每一行match了lines，输出
        return extract  #返回的是列表生成器生成的列表
    return inner_filter

f=filter_163("163.com")  #f此时相当于inner_filter
f_result=f("result.txt")
print(f_result)  #['1dddsd163.com\n', 'sdasda@163.com']

