![[Pasted image 20230515180512.png]]
# Management Foundations
## Shared Responsibility model
- which part of the stack is the cloud responsible for
-> depends on Paas or Saas or Aaas
Aaas -> responsible for everyt above Managment
Paas -> responsible for the workload only
Saas -> responsible for everyt above workload (ie settings in the webapp etc)

## Security responsibilty
- Provider Responibility:
	- physical sec
	- Infrastucture
	- Identity system security
	- Standards compliance

- Customer Responsibility
	- Identity security
	- Data security (data in rest or transit)
	- Application security
	- Standards compliance

## Resilience Responsibility
- uptime 99.9% (based on SLA)
- Build redundancy/resilience
-> need to known that the cloud can go down (but cloud have services to help)

## Workload Responsibility
- Saas right out the box (no customisations) -> providers responsibility
- ==Good software lifecycle management practices are crucial ==
tldr: Good DevOps security practices are still important

Note:
Standards compliance is a shared responsibility
Identity system security is important in the cloud (How users interact with the system)

# Resource Management
## Managing cloud assets
- maintain code base
- maintain data
- maintain security

Through web interface,
-> lots of nobs to turn

Command line (thru code)
- use templates (eg Azure Templates) -> just tweak certain values and run
- using REST APIs

Monitoring Resources
- cloud providers have tools built in to monitor

### Change management
- its very easy to change things
- So, Governance is critical (ie so the intern doesnt delete a machine)

## Alerts and monitoring
- Resource monitoring (performance etc)
- System Monitoring:
	- Azure Monitor
	- AWS CloudWatch
	- Google Cloud Monitoring
	- Thirdparties:
		- Nagios
		- Splunk
		- PRTG
		
- Proactivce resource managment (dynamic monitoring)
	- Cloud automation (autoscaling etc)
	- Cloud Alerting (fire based-off perfomance/ budget level e
	- 
	- tc)

## Identity and access Management
Root user -> absolute rights

Identity   |     Resource
- Users/Groups |  - Resource

Federated Users
- managed directly by cloud director (from some AD)
- Migrate from elsewhere

## Access Management
Azure
- Users/groups/roles
- Federated users

AWS
- Users/Groups/Permissions
- Federated users
- Policies grant permissions
	- Effect(allow/deny)
	- Action
	- Resources
	- Conditions

GCP
- Users/Groups/Roles/Policies
- Federated users
- Policies link users to roles on resources
	- User
	- Role
	- Resource
	- Condition

Note: Just look at IAM (Identity and Access Management)
