# encoding: utf-8

# decorator
# 装饰模式

# 有顺序地装饰类，相当于给类一层层穿衣服

from abc import ABCMeta, abstractmethod

# 抽象类
class Component(metaclass=ABCMeta):
    
    @abstractmethod
    def operation(self):
        pass

# 实现类的功能扩展
class ConcreteComponent(Component):
    
    def operation(self):
        print("concrete component")

# 装饰抽象类
class Decorator(Component):
    
    def __init__(self, component):
        self.__component=component
    
    def operation(self):
        if self.__component:
            self.__component.operation()

# 扩展部位：扩展装饰类功能
class DecoratorA(Decorator):
    
    def operation(self):
        print(" A ")
        super(DecoratorA, self).operation()
        print(" /A ")


class DecoratorB(Decorator):
    
    def operation(self):
        print(" B ")
        super(DecoratorB, self).operation()
        print(" /B ")
        

if __name__=='__main__':
    res=ConcreteComponent()
    
    fun1=DecoratorA(res)
    
    fun1.operation()
    
    fun2=DecoratorB(fun1)
    
    fun2.operation()