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
	- A records:  Map domain to IPv4
	- AAAA: Map domain to IPv6
	- Cname records: : Map domain to another domain
	- MX Record: Map domain to mail servers
	- CAA: Specifies which certificate authorities are permitted to issue certificates for a domain

## 1.2 Registration process
1. Users go to registrars to purchase domain
2. after user purchases, registrar:
	1. check with domain registry and purchase domain
	2. Insert the domain with user's info in their db
	3. configure the domain's DNS records to point to a set of nameservers and update those nameservers
3. when user wants to map domain to an IP address:
	1. log in to registrar's control pannel to configure DNS records to point to their IP