'''
@author: ad
'''
from _pyio import __metaclass__
 
class pyAOP(type): 


 
    def nop(self):
        pass  
    
    beforeop=nop
    afterop=nop
    
    @classmethod  
    def setbefore(self,func):
        pyAOP.beforeop=func 
    @classmethod  
    def setafter(self,func):
        pyAOP.afterop=func 
     
    def __new__(self,name,bases,dict):
        from types import FunctionType
        obj=object()
        def AOP(func):
            def wrapper(*args, **kwds):  
                pyAOP.beforeop(obj)
                value = func(*args, **kwds)
                pyAOP.afterop(obj)
                return value
            return wrapper  
        for attr, value in dict.iteritems():  
            if isinstance(value, FunctionType):  
                dict[attr] = AOP(value)
                obj=super(pyAOP, self).__new__(self, name, bases, dict)
                return obj 
            
            
class A(object):
    __metaclass__ = pyAOP
    
    def foo(self):
        total = 0
        for i in range(100):
            total += 1
            print total
            
    def foo2(self):
        from time import sleep
        total = 0
        for i in range(100):
            total += 1
            sleep(0.0001)
            print total


