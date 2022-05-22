# -*- coding: utf-8 -*- 

# facade
# 外观模式

# 为子系统的一组接口提供一致界面

# 一组子系统
class SubSystemOne(object):
    
    def fun(self):
        print("SubSystemOne")

class SubSystemTwo(object):
    
    def fun(self):
        print("SubSystemTwo")

class SubSystemThree(object):
    
    def fun(self):
        print("SubSystemThree")

# 外观类，为外界提供对子系统的统一接口
class Facade(object):
    
    def __init__(self) :
        self.a=SubSystemOne()
        self.b=SubSystemTwo()
        self.c=SubSystemThree()
    
    def actionA(self):
        self.a.fun()
        self.b.fun()

    def actionB(self):
        self.b.fun()
        self.c.fun()


if __name__=='__main__':
    
    f=Facade()
    
    f.actionA()
    f.actionB()