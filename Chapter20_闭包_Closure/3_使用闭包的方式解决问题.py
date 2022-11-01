# Qingxiang Guo
# {2022/7/9} {11:29}
def who(name):
    def do(content):
        print('(%s):%s' % (name,content))
    return do

j=who('john')
m=who('mary')

j('hello')
m('how are u')
j('Sure?')
m('of course')

'''
(john):hello
(mary):how are u
(john):Sure?
(mary):of course
'''