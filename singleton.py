# -*- coding: utf-8 -*- 

# singleton
# 单例模式

# 类仅有一个实例

import threading


# 双重锁定
class Singleton(type):
    
    _lock=threading.Lock()
    
    def __init__(self, *args, **kargs):
        self.__instance=None
    
    def __call__(self, *args, **kargs ) :
        if self.__instance is None:
            with self._lock:
                if self.__instance is None:
                    self.__instance=super().__call__(*args, **kargs)
                    return self.__instance
        else:
            return self.__instance


class Myclass(metaclass=Singleton):
    pass


def run():
    m=Myclass()
    print('thread_id:', threading.get_ident(), 'instance_id:', id(m))
    


if __name__=='__main__':
    
    a=Myclass()
    b=Myclass()
    
    print(a==b)
    print(a is b)
    print(a,b)
    
    print('thread_id:', threading.get_ident(), 'instance_id:', id(a))
    
    t1=threading.Thread(target=run)
    t2=threading.Thread(target=run)
    
    t1.start()
    t2.start()