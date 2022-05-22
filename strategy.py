# -*- coding: utf-8 -*- 

# strategy
# 策略模式

# 封装算法，每个类可单独测试

from abc import ABCMeta, abstractmethod

# 抽象类
class Strategy(metaclass=ABCMeta):
    
    @abstractmethod
    def calculate(self):
        pass
    
# 扩展部位：增加方法
class StrategyA(Strategy):
    
    def calculate(self):
        print("Strategy A")

class StrategyB(Strategy):
    
    def calculate(self):
        print("Strategy B")


# 用户端的统一接口
class Context(object):
    
    def __init__(self,strategy):
        self.__strategy=strategy
    
    def execute_calculate(self):
        self.__strategy.calculate()


if __name__=='__main__':
    
    res=Context(StrategyA())
    res.execute_calculate()