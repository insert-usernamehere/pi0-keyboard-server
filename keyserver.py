from bottle import run, post, request, response, get, route
from time import sleep
from key import *
NULL_CHAR = chr(0)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

@route('/marco/<path>',method = 'POST')
def process(path):
    if path == "wake":
        print("waking pc")
        write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
        sleep(0.2)
        write_report(NULL_CHAR*8)
        
@route('/presskey/<path>',method = 'POST')
def process(path):
    newpath = eval(path)
    write_report(NULL_CHAR*2+chr(key[newpath])+NULL_CHAR*5)
    write_report(NULL_CHAR*8)
  
@route('/presswithoutrelease/<path>',method = 'POST')
def process(path):
    if path == "release":
        write_report(NULL_CHAR*8)
    else:
        newpath = eval(path)
        write_report(NULL_CHAR*2+chr(key[newpath])+NULL_CHAR*5)
        
run(host='0.0.0.0', port=80, debug=True)
