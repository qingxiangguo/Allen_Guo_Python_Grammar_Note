# Qingxiang Guo
# {2022/6/22} {12:25}
'''
写一个程序进行商品登记，以及商品入库
'''
lst=[]  #用来装商品的登记库
for i in range(0,5): #只能输入5个
    goods=input('请输入商品编号和商品名称，进行商品的入库')
    lst.append(goods)  #将每一个写入列表
for item in lst:
    print(item)  #输入你的输出

cart=[]
while True:
    num=input('请输入要买的商品编号')
    for item in lst:   #遍历仓库
        if item.find(num)!=-1:  #find函数会输出位置，如果找不到会输出-1，这里的意思是，如果仓库中match到输入的编号
            cart.append(item)
            break  #退出for

    if num=='q':
        break  #退出while循环

print('您选好的商品为')  #倒着遍历，最新选择的，在最上面
for i in range(len(cart)-1,-1,-1):  #左闭右开，左边是长度减一，右边-1，才能到0,步长是-1
    print(cart[i])

'''
请输入商品编号和商品名称，进行商品的入库1001 car
请输入商品编号和商品名称，进行商品的入库1002 ship
请输入商品编号和商品名称，进行商品的入库1192 jerri
请输入商品编号和商品名称，进行商品的入库1200 heaa
请输入商品编号和商品名称，进行商品的入库1033 heee
1001 car
1002 ship
1192 jes
1200 heaa
1033 heee
请输入要买的商品编号1001
请输入要买的商品编号1002
请输入要买的商品编号q
您选好的商品为
1002 ship
1001 car
'''
