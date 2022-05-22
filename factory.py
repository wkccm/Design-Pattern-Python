# -*- coding: utf-8 -*- 

# factory
# 工厂模式

# 将类的实例化延迟到子类

from abc import ABCMeta, abstractmethod

# 抽象产品类
class Product(metaclass=ABCMeta):
    
    @abstractmethod
    def fun(self):
        pass

# 产品A
class ConcreteProductA(Product):
    
    def fun(self):
        print(self.__class__.__name__)

# 产品B
class ConcreteProductB(Product):
    
    def fun(self):
        print(self.__class__.__name__)

# 抽象生产类
class Factory(object):
    
    @abstractmethod
    def create(self):
        pass

# 工厂A
class ConcreteFactoryA(Factory):
    
    def create(self):
        return ConcreteProductA()
    
# 工厂B
class ConcreteFactoryB(Factory):
    
    def create(self):
        return ConcreteProductB()

# 先造工厂，然后生产
# 将分支选择的处理延迟到子类
if __name__=='__main__':
    
    fac_a=ConcreteFactoryA()
    product=fac_a.create()
    product.fun()
    
    fac_b=ConcreteFactoryB()
    product=fac_b.create()
    product.fun()