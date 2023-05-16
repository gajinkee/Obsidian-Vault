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