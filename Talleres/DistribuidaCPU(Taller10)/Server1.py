from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import time
import ntplib
from time import ctime
import _thread
import math
import psutil

class nn():
    def __init__(self):
        self.x = True
    def estado(self):
        self.x = not self.x
        return self.x
    def stress(self):
        y = (1254*12343)*math.log(299)/(math.sqrt(math.pow(234435, 10)))
        return y


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ('RPC2',)

yolo = nn()

server = SimpleXMLRPCServer(("localhost", 9600), requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(yolo.estado, "estado")
server.register_function(yolo.stress, "stress")

server.serve_forever()