# encoding: utf-8

# prototype
# 原型模式

# 从一个对象创建另一个可定制的对象，而不需要知道创建细节

# 导入copy库中的深浅复制
from copy import copy, deepcopy
from abc import ABCMeta, abstractmethod

# 原型抽象类
class Prototype(metaclass=ABCMeta):
    
    def __init__(self, id):
        self.id=id
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id=value
        
    @abstractmethod
    def clone(self):
        pass
    
# 原型具体类（深浅复制）
class ConcretePrototypeA(Prototype):
    
    def clone(self):
        return copy(self)

class ConcretePrototypeB(Prototype):
    
    def clone(self):
        return copy(self)

class ConcretePrototypeC(Prototype):
    
    def clone(self):
        return deepcopy(self)


# 管理类，负责登记原型类对象的信息，检查复制是否成功
class Manager(object):
    
    def __init__(self):
        self.__dict={}
    
    def register(self, name, prototype):
        self.__dict[name]=prototype
    
    def create(self, proto_name):
        p=self.__dict.get(proto_name)
        return p.clone()
    

if __name__=='__main__':
    
    conA=ConcretePrototypeA(1)
    b=conA.clone()
    print(b.id)
    
    conB=ConcretePrototypeB(2)
    
    m=Manager()
    m.register("conA",conA)
    m.register("conB",conB)
    
    x=m.create("conB")
    print(x.id)
    
    conC=ConcretePrototypeC(3)
    d=conC.clone()
    print(d.id)