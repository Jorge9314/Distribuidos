from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import random
import _thread
import time
import tempfile 
import os
import socket

PATH = os.path.abspath("./tmp/")
PATHF = os.path.abspath("./files/")
tmpname = '\esteeselarchivitotemporal.txt'

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ('RPC2',)


PORT = 8000
BUFF = 1024
HOST = '192.168.9.124'
HOST2 = '192.168.9.182'

def readingfile(clientsock):
    #print("*Received request to read file*")
    data = clientsock.recv(BUFF).decode("utf-8")
    #print(data)
    f = open ('files/'+data, 'r')
    #print("file opened.")
    for line in f:
        clientsock.send(line.encode("utf-8"))
    #print("End of file")
    time.sleep(0.5)
    clientsock.send("EOF".encode("utf-8"))
    f.close()
    #print("File closed.")
    return data

def sockets():
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.bind((HOST,PORT))
    sckt.listen(5)
    print("*Conected to server*")
    while True:
        clientsock, addr = sckt.accept()
        op = clientsock.recv(BUFF).decode("utf-8")
        if op == 'r':
            data = readingfile(clientsock)
        if op == 'w':
            data = readingfile(clientsock)
            f = open ('files/'+data, 'w')
            print('Waiting modifications...')
            while True:
                stream = clientsock.recv(BUFF).decode("utf-8")
                if stream == "EOF":
                    break
                f.write(stream)
                print (stream)
            f.close()
        if op == "d":
            print("*Received request to read file MODE EDIT*")
            data = clientsock.recv(BUFF).decode("utf-8")
            print(data)
            os.remove(PATHF+"\\"+data)

            
            

#parte servidor del cliente
class client_functions():
    def __init__(self):
        self.s = xmlrpc.client.ServerProxy("http://192.168.9.124:9000")
    def newClient(self):
        listFiles = os.listdir("files")
        print (self.s.newClient(listFiles, PORT))
    def read(self,file):
        filename, portFile = self.s.requestFile(file)
        print ("Connecting... to ",portFile)
        filesocket = socket.socket()
        filesocket.connect((HOST2,portFile))
        print ("Conected\n")
        filesocket.send("r".encode("utf-8"))
        print ("Read request send... ")
        print("Sending filename... ")
        filesocket.send(filename.encode("utf-8"))
        print("OK")
        ft = open('tmp/'+tmpname,"w")
        while True:
            stream = filesocket.recv(BUFF).decode("utf-8")
            if stream == "EOF":
                break
            ft.write(stream)    
        ft.close()
        filesocket.close()
        fd = os.open(PATH+tmpname,os.O_RDONLY)
        os.system(PATH+tmpname)
        os.close(fd)
        os.remove(PATH+tmpname)
        print(self.s.release(file))
    def edit(self,file):
        print("Editing... \n")
        filename, portFile = self.s.requestFile(file)
        print ("Connecting... to ",portFile)
        filesocket = socket.socket()
        filesocket.connect((HOST2,portFile))
        print ("Conected\n")
        filesocket.send("w".encode("utf-8"))
        print ("Write request send... ")
        print("Sending filename... ")
        filesocket.send(filename.encode("utf-8"))
        print("OK")
        ft = open('tmp/'+tmpname,"w")
        while True:
            stream = filesocket.recv(BUFF).decode("utf-8")
            if stream == "EOF":
                break
            ft.write(stream)   
        print('Successfully get the file')
        print('connection closed')
        ft.close()
        os.system(PATH+tmpname)
        ft = open('tmp/'+tmpname, 'r')
        for line in ft:
            filesocket.send(line.encode("utf-8"))
        time.sleep(0.5)
        filesocket.send("EOF".encode("utf-8"))
        ft.close()
        os.remove(PATH+tmpname)
        filesocket.close()
        print(self.s.release(file))
    def delete(self,file):
        print("Delete... \n")
        filename, portFile = self.s.requestFile(file)
        print(self.s.deleteFile(file))
        print ("Connecting... to ",portFile)
        filesocket = socket.socket()
        filesocket.connect((HOST2,portFile))
        print ("Conected\n")
        filesocket.send("d".encode("utf-8"))
        print("Sending filename... ")
        filesocket.send(filename.encode("utf-8"))
        filesocket.close()
        print("Deleted succesfully...")


def main():
    while True:
            op=input("What do you want to do?, Select an option with ID: 1.Read   2.Edit   3.Delete   4.List Files\n: ")
            if op == '4':
                print("Asking for file names...\n")
                d = clientObject.s.filesAvailable(PORT)
                print("Files available:\n")
                for i in d:
                    tupl = d.get(i)
                    print('ID: {}\tFilename: {}\tPermissions: {}\n'.format(i, tupl[0], tupl[1]))
            else:
                fileToOpen=input("Select the ID of file: ")
                fileToOpen=int(fileToOpen)
                exist, notbusy = clientObject.s.searchFile(fileToOpen)
                if exist==True:
                    if notbusy == True:
                        #mirar permisos
                        print('File available...\n')
                        perm = clientObject.s.checkPermissions(fileToOpen,PORT) #devuelve los permisos del archivo.
                        print (perm)
                        if op == '1':
                            if 'r' in perm:
                                clientObject.read(fileToOpen)
                            else:
                                print("You're not allowed to do that.")
                        if op == '2':
                            if 'w' in perm:
                                clientObject.edit(fileToOpen)
                            else:
                                print("You're not allowed to do that.")
                        if op == '3':
                            if 'd' in perm:
                                clientObject.delete(fileToOpen)
                            else:
                                print("You're not allowed to do that.")
                    else:
                        print("The file is already been used.")
                else:
                    print("This file doesn't exist.")
    
_thread.start_new_thread(sockets,())
clientObject = client_functions()
clientObject.newClient()
main()