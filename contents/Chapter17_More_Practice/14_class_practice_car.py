# Qingxiang Guo
# {2022/6/27} {19:47}
'''使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息'''
'''子类继承了父类，那么子类就拥有了父类所有的类属性和类方法。通常情况下，子类会在此基础上，扩展一些新的类属性和类方法。
但凡事都有例外，我们可能会遇到这样一种情况，即子类从父类继承得来的类方法中，大部分是适合子类使用的，但有个别的类方法，并不能直接照搬父类的，
如果不对这部分类方法进行修改，子类对象无法使用。针对这种情况，我们就需要在子类中重复父类的方法。'''
class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no
    def start(self):
        pass
    def stop(self):
        pass

class Taxi(Car):
    def __init__(self,type,no,company):  #company是出租车特有属性
        super().__init__(type,no)
        self.company=company
    def start(self):  #在子类中，重新父类方法
        print(f'I am from {self.company},my number is {self.no}')
    def stop(self):
        print('Thanks!')

class FamilyCar(Car):
    def __init__(self,type,no,name):  #name特有
        super().__init__(type,no)
        self.name=name
    def start(self):
        print(f'I am {self.name},my number is {self.no}')
    def stop(self):
        print('Thanks!')

if __name__=='__main__':
    taxi=Taxi('BMW','AB7854','uber')
    taxi.start()
    taxi.stop()
    print('-'*30)
    familycar=FamilyCar('Benz','EBSS54','John')
    familycar.start()
    familycar.stop()

'''
I am from uber,my number is AB7854
Thanks!
------------------------------
I am John,my number is EBSS54
Thanks!
'''