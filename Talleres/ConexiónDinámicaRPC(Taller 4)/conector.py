from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server - primary
class PrimaryServer():   
    with SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler) as server:
        server.register_introspection_functions()
       
        def conection(op, x, y, z, t):
            w = xmlrpc.client.ServerProxy('http://localhost:8001')
            
            #Validation
            Methods = w.system.listMethods()
            Methods = Methods[:-3]
            exist = False
            for i in Methods:
               if op == i:
                   exist = True
                   break
            if not exist:
                return "La operación solicitada no existe"
            #Operations
            if op == "addv1":
                return w.addv1(x,y)
            elif op == "addv2":
                return w.addv2(x,y,z)
            elif op == "addv3":
                return w.addv3(x,y,z,t)    
            elif op == "subv1":
                return w.subv1(x,y)
            elif op == "subv2":
                return w.subv2(x,y,z)
            elif op == "subv3":
                return w.subv3(x,y,z,t)    
            elif op == "mulv1":
                return w.mulv1(x,y)
            elif op == "mulv2":
                return w.mulv2(x,y,z)
            elif op == "mulv3":
                return w.mulv3(x,y,z,t)    
        server.register_function(conection, 'com')
    
        # Run the server'w main loop
        server.serve_forever()

# Create server - Operations

if __name__ == '__main__':
    PrimaryServer()
    
