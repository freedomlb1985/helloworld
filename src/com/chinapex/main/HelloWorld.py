import sys

import com.chinapex.libs.MyLibs as mylibs

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
        
    def showMe(self):
        print 'my name is %s' % self.name
        print 'i am %d years old' % self.age
        print "i am %d cm and %d kg" % (self.height, self.weight)
        
    def getInformation(self):
        return (self.name, self.age, self.height, self.weight)
    
    
    

if __name__ == '__main__':
    foo = FooClass('kobe', 39, 198, 100);
    foo.showMe()
    info = foo.getInformation()
    print info
    print sys.path
    mylibs.func1(1, 2)
    mylibs.func2(4, 2)
    