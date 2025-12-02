---
date:
    created: 2025-11-22
tags:
  - DevOps
---
My note about Linux(mostly Ubuntu 22.04 LTS)
<!-- more -->

# 1. Initialize config

## 1.1 Firewall
after provisioning a new linux instance, we set firewall rules as following:

| inbound/outbound | ip_address | port | rule    | protocol |
| ---------------- | ---------- | ---- | ------- | -------- |
| inbound          | 0.0.0.0/0  | 22   | allowed | SSH      |
| inbound          | 0.0.0.0/0  | 80   | allowed | TCP      |
| inbound          | 0.0.0.0/0  | 443  | allowed | TLS      |
| outbound         | 0.0.0.0/0  | *    | allowed | All      |

```bash
# iptables

# ufw
# ufw [allow/deny] [out]  <port>[:<protocol>]
sudo ufw default allow outgoing
sudo ufw default deny incoming

sudo ufw allow 80/tcp
sudo ufw allow https
sudo ufw allow ssh
```

## 1.2 SSH

### 1.2.1 passwordless login
1. edit `/etc/ssh/sshd_config` and ensure the following lines:
```bash
PubkeyAuthentication yes
PasswordAuthentication yes   # optional during testing
AuthorizedKeysFile .ssh/authorized_keys
```
2. Launch the ssh with the above config: `sudo systemctl restart ssh`
3. On client machine, `ssh-keygen -t rsa -b 4096` generates `id_rsa.pub` and `id_rsa`
4. edit config:
- remote: copy the contents of `id_rsa.pub` at the end of `~/.ssh/authorized_keys`
- client: edit `.ssh\config`:
```bash
Host digitalocean
    HostName <REMOTE_HOST_IP>
    User <REMOTE_USER>
    IdentityFile <id_rsa_path>
```


## 1.3 Important config file
- `/etc/profile`: config `PATH` variable
- `/etc/ssh/sshd_config`: ssh server config

## 1.4 Package manager
```bash
apt list --installed
apt install -y <PACKAGE_NAME>
apt download <PACKAGE_NAME>   # only download but not install
```

## 1.5 User
# 2. Commands
## 2.1 common
common:
```bash
mkdir a
cd /root
ls ~
ls /etc -larth
cat a.txt
pwd
cp a.txt b.txt
mv b.txt ../b.txt
```
Files:
```bash
touch a.txt

# chmod
# owner     group    other
# rwx       r-x       r-- (r:4, w: 2, x: 1)
chmod 764 a.txt

# lsattr/chattr

#chown:
# change the owner group/user of file/directory to <GROUP_NAME> or <OWNER>
chown <OWNER_NAME>:<GROUP_NAME> <FILE_NAME/DIRECTORY_NAME>
chown :<GROUP_NAME> <FILE_NAME/DIRECTORY_NAME>
chown <OWNER_NAME> <FILE_NAME/DIRECTORY_NAME>

# stat
stat <FILE_NAME>

# ln
ln <ORIGINAL_FILE_PATH> <HARD_LINK_NAME>
ln -s <ORIGINAL_FILE_PATH/ORIGINAL_DIRECTORY_PATH> <SOFT_LINK_NAME>

# mount storage device to file system
lsblk # list all storage device name
mount /dev/<DEVICE_NAME> /mnt/<DEVICE_NAME>
unmount /dev/<DEVICE_NAME>
```
Services:
```bash
# systemctl
systemctl status firewalld
systemctl start firewalld
systemctl stop firewalld
# onfigure to start the <SERVICE> when system boot up
systemctl enable <SERVICE>
# List all services on this machine
systemctl list-units --type=service
# check service log
journalctl -u <SERVICE>.service --no-pager

# service
service <SERVICE> status
service <SERVICE> start
service <SERVICE> stop
```
Processes:
```bash
# List running processes
ps -aux
# check processes created by a user
ps -u <USER>

# Terminate process(ctrl + C)
kill -s SIGINT <PROCESS_ID>
```
Port:
```bash
# find the PID on a port
sudo netstat -nlp | grep :<PORT>
```

ACL Control:
```bash
# umask: set permission for newly created files/directories
```

User:
```bash
# add/remove user
sudo adduser <USER>
sudo userdel -r <USER>

# add/remove group
sudo groupadd <GROUPNAME>
sudo groupdel <GROUPNAME>

# add/remove a user to a group
sudo usermod -aG groupname username
sudo deluser <USER> <GROUPNAME>

# list user's groups
groups <USER>

# switch user
su <USER>

whoami
```


Other useful:
```bash
# find
find / -name "hi.txt"
find / -type "f"
# find files of size between 20kB and 25kB
find / -size +20k -size -25k
find / - user "<USER>"
# find files that has modification time after certain date
find / -newermt "yyyy-mm-dd"
# find files that has modification time before certain date
find / \! -newermt "yyyy-mm-dd"
# not display error message of find command
find / -name "hi.txt" 2>/dev/null


# curl
# save contents of URL into filename
curl -o <FILE_NAME> <URL>
# follow redirection if URL redirect
curl -L <URL>
curl -H "Content-Type: application/json" \
	-H "Authorization: Bearer your_token_here" \
	-H "<CUSTOM_HEADER_KEY>:<HEADER_KEY_VALUE>"
curl -X POST -d "param1=value1&param2=value2" <URL>
# upload file.txt to URL
curl -F "<FILE_PATH>/file.txt" <URL>

# whereis
```
## 2.2 Schedule commands
We schedule command using either `cron` or `at`:

Cron: schedule periodic task
- Create a crob job:
	1. check cron service status: `systemctl status cron` or `service cron status`
	2. `crontab -e` will open up a cron file in text editor, once file is saved, cron will execute. Cron file format:
```text
minute hour day_of_month month day_of_week command_to_run
```
- List cron jobs: `crontab -l`
- Delete all user's cron job: `crontab -r`

`at`: schedule one-time task
- create at job:
	1. check service: `systemctl status atd` or `service atd status`
	2. execute single command: `echo "<COMMAND>" | at [hour]:[minute] [AM/PM] [MM/DD/YYYY]`; executes file: `at -f <SCRIPT> [hour]:[minute] [AM/PM] [MM/DD/YYYY]`
- list jobs: `at -l`
- delete job: `at -r <JOB_ID>`
	

### 2.2.1 Schedule one time task
at: `at -f ~/myscript.sh 14:00`

## 2.2.2 Schedule periodic task
cron file:
```text
30 3 5 12 * <COMMAND>
```
This will creates a job that runs at `12/05 3:30` **every year**. 

```text
0 3 * * * <COMMAND>
```
This will creates task at `3:00` **every day**.




# 3. Network

## 3.1 Create TLS certificate
- self-signed certificate
- Letsencrypt

self-signed certificate: This is generally used for self-hosting multiple host machines. Letsencrypt is suitable when you have only one domain for running one host
```bash
# one command to generate the key and crt
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/gitlab/trusted-certs/gitlab.key -out /etc/gitlab/trusted-certs/gitlab.crt -subj "/CN=<IP_ADDRESS>"

```


**LetsEncrypt:** LetsEncrypt is a CA service that can freely request and generate a trusted CA certificate. Users interact with  letsencrypt through certbot command. To use LetsEncrypt, you must have a domain name.

```bash
apt install certbot
# 1. obtain CA certificate, enter email address and select yes
#   generates: - /etc/letsencrypt/live/<DOMAIN>/fullchain.pem
#              - /etc/letsencrypt/live/<DOMAIN>/privkey.pem
sudo certbot certonly --standalone --preferred_challenges http -d <DOMAIN_NAME>
```

## 3.2 Apache


# 4. Bash

## 4.1 Declare Variables
```bash
#!/bin/bash
greeting="hello"  # ensure no space on both sides of =
var=$(ls -l | wc -l)

let var=var+1
i = `expr $j + $i`

# common built-in variables:
# $0: the invoked name of the bash script
# $1 - $9: the first 9 arguments to the bash script
# $#: number of arguments passed to this bash script
# $?: The exit status of the most recent progress


echo "${greeting} world"
```

## 4.2 Operators
redirect:
- `<COMMAND> > <FILE>`: redirect contents written to `/dev/stdin` to `<FILE>`
- `<COMMAND> >> <FILE>`: append output from `<COMMAND>` to the end of `<FILE>`
- `<COMMAND> m>& <FILE>`: point file descriptor of m to `FILE`, and redirect contents written to file descriptor m to `<FILE>`
- ``<COMMAND> 2>/dev/null`: do not display error messages:
More:
- https://blog.csdn.net/weixin_29476595/article/details/112665057
- https://blog.csdn.net/xyz_dream/article/details/89547687

## 4.3 if statement
```bash
if [-d "$WRITEDIR"]
then
	echo "$WRITEDIR created"
elif ((2 / 2 == 1))
then
	echo "hello"
elif ["$value1" -eq "$value2"]
then
	echo $value1
else
	exit 1
fi
```

reference: https://www.jianshu.com/p/f3bb2468c7af


