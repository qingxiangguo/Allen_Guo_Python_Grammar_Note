# Qingxiang Guo
# {2022/6/23} {15:28}
'''创造星座的对应列表'''
constellation=['白羊座','金牛座','双子座']
nature=['积极乐观','固执内向','圆滑世故']

#将两个列表联合成字典
d=dict(zip(constellation,nature))
print (d)   #{'白羊座': '积极乐观', '金牛座': '固执内向', '双子座': '圆滑世故'}

key=input('请输入您的星座')
for item in d:  #取键
    if item==key:
        print(key,'的性格特点为',d[key])
        break
    else:
        pass


