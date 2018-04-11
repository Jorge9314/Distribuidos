from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import time
import ntplib
from time import ctime
import _thread
import math
import psutil

s = xmlrpc.client.ServerProxy("http://localhost:9700")


while(True):
    per_cpu = psutil.cpu_percent();
    print("porcentaje:" + str(per_cpu));
    if(per_cpu > 20.0):
        print("soy mayor que 20")
        print(str(s.asignar()) + " viene de servidor")
    else:
        x = (1254*12343)*math.log(299)/(math.sqrt(math.pow(234435, 10)))
        print (str(x) + " Local")
    time.sleep(1)


