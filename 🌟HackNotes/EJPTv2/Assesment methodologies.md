# Information gathering
#infogathering

## Passive info gathering (legal public info)
### website recon & footprinting:
whatis --> check the use of a function (eg whatis host)
host --> DNS lookup utility find the ip for given domain name

important directories to look for info:
/robots.txt --> used to specify directories that search engines web crawlers will disregard
/sitemap.xml --> provides search engines an organised way of indexing a site

wappalyzer --> used to see technologies used by site
whatweb --> tool to see check tech used by sites
webhttrack --> can be used to download and mirror unsecure sites

### whois Enumeration
--> gives bunch of info on site  (Admin/domain emails city/state address registrant contact etc)

### Netcraft
--> gather info about a domain (like whois,but also the technology like wappalyzer)
Note: VPN services like cloudflare means not all info is correct, some redacted by cloudflare

--> Exploit history can also be found 

### DNSrecon / DNS dumpster
--> dns info, mail server info

## WAF
wafwoof --> checks if a webapp is protected by firewall

### Google Dorks 
google tricks,
site:somesite.com --> search only the site
inurl:admin
intitle: index of --> common vulnerability of webservers not configured properly(directory is public)
site: "star".ine.com --> searches for subdomains
filetype: pdf, xls
inurl:auth_user_file.txt
inurl:passwd.txt

google hacking database --> gives some dork templates to search for vulnerable sites
waybackmachine....cool i guess?? to see old info possibly leaked 

### Email harvester
theharvester --> uses public info to find emails, hosts, ips, subdomains (works like netcraft etc)
eg:
theHarvester -d hacks.com -b bing,google,linkedin
Gather emails to password spray different account (when users reuse pwd for diff sites)

### Password Spray
haveibeenpwned.com --> use to see if email/number has been compromised 


## Active info gathering

### Zone Transfer
--> provides a good map of the network layout on the target network

DNS records:
A - ipv4
AAAA - ipv6
NS - reference to the domains nameserver
MX - dns to a mail server
CNAME - used for domain aliases
TXT - Text record
HINFO - displays host info
SOA - domain authority
SRV - service records
PTR - resolve ip to hostname (reverse DNS basically)

Tools:
dnsrecon -d {name of domain}
dnsenum
fierce -dns {domain name} ------> eg fierce -dns zonetransfer.me

sudo vim /etc/hosts --> "local" DNS records. List of hostnames and ip addr
	--> can add your router config ip with something like router.home.admin to make it searchable in browser
note: For zone transfer to work it must be enabled on the networks DNS server


### NMAP
Standard nmap stuff
gtk stuff:
-sn ping sweep
-Pn port scan w/o checking if host is alive (do this for windows systems as they usually block icmp reqs)
-F fast scan. only the top10o popular ports
-sC run some nmap scripts to identify more info about ports
-A aggressive scan. Uses -sV -sO and -sC
-T<0-5> speed up time of scan. Higher is faster
| T0       | T1     | T2     | T3     | T4         | T5     |
| -------- | ------ | ------ | ------ | ---------- | ------ |
| Paranoid | Sneaky | Polite | normal | Aggressive | Insane | 

-oN outputs to a new file.....(use it!!!)
-oX outputs into a XML format. Useful for metapsloit


# FootPrinting and Scanning

## ARP scan
arp-scan
eg:
sudo arp-scan -I tap0 -g 10.142.111.0/24
--> asks for the mac adresses of all the hosts connected to the subnet on interface tap0
--> note arp-scan doesnt show your own ip and mac address



## ICMP scan
-Ping
	-echo request...wait for reply
-fping (ping but for multiple)
eg:
	fping -I tap0 -g 10.142.111.0/24 -a
	--> outputs all hosts that are alive but includes the error messages.
	fping -I tap0 -g 10.142.111.0/24 -a 2>/dev/null
	--> redirects error (shown as output 2) to /dev/null blackhole
	--> note: stdin is 0, stdout is 1, stderr is 2
-Traceroute
-NMAP (uses more than just ICMP can check wireshark to see)
eg:
	nmap -sn 10.142.111.0/24
-zenmap (GUI version of NMAP)

IMPT: ARP and FPING shows different hosts alive sometimes as not all hosts replys to ping msgs

## Host discovery
--> nmap compares the hosts signature to a databse to guess the OS and services etc

--> NMAP scans for UDP are slow but can be sped up 
eg T5
Note Windows blocks certain icmp scans .... use  -Pn flag on nmap

GTK:
nmap UDP service scan -sUV
usually the open UDP ports are -p1-250 (a lot of guess work for the srervices tho)

# Enumeration
#services #enums 
## Servers and Services
A server is any computer that provides a service (a programme that give functionality)
Common services provided by servers: File sharing, Deliver/collect emails, host a website

File sharing : Server Message Block (SMB) ,Network File system(NFS)
File transfer (upload/download) :  File Transfer protocol (FTP) 
Command execution: Secure Shell Protocol (SSH)
Hyper text: HTTP
Database: MySQL, MSSQL

## SMB
Generic term: Common Internet File System (CIFS)
Windows implimentation of a file system
Common ports on windows machines: 135, 139, 445, 3389
SMB port: 445 and usually Netbios port: 139 is used to set up session for SMB
Version: Windows server etc
use NMAP -sC scripts to get more info

How its usually used:
```powershell
net use z: \\10.4.17.133\c$ smbserver_password /user:administrator
```
This adds the drive to windows network folder. Seen in windows file explorer as a shared drive.

To delete sessions
```powershell
net use * / delete
```


## FTP

## SSH

## HTTP

## SQL
