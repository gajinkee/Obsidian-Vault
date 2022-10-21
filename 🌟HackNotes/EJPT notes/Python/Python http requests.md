```python
from http.client import *

host = input("host: ")
port = input("port(default80): ")
testurl= input("Check if this url exist (eg /index.php): ")


if port == "":
    port = 80
  

try:
    connection = HTTPConnection(host,port)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("Available methods are: ",response.getheader('allow'))

	#test if a given url exists
    connection.request('GET',testurl)
    response = connection.getresponse()

    if response.status == 200:

        print("Resource exists")
        
    connection.close()

except ConnectionRefusedError:
    print('connection refused')
```