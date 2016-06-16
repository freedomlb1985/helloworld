import logging
from logging.handlers import RotatingFileHandler
import sys
import urllib
import uuid
import IP2Location
from flask import Flask, Response, request, g, redirect, make_response, abort, render_template
from flask import jsonify
import woothee
import com.chinapex.js
import pdb
import time
import json

app = Flask(__name__)

@app.route('/debug/ip/')
def debug_ip():
    ret = ''
    print "received request!"
    print request
    http_client_ip = request.headers.get('HTTP_CLIENT_IP')
    if http_client_ip:
        ret += 'HTTP_CLIENT_IP: %s<br />' % http_client_ip
    ips = request.headers.getlist('X-Forwarded-For')
    if ips:
        ret += 'X-Forwarded-For: %s<br />' % ips
    ret += 'remote_addr: %s<br />access_route: %s<br />client_ip: %s' % \
           (request.remote_addr, request.access_route, request)
    return ret


@app.route('/') 
@app.route('/<name>') 
def hello(name = None):
    print 'call hello function'  
   
    if name == None:  
        name = "handsome boy"  
    templateDate = {'name' : name};  
    return render_template("helloworld.html", **templateDate);


@app.route('/pixel.gif', methods = ['GET', 'POST']) 
def pixel():
    print 'call pixel function'
    http_client_ip = request.headers.get('HTTP_CLIENT_IP')
    params = request.headers
    print request._get_current_object()
    aDict = request.__dict__
    bDict = aDict['environ']
#     print bDict['QUERY_STRING']
    print aDict['environ']['QUERY_STRING']
    
#     for key in aDict:
#         print key 
#         print aDict[key]
    
    print "********************beautiful line********************"
    print "Page id = %s" % request.args.get('pageId', None)
    print "event id = %s" % request.args.get('eventId', None)
    
#     for key in params :
#         print key
#         print params[key]
#     
    return "hehe"






if __name__ == '__main__':
    app.run(debug=True, port=8000, host='localhost')