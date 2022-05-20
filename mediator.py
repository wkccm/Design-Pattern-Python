# encoding: utf-8

# mediator
# 中介模式

# 中介者使对象不需要显式相互引用


from abc import ABCMeta, abstractmethod

# 中介抽象类
class Mediator(metaclass=ABCMeta):
    
    @abstractmethod
    def send(self, msg, people):
        pass
    
# 中介负担较重，需实现交互逻辑
class ConcreteMediator(Mediator):
    
    @property
    def people1(self):
        return self.__people1
    
    @people1.setter
    def people1(self, value):
        self.__people1=value
    
    
    @property
    def people2(self):
        return self.__people2
    
    @people2.setter
    def people2(self, value):
        self.__people2=value
        
    def send(self, msg, people):
        if(people==self.__people1):
            self.__people2.notify(msg)
        else:
            self.__people1.notify(msg)

# 客户，需实现与中介的交互
class People(metaclass=ABCMeta):
    
    def __init__(self, mediator) -> None:
        self.__mediator=mediator
    
    
    @property
    def mediator(self):
        return self.__mediator
    
    @abstractmethod
    def send(self, message):
        pass
    
    @abstractmethod
    def notify(self, message):
        pass
    
    
class ConcretePeople1(People):
    
    def send(self, message):
        self.mediator.send(message, self)
    
    def notify(self, message):
        print("people 1 get message: ",message)


class ConcretePeople2(People):
    
    def send(self, message):
        self.mediator.send(message, self)
    
    def notify(self, message):
        print("people 2 get message: ",message)


if __name__=='__main__':
    
    m=ConcreteMediator()
    
    c1=ConcretePeople1(m)
    c2=ConcretePeople2(m)
    
    m.people1=c1
    m.people2=c2
    
    c1.send("I'm C1")
    c2.send("I'm C2")