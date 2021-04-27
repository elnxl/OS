import hashlib
from wsgiref import simple_server
from AuthRPC.server import AuthRPCApp

def myauth(username, password, useragent):
    return username  == 'myuser' and \
           password  == hashlib.md5('secret'.encode()).hexdigest() and \
           useragent == 'myprogram'

class api(object):
    def square(self,n):
        return n**2

application = AuthRPCApp(api(), auth=myauth)
server = simple_server.make_server('localhost', 1234, application)
server.serve_forever()
