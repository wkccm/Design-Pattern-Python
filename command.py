# encoding: utf-8

# command
# 命令模式

# 将一个请求封装成对象


from abc import ABCMeta, abstractmethod

# 命令抽象类
class Command(metaclass=ABCMeta):
    
    def __init__(self, receiver) -> None:
        self.receiver=receiver
    
    @abstractmethod
    def execute(self):
        pass

# 命令类实现接收接口
class ConcreteCommand(Command):
    
    def execute(self):
        self.receiver.action()

# 唤醒类，控制命令类
class Invoker(object):
    
    @property
    def command(self):
        return self.__command
    
    @command.setter
    def command(self, value):
        self.__command=value
    
    def execute_command(self):
        self.__command.execute()

# 接收类
class Receiver(object):
    
    def action(self):
        print("execute command")

if __name__=='__main__':
    
    r=Receiver()
    
    cmd=ConcreteCommand(r)
    
    invoker=Invoker()
    invoker.command=cmd
    invoker.execute_command()