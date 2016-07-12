import sys

import com.chinapex.libs.MyLibs as mylibs
from com.chinapex.aop.DecoratorDemo import deco
import logging

logger = logging.getLogger('django_debug')

sys.stderr.write("import test!\n")
sys.stdout.write("import test!\n")
# aa = sys.stdin.readline()
# print aa
name = 111



    
    
class FooClass:
    '''my first version'''
    name = ''
    age= 0
    height = 0
    weight = 0
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    @deco
    def showMe(self):
        print 'my name is %s' % self.name
        print 'i am %d years old' % self.age
        print "i am %d cm and %d kg" % (self.height, self.weight)
        
    def getInformation(self):
        return (self.name, self.age, self.height, self.weight)
    
    
def test1(instance = None, data = None, **kwargs):
    print instance
    print data
    print kwargs
    
    

if __name__ == '__main__':
#     test1(instance = 'instance', data1 = "data",ss = 111,k = 222)
#     test1('instance', 'data',a = '1111')
#     a = {}
#     b = a.pop('a' , None)
#     print b
#     if 3> 1:
#         print '11111111111'
#     elif 2>1:
#         print '222222222222222'
#     else:
#         print '333333333333333'
      print 'MY_creae'.find('create')
      print 'MY_create'.find('update')
      if 'MY_creae'.find('create'):
          print 'create'
      elif 'MY_update'.find('up'):
          print 'update'
      else:
          print 'aaaa'
#     foo = FooClass('kobe', 39, 198, 100);
#     foo.showMe()
#     print foo
#     info = foo.getInformation()
#     print info
#     print sys.path
#     mylibs.func1(1, 2)
#     mylibs.func2(4, 2)
    