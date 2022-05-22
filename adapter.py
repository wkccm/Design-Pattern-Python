# -*- coding: utf-8 -*- 

# adapter
# 适配器模式

# 将一个类的接口转换为客户希望的另一个接口

from abc import ABCMeta, abstractmethod

# 被适配者
class Adaptee(object):
    
    def special_request(self):
        print("special request")

# 目标接口
class Target(metaclass=ABCMeta):
    
    @abstractmethod
    def request(self):
        pass

# 适配器
class Adapter(Target):
    
    def __init__(self) -> None:
        self.adaptee=Adaptee()
    
    def request(self):
        self.adaptee.special_request()

if __name__=='__main__':
    
    a=Adapter()
    
    a.request()
