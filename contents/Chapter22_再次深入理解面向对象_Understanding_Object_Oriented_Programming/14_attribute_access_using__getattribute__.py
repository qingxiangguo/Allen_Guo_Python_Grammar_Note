# _*_ coding=utf8 _*_
#This method is always called unconditionally when accessing the properties of an object
#Using this method, we can intercept the attribute and return fake value if you don't want the true
#attribute to be accessed
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1  #python
        self.subject2 = 'cpp'
        self.count_num = 0 #To record the times that you access the attribute

    def __getattribute__(self, item):  #The item is the name of instance attribute, like "subject1"
        if item == 'subject1':
            print('You will get a fake value for subject1')
            self.count_num += 1
            with open("log.txt", "a") as f:  #You can write something everytime
                pass
            return "fake value"
        else:
            return object.__getattribute__(self,item)   #If not subject1, you can access the true value
            # Use the method of parent class (object). And give the instance "self" and "item" (e. g. subject2) to the method

s = Itcast("python")
print(s.subject1)
print(s.subject1)
print(s.subject1)
print("The number you access the attribute is ", s.count_num)
print(s.subject2)

'''
You will get a fake value for subject1
fake value
You will get a fake value for subject1
fake value
You will get a fake value for subject1
fake value
The number you access the attribute is  3
cpp
'''