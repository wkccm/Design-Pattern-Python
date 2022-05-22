# -*- coding: utf-8 -*- 

# flyweight
# 享元模式

# 避免大量相似类的开销，只能实例化不同的对象

from abc import ABCMeta, abstractmethod

# 抽象类
class Flyweight(metaclass=ABCMeta):
    
    @abstractmethod
    def operation(self, extrinsic_state):
        pass

# 共享类
class ConcreteFlyweight(Flyweight):
    
    def operation(self, extrinsic_state):
        print("specific flyweight:",extrinsic_state)


# 不可共享类       
class UnsharedConcreteFlyweight(Flyweight):
    
    def operation(self, extrinsic_state):
        print("unshared flyweight:",extrinsic_state)

# 工厂，若对象已生成就跳过
class FlyweightFactory(object):
    
    def __init__(self) -> None:
        self.__flyweights=dict()
        
        fx=ConcreteFlyweight()
        self.__flyweights["x"]=fx
        
        fy=ConcreteFlyweight()
        self.__flyweights["y"]=fy
        
    def add_flyweight(self, key, flyweight):
        self.__flyweights[key]=flyweight
    
    def get_flyweight(self, key):
        flyweight=self.__flyweights.get(key)
        if not flyweight:
            flyweight=ConcreteFlyweight()
            self.__flyweights[key]=flyweight
        return flyweight
    
    def get_count(self):
        return len(self.__flyweights)
    

if __name__=='__main__':
    
    f=FlyweightFactory()
    
    flyweight=f.get_flyweight("x")
    flyweight.operation(1)
    test=f.get_flyweight("e")
    test.operation(2)
    
    print(f.get_count())
    
    u=UnsharedConcreteFlyweight()
    u.operation(12)