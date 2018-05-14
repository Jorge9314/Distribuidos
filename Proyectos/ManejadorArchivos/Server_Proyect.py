from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client 
import random
import _thread
import time

PORT = 9000
perm = ['n','r','rwd']


class nn():
    def __init__(self):
        self.listFiles=[]  #ID - Filename - port client - status
        self.clients={}
        self.idnum = 0
    def newClient(self,listf,port):
        self.permissions(port,listf)
        return ('Added.')
    def permissions(self,port,listf):
        if len(self.clients)==0:
            tmp = {}
            for i in listf:
                tmp[str(self.idnum)] = [i,'rwd']
                self.listFiles.append([self.idnum, i,port,0])
                self.idnum += 1    
            self.clients[port] = tmp
        else:
            tmp = {}
            tmp2 = {}
            for i in self.listFiles:
                print(i[0])
                tmp[str(i[0])] = [i[1],random.choice(perm)]
            self.clients[port] = tmp
            for i in listf:
                tmp[str(self.idnum)] = [i,'rwd']
                self.listFiles.append([self.idnum,i,port,0])
                for k in self.clients.keys():
                    if k != port:
                        tmp2[str(self.idnum)] = [i,random.choice(perm)]
                        self.clients[k].update(tmp2)
                self.idnum += 1
    def filesAvailable(self,port):
        print (self.clients[port])
        return self.clients[port]
    def searchFile(self,id):
        for i in self.listFiles:
            if id == i[0]:
                if i[3] != 1:
                    i[3] = 1
                    return (True, True)
                else:
                    return (True, False)
        return (False, False)
    def checkPermissions(self,file,port):
        return self.clients[port][str(file)][1] #Retorna los permisos
    def requestFile(self,file):
        for i in self.listFiles:
            if file == i[0]:
                return (i[1],i[2])
    def deleteFile(self,file):
        print (file)
        for i in self.listFiles:
            print(i)
            if file == i[0]:
                self.listFiles.remove(i)
            print (self.listFiles)
        for i in self.clients:
            print (i)
            print (self.clients[i][str(file)])
            self.clients[i].pop(str(file))
        return 'Deleted from server database'
    def release(self,file):
        for i in self.listFiles:
            if file == i[0]:
                i[3] = 0
                return "Released."
        else:
            return "Error"




class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ('RPC2',)

servidor = nn()

server = SimpleXMLRPCServer(("192.168.9.124", PORT), requestHandler=RequestHandler)
server.register_introspection_functions()
server.register_function(servidor.newClient, "newClient")
server.register_function(servidor.permissions, "permissions")
server.register_function(servidor.filesAvailable, "filesAvailable")
server.register_function(servidor.searchFile, "searchFile")
server.register_function(servidor.checkPermissions, "checkPermissions")
server.register_function(servidor.requestFile, "requestFile")
server.register_function(servidor.deleteFile, "deleteFile")
server.register_function(servidor.release, "release")
server.serve_forever()