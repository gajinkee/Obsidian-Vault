from socket import *

SRV_ADD = input( "Enter Servers ip to connect: ")
SRV_PORT = int(input("Enter port: "))

sock = socket(AF_INET,SOCK_STREAM)

sock.connect((SRV_ADD,SRV_PORT))
sock.sendall(b"Hello u ")
data = sock.recv(1024)

print("Connected to server....")

