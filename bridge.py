# -*- coding: utf-8 -*- 

# bridge
# 桥接模式

# 将抽象部分与它的实现部分分离

from abc import ABCMeta, abstractmethod


class Implementor(metaclass=ABCMeta):
    
    @abstractmethod
    def operation(self):
        pass

class ConcreteImplementorA(Implementor):
    
    def operation(self):
        print("implementor A")


class ConcreteImplementorB(Implementor):
    
    def operation(self):
        print("implementor B")

# 实现桥接接口
class Abstraction(object):
    
    def __init__(self,implementor=None):
        if implementor is not None:
            self.__implementor=implementor
    
    
    @property
    def implementor(self):
        return self.__implementor
    
    @implementor.setter
    def implementor(self, value):
        self.__implementor=value
    
    def operation(self):
        self.__implementor.operation()


class RefinedAbstraction(Abstraction):
    pass

if __name__=='__main__':
    
    res=RefinedAbstraction()
    
    res.implementor=ConcreteImplementorA()
    res.operation()
    
    res.implementor=ConcreteImplementorB()
    res.operation()