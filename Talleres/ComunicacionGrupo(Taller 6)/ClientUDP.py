import socket

UDP_IP = "127.0.0.1"
NPPORT = 5005
CLTPORT = 6005
BUFF =  1024
ADMPORT = 9999
GRPPORT = 7000
NCPORT=3000
process=[]

serversock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP

groupsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP

escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
escucha.bind((UDP_IP,NCPORT))


while True:
    print ('Enviando al servidor.')
    serversock.sendto('suma'.encode('utf-8'),(UDP_IP,CLTPORT))
    dataserver, addrserver = escucha.recvfrom(BUFF)
    dataserver = dataserver.decode('utf-8')
    process=dataserver[1:-1].split(', ')
    for i in process:
        groupsock.sendto('suma'.encode('utf-8'),(UDP_IP,int(i[1:-1])))
    op = input('Ingrese los operandos separados por espacio, ejemplo: 1 2 3 4. =').split(' ')
    for i in process:
        groupsock.sendto(str(op).encode('utf-8'),(UDP_IP,int(i[1:-1])))
    groupdata, addrgroup = escucha.recvfrom(BUFF)
    groupdata = groupdata.decode('utf-8')
    print ('Resultado = ',groupdata)
