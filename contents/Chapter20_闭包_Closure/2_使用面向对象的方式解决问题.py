# Qingxiang Guo
# {2022/7/9} {11:18}
class Person(object):
    def __init__(self,name):
        self.usr_name = name

    def say(self, content):
        print("(%s):%s" % (self.usr_name, content))

p1=Person('John')
p2=Person('Mary')

p1.say('hello')
p2.say('how are u')

p1.say('Sure?')
p2.say('of course')

'''
(John):hello
(Mary):how are u
(John):Sure?
(Mary):of course
'''