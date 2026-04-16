---
date:
    created: 2025-11-22
draft: true
tags:
  - Programming
---
My note about Computer networks
<!-- more -->
# 1. How register domain works
## 1.1 Terminology
- domain registrar: business organizations that reserve a pool of registered domains and mapping of IP address to these domains
- registry: Registries are organizations that manage [top-level domains (TLDs)](https://www.cloudflare.com/learning/dns/top-level-domain/) ‘.com’ and ‘.net’
- Resellers: organization that sells domain name registrations.
- name server: servers managed by registrars to translates domain to IP, components of DNS server
- DNS records common types:
	- A records:  Map a domain to IPv4 address(the address can be multiple)
	- AAAA: Map domain to IPv6
	- Cname records: : Map domain to another domain
	- MX Record: Map domain to mail servers
	- CAA: Specifies which certificate authorities are permitted to issue certificates for a domain
	- SRV: Define locations of various services

## 1.2 Registration process
1. Users go to registrars to purchase domain
2. after user purchases, registrar:
	1. check with domain registry and purchase domain
	2. Insert the domain with user's info in their db
	3. configure the domain's DNS records to point to a set of nameservers and update those nameservers
3. when user wants to map domain to an IP address:
	1. log in to registrar's control pannel to configure DNS records to point to their IP

## 1.3 DNS
DNS server type:
- Caching & recursive name server: store known domain name lookups for a certain time. When the entry is not found, it performs a full name resolution and store on the cache. This is provided by ISP or local network
- Root server: respond with a TLD server ip address for name queries based on the name request
- TLD(Top-level domain) server: respond with an authoritative name server ip for the name queries
- name server: respond with the actual ip for the name queries

Full name resolution flow:
![[Pasted image 20260408200816.png]]


# 2. Network devices
Network device list: https://www.youtube.com/watch?v=5_GDs-SCYuo
hub vs switch vs router vs modem:
- hub:  operates on layer 1 and has a limitation that causes it to be rare(if a computer wants to talk to another computer, it will send its message to all other computers at the same network)
- switch: operates on layer 2 and solve the limitation(allow computer to talk to the only target computer in the same network). It's often included in a router
- router: operates on layer 3. It's a device that can forward data between different networks. It includes switch as one of its components. There are 2 types of routers: one is the home/office router, while the other one is the core router at the ISP. The home router just sends the data to the core router of the ISP.

Firewall:

# 3. Subnet
# 4. Protocol
- BGP: routers share data among each other through this

Routing protocol:
- Interior Gateway protocols:
	- link state routing protocol
	- distance-vector protocol
- exterior gateway protocol

routing table:
![[Pasted image 20260408161545.png]]
(if the detination network does not belong to the above table, there is a catch all entry for that destination network row)
- destination network: the cidr network the router knows about
- next hop: the IP address of the next router that should receive data intended for the destination
- total hops: shortest posible path length to the destination
- interface: which interface the router should forward traffic matching the destination network

UDP protocol: used in DNS queries

Anycast protocol

DHCP: 
DHCP discovery:
![[Pasted image 20260409120559.png]]

- NAT:


- email protocol:
	- pop3: retrieve email from email server and delete them from email server
	- imap: retrieve email from email server but still keep the email for future download
	- smtp: protocol for sending email


# 5. Network hardening
Methods to harden network:
- use splunk(a tool) for monitoring and analyzing network logs
- enable fail2ban as a flood guard tool in firewall
- enable DHCP snooping on enterprise router(monitor DHCP traffic, keep track of the source of trusted DHCP server, discard DHCP messages from untrusted server to prevent rogue DHCP server)
- enable Dynamic ARP inspection on enterprise router(use IP-to-MAC table from DHCP snooping and rate-limit ARP packets per port to prevent ARP spoofing attack)
- enable IP Source guard(IPSG) on enterprise router to prevent IP Spoofing(based on DHCP snooping)
- enable EAPoL/EAPTLS to set up authentication in LAN(EAPol authenticates user's certificates or credentials)

# 6. IT standard
Credit card payment standard: if a company handles credit card payment, you have to follow PCI DSS(payment card industry data security standard, contain firewall config requirement)
