import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("Las operaciones existentes son: SUMA, RESTA, MULTIPLICACION", end='\n')
print("SUMA - para ejecutar suma - addv1(num1, num2) - addv2(num1, num2, num3) - addv3(num1, num2, num3, num4)", end='\n')
print("RESTA - para ejecutar resta - subv1(num1, num2) - subv2(num1, num2, num3) - sub3(num1, num2, num3, num4)", end='\n' )
print("MULTIPLICACION - para ejecutar multiplicacion - mulv1(num1, num2) - mulv2(num1, num2, num3) - mulv3(num1, num2, num3, num4)", end='\n')
op = input ("Ingrese el tipo de operacion a realizar: ")
x = y = z = w = 0
if (op == "addv1" or op == "subv1" or op =="mulv1"):
    x = (int)(input ("Ingrese el primer numero "))
    y = (int)(input ("Ingrese el segundo numero "))
elif (op == "addv2" or op == "subv2" or op =="mulv2"):
    x = (int)(input ("Ingrese el primer numero "))
    y = (int)(input ("Ingrese el segundo numero "))
    z = (int)(input ("Ingrese el tercer numero "))
elif (op == "addv3" or op == "subv3" or op =="mulv3"):
    x = (int)(input ("Ingrese el primer numero "))
    y = (int)(input ("Ingrese el segundo numero "))
    z = (int)(input ("Ingrese el tercer numero "))
    w = (int)(input ("Ingrese el cuarto numero "))
print (s.com(op, x, y, z, w)) 