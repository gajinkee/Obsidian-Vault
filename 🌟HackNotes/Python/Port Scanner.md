Uses socket to test if a port is open.
- given an ip addr, test a range of given ports
- does three-way handshake to ensure server is alive
connect_ex() is used to received 0 if successful connection else error

```python
from socket import *

target = input("Server ipv4 addr: ")
portrange = input ("Enter port range(eg 5-200): ")


psplit = portrange.split('-')
lowport = int(psplit[0])
highport = int(psplit[1])

print("scanning host", target, "from port",lowport,'to port', highport)

for port in range(lowport,highport):

    s = socket(AF_INET, SOCK_STREAM)
    status = s.connect_ex((target,port))

    if (status == 0):
        print("***port",port,'-open')
    else:
        print("port",port,"-closed")

    s.close()

```