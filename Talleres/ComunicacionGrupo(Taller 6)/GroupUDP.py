import socket
import _thread
import random

GRPPORT=7000
OTPORT=8000
GRPPORT,OTPORT= input('Ingrese 2 puertos para el proceso: entre 7000-8000 separados por espacio = ').split(' ')
GRPPORT=int(GRPPORT)
OTPORT=int(OTPORT)
UDP_IP = "127.0.0.1"
NPPORT = 5005
BUFF =  1024
ADMPORT = 9999
OPPORT =9000
NCPORT=3000
LTPORT=4000
admin=False
operator=False
process=[]

listsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

class handler():
    def __init__(self):
        self.process=[]
    def run(self):
        while True:
            newlist, addradmin = adminsock.recvfrom(BUFF)
            self.process = newlist.decode('utf-8')[1:-1].split(', ')

hand=handler()

def funciones(p):
    while True:
        o = input('Seleccione su opcion.\n1. Listar grupo.\n2. Eliminar proceso.\n3. Eliminar Grupo. = ')
        o = int(o)
        if o == 1:
            for enum,i in enumerate(p.process):
                print (enum, ': ',i)
        if o == 2:
            for enum,i in enumerate(p.process):
                print (enum, ': ',i)
            pos = input('Ingrese la posicion.= ')
            pos = int(pos)
            if pos == 0:
                print('No jodas ome')
            else:
                del p.process[pos]
                listsock.sendto(str(p.process).encode('utf-8'),(UDP_IP,LTPORT))
        if o == 3:
            p.process = []
            listsock.sendto('vaciar'.encode('utf-8'),(UDP_IP,LTPORT))
        



def suma(op):
    r=0
    for i in op:
        r = r + int(i[1:-1])
    return r

newprocesssock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


clientsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
clientsock.bind((UDP_IP, GRPPORT))

groupsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP

newprocesssock.sendto(str(GRPPORT).encode('utf-8'),(UDP_IP,NPPORT))
serverdata, addrserver = clientsock.recvfrom(BUFF)
serverdata = serverdata.decode('utf-8')
newprocesssock.close()


if serverdata == 'admin':
    admin = True
else:
    admin = False
if admin:
    adminsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    adminsock.bind((UDP_IP, ADMPORT))
    _thread.start_new_thread(hand.run,())
else:
    groupsock.bind((UDP_IP,OTPORT))

if admin:
        _thread.start_new_thread(funciones, (hand,))

while True:
    dataclient, addrclient = clientsock.recvfrom(BUFF)
    dataclient = dataclient.decode('utf-8')
    if len(process)>1:
        n = random.randint(0,len(process)-1)
    else:
        n = 0
    if dataclient == 'suma':
        if admin:
            if n == 0:
                op, opaddr = clientsock.recvfrom(BUFF)
                op = op.decode('utf-8')
                op = op[1:-1].split(', ')
                op = suma(op)
                clientsock.sendto(str(op).encode('utf-8'),(UDP_IP,NCPORT))
            else:
                for i,j in enumerate(process[1:]):
                    if i == n:
                        groupsock.sendto('yes'.encode('utf-8'),(UDP_IP,OTPORT))
                    else:
                        groupsock.sendto('no'.encode('utf-8'),(UDP_IP,OTPORT))
        else:
            dataadmin, dataddr = groupsock.recvfrom(BUFF)
            dataadmin = dataadmin.decode('utf-8')
            if dataadmin == 'yes':
                op, opaddr = clientsock.recvfrom(BUFF)
                op = op.decode('utf-8')
                op = op[1:-1].split(' ')
                op = suma(op)
                clientsock.sendto(str(op).encode('utf-8'))
    

