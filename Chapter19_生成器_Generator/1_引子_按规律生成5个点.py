#下面是生成器

#用一个例子，来引出生成器，按一定规律生成五个坐标
point_x_y_list=[]  #定一个空列表用来存元组
i=0
x=0
while i<5:  #控制循环次数
    y=2*x+1
    point_x_y_list.append((x,y))  #将生成元组储存到列表中
    x=y
    i+=1

print(point_x_y_list)  #[(0, 1), (1, 3), (3, 7), (7, 15), (15, 31)]
