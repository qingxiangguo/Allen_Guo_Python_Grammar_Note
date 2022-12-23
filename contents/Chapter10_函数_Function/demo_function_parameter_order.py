# Qingxiang Guo
# {2022/5/19} {11:48}
'''！！！总结：函数的定义def参数顺序都要遵守，位置优先，即位置参数在关键字参数的前面，等号在后面
如果遇到单个的位置参数，单个的关键字参数，以及星号多个位置参数，星号多个关键字参数
只分别要求【单个的位置参数】在【单个的关键字参数】之前；【星号多个位置参数】在【星号多个关键字参数】之前就可以
也就是，【星号多个位置参数】是有可能在【单个的关键字参数】之前的，如后面会提到的例子，def test2(x,*args,a=4,**kwargs):
'''
def func(name, age, sex=1):
    print(name, age, sex)

func('qingxiang', 99, 2)  #输出qingxiang 99 2，因为2代替了默认关键字参数sex=1

def func(name, age, sex=1, *args, **kargs):  #kargs=keyword arguments
    print (name, age, sex, args, kargs)

func('qingxiang', 99, 2, 'music', 'sport', a=2)
'''输出，qingxiang 99 2 ('music', 'sport') {'a': 2}，因为qingxiang 99 2分别对应name,age,sex。而music,sport对应
*args，输出一个元组；a=2对应**kargs，输出一个字典
'''

#func('qingxiang', 99, sex=2, 'music', 'sport', a=2)
#上面会报错，因为sex=2在'music', 'sport'这两个位置参数的前面，所以正确的写法是，省掉sex=，将其作为位置参数传递

#还是关于这个顺序问题，举第一个例子

def test(*args, **kwargs):
    print ('args = ', args)
    print ('kwargs = ', kwargs)
    print ('-----------------------------')

test(1,2,3,4)  #args =  (1, 2, 3, 4)，kwargs =  {}，全部是位置参数，没有关键字参数，输出空字典
test(a=1,b=2,c=3) #args =  ()，kwargs =  {'a': 1, 'b': 2, 'c': 3}，全部是关键字参数，没有位置参数，输出空元组
test(1,2,3,4, a=1,b=2,c=3)   #args =  (1, 2, 3, 4)，kwargs =  {'a': 1, 'b': 2, 'c': 3}
test('a', 1, None, a=1, b='2', c=3)  #args =  ('a', 1, None)，kwargs =  {'a': 1, 'b': '2', 'c': 3}
#test(a=1,b=2,'qingxiang') 顺序不对，位置需要在前，报错

#还是关于这个顺序问题，举第二个例子，他们的顺序为，位置参数，包裹位置参数(也就是多个的)，关键字参数，包裹关键字参数（也就是多个的）
def test2(x,*args,a=4,**kwargs):
    print(x)
    print(a)
    print(args)
    print(kwargs)

test2(2,3,'qingxiang',7,8,9,y=2,z=3,w=4)
''' 会输出
2  #x的值
4  #a的值，因为a没有被改变
(3, 'qingxiang', 7, 8, 9)
{'y': 2, 'z': 3, 'w': 4}
'''

#尝试改变a的值
test2(2,3,'qingxiang',7,8,9,a=99,y=2,z=3,w=4)
'''
2 #x的值
99  #a=99
(3, 'qingxiang', 7, 8, 9)
{'y': 2, 'z': 3, 'w': 4}
'''

#还是关于这个顺序问题，举第三个例子，他们的顺序为，位置参数，关键字参数，包裹位置参数(也就是多个的)，包裹关键字参数（也就是多个的）
def test3(x,a=4,*args,**kwargs):
    print(x)
    print(a)
    print(args)
    print(kwargs)

test3(2,3,'qingxiang',7,8,9,y=2,z=3,w=4)
'''会输出
2  #x的值
3  #第二个3被传递给a了
('qingxiang',7,8,9)
{'y': 2, 'z': 3, 'w': 4}
'''
