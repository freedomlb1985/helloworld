from _ctypes_test import func
from activity.models.activity import AccountActivity, ContainerActivity
import copy
from container.serializers.projects import ProjectSerializer 


def test_deco(action):
    def _deco(func):
        def wrapper(*args, **kwargs):
            if(len(args) < 1):
                print 'No activity need to be recorded'
            else:
                self = args[0]
                rs = func(*args, **kwargs)
                print type(action)
                print action
                return rs
        return wrapper
    return _deco

def project_handler(func, args, kwargs):
    
    params = args[1]
#     containers_data = params.pop('containers', None)
    account = params.pop('account', None)
    activity = func.__name__
    type = "project"
    typename = params.pop('name', None)
    ip_address = ''
    return None

def container_handler(args, kwargs):
    return None

def tag_handler(args, kwargs):
    return None

def trigger_handler(args, kwargs):
    return None

def variable_handler(args, kwargs):
    return None

handler_mapping = {ProjectSerializer : project_handler,
                   }

def generate_container_activity_model(func, args, kwargs):
    self = args[0]
    class_name = self.__class__.__name__
    func_name = func.__name__
    container_activity = ContainerActivity.objects.create()



def container_deco(func):
    def wrapper(*args, **kwargs):
        if(len(args) < 1):
            print 'No activity need to be recorded'
        else:
            targs = copy.deepcopy(args);
            dkwargs = copy.deepcopy(kwargs)
            rs = func(*args, **kwargs)
            for i in range(len(targs)):
                print "index = %d, content = %s" % (i, targs[i])
            for k in dkwargs.keys():
                print "key = %s, and value = %s" % (k, dkwargs[k])
                
            print '***************************'
            self = targs[0]
            class_name = self.__class__.__name__
            func_name = func.__name__
            
            print self.__class__.__name__
            print func.__name__
            return rs
    return wrapper
