
samba recon basics 2:
user:[john] rid:[0x3e8]
user:[elie] rid:[0x3ea]
user:[aisha] rid:[0x3ec]
user:[shawn] rid:[0x3e9]
user:[emma] rid:[0x3eb]
user:[admin] rid:[0x3ed]

192.213.93.3
samba recon 3:

192.210.95.3

recon 4:
192.152.85.3
- Success: ' 
- jane:abc123
- admin:password1

ProFTP recon:
192.155.248.3
ProFTPD 1.3.5a
hydra results:
[21][ftp] host: 192.155.248.3   login: sysadmin   password: 654321
[21][ftp] host: 192.155.248.3   login: rooty   password: qwerty
[21][ftp] host: 192.155.248.3   login: demo   password: butterfly
[21][ftp] host: 192.155.248.3   login: auditor   password: chocolate
[21][ftp] host: 192.155.248.3   login: anon   password: purple
[21][ftp] host: 192.155.248.3   login: administrator   password: tweety
[21][ftp] host: 192.155.248.3   login: diag   password: tigger

1. 260ca9dd8a4577fc00b7bd5810298076
2. e529a9cea4a728eb9c5828b13b22844c
3. AUDITOR: 098f6bcd4621d373cade4e832627b4f6

vsftp
192.105.16.3

ssh basic:
192.158.121.3
SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.6

encryption_algorithms: (6)
| chacha20-poly1305@openssh.com |
| ----------------------------- |
| aes128-ctr                    |
| aes192-ctr                    |
| aes256-ctr                    |
| aes128-gcm@openssh.com        |
| aes256-gcm@openssh.com        |

ssh dic atack:
192.16.206.3
hydra attack
host: 192.16.206.3   login: student   password: friend
administrator:sunshine
success!!
'root:attack' 'uid=0(root) gid=0(root) groups=0(root) Linux victim-1 5.4.0-125-generic #141-Ubuntu SMP Wed Aug 10 13:42:03 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux '