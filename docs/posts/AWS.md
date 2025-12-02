---
date:
    created: 2025-11-10
draft: true
tags:
  - DevOps
---
My note for AWS SAA
<!-- more -->
# 1. Set up

## 1.1 Config & Init AWS cli
1. Go to IAM Dashboard
2. Sidepannel > Users > Create User
3. Input user detail:
	- username: jaxyz;
	- user access to AWS Management console(whether allow the created user to login the AWS console like using root user)
4. SidePannel > User > Choose the user > 
	Security Credentials > 
	Create Access key > 
	Command Line Interface
5. Copy the Access Key & Secret Access Key
6. Type `aws configure` and paste the access Key, Secret Access key, set `default-region` to be `us-east-1`, output format to be `json`
7. check configuration: `aws configure list`
8. **Attach ECS permission:** Choose the user > Permissions Policies > Attach permissions
		> choose `AmazonECS_FullAccess`
9. **Create Roles:**  sidePanel > roles > AWS User account > ecsTaskExecutionRole > roleName: ecsTaskExecutionRole
10. 


# 2. IAM
What can be configured for a user:
- role and permission attached to this role
- permission policies
- access key & secret access key
# 3. ECS
terminology:
1. create ECS Cluster: provision physical infrastructure(e.g: EC2 instances or Fargate tasks) to deploy containers, but do not create containers yet
2. define task definitions: define containerized applications that runs shortly
3. define service: define containerized applications that provide long-time daemon
4. run tasks: deploy the container on ECS cluster and start it

## 3.1 Config ECS-Cli
1. Download the ecs-cli.exe from this link and put it in PATH variable: https://github.com/aws/amazon-ecs-cli?tab=readme-ov-file#installing
2. Rename the exe file to `ecs-cli.exe`, otherwise it does not work
3. Verify installation: `ecs-cli --version`
4. Config Profile: `ecs-cli configure profile --access-key <ACCESS_KEY_ID> --secret-key <SECRET_ACCESS_KEY>`
5. Config Cluster: `ecs-cli configure --cluster <cluster_name> --region <region_name> --config-name <configuration_name>`
6. Create ECS Cluster: `ecs-cli up --launch-type FARGATE`
7. Define Service: `ecs-cli compose --file docker-compose.yaml --project-name kafka_demo service up`

reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-connect.html

## 3.2 create image in ECS
https://www.youtube.com/watch?v=YDNSItBN15w

1. Configure & initialize ECS-cli:

## 3.3 use docker compose
ecs-cli compose:
- https://medium.com/@hrishikesh.nangare/amazon-ecs-cli-command-line-tool-for-amazon-elastic-container-service-eee7ee6f60c9
- https://www.youtube.com/watch?v=1sFNTKmy2SA
https://www.youtube.com/watch?v=1_AlV-FFxM8

# 4. EC2
## 4.1 How to run for short period

## 4.2 How to schedule regularly

# 5. Route 53
## 5.1 transfer domain