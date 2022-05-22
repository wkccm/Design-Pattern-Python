# -*- coding: utf-8 -*- 

# iterator
# 迭代器模式

# 提供一种方法顺序访问一个聚合对象中各个元素，又不暴露对象的内部表示


from abc import ABCMeta, abstractmethod

# 迭代器抽象类
class Iterator(metaclass=ABCMeta):
    
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __next__(self):
        pass
    
    @abstractmethod
    def __exist__(self):
        pass


# 迭代器类，可按多种方式遍历，构建多个迭代类
class ConcreteIterotor(Iterator):
    
    def __init__(self, aggregate) -> None:
        self.__aggregate=aggregate
        self.index=0
    
    def __next__(self):
        try:
            value=self.__aggregate[self.index]
        except IndexError:
            return False
        self.index+=1
        return value
    
    def __iter__(self):
        return self
    
    def __exist__(self):
        try:
            return self.__aggregate[self.index] != None
        
        except IndexError:
            return False

if __name__=='__main__':
    
    aggregate="a b c d e".split()
    
    it=ConcreteIterotor(aggregate)
    
    while it.__exist__():
        print(it.__next__())
    
    