# Qingxiang Guo
# {2022/7/9} {11:13}
#本程序是通过面向过程的方式
#如果一个程序有很多个函数实现，有时称呼为他们函数式编程
def say(usr_name,content):
    print("(%s):%s" % (usr_name, content))

usr_name1='john'
usr_name2='mary'

say(usr_name1, 'hello')
say(usr_name2, 'how are u')

say(usr_name1, 'Sure?')
say(usr_name2, 'of course')

'''
(john):hello
(mary):how are u
(john):Sure?
(mary):of course
'''