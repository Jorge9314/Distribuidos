import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("Las operaciones existentes son: SUMA, RESTA, MULTIPLICACION", end='\n')
print("SUMA - para ejecutar suma - add", end='\n')
print("RESTA - para ejecutar resta - sub", end='\n')
print("MULTIPLICACION - para ejecutar multiplicacion - mul", end='\n')
op = input ("Ingrese el tipo de operacion a realizar: ")
n = list(map(int, input("Ingrese los numeros, separados por ',': ").split(',')))

if len(n)==1:
    print("Minimo dos numeros")
elif len(n)==2:
    op = op+"v1"
elif len(n)==3:
    op = op+"v2"
elif len(n)==4:
    op = op+"v3"
print (s.com(op, n))