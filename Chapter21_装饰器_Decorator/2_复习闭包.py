# Qingxiang Guo
# {2022/7/16} {17:37}
'''
学习装饰器，需要闭包的知识，因为装饰器用到了闭包，复习一下
'''
def make_pencil(color):
    def write(content):
        print('I like %s, I said: %s' % (color, content))

    return write

black_pencil=make_pencil('black')  #创建一个闭包
black_pencil('How are you')    #black_pencil指向了write
#I like black, I said: How are you

red_pencil=make_pencil('red')  #创建一个闭包
red_pencil('Thank you')  #red_pencil指向了write
#I like red, I said: Thank you