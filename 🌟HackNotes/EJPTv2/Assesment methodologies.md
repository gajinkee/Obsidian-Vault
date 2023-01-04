## Information gathering
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