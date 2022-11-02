# Qingxiang Guo
# {2022/5/6} {17:40}
'''多分支结构，多选一执行
      从键盘录入一个整数成绩
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
小于0或大于100，为非法数据（不是成绩的有效范围）
'''
a=int(float(input('请输入你的成绩')))
if a<0 or a>100:
    print('请输入有效的成绩')
elif a>=90:
    print('你的成绩为A')
elif a<=89 and a>=80:
    print('你的成绩为B')
elif a<=79 and a>=70:
    print('你的成绩为C')
elif a <= 69 and a >= 60:
    print('你的成绩为D')
elif a<60:
    print('你的成绩为E')
