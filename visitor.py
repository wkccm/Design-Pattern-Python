# -*- coding: utf-8 -*- 

# visitor
# 访问者模式

# 作用于某对象结构中各元素的操作，在不改变各元素的类的前提下定义新操作
# 扩展Element较难，扩展Visitor容易

from abc import ABCMeta, abstractmethod


# 访问者
class Visitor(metaclass=ABCMeta):
    
    @abstractmethod
    def visitor_concrete_element_a(self, concrete_element_a):
        pass
    
    @abstractmethod
    def visitor_concrete_element_b(self, concrete_element_b):
        pass
    
class ConcreteVisitor1(Visitor):
    
    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,concrete_element_a.__class__.__name__))
        
    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,concrete_element_b.__class__.__name__))


class ConcreteVisitor2(Visitor):
    
    def visitor_concrete_element_a(self, concrete_element_a):
        print("%s visit %s" % (self.__class__.__name__,concrete_element_a.__class__.__name__))
        
    def visitor_concrete_element_b(self, concrete_element_b):
        print("%s visit %s" % (self.__class__.__name__,concrete_element_b.__class__.__name__))
        

# 不变数据结构
class Element(metaclass=ABCMeta):
    
    @abstractmethod
    def accept(self, visitor):
        pass
    

class ConcreteElementA(Element):
    
    def accept(self, visitor):
        visitor.visitor_concrete_element_a(self)
        

class ConcreteElementB(Element):
    
    def accept(self, visitor):
        visitor.visitor_concrete_element_b(self)

# 允许访问者访问它的元素
class ObjectStructure(object):
    
    def __init__(self) -> None:
        self.__elements=[]
        
    def attach(self, element):
        self.__elements.append(element)
    
    def detach(self, element):
        self.__elements.remove(element)
    
    def accept(self, visitor):
        for e in self.__elements:
            e.accept(visitor)


if __name__=='__main__':
    
    os=ObjectStructure()
    
    os.attach(ConcreteElementA())
    os.attach(ConcreteElementB())
    
    v1=ConcreteVisitor1()
    os.accept(v1)
    
    v2=ConcreteVisitor2()
    os.accept(v2)