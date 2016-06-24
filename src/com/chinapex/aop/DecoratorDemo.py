'''
@author: ad
'''
from _ctypes_test import func

def test_deco(action):
    def _deco(func):
        def wrapper(*args, **kwargs):
            if(len(args) < 1):
                print 'No activity need to be recorded'
            else:
                self = args[0]
                print type(self)
                print self
                rs = func(*args, **kwargs)
                print type(action)
                print action
                return rs
        return wrapper
    return _deco

def deco(func):
    def wrapper(*args, **kwargs):
        print "Wrap start"
        print type(args)
        print args
        print type(kwargs)
        print kwargs
        func(*args, **kwargs)
        print func
        print type(func)
        print "Wrap end\n"
    return wrapper

@deco
def foo(x):
    print "In foo:"
    print "params: %s" % x
       
@deco
def bar(x, y):
    print "In bar:"
    print "params: x = %s, y = %s" % (x, y)

@test_deco('create')
@deco    
def result(*vargs_tuple, **vargs_dict):
    for p in vargs_tuple:
        print p
    
    for k in vargs_dict.keys():
        print "key = %s, value = %s" % (k, vargs_dict[k])
    
if __name__ == "__main__":
    foo('i am a handsome boy')
    bar('u r a beauty girl', 'then...')
    result('sorry, i do not know you.', result = 'get out')









