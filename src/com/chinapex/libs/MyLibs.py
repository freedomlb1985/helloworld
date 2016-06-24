'''

@author: ad
'''
from com.chinapex.aop.DecoratorDemo import deco

@deco
def func1 (a, b):
    a += 1
    b += 1
    return a + b
@deco
def func2(a, b):
    return a - b