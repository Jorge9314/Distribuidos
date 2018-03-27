from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import time
import ntplib
from time import ctime
import _thread
import math

s = xmlrpc.client.ServerProxy("http://localhost:9700")
s2 = xmlrpc.client.ServerProxy("http://localhost:9600")
s3 = xmlrpc.client.ServerProxy("http://localhost:9500")
s4 = xmlrpc.client.ServerProxy("http://localhost:9400")

class timer():
    def __init__(self, actualTime):
        self.actualTime= actualTime
        self.x=[]
        self.removed = False
    def hanlder(self):
        while True:
            print (time.asctime(time.localtime(self.actualTime+time.clock())))
            time.sleep(1)
    def getTime(self):
        return self.actualTime+time.clock()
    def askTime(self):
        while True:
            input('Presione ENTER para empezar a sincronizar con los servidores\n')
            print ('ENTER.')
            self.x.append(s.getTime())
            print('Obtenido 1')
            self.x.append(s2.getTime())
            self.x.append(s3.getTime())
            self.x.append(s4.getTime())
            print('Obtenidos.')
            xm = (self.x[0] + self.x[1] + self.x[2] + self.x[3])/4
            des = math.sqrt((1/3)*(pow(self.x[0]-xm,2)+pow(self.x[1]-xm,2)+pow(self.x[2]-xm,2)+pow(self.x[3]-xm,2)))
            for i in self.x:
                if i<(xm-2*des) or i>(xm+2*des):
                    self.x.remove(i)
                    self.removed = True
            if self.removed:
                xm = 0
                des = 0
                for i in self.x:
                    xm = xm + i
                xm = xm/len(self.x)
            self.actualTime = xm



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

c = ntplib.NTPClient()
response = c.request('time.google.com')
currentTime = response.tx_time

timerTimer = timer(currentTime)

server = SimpleXMLRPCServer(("localhost", 9650), requestHandler=RequestHandler)
server.register_introspection_functions()
server.register_function(timerTimer.getTime, 'getTime')
print('Waiting... ')
_thread.start_new_thread(timerTimer.hanlder,())
_thread.start_new_thread(timerTimer.askTime,())

server.serve_forever()

