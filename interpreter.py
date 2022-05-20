# encoding: utf-8

# interpreter
# 解释器模式

# 当某问题发生频率过高，可构建解释器，容易扩展文法

from abc import ABCMeta, abstractmethod


# 解释器抽象类
class AbstractExpression(metaclass=ABCMeta):
    
    @abstractmethod
    def interpret(self, context):
        pass
    
# 不同种类的解释器
class TerminalExpression(AbstractExpression):
    
    def interpret(self, context):
        if context.input=="in":
            print("terminal_in")
        else:
            print("terminal_other")
        if context.output=="out":
            print("terminal_out")
        else:
            print("terminal_other")


class NoterminalExpression(AbstractExpression):
    
    def interpret(self, context):
        print("nothing")

# 文本类
class Context(object):
    
    def __init__(self, input, output) -> None:
        self.__input=input
        self.__output=output
    
    @property
    def input(self):
        return self.__input
    
    @input.setter
    def input(self, value):
        self.__input=value
    
    @property
    def output(self):
        return self.__output
    
    @output.setter
    def output(self, value):
        self.__output=value


if __name__=='__main__':
    
    context=Context("in","out")

    
    res=[]
    res.append(TerminalExpression())
    res.append(NoterminalExpression())
    
    for i in res:
        i.interpret(context)