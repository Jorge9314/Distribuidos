import socket
import _thread

UDP_IP = "127.0.0.1"
NPPORT = 5005
CLTPORT = 6005
ADMPORT = 9999
NCPORT=3000
BUFF=1024
LTPORT=4000
process=[]

newprocess = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
newprocess.bind((UDP_IP, NPPORT))

clientsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
clientsock.bind((UDP_IP, CLTPORT))

adminsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP


listsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
listsock.bind((UDP_IP,LTPORT))

def lista():
    while True:
        print('Esperando lista')
        lt, alt = listsock.recvfrom(BUFF)
        lt= lt.decode('utf-8')
        if lt == 'vaciar':
            process=[]
            print (process)

_thread.start_new_thread(lista,())

def handler():
    while True:
        datanewprocess, addrnewprocess = newprocess.recvfrom(BUFF)
        print ('Nuevo integrante.')
        datanewprocess = datanewprocess.decode('utf-8')
        if datanewprocess != '':
            if len(process) == 0:
                adminsock.sendto('admin'.encode('utf-8'),(UDP_IP, int(datanewprocess)))
                process.append(datanewprocess)
                print (process)
                print ('Administrador creado.')
            else:
                adminsock.sendto('added'.encode('utf-8'),(UDP_IP, int(datanewprocess)))
                process.append(datanewprocess)
                adminsock.sendto(str(process).encode('utf-8'),(UDP_IP,ADMPORT))
                print(process)
                print('Proceso añadido.')

_thread.start_new_thread(handler,())
while True:
    print ('Esperando cliente.')
    dataclient, addrclient = clientsock.recvfrom(BUFF)
    dataclient = dataclient.decode('utf-8')
    print ('Recibido: ',dataclient)
    if dataclient == 'suma':
        adminsock.sendto(str(process).encode('utf-8'),(UDP_IP,NCPORT))
