# encoding: utf-8

# memento
# 备忘录模式

# 不破坏封装性的前提下，捕获一个对象内部状态，并在对象之外保存状态

# 发起人
class Originator(object):
    
    def __init__(self, state) -> None:
        self.__state=state
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, value):
        self.__state=value
    
    def create_memento(self):
        return Memento(self.__state)
    
    def set_memento(self, memento):
        self.__state=memento.state
    
    def show(self):
        print("State: ",self.__state)

# 备忘录，负责记录状态
class Memento(object):
    
    def __init__(self,state) -> None:
        self.__state=state
    
    @property
    def state(self):
        return self.__state

# 管理者，负责保存备忘录
class Caretaker(object):
    
    def __init__(self) -> None:
        self.__memento=None
    
    @property
    def memento(self):
        return self.__memento
    
    @memento.setter
    def memento(self, value):
        self.__memento=value
    
if __name__=='__main__':
    
    o=Originator("state 1")
    o.show()
    
    o.state="state 2"
    o.show()
    
    mem=o.create_memento()
    
    c=Caretaker()
    c.memento=mem
    
    o.state="state 3"
    o.show()
    
    o.set_memento(c.memento)
    o.show()