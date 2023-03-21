from http.client import *
from urllib.parse import *

host = input("Host: ")
port = input("Port: ")
if port == "":
    port = 80

try:
    connection = HTTPConnection(host,port)
    

except ConnectionRefusedError:
    print('connection refused')
