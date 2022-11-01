# Qingxiang Guo
# {2022/5/19} {21:25}
#变量的作用域
def fun(a,b):
    c=a+b  #c，就称为局部变量，因为c是在函数体内进行定义的变量，a，b作为形参，也是局部变量
    print(c)

#print(c)  不行，超出了作用域
#print(a)  不行，超出了作用域

print('---------全局变量的例子------------')
name='qingxiang'
print(name)

def fun2():
    print(name)  #因为name是全局变量，所以函数内部外部都可以使用

#调用函数
fun2()

print('---------局部变量变为全局变量------------')
def fun3():
    global age  #函数体内部的局部变量使用global声明后，这个变量实际上就变成了全局
    age=20
    print(age)

fun3()  #输出20
print(age)  #在外面也可以调用函数体内部的age