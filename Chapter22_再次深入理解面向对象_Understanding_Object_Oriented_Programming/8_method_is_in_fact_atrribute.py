class A(object):
    name = 'Allen'
    func = lambda self, x: x*2 +1  #Because the lambda refers to an instance method, so we need to add a "self"

    def print_name(self):
        print('ssss', self.name)

a = A()
print(a.name)

a.print_name()

print(a.func(100))

'''
Allen
ssss Allen
201
'''
#In a class, both methods and attributes point to a block of code or data,
# which is essentially the same, and the boundary between the two is blurred