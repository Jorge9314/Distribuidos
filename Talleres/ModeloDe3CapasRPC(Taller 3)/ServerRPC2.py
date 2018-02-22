from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class OperationServer():
    with SimpleXMLRPCServer(("localhost", 8001),
                            requestHandler=RequestHandler, allow_none=True) as serverOp:

        serverOp.register_introspection_functions()
        # Register pow() function; this will use the value of
        # pow.__name__ as the name, which is just 'pow'.
        serverOp.register_function(pow)
        serverOp.register_function(lambda x,y: x+y, 'add')
        serverOp.register_function(lambda x,y: x//y, 'div')
        serverOp.register_function(lambda x,y: x-y, 'sub')
        serverOp.register_function(lambda x,y: x*y, 'mul')

        # Register a function under a different name

        def sqrt_function(x,y):
            return math.pow(x, 1/y)

        def log_function(x,y):
            return math.log(x,y)

        serverOp.register_function(sqrt_function, 'sqrt')    
        serverOp.register_function(log_function, 'log')

        # Run the server's main loop
        serverOp.serve_forever()


if __name__ == '__main__':
    OperationServer()