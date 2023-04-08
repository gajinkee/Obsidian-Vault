“Inspiration does exist, but it must find you working.”
“If there is no struggle, there is no progress.”
"More is lost by indecision than wrong decision.”
“Don’t worry about failure; you only have to be right once.”
“A surplus of effort could overcome a deficit of confidence.”


# Main system
192.168.100.5

pingsweeped
192.168.100.1 (gateway)
192.168.100.50
192.168.100.51
192.168.100.52
192.168.100.55
192.168.100.63
192.168.100.67
192.168.100.5 (me)


# IMPT:
Internal network found
Ethernet adapter Ethernet 4:

   Connection-specific DNS Suffix  . : ap-southeast-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::84d1:5959:fb1:7f92%27
   IPv4 Address. . . . . . . . . . . : 192.168.0.50
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1

arp -a
Interface: 192.168.100.55 --- 0x8
  Internet Address      Physical Address      Type
  169.254.169.123       06-d9-5b-bc-79-be     dynamic   
  169.254.169.254       06-d9-5b-bc-79-be     dynamic   
  192.168.100.1         06-d9-5b-bc-79-be     dynamic   
  192.168.100.5         06-0d-0b-e4-9f-4a     dynamic   
  192.168.100.50        06-17-4e-31-9d-32     dynamic   
  192.168.100.255       ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    
  255.255.255.255       ff-ff-ff-ff-ff-ff     static    

Interface: 192.168.0.50 --- 0x1b
  Internet Address      Physical Address      Type
  192.168.0.1           06-35-57-23-d1-12     dynamic   
  192.168.0.2           06-35-57-23-d1-12     dynamic   
  192.168.0.255         ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    
  255.255.255.255       ff-ff-ff-ff-ff-ff     static 


run arp_scanner -r 192.168.0.0/24
```
[*] ARP Scanning 192.168.0.0/24
[*] IP: 192.168.0.1 MAC 06:35:57:23:d1:12
[*] IP: 192.168.0.2 MAC 06:35:57:23:d1:12
[*] IP: 192.168.0.51 MAC 06:ad:c3:5b:a1:5a
[*] IP: 192.168.0.50 MAC 06:22:42:6d:06:7e
[*] IP: 192.168.0.61 MAC 06:a5:eb:19:a6:16
[*] IP: 192.168.0.57 MAC 06:8b:ad:d7:47:5e
[*] IP: 192.168.0.255 MAC 06:22:42:6d:06:7e

```

192.168.0.50 --> DMZ network

192.168.0.1
192.168.0.2
192.168.0.51
192.168.0.61
192.168.0.57

TCP PORT scan
[+] 192.168.0.51:         - 192.168.0.51:22 - TCP OPEN              --> fwd 1234
[+] 192.168.0.51:         - 192.168.0.51:3389 - TCP OPEN         --> fwd 1235
[+] 192.168.0.51:         - 192.168.0.51:80 - TCP OPEN              --> fwd 1236
[+] 192.168.0.51:         - 192.168.0.51:10000 - TCP OPEN         --> fwd 1237

[+] 192.168.0.61:         - 192.168.0.61:3389 - TCP OPEN         --> fwd 1238

[+] 192.168.0.57:         - 192.168.0.57:22 - TCP OPEN         --> fwd 1239

