import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

op = input ("Ingrese el tipo de operacion a realizar: ")
x = (int)(input ("Ingrese el primer numero"))
y = (int)(input ("Ingrese el segundo numero"))
print (s.com(op, x, y)) 
