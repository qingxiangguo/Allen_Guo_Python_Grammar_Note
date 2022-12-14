# _*_ coding=utf-8 _*_
# 要从下面的文本里面提取出薪资信息

content = '''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
'''

# 将文本内容按行放入列表
lines = content.splitlines()
for line in lines:
    # 查找'万/月' 在 字符串中什么地方，pos2是坐标位置
    pos2 = line.find('万/月')
    if pos2 < 0:  #当找不到的时候会输出-1
        # 查找'万/每月' 在 字符串中什么地方
        pos2 = line.find('万/每月')   #不是万/每月，那就找万/月
        # 都找不到
        if pos2 < 0: #都没有相关信息
            continue  #跳过当前，回到最近都一个循环，相当于下一行

    # 执行到这里，说明可以找到薪资关键字
    # 接下来分析 薪资 数字的起始位置
    # 方法是 找到 pos2 前面薪资数字开始的位置
    idx = pos2-1

    # 只要是数字或者小数点，就继续往前面找，直到捕获所有的薪资信息
    while line[idx].isdigit() or line[idx]=='.':
        idx -= 1

    # 现在 idx 指向 薪资数字前面的那个字，比如浦东新区2.5万/每月的，“区”
    # 所以薪资开始的 索引 就是 idx+1
    pos1 = idx + 1

    print(line[pos1:pos2]) # 切片操作

'''
2
2.5
1.3
1.1
2.8
2.5
'''