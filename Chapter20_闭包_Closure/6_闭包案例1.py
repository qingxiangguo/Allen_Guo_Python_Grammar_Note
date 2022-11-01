# Qingxiang Guo
# {2022/7/9} {12:14}
def test(number):
    def inner_test(number_in):
        return number+number_in
    return inner_test

ret = test(20)  #给test函数赋值，20赋值给number并被保存
print(ret(100))  #输出120，ret调用了inner_test，100赋值给number_in

'''
正常来说，调用一个函数时，这个函数中所有局部变量+形参，都只会在函数执行过程中才出现
函数执行完毕，这些数据会被自动释放
但是，闭包很特殊，比普通要强大很多，它在外部函数执行完毕后，这个外部函数中
所有局部变量+形参，都不会被释放，以便于调用内部函数的时候可以使用
闭包的好处：可以将局部变量，永久储存，坏处是占用内存
比如：
有一个函数a
for i in range(100):
有一个闭包b
for i in range(100):
如果调用了100次a，会不断申请和释放空间
如果调用了100次b，会创造100个闭包，消耗内存
'''