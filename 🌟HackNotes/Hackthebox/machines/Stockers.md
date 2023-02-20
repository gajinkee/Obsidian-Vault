Outline:
Fuzz for subdomain. Look for code 200 or 302 (I didnt know 302 gives stuff too)
Login page provided
dirb to see /stocker page needs authorisation
Use burp to intercept and alter content type to application/json
--> Make use of NoSQL injection tricks with json to gain access

/Stocker page shown
Pdf generator is used to give "receipt" 
Using exiftool to check the pdf file downloaded, Some /producer (Skia/PDF m108) is used to generate the pdf

Use a iframe attack on the title of the receipt created changes pdf contents
Use attack to check out /var/www/dev/index.js  (common for node applications) -->app.js,main.js also could have stuff

user password found in index.js --> ssh in using updated known username (assume pwd same)
user priv allows running as root in /usr/bin/node /usr/local/scripts/\*.js

Getting a rev shell from revshell.com for node
Running using path traversal
sudo  /usr/bin/node /usr/local/scripts/../../../../tmp/revshell.js

Root the machine gg

[NoSQL injection - HackTricks](https://book.hacktricks.xyz/pentesting-web/nosql-injection#basic-authentication-bypass)


const dbURI = "mongodb://dev:IHeardPassphrasesArePrettySecure@localhost/dev?authSource=admin&w=1";


17dcdbc47189f3841694c8f3b57ad6fc
6b401c0d9996d723c88357b0f42a34f0
