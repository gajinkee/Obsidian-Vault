
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


Apache recon:
192.50.79.3

mysql recon:
---+------------+-----------+-----------------------------+------------+---------------------+
|  1 | Gregoria   | Lowe      | gutmann.rebekah@example.net | 1982-03-09 | 1983-01-11 11:25:43 |
|  2 | Ona        | Anderson  | ethelyn02@example.net       | 1980-06-02 | 1972-05-05 07:26:52 |
|  3 | Emile      | Lakin     | rippin.freda@example.com    | 1979-04-06 | 2010-05-30 20:03:07 |
|  4 | Raul       | Barton    | mschiller@example.com       | 1976-05-06 | 1979-02-08 12:32:29 |
|  5 | Sofia      | Collier   | rodrigo34@example.net       | 1978-06-09 | 1991-05-01 10:02:54 |
|  6 | Wellington | Fay       | jared98@example.com         | 2011-08-11 | 1992-05-27 23:20:20 |
|  7 | Garnet     | Braun     | hickle.howell@example.net   | 1990-04-27 | 2010-04-13 09:48:36 |
|  8 | Alessia    | Kuphal    | skiles.reggie@example.net   | 1978-04-06 | 2014-08-22 21:23:00 |
|  9 | Deven      | Carroll   | savanah.zulauf@example.net  | 2007-02-15 | 1998-02-16 11:45:32 |
| 10 | Issac      | Stanton   | ozella10@example.net        | 2013-10-13 | 1976-12-09 13:18:45 |
+----+------------+-----------+-----------------------------+------------+-------------------
