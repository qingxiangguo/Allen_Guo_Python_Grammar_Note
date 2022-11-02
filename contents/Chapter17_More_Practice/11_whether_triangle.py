# Qingxiang Guo
# {2022/6/24} {15:19}
'''判断三个参数能否组成三角形'''
def is_triangle(a,b,c):
    if a<0 or b<0 or c<0:
        raise Exception('三条边不能负数')  #手动抛异常

    #判断是否构成三角形
    if a+b>c and b+c>a and a+c>b:
        print(f'可以构成三角形，边长为{a},{b},{c}')
    else:
        raise Exception(f'{a},{b},{c},不能构成三角形')

if __name__== '__main__':
    try:
        a=int(input('第一条边'))
        b = int(input('第二条边'))
        c = int(input('第三条边'))
        is_triangle(a,b,c)
    except Exception as e:
        print(e)

'''第一条边5
第二条边6
第三条边7
可以构成三角形，边长为5,6,7'''