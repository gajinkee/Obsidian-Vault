# Architecture

### On Premises Information Systems Architecture
- Workload 
- Services - MongoDB/MySQL etc
- Virtual Machine - windows/variants of linux
- Virtualisation - Vmware/Hyper-V
- Physical Infrastructure - cables/servers etc
- Physical facility - building/server room
(Typical IT tech stack, see from bttom up)

For cloud,
- Physical facility, Infrastructure and Virtualisation (subscription fee etc) costs borne by cloud providers
- Redundancy provided by cloud provider
Looks more like:
- Workload 
- Services 
- Virtual Machine
- Management plane - someone to manage cloud services
- cloud service - Azure/AWS etc

Cool: There is no "cloud" ur just using someone elses computer....


### Types of cloud services
- Workload
- Services
- Virtual Machine
"Lift and Shift" -> move parts into the cloud service

Examples:
Move virtual machine into cloud -> ==Infrastructure== as a service
(Just using the cloud as a virtual machine host)

Use cloud at a higher level for a service -> ==Platform== as a service
(Hosting webapps/databases etc)

Just push the workload to the cloud -> ==Software== as a service
(Google sheets/Microsoft365 etc)

![[AAS.png]]

### Cloud Providers

AWS
- over 175 prroducts and services

Azure
- as many services but less mature than AWS

Google Cloud service
- pretty big

Other providers
- Tencent & Alibaba
- IBM and Oracle
- Digital Ocean
- private providers


## Why the cloud?

### Economics
Storage and Compute requirements
- Trying to match these reqs difficult on prem
- Dont need to engineer the physical architecture
- Versatile within seconds/minutes

### CapitalExpense vs OperatingExpense
Capacity Expansion:
on prem,
(Capacity Expense)
- purchase equipment/licensing
- replace equipment/renew licenses

Cloud-base,
(OperatingExpense)
- Billed monthly for use
- no equipment purchased
- may need to pay software licensing

Capacity Reduction:
OnPrem -> possibly sell excess eqm
Cloud -> simply reduce monthly cost

### Ways to be billed on cloud
Capacity-based spending
- charge for resources used (virtual machines etc)

Consumption-based spending
	- charge on use. Functions/Lambda/Services/storage


TLDR:
- Cloud can help minimise overhead 

Why maybe not cloud
- existing investment
- On-going operational expense (could be very expensive)
- Data fencing (security for sensitive data)
- Regulatory compliance





# Management

## Tools
1. Web-based
2. Command line (CLI)
3. REST API

For the 3 major providers (ie Azure/AWS/GCP)
1. portal/console -> web interface
2. CLI/Cloud shell available for all -> allows to write scripts to automate
-> note the cloud shells make it easier than downloading the CLI for the cloud provider locally


Demo:
AWS
1) create VM instance (EC2)
2) change settings
3) Delete

1) create bucket (S3)
2) change settings
3) Delete
Overall: quite intuitive. Search for service -> create/tweek -> manage

Azure
Similar but, services are called resources
and the console abit more cluttered

GCP
Similar also...


# Cost savings
- A possible reason why companies choose against cloud

## Cloud pricing models
- Capacity based
-> pay per min etc for a given architecture

- Consumption based
-> eg storage (pay for the amount stored)
or 
-> compute (pay for computing used)

- hybrid based (partly capacity partly consumption)

Note: Providers usually provide free data transfer in but must pay to transfer out!!!

TLDR: Providers have cost calculators. Use them.

### Other things to note
- 3rd party vendor cost (ie premium linux distros)
- Many tweeking needed to optimise costs (eg using less redudndancy in storage)
- 

# Cloud Support/SLAs
(Service Level agreements)
## Responsibilty
- Workload
- Services
- VMs
- Management plane
- Virtualisation
- Physical Infrastructure
- Physical Facility

Note: Everthing below Management plan is responsible by cloud provider / Everything above is ur responsibility

Service level agreements (eg when using software as a service)
Everything below is responsible by cloud, rest by u
D.P. -> Data plane. Everything here is maaged by the customer
![[Screenshot 2023-05-13 193520.png]]

Note:
SLAs are 