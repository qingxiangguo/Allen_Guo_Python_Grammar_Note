# Qingxiang Guo
# {2022/7/16} {17:54}
def A(func):
    def B():
        print('--------1----------')
        func()
        print('-------2---------')
    return B

@A  #会首先执行这一个代码，并执行helloworld=A(helloworld)，然后又由于闭包的性质，helloworld被储存在func里面
def helloworld():    #然后helloworld就指向了B
    print('my name is helloworld')

helloworld()   #所以实际上是执行B()

'''
--------1----------
my name is helloworld
-------2---------
'''