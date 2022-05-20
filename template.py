# encoding: utf-8

# template
# 模板模式

# 将不变代码放到父类，子类只需要专注于可变部分

from abc import ABCMeta, abstractmethod


# 抽象父类，定义公共部分，为可变部分留下抽象方法
class AbstractClass(metaclass=ABCMeta):
    
    def fun(self):
        print("prefix")
        self.fun1()
        self.fun2()
        print("suffix")
    
    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass
    
# 实现可变方法
class ConcreteClass(AbstractClass):
    
    def fun1(self):
        print("fun1()")

    def fun2(self):
        print("fun2()")



if __name__=='__main__':
    
    res=ConcreteClass()
    res.fun()