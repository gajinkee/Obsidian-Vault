Identity/Security/Compliance

# Fundamentals
## Shared responsibility
- the same diagram
![[Pasted image 20230515180512.png]]

-> management plane is the interface the cloud gives the user to interact with the cloud
Basically 3 levels:
Data Plane
Control Plane (CLI, cloud control panel)
Cloud Provider

## Securing cloud resources
- Of the 3 levels, 
-> still need to secure your own data/applicatns (ie with a IAM)
-> also secure the cloud

## Defence in depth

- No single security control that is 100% fool proof
- Add as many security controls as u can
-> every control adds to cost adds to overhead

Depth:
Public network
Local network
Operating system
Service
Workload
![[Pasted image 20230516122403.png]]

- 3 A's - Authorisation, Authentication, Auditing
- NACL - network access control lists
- Encryption of data in transit and rest

# Attacks
## Targets
### Identities
- SaaS identities (creds to login to software)
- Cloud platform identities (creds for cloud platform)
- Data plane identities (creds for the workload)

### Data
- Eg S3 bucket (BLOB storage)
- relational/ non-relational data

### Services
- Email 
- Control plane service (eg Automation -> DDOS to autoscale to incur costs)
- API services

## Attack methods
### Misconfigs
- intentional or inadvertent
- For datastores/services (public API etc)
- Allowing unauthorised access

### Account hijacking
- bruteforce/password spraying (use the same known password for multiple users)
- credential stuffing (use a known set of creds and try on all services)

### Service hijacking
- steal the service token etc used by clients to authenticate with server
- RedLine stealer eg

### Malware
- Implant bad code
Eg in open libraries (CI/CD attack)


# IAM
- identity access management

### Access/manage cloud resource
- think of the cloud as a control panel
-> clients/users need an "identity"
-> cloud have stuff for them to asses

### Manage Cloud users
- minimise "root" privs
- Organise into groups (via department etc)
- use dynamic managment when possible (allow access to users in specific scenarios eg time or place)
- Audit and review user configuration (zombie accts / new permissions etc)

### Manage Resource Access
- always apply least priv (give lowest rights possible)
- use dynamic policies (temporary privs etc)
- Audit resource access (not always practical to monitor every user, so better to audit resource/activity)
- seperate control plane and data plane (dont use Active dir system for managing cloud and managing service)

## Cloud Identity protection

### identity sources
- Identity service (IAM in AWS, AAD azure active direvtory)
Types:
Cloud users -> in the IAM specifically for the cloud service
Guest users -> from others IAMs allowing them to acces the cloud service (eg Google login)

Hybrid users -> Active directory (eg Azure AD) elsewhere is synced into id for login
-> user id is managed externally but auth happens in Azure AD
Users can come from completely external sources on premises somewhere else (non-cloud etc) from an active directory somewhere

Federated users -> similar to hybrid but auth happens thru the cloud externally (proven id is sent as a token)
![[Pasted image 20230517190659.png]]

### Identity vulnerabilities

	Account Vulnerability | Login Vulnerability
	- weak password | - IP address and location anomalies
	- Leaked creds | - Password spraying
	- General threat intel | Brute force attacks

### Manage Identities
IGRR

Identity -> Groups -> Roles -> Resource
- Priveledged access
- Rights management
- Password managment
- Dynamic access management (based on login location etc)
![[Pasted image 20230517191232.png]]

### Id protection service
- all cloud providers provides multi-factor Authentication
![[Pasted image 20230517191444.png]]

### Id best practice
- apply password policy
- implement conditional access
- implement MFA
- Monitor
- Audit unused accounts

# Response to compromise
## 5 R's
Revoke
Reset
Review
Remediate
Return

### Revoke
- revoke permissions fro compromised id
- Isolate the id from data services and resources

### Reset 
- Session tokens
- API keys
-  Resource access keys
- any form of trusted id

### Review
- review with cybersec team
- review with business partners
- determine impact

### Remediate
- training (eg user negligence)
- process improvement
- define forward plan of action
- report as needed (corporate or regulatory reporting)

### Return
- return operating state
- monitor



# Data protection

Types of cloud data (ordered from most to least vuln)
![[Pasted image 20230518171038.png]]

Notes:
- managed data is not cloud specific (eg MongoDB, MySQL)
- proprietary (databases provided by the cloud providers)

## Protect data at rest
- network controls
- permissions
- encryption
- HSM (hardware security module) -> like an ISAC card

- Replication
- Backups

## Protect data in transit
- encrypt

## Connecting to data
client -> DB (eg MySQL controlled from the cloud)
Note that thrs additional endpt on the DB for cloud compared to on-premises -> additn attack vector to take care of

## Data protection best practices
- Limit access
	-> resource
	->Data network
- Always encrypt
 -> at rest
 -> in transit
 -> end-to-end

- Protect from failure
	-> replicate
	-> backup

- Audit

# Network protection
### Cloud provider network protection
offers:
- DDOS protection
- General threat protection
The cloud providers have large datacentres to protect
(protect virtualized infrastructure/Physical Infrastructure/Physical facility)

## Tenant network protection (you)
![[Pasted image 20230518173941.png]]
Basic architecture above:
virtual cloud subnet -> virtual machine(EC2) connected

- perimeter defence (firewalls)
Protect at the Subnet level -> network ACL
individual EC2 instances -> rules, security group

Example for Azure
![[Pasted image 20230518174337.png]]

Example for GCP
![[Pasted image 20230518174412.png]]

The system can be locked down as such using the given services(diff names same thing) by the cloud
Limits access to the resource from outside (only allows from the instance)
![[Pasted image 20230518174659.png]]

Some network security services by cloud providers (most paid)
![[Pasted image 20230518174755.png]]
- some are abit like insurance
- DDoS protection / firewalls etc

### Network protection best practices
- leverage provider tools (ACLs, firewalls etc)
- Limit public attack surface
- Monitor
- Alert atypical usage patterns
- Have a playbook






# Compute protection
## Infrastruture compute protection
- Patch management (updates etc)

- Attack surface minimisation (run only essential services / dont leave unused ports open)
-> Eg Windows server instance running for MySQL as a sql server. Should not have file share enabled.

- OS hardening
-> setup the OS to be most secure (look for an image that is a hardened version)

- Resource protection (special to the cloud)
-> resource is managed at the control plane level seperate from the OS
-> only allow authorised users to access the control (simillar to physical protection on-prem)

- Monitoring

## Infrastructure Compute protection
- mulitple instances

## Platform Compute protection
Eg
Kubernates, Webapp, Function app provided from Azure
- It is in cloud providers best interest to protect their platform
- There are options (eg Encrpytion/Autopatching) but core compute protection responsibility is on cloud provider

## Patching
- Infrastructure as a service
-> OS - automated option in AWS and Azure (or worst case manual patching)
-> service (web server/db server etc)

- Platform as a service
-> patched by provider (only the workload is on us)

## Confidential Compute
![[Pasted image 20230518212557.png]]
- Basically a way to protect data while it is being computed
-> Data being computed is done in an Enclave
-> Enclave is a trusted exec environ that isolates data being computed from everything. Even the OS cant access it. 
(Only the processor is used)
-> Available only for specific machine sizes on the cloud
-> Enclave could be physical or virtual isolation (but preferably physical)

# Compute Monitoring
- built-in monitoring is availble for all cloud platforms (platform monitor)
- 3rd party monitoring by agent is available
- Monitoring can be aggregated from both types also


# Compliance and Regulation

Disclaimer: Mostly US based support here but should apply to SG(??)

## Cloud regulatory support 
- Cloud tools
- Documentation
![[Pasted image 20230518213818.png]]

## Tenant responsibility
- Understand regulatory requirments
- Document provider compliance with regulation
- Implement your responsibility
- Use the provider tools to achieve, maintain, and document compliance

## Common Protected data
- types of data
-> Personal Identifiable Information (PII)
-> Health Care (Protected Health Information)
-> Financial service (PII, PCI-DSS, Sarbanes Oxley)

- Business Relevance
-> Intellectual property
-> legal consideration
-> business reputation

- Regional Considerations
-> GDPR - EU   --> Critical for companies wanting to expand in EU
-> California (interesting has its own set of rules diff from US)
-> US Federal Protected Data Type (research, tech, weapons etc)


Demo:
The cloud providers have links for regulation to learn more
Some even show which services are compliant to the required regulation

Can check based on country/Specific compliance
