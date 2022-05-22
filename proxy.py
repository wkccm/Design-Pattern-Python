# -*- coding: utf-8 -*- 

# proxy
# 代理模式

# 为其他对象提供代理，控制对该对象的访问

from abc import ABCMeta, abstractmethod


# 定义实体与代理的公共接口，使代理可以替换实体
class Subject(metaclass=ABCMeta):
    
    @abstractmethod
    def request(self):
        pass

# 实体
class RealSubject(Subject):
    
    def request(self):
        print("real subject")

# 代理
class Proxy(Subject):
    
    def __init__(self) :
        self.__realsubject=RealSubject()
    
    def request(self):
        self.__realsubject.request()


if __name__=='__main__':
    
    proxy=Proxy()
    
    proxy.request()
