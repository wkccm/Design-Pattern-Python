# encoding: utf-8

# abstract factory
# 抽象工厂模式

# 便于创建工厂，增加产品族
# 但不便于增加产品等级结构
# 增加产品等级结构时，需要修改所有工厂类
# 增加产品族时，只需要增加一个具体工厂

# 改进1：将工厂类用简单工厂模式实现，类内切换工厂分支，但扩展时需要在每个分支修改代码
# 改进2：采用反射+配置文件实现类外切换分支，扩展时只需增加若干产品类，并在工厂中添加一个方法

from abc import ABCMeta, abstractmethod

# 抽象产品类A
class AbstractProductA(object):
    
    def __init__(self, name) -> None:
        self.name=name
    
    def __str__(self):
        return "ProductA: %s" % self.name

# 具体产品A1
class ConcreteProductA1(AbstractProductA):
    pass

# 具体产品A2
class ConcreteProductA2(AbstractProductA):
    pass

# 抽象产品类B
class AbstractProductB(object):
    
    def __init__(self, name) -> None:
        self.name=name
    
    def __str__(self):
        return "ProductB: %s" % self.name

# 具体产品B1
class ConcreteProductB1(AbstractProductB):
    pass

# 具体产品B2
class ConcreteProductB2(AbstractProductB):
    pass

# 抽象工厂
class AbstractFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# 具体工厂1
class ConcreteFactory1(AbstractFactory):
    
    def create_product_a(self):
        return ConcreteProductA1("PA1")
    
    def create_product_b(self):
        return ConcreteProductB1("PB1")

# 具体工厂2
class ConcreteFactory2(AbstractFactory):
    
    def create_product_a(self):
        return ConcreteProductA2("PA2")
    
    def create_product_b(self):
        return ConcreteProductB2("PB2")


if __name__=='__main__':
    
    factory=ConcreteFactory1()
    
    product=factory.create_product_a()
    
    print(product)