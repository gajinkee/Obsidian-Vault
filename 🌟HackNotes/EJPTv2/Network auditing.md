# Auditing fundamentals

## Cyber basics:

CIA triad
Confidentiality:
For ur eyes only
Integrity:
Only authorised changes
Availability:
Service must be usable
--> Balance the 3 to meet business needs

Defence in depth
- use multiple layers of security for holistsic protection
Inclusive but not limited to:
1. administrative controls
	1. policy
	2. Procedures
2. Technical controls
	1. Network
	2. Software
	3. Hardware
3. Physical controls

--> different frameworks exist

Risk management (money plays a big factor)
- cost to secure
- cost if poorly secured
- issurance
- lawsuit
- loss of revenue if intelectual property is lost
--> Cost-benefit analysis

#### Compliance
Some risks by companies are allowed
Other times, these risks are not allowed (must comply)
Regulations (not limited to):
- PCI DSS
	- Payment Card Industry Data Security Standard
	- mandated by cardbrands (master card,visa etc)
	-  control cardholder data to reduce fraud etc
	- Company will be fined by PCI if the
- HIPAA
	- US regulations for use and disclosure for healthcare data
	- Protected Health Information (PHI)
	- Defense in depth safeguard must be in place
- GDPR
	- Data protection in the EU for anyone setting up in EU
- CPPA
	- California Consumer Privacy Act
- SOX
	- Sarbanse-Oxley Act of 2002
	- Mandates practices in financial keeping and reporting (Not limited to cyber per se)
	- Requires strong internal control processes over the IT infrastructure and applications that house financial info
tldr:
for companies that want to operate in these verticals (heathcare/finance/a certain country), companies must comply to regulations or get fined.
Local examples: MAS for fintech in sg, PDPC for PDPA

#### Implementation of regulations/compliance
--> done using frameworks usually

Some common frameworks:
- ISO/IEC 27000
	- International Organisation for Standardisation
	- Internal Electrotechnical Commission
	- Broad scope covers more than privacy/confidentiality/IT
	- Applicatble to many types of organisations
	- ISO/IEC 27001 --> Basic guidelines
	- ISO/IEC 27002 --> Code of practice on how to implement the guidelines given
- COBIT
	- Control Objectives for information n related tech
	- created by ISACA for IT and IT governance
	- Business focused, defines generic processes for management of IT
- NIST
	- National Institute of standards and tech
	- US government requires for all US federal info
	- Developed by US govt for themselves but can be used by others
- CIS
	- Center for Internet Security
	- 18 prioritised safeguards to mitigate cyber attacks
	- defence-in-depth model to help prevent and detect malware
	- Offers a free software tool to access CIS-CSAT
- CMMC
	- Cybersecurity model certification
	- Requires 3rd party to access maturity of security (5 maturity levels and 17 capability domains)
- ASD
	- Australian cybersecurity Centre (4 maturity levels 8 security controls)
	- Essential 8 designed to protect Microsoft Windows-based internet connected networks

#### Auditing
--> company to check if they follow the guidelines
through:
- Interviews
- Paperwork (Logs, records, documentation )
- Technical assesment, Auditing automated tools (Nesses scan, solarwinds)
- Take notes on findings (mindmap? etc)
Reports (u r paid for the report not the pentest...)
Note: Not every audit has a pentest

#### Auditing in Practice
Some tools from the US Department of defence for CMMC standard

Security Content Automation Protocol (SCAP)
--> part of Security Technical Implementations Guide (STIGs)
--> Developed for NIST 800-53 as a scanning benchmark
--> run  a SCAP scan, use STIG viewer to see whr and how to fix non-compliance issues

NMAP for assest management
--> Usually you have a network map (an excel file/databse with all the machines, endpts, routers, switches, firewalls etc)
--> unlike pentest where its a blackbox, audit should alrdy know what is there and look for hidden devices not part of the supposed network
--> Simple ping sweep -sn or just scan all devices using CIDR (198.143.5.0/24)
--> make sure wat is declared is actually thr, see if they match the network map given

Nessus (Free version exists)
--> run scans (SYN scans/ ARP scans/ Host Discovery etc)
--> Asset management Match what is seen from the scans to what u r given about the network
--> Advanced scans to check for vulnerability in services
--> Include in the vulnerability report stuff like XSS SQLi etc
--> then DevOps will need to look at it