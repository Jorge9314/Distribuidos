# coding=utf-8
import sys
import socket
import random
import time
import struct
import thread

HOST = '127.0.0.1'
RECV_BUFFER = 1024
PORT = 9000

def send_values(socket, num1, num2):
    packet = struct.pack("hh", num1, num2)
    socket.send(packet)
    print("ingrese el primer numero")
    num1 = int(input())
    print("ingrese el segundo numero")
    num2 = int(input())
    time.sleep(5)
    send_values(socket, num1, num2)

def send_position(socket,x,y):
    packet = struct.pack("hh", x, y)
    socket.send(packet)
    # print "My current position is: " + str(x) + "," + str(y) + "\n"
    x += random.randint(-1,1)
    y += random.randint(-1,1)
    time.sleep(5)
    send_position(socket,x,y)


def client():
    addr = (HOST, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(10)
    client_socket.connect(addr)
    
    # Send starting position packet
    # thread.start_new_thread(send_position, (client_socket,0,0))
    thread.start_new_thread(send_values, (client_socket,0,0))
    while 1:

        # Read the local socket
        data = client_socket.recv(RECV_BUFFER)
        print data

if __name__ == "__main__":
    sys.exit(client())