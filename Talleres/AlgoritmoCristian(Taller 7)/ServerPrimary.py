from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from urllib.request import urlopen
import math
import time
import ntplib
import _thread 

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

class ConnectwithWebServer():
    def __init__(self):
        serverP=SimpleXMLRPCServer(("localhost", 8001),requestHandler=RequestHandler)
        serverP.register_introspection_functions()
        self.time_act()
    # Register a function under a different name
    
    def time_web(self):
        res = ntplib.NTPClient()
        result = res.request('time.google.com') 
        fecha = result.tx_time
        return (fecha) 

    def time_pc(self):
        tm = time.time()
        return (tm)

    def time_act(self):
        reloj = self.time_web()
        eject = self.time_pc()
        time.sleep(3)
        eject = eject - self.time_pc() + reloj
        print (time.asctime(time.localtime(eject)))

        x=_thread.start_new_thread(self.time_act, ())
        x.start()
        serverP.register_function(self.time_act, 'sinc') 
        serverP.serve_forever()

if __name__ == '__main__':
    ConnectwithWebServer()

