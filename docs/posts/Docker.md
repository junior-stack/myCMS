---
date:
    created: 2025-11-10
tags:
  - DevOps
---
My cheatsheet for using docker
<!-- more -->
# 1. docker command
boot up or shutdown docker daemon: (go to admin powershell)
```powershell
net start "Docker Desktop Service"
Get-Service  -Name "Docker Desktop Service"
net stop "Docker Desktop Service"
```

## 1.1 common
```powershell
# images
docker images               # List all images
docker pull <imageName>     # download image
docker push <imageName>     # upload image to dockerhub or AWS ECR

# container
docker ps -a                          # List all containers
# creates a new container and run the main application process within it
docker run <imageName>
# create the container in background process
docker run -d <imageName>
# creates a new container and create a new bash process beside the application process in it to interact with the container
docker run -it <imageName> /bin/bash
# enter a running container & create a new bash process in that container; this does not create new container like docker run
docker exec -it <containerID> /bin/bash
docker stop <containerID>         # stop a container
docker start <containerID>        # start a stopped container
# connect the terminal to the input/output/error stream of main process of a running container; usually a container runs one process, if the container is running a program, you see the program output in the terminal & can't type new command
docker attach <containerID>
docker rm <containerID>

# Other
docker inspect <containerID>
```

## 1.2 docker volume: 
If we save files within a docker container and delete that container, we lose those files. Thus, we introduce docker volume. Docker volume is the backup storage that allows us to save the files on host machines, when the container is deleted. Think of it as a USB.

```powershell
docker volume ls                     # list created docker volumes
# creates the volume under /var/lib/docker/volumes/
docker volume create <volume_name>
docker volume inspect <volume_name>
docker volume rm <volume_name>

# attach the volume to a container; a volume can be used by multiple containers
docker run -v <volume_name>:<container_path> <imageName>
docker volume prune                # delete all unused volumes

```

## 1.3 docker network
 When container is created without `--network` through `docker run`, they are default in the `docker0` network. Containers within this network can communicate with host and other containers within this network. They can also access the Internet. `docker0` is bridge type. Docker networks have following types: 
 - Bridge: containers communicate each other through the host gateway and can access Internet through NAT
 - Host: containers themselves won't have IPs or ports. No ports mapping. They share the IPs and ports with the host
 - Overlay: used in docker swarm to communicate containers within different docker daemons
 - None

```powershell
# port mapping command for containers in bridge network
docker run -p <HOST_PORT>:<HOST_PORT>:<CONTAINER_PORT> <IMAGE_NAME>
 
docker network create -d <NETWORK_TYPE> <NETWORK_NAME> # create network
docker network inspect <NETWORK_NAME>
docker network rm <NETWORK_NAME>
docker network prune

# create a container using specific network
docker run --net <NETWORK_NAME> <IMAGE_NAME>
# connect existing container to a network; a container can be in multiple networks
docker network connect <NETWORK_NAME> <containerID>
docker network disconnect <NETWORK_NAME> <containerID>
```

# 2. Docker Context
Docker context allows us to connect to different docker daemons either on local machines or on remote machines that install dockers. This allows us to build docker compose or docker file on remote docker engines. Remote machines that support docker include:
- DigitalOcean(simplest + cheapest)
- AWS EC2(mannually install docker)
- AWS ECS(retired: https://forums.docker.com/t/query-why-is-docker-composes-integration-for-ecs-and-aci-retiring-in-november-2023/138461): replacement soln is docker compose-x/ECS-cli(not stable)

```powershell
docker context ls     # list all docker contexts
docker context inspect <contextName>
docker context rm <contextName>

# to find the host of remote docker, check the host field of docker context inspect <RemoteContextName>, host can be ssh, tcp, etc.
docker context create <contextName> --docker "host=ssh://user@remote-host"
docker context use <contextName>
```
# 3. Dockerfile
**Creating single dockerfile(`docker build dockerfile`)**
```Dockerfile
# build from base image, appear in the first line
FROM <IMAGE_NAME>:<tag>
# pass variable and default value of it at build time; can be attached multiple variables & values
ARG <VAR_NAME>[=<DEFAULT_VALUE>]

# set the working directories for following RUN, CMD, ENTRYPOINT, COPY, ADD; can be set multiple times
WORKDIR "<CONTAINER_PATH>"
# copies files from HOST_PATH to CONTAINER_PATH,HOST_PATH is host file path 
COPY "<HOST_PATH>" "<CONTAINER_PATH>"
# same as COPY; except that HOST_PATH can be remote url and when HOST_PATH is a tar file, ADD will extract it into CONTAINER_PATH
ADD "<HOST_PATH>" "<CONTAINER_PATH>"

# set the environment variable to value when container is running
ENV <VARIABLE> <VALUE>
# mount the HOST_PATH as external volume
VOLUME <HOST_PATH>
# specifies the port the container listens on; still need port mapping in order to access the port, ex: docker run -p 80:8080 if 8080 is EXPOSE
EXPOSE <CONTAINER_PORT>
# set the username/UID for following RUN, CMD, ENTRYPOINT
USER <USERNAME/UID>


# executes commands/executables during build process; executables must be in image file system path
RUN <command1/executable1> <arg1> <arg2> &&\
	<command2/exectable2> <arg1> <arg2>
# executes commands/executables when container is started or provide arguments to ENTRYPOINT executables if ENTRYPOINT appears; when multiple CMD lines appear, only the last one takes effect
CMD <command1/executable1> <arg1> <arg2> &&\
	<command2/executable2> <arg1> <arg2>
CMD <command1/executable1> <arg1> <arg2> ;\
	<command2/executable2> <arg1> <arg2>
CMD <arg1> <arg2>
# runs the executable when container is launched; when CMD and ENTRYPOINT both appear, the arguments to CMD will be appended to ENTRYPOINT
ENTRYPOINT <command/executable> <arg1> <arg2>
```

**Link multiple dockerfiles(use `onBuild`)** 
We can reuse a parent dockerfile instructions in children dockerfile. We define commands through `onBuild` in parent dockerfile. The parent dockerfile won't execute `onBuild` instructions when parent dockerfile is built. They will be executed when the children dockerfile import parent dockerfile through `FROM`
- parent dockerfile:
```dockerfile
FROM base_image  
ONBUILD COPY . /app  
ONBUILD RUN npm install
```
- children dockerfile:
```dockerfile
FROM parent_image:latest
```


reference: https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index

# 4. Docker Compose

`docker-compose.yaml` basic structure:
```yaml
version: '3.8'
services:
	service1:
		# service1 configuration
	service2:
		# service1 configuration
volumes:
	volume1
networks:
	network1
```

service configuration:
- image/build: 
	- image: specify docker image
	- build: specify the directory path of `dockerfile`
- ports: list of`<HOST_PORT>:<CONTAINER_PORT>`or `<CONTAINER_PORT>`, map host port to container port or map random port to container port
- environment/env_file:
	- environment: list of `<env_variable>: <values>`
	- env_file: location of env file
- volumes
- networks
- depends_on: list of other `<service_name>`, specify the order of launching container services
- healthcheck:
	- test
	- interval
	- timeout
	- retries

start up container application: `docker compose up -d`
stop applications: 

# 5. Docker Swarm
docker compose can only create containers on one server, while docker swarm can distribute containers among different servers.

# 6. Clean the disk file
When we no longer needs docker images/containers, we can clean it through following(windows):
1. delete all images/containers: `docker system prune -a`
2. `wsl --shutdown`
3. shrink .vhdx:
```powershell
diskpart
# open Diskpart in new window
select vdisk file="D:\program\wsl\docker-desktop-data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exi
```
4. `optimize-vhd "D:\program\wsl\docker-desktop-data\ext4.vhdx" -mode full`

