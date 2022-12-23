# Qingxiang Guo
# {2022/7/17} {22:09}
'''
如果多个装饰器对同一个函数进行装饰，其机制如何呢？
'''
#定义函数，完成包裹数据，加粗
def makebold(fn):
    def wrapped():
        return '<b>'+fn()+'</b>'
    return wrapped

#定义函数，完成包裹数据，斜体
def makeitalic(fn):
    def wrapped():
        return '<i>'+fn()+'</i>'
    return wrapped

@makebold  #相当于test3=makebold(test3)，再执行这一行
@makeitalic  #相当于test3=makeitalic(test3)，先执行这一行
def test3():
    return 'hello world'

print(test3())
#<b><i>hello world</i></b>

'''
执行时，先装饰makeitalic，然后test3就变成了makeitalic中的内部函数wrapped，返回最初的test3函数与<i>
然后再套娃执行，装饰makebold，然后test3就变成了makebold中的内部函数wrapped，返回
'<b>'+fn()+'</b>'，其中fn()是上一级中的test3，实际上是makeitalic中的内部函数wrapped，返回最初的test3函数与<i>
所以最后结果是<b><i>hello world</i></b>
也就是装饰的时候，是从下往上，运行的时候，是从上往下
'''