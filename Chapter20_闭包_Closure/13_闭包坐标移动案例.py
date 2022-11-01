# Qingxiang Guo
# {2022/7/10} {8:49}
#下面是闭包的经典题目，一个人在坐标原点0,0，然后向x,y轴进行移动，每次移动后打印当前位置
def create():
    pos=[0,0]  #设定一个起始坐标
    def player(direction,step):
        new_x=pos[0] + direction[0]*step  #计算新坐标
        new_y=pos[1] + direction[1]*step
        pos[0]=new_x
        pos[1]=new_y
        return pos  #会返回当前坐标值
    return player

p=create()  #创建棋子p，是一个闭包
print(p([0,0],0))  #[0, 0]   不移动
print(p([1,0],10))  #[10, 0]  向x轴正向移动10步
print(p([-1,0],5))  #[5, 0]  向x轴负方向移动5步



