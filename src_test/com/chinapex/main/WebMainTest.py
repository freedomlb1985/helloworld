'''
@author: ad
'''
from flask import request, Flask

app = Flask(__name__)

def test_hello():
    with app.test_request_context('/hello', method = 'GET'):
        assert request.path == '/hello'
        assert request.method == 'GET'
    print "test_hello success"
        
if __name__ == '__main__':
    test_hello()