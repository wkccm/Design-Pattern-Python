# encoding: utf-8

# state
# 状态模式

# 当一个对象的内在状态改变时，允许改变其行为

from abc import ABCMeta, abstractmethod

# 状态抽象
class State(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, context):
        pass

# 状态，实现跳转
class ConcreteStateA(State):
    
    def handle(self, context):
        context.state=ConcreteStateB()

class ConcreteStateB(State):
    
    def handle(self, context):
        context.state=ConcreteStateA()

# 注意记录当前状态
class Context(object):
    
    def __init__(self,state) -> None:
        self.__state=state
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, value):
        print("current status:",value.__class__.__name__)
        self.__state=value
    
    def request(self):
        self.__state.handle(self)


if __name__=='__main__':
    
    c=Context(ConcreteStateA())
    
    c.request()
    c.request()
    c.request()
    c.request()