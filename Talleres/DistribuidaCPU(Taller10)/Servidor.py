from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import time
import ntplib
from time import ctime
import _thread
import math
import psutil

s1 = xmlrpc.client.ServerProxy("http://localhost:9600")
s2 = xmlrpc.client.ServerProxy("http://localhost:9800")
s3 = xmlrpc.client.ServerProxy("http://localhost:9900")


def asignar():
    for i in range(3):
        if i == 0:
            if not s1.estado():
                return s1.stress()
        elif i == 1:
            if not s2.estado():
                return s2.stress()
        elif i == 2:
            if not s3.estado():
                return s3.stress()

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ('RPC2',)


server = SimpleXMLRPCServer(("localhost", 9700), requestHandler=RequestHandler)
server.register_introspection_functions()
server.register_function(asignar, "asignar")

server.serve_forever()