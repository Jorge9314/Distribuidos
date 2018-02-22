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
       
        def conection(op, x, y):
            w = xmlrpc.client.ServerProxy('http://localhost:8001')
            if op == "add":
                return w.add(x,y)
            elif op == "div":
                return w.div(x,y)
            elif op == "sub":
                return w.sub(x,y)
            elif op == "pow":
                return w.pow(x,y)
            elif op == "mul":
                return w.mul(x,y)
            elif op == "sqrt":
                return w.sqrt(x,y)
            elif op == "log":
                return w.log(x,y)
        
        server.register_function(conection, 'com')
        '''
        # Register an instance; all the methods of the instance are
        # published as XML-RPC methods (in this case, just 'div').
        class MyFuncs:
            def div(self, x, y):
                return x // y

        server.register_instance(MyFuncs())
        '''
        # Run the server'w main loop
        server.serve_forever()

# Create server - Operations

if __name__ == '__main__':
    PrimaryServer()
    




