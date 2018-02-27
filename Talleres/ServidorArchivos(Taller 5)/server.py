TCP_PORT = 5005

import socket
import math
import time

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
BUFFER_TRAMA_SIZES = 1038
SEPARATOR = '##$#'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

listFiles = [
    '1.txt',
    '2.txt',
    '3.txt'
]

def getStrListFiles():
    tempStr = ''
    for fileName in listFiles:
        tempStr += fileName + ","
    return tempStr

conn, addr = s.accept()

getFileNumber = False
fileSelected = -1
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break

    data = data.decode('UTF-8')
    
    if data == 'GET LIST':
        conn.send(getStrListFiles().encode('UTF-8'))
    elif data == 'GET FILE':
        getFileNumber = True
    elif getFileNumber:
        fileSelected = int(data)
        getFileNumber = False
        file = open(listFiles[fileSelected], 'r')
        
        lines = file.read()
        numCaracthers = len(lines)

        file.close()

        NUM_TRAMAS = math.ceil(numCaracthers/BUFFER_SIZE)
        conn.send(str(NUM_TRAMAS).encode('UTF-8'))

        time.sleep(1)

        for NUM_TRAMA in range(0, NUM_TRAMAS):
            LINE = lines[NUM_TRAMA*BUFFER_SIZE:(NUM_TRAMA+1)*BUFFER_SIZE]
            NUMBER_TRAMA = str(NUM_TRAMA)

            if NUM_TRAMA < 10:
                NUMBER_TRAMA = "0%i" % NUM_TRAMA

            msg = "FILE" + SEPARATOR + LINE + SEPARATOR + NUMBER_TRAMA
            conn.send(msg.encode('UTF-8'))
            time.sleep(1)

        conn.send(str("END FILE"+SEPARATOR+"B"+SEPARATOR+"XX").encode('UTF-8'))

conn.close()
