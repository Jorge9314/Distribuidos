from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

class OperationServerAdd():
	def __init__(self):
		serverOp=SimpleXMLRPCServer(("localhost", 8001),requestHandler=RequestHandler)
		serverOp.register_introspection_functions()
		# Register pow() function; this will use the value of
		# pow.__name__ as the name, which is just 'pow'.
		serverOp.register_function(lambda x,y: x+y, 'addv1')
		serverOp.register_function(lambda x,y,z: x+y+z, 'addv2')
		serverOp.register_function(lambda x,y,z,w: x+y+z+w, 'addv3')


		# Run the server's main loop
		serverOp.serve_forever()

class OperationServerSub():
	def __init__(self):
		serverOp=SimpleXMLRPCServer(("localhost", 8001), requestHandler=RequestHandler)
		serverOp.register_introspection_functions()
		serverOp.register_function(lambda x,y: x-y, 'subv1')
		serverOp.register_function(lambda x,y,z: x-y-z, 'subv2')
		serverOp.register_function(lambda w,x,y,z: w-x-y-z, 'subv3')
		# Run the server's main loop
		serverOp.serve_forever()
class OperationServerMul():
	def __init__(self):
		serverOp=SimpleXMLRPCServer(("localhost", 8001), requestHandler=RequestHandler)
		serverOp.register_introspection_functions()
		serverOp.register_function(lambda x,y: x*y, 'mulv1')
		serverOp.register_function(lambda x,y,z: x*y*z, 'mulv2')
		serverOp.register_function(lambda w,x,y,z: x*y*z*w, 'mulv3')
		# Run the server's main loop
		serverOp.serve_forever()


if __name__ == '__main__':
	
	tipo = input("Ingrese el tipo se servidor de Operaciones a Crear - (Add - Sub - Mul)")
	if tipo == "Add":
		OperationServerAdd()
	elif tipo == "Sub":
		OperationServerSub()
	elif tipo == "Mul":
		OperationServerMul()
	else:
		"El servidor solicitado no existe"