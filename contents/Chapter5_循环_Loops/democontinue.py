# Qingxiang Guo
# {2022/5/8} {14:36}
'''流程控制语句continue，要求输出所有5的倍数'''
for item in range(1,51):
    if item%5==0:
        print(item)

print('使用continue')
for item in range(1,51):
    if item%5!=0:
        continue   #continue相当于弹反，立即放弃后面的，回到开头重新执行
    print(item)
