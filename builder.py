# encoding: utf-8

# builder
# 建造者模式

# 将一个复杂对象的构建与它的表示分离，用户只需要知道建造的类型，不需要知道细节

from abc import ABCMeta, abstractmethod


# 产品类，定义产品细节
class Product(object):
    
    def __init__(self):
        self.__parts=[]
    
    def add(self,part):
        self.__parts.append(part)
    
    def show(self):
        print('-'.join(item for item in self.__parts))
        
# 建造者抽象类，定义建造产品的抽象方法
class Builder(metaclass=ABCMeta):
    
    @abstractmethod
    def build_partA(self):
        pass

    @abstractmethod
    def build_partB(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    
# 建造者实例，定义具体方法
class Builder1(Builder):
    
    def __init__(self):
        self.__product=Product()
    
    def build_partA(self):
        self.__product.add("part1A")

    def build_partB(self):
        self.__product.add("part1B")
    
    def get_result(self):
        return self.__product
    

class Builder2(Builder):
    
    def __init__(self):
        self.__product=Product()
    
    def build_partA(self):
        self.__product.add("part2A")

    def build_partB(self):
        self.__product.add("part2B")
    
    def get_result(self):
        return self.__product

# 指导者，不关注自己用的是哪个建造者，但知道所有建造者的建造步骤相同
# 若某建造者有步骤遗漏，则报错
class Director(object):
    
    @staticmethod
    def construct(builder):
        builder.build_partA()
        builder.build_partB()

if __name__=='__main__':
    
    b1=Builder1()
    b2=Builder2()
    
    Director.construct(b1)
    product=b1.get_result()
    product.show()
    
    Director.construct(b2)
    product=b2.get_result()
    product.show()
    