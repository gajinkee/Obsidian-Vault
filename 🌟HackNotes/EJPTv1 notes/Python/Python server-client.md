## sockets

Just give a valid address and port and boom!
```python
from socket import *

#Create given server addr and port from user
SRV_ADDR = input ("Server ip addr: ")
SRV_PORT = int(input ("Server port:"))

#create a new socket using default ipv4 tcp conenction
sock = socket(AF_INET, SOCK_STREAM)

#binds the socket to provided address and port/ receives conenctions for this addr and port
sock.bind((SRV_ADDR, SRV_PORT))

#listens for incoming connnections max number is 1 client
sock.listen(1)
print("SERver starto! Waiting connections...")

#accepts incoming connections returning 2 values
#connection is the socket object to send and receive data
#address contains clients address bound to the socket
connection, address = sock.accept()

#prints address of connected client
print('Client connected with address:', address)

#infinite loop to receive all msgs
while True:
 data = connection.recv(1024)
 if not data: break
 connection.sendall(b'--Message Received --\n')
 print(data.decode('utf-8'))
connection.close()

```
![[Pasted image 20221020181717.png]]

# Simple Client

```python
from socket import *

  

SRV_ADD = input( "Enter Servers ip to connect: ")

SRV_PORT = int(input("Enter port: "))

  

sock = socket(AF_INET,SOCK_STREAM)

  

sock.connect((SRV_ADD,SRV_PORT))
#b"msg" encodes the msg
#another way is message.encode()

sock.sendall(b"Hello u ")

data = sock.recv(1024)

  

print("Connected to server....")
```
