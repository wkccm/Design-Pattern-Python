# encoding: utf-8

# composite
# 组合模式

# 使用户对单个对象和组合对象的使用具有一致性

# 公共组件
class Component(object):
    
    def __init__(self, name) -> None:
        self.name=name
    
    def add(self, component):
        pass
    
    def remove(self, component):
        pass
    
    def display(self, component):
        pass

# 叶节点（透明模式）
class Leaf(Component):
    
    def add(self,component):
        print("can't add to a leaf")
    
    def remove(self,component):
        print("can't remove from a leaf")
        
    def display(self, depth):
        print('-'*depth+self.name)

# 非叶节点
class Composite(Component):
    
    def __init__(self, name) -> None:
        super(Composite,self).__init__(name)
        self.__children=[]
    
    def add(self, component):
        self.__children.append(component)
    
    def remove(self, component):
        self.__children.remove(component)
        
    def display(self, depth):
        print('-'*depth+self.name)
        for child in self.__children:
            child.display(depth+2)


if __name__=='__main__':
    
    root=Composite("root")
    
    root.add(Leaf("A"))
    root.add(Leaf("B"))
    
    subtree=Composite("Sub")
    subtree.add(Leaf("subA"))
    subtree.add(Leaf("subB"))
    
    root.add(subtree)
    
    root.display(1)