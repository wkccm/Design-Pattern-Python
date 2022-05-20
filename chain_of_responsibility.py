# encoding: utf-8

# chain of responsibility
# 职责链模式

# 多个对象都有机会处理请求，且形成一条链，直到有一个对象处理为止


from abc import ABCMeta, abstractmethod

# 可处理请求的抽象类
class Handler(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        self.__successor=None
    
    @property
    def successor(self):
        return self.__successor
    
    @successor.setter
    def successor(self, value):
        self.__successor=value
    
    @abstractmethod
    def handle_request(self, request):
        pass

# 不同权限的处理者
class ConcreteHandlerA(Handler):
    
    def handle_request(self, request):
        if 0<=request<10:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)


class ConcreteHandlerB(Handler):
    
    def handle_request(self, request):
        if 10<=request<20:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)

class ConcreteHandlerC(Handler):
    
    def handle_request(self, request):
        if 20<=request<30:
            print("%s process %s" % (self.__class__.__name__, request))
        else:
            self.successor.handle_request(request)


if __name__=='__main__':
    
    h1=ConcreteHandlerA()
    h2=ConcreteHandlerB()
    h3=ConcreteHandlerC()
    
    h1.successor=h2
    h2.successor=h3
    
    for request in [1,11,21]:
        print(request)
        h1.handle_request(request)