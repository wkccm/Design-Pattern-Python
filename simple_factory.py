# -*- coding: utf-8 -*- 

# simple factory
# 简单工厂模式

# 可扩展、代码复用

# 设置被操作属性
class Operation(object):
    
    @property
    def number_A(self):
        return self.__number_A
    
    @number_A.setter
    def number_A(self, value):
        self.__number_A=value
    
    @property
    def number_B(self):
        return self.__number_B
    
    @number_B.setter
    def number_B(self, value):
        self.__number_B=value
    

# 扩展部位：增加方法
class OperationAdd(Operation):
    
    def get_result(self):
        return self.number_A + self.number_B

class OperationSub(Operation):
    
    def get_result(self):
        return self.number_A - self.number_B


# 扩展部位：增加分支
class OperationFactory(object):
    
    @staticmethod
    def create_operation(operate):
        if operate == "+":
            return OperationAdd()
        elif operate == "-":
            return OperationSub()


if __name__=='__main__':
    op=OperationFactory.create_operation('-')
    op.number_A=10
    op.number_B=15
    
    print(op.get_result())