# encoding: utf-8

# observer
# 观察者模式

# 多个观察者监听某个对象，对象变化时通知所有观察者对象

from abc import ABCMeta, abstractmethod

# 被观察事件
class Subject(object):
    
    def __init__(self):
        self.__observers=[]
    
    def attach(self, observer):
        self.__observers.append(observer)
    
    def detach(self, observer):
        self.__observers.remove(observer)
    
    def notify(self):
        for observer in self.__observers:
            observer.update()

# 具体事件状态
class ConcreteSubject(Subject):
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status=value

# 观察者抽象类
class Observer(metaclass=ABCMeta):
    
    @abstractmethod
    def update(self):
        pass
    
# 观察者具体类，实现通知方式
# 可用委托搭载多个类中的多种不同名方式
class ConcreteObserver(Observer):
    
    def __init__(self, subject, name) -> None:
        self.subject=subject
        self.name=name
        self.objserver_status=None
    
    def update(self):
        self.objserver_status=self.subject.status
        print(":the observer: %s status change to %s" % (self.name, self.objserver_status))


if __name__=='__main__':
    
    s=ConcreteSubject()
    
    s.attach(ConcreteObserver(s,"observer 1 "))
    s.attach(ConcreteObserver(s,"observer 2 "))
    s.attach(ConcreteObserver(s,"observer 3 "))
    
    s.status="status 1"
    s.notify()
    
    s.status="status 2"
    s.notify()