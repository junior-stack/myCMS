---
date:
    created: 2025-11-22
draft: true
tags:
  - DevOps
---
My note about Gitlab
<!-- more -->
# 1. Install & Config

## 1.1 Install in Ubuntu
Hardware requirements:
- RAM: 8GB
- CPU: 2, recommend 4

Steps:
1. Ensure http, https ssh ports are open on firewall
2. Deploy gitlab:
- general Ubuntu(**22.04**) server:
```bash
curl "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh" | sudo bash

sudo apt install gitlab-ce
```
- AWS: search AMI "GitLab Server CE Community Edition with Lets Encrypt SSL on Ubuntu" under AWS marketplace
3.  `cat /etc/gitlab/initial_root_password` to get the root password first, otherwise, it will be destroyed after you reconfigure
4. Reconfig:
- **has domain(recommend):** customization with letsencrypt, `/etc/gitlab/gitlab.rb`:
	```rb
	external_url "https://<YOUR_DOMAIN>"
	
	# letsencrypt
	# Note: letsencrypt fail if you use set external_url to be public_dns in aws ec2, must use own domain
	letsencrypt['enable'] = true
	letsencrypt['contact_emails'] = ['<EMAIL>']  # array of log in user's email
	letsencrypt['auto_renew'] = true
	```
- **no domain:** self-signed certificates + customization with existing certificate
	1. self-sign certificate: `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/gitlab/trusted-certs/gitlab.key -out /etc/gitlab/trusted-certs/gitlab.crt -subj "/CN=<IP_ADDRESS>"`
	2. (Optionally): upload gitlab.crt into your browser
	3. `gitlab.rb`:
	```rb
	external_url "https://<IP_ADDRESS>"
		
	letsencrypt['enable'] = false
		
	nginx['ssl_certificate'] = "/etc/gitlab/trusted-certs/gitlab.crt"
	nginx['ssl_certificate_key'] = "/etc/gitlab/trusted-certs/gitlab.key"
	nginx['redirect_http_to_https'] = true
	```
5. restart the gitlab service: `sudo gitlab-ctl reconfigure`
6. log into gitlab through `https://<YOUR_DOMAIN>` 
7. Log into the gitlab with root, the password found in step 3
8. **Config sign-in users:** passwd: exzr19386
	1. disable new signup option
	2. Side pannel > Admin > Overview > Users, select new users, fill-in name, email, username, passwd, choose role, then create new user
9. **config ssh key:** 
	1. side pannel > SSH keys > add new keys, copy the contents of id_rsa.pub into the field and create
	2. Go to the config file on client machine, filled the gitlab host Ip and the location of the ssh key
## 1.2 How to reconfig after restart
After an instance stops and restart again, what is changed is the IP address, you need to change for gitlab:
1. change 	external_url in gitlab.rb, then `sudo gitlab-ctl reconfigure`
2. change the config file on client machine to fill the new IP address
3. Reset the origin url of git repo to new IP address
# 2. Migrate projects