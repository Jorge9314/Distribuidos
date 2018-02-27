TCP_PORT = 5005

import socket
import math

SEPARATOR = '##$#'

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
BUFFER_TRAMA_SIZE = 2048
MESSAGE_GET_LIST = 'GET LIST'
MESSAGE_GET_FILE = 'GET FILE'

# Inicializando socekt
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando Socket
s.connect((TCP_IP, TCP_PORT))

# Solicitando lista de archivos a servidor
s.send(MESSAGE_GET_LIST.encode('UTF-8'))

# Recibiendo y mostrando lista
dataList = s.recv(BUFFER_SIZE).decode('UTF-8')

nameFiles = dataList.split(',')
print(nameFiles)
for index in range(0, len(nameFiles)-1):
    nameFile = nameFiles[index].replace(',', '')
    print("%i. %s" % (index, nameFile))

fileSelect = int(input('Ingrese el número del archivo a traer: '))

if fileSelect >= len(nameFiles):
    s.close()
    raise SystemError(1)

fileNameSelected = nameFiles[fileSelect]

s.send(MESSAGE_GET_FILE.encode('UTF-8'))
s.send(str(fileSelect).encode('UTF-8'))

NUM_TRAMAS = float(s.recv(BUFFER_SIZE).decode('UTF-8'))
NUM_TRAMAS = math.ceil(NUM_TRAMAS)

print('Num Tramas: %i' % NUM_TRAMAS)

TRAMAS = ['']*NUM_TRAMAS
num_trama = 0
while True:
    data = str(s.recv(BUFFER_TRAMA_SIZE).decode('UTF-8'))
    MSG, TRAMA, NUM_TRAMA = data.split(SEPARATOR)
    num_trama += 1
    if MSG != 'END FILE':
        TRAMAS[int(NUM_TRAMA)] = TRAMA
    else:
        break

TRAMA = ''

for TRAMA_ELEMENT in TRAMAS:
    TRAMA += TRAMA_ELEMENT

a = open("rcv-" + fileNameSelected, 'w')
a.write(TRAMA)
a.close()

print('FILE RECEIVED')

s.close()