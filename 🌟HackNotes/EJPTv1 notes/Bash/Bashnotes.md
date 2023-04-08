## Environment 
#bash #scirpt #codenotes 
- Os checks for several file on startup (useful to backdoor a linux user acct)
	- ~/.bashrc
	- ~/bash_login
	- ~/bash_profile
	- ~/bash_logout (on shutdown)

## Environmet vars
- type "env " to view them
-  $PATH contains locations where bash checks for executables (ie whr u can run scripts)
-  cp a program to a location in pp to execute
-  useful commands:
	- ls ping passwd chmod more man
	- "which" -> gives the commands real location /usr/bin/chmod etc
	-  absolute pathing can be used if program not in path (eg /desktop/ping)
	- or relative pathing ( at bin  ../../bin/ping)

## Special Characters

- ~ is the current users home directory (echo ~ ,  returns /root or /user etc )
- * is a wildcard to choose certain file types (ls /etc/* .conf , returns only conf  files)
- Data between `<code> `` </code>` and $() are evaluated before statment ei put code between/variables

## Redirectors
Good for creating oneliners
```bash
#create or overwrite a file containing the commands output
command > file.txt 

#create or append a file containing the commands output
command >>file.txt

//pipe sends output to next command
ls /etc/*.conf | sort

# && means if prev command succeeds proceed to next
# wc -l command checks the number of lines (can be used to count words etc also)
file 'ls /etc/*.conf | sort' > test.txt && cat test.txt |wc -l
--> output: 44
```
  
# Bash scripts
- Any file with bash statments can be executed. but by right **.sh** is the extension
- First line indicates which shell to use #!/bin/bash
- Makes sure file is "chmod +x  filename" to make it executable
- use ./script.sh to run

## syntax
```bash
if [x]: then 
	do
elif [y]: then
	doother
else
	smt
fi
```

Comparators:
| -eq | equal              |
| --- | ------------------ |
| -ne | not equal          |
| -lt | less than          |
| -le | less than or equal |
| -gt | greater than       |
| -ge | greater than or equal                   |

impt: proper spacing in the square bracket is needed
```bash
if [ "$a" -eq "$b" ];then
	echo "they equal";
fi
```
## Loops
```bash
#!/bin/bash
for i in $( ls ); do
	echo item: $i
done

for i in `seq 1 10`;
do
	echo $i
done

//file.txt is sent to the loop and every line in the file is printed
while read line; do echo $line; done < file.txt
```


# GTK Windows
- windows cmd directory slashes are opposite to bash
- bash "/ "  slash
- windows ```\```  backslash
- windows cmd variable are in %variable% (eg echo %PATH% )
- windows set command to set variable. Also to see set variables
- windows output redirection works >> and  >
- cmd1 & cmd2 execute both regardless of result
- cmd1 && cmd2 exec only if cmd1 succeeds
- cmd1|cmd2 send output from first to next
- cmd1||cmd2 executes cmd2 only if cmd1 fails
- Save longs scripts as **.bat files** which are auto executable