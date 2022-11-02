# Qingxiang Guo
# {2022/6/23} {17:20}
'''对商品信息进行格式化输出'''
lst=[['01','电风扇','品牌1',500],['02','空调','品牌2',900],['03','电脑','品牌3',700]]

#定义一个函数进行格式化输出：
def show(lst):
    for item in lst:
        for i in item:
            print(i,end='\t\t')
        print()

print('编号\t\t品牌\t\t名称\t\t单价')
show(lst)
print('---格式化之后----')
print('编号\t\t品牌\t\t名称\t\t单价')
for item in lst:  #item是个列表
    item[0]='000'+item[0]
    item[3]='${0:.2f}'.format(item[3])

show(lst)

'''
编号		品牌		名称		单价
01		电风扇		品牌1		500		
02		空调		品牌2		900		
03		电脑		品牌3		700		
---格式化之后----
编号		品牌		名称		单价
00001		电风扇		品牌1		$500.00		
00002		空调		品牌2		$900.00		
00003		电脑		品牌3		$700.00		

Process finished with exit code 0

'''