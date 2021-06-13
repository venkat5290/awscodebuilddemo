#CI/CD Pipeline using Git,ECR,Codebuild,Codepipeline and ECS FARGATE

Steps:

(1) Create a AWS Elastic Container Registry where we store the docker images  
(2) Create a Codebuild project with git as source and ecr role arn as destination  
(3) Create a Deployment Target  
(4) Create a codepipeline with git,codebuild and ecs as target  
(5) Modify the git and see automatic deployment happens  

Step 1:

Create a registry name in ecr:
let name of ecr be:venkat1

registry uri: 459867363038.dkr.ecr.us-east-2.amazonaws.com/venkat  

The output of the ecr creation gives us the following commands:  

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 459867363038.dkr.ecr.us-east-2.amazonaws.com

docker build -t venkat .

docker tag venkat:latest 459867363038.dkr.ecr.us-east-2.amazonaws.com/venkat:latest

docker push 459867363038.dkr.ecr.us-east-2.amazonaws.com/venkat:latest

Step 2:

Create a project in CodeBuild: builddemo

The important parameters are:

	source ->Github Repo
	role: EC2ContainerRegistryFullAccessRole
	buildspec.yml file
![build3](https://user-images.githubusercontent.com/25465240/121798682-57a25c00-cc45-11eb-996d-9a6158b8e892.PNG)


source:  
![build2](https://user-images.githubusercontent.com/25465240/121798697-6b4dc280-cc45-11eb-940e-2d606bf5617f.PNG)

![build4](https://user-images.githubusercontent.com/25465240/121798689-638e1e00-cc45-11eb-99d1-2707be46793b.PNG)


create a buildspec.yml

buildspec.yml: https://github.com/venkat5290/awscodebuilddemo/blob/main/buildspec.yml


      
   ![build6](https://user-images.githubusercontent.com/25465240/121798731-8ae4eb00-cc45-11eb-92a7-e354798b3a2a.PNG)


Step 3:

Create a deployment target

(a) Create a ECS Fargate Cluster
![fargate1](https://user-images.githubusercontent.com/25465240/121798745-a3550580-cc45-11eb-8d9e-17efc77f55b4.PNG)

![fargate2](https://user-images.githubusercontent.com/25465240/121798741-9c2df780-cc45-11eb-9c33-09acb675d0ea.PNG)

(b) Create a Task definition  
(c) Create a target and Loadbalancer foe hosting the containers  
(d) Create a service with above all  


Note: By now containers are running 


Step 4:

Create a CodePipeline

![pipeline1](https://user-images.githubusercontent.com/25465240/121798755-b5cf3f00-cc45-11eb-92fe-19759672f1e8.PNG)

(a)Git will act as source 

![pipeline2](https://user-images.githubusercontent.com/25465240/121798761-c384c480-cc45-11eb-873c-9dff645f8f65.PNG)
![pipeline3](https://user-images.githubusercontent.com/25465240/121798764-ca133c00-cc45-11eb-96f0-c884f2da3cf3.PNG)

(b) CodeBuild triggered by codepipeline which is used to build containers when source code is modified and save the artifacts into s3

  ![pipeline5](https://user-images.githubusercontent.com/25465240/121798777-ddbea280-cc45-11eb-8513-b6c8100a0181.PNG)
![pipeline6](https://user-images.githubusercontent.com/25465240/121798780-e4e5b080-cc45-11eb-8ce6-5ba1d210a21f.PNG)

(c) finally codedeploy with ecs as target

![pipeline7](https://user-images.githubusercontent.com/25465240/121798785-efa04580-cc45-11eb-8796-59508ca27a62.PNG)
![pipeline8](https://user-images.githubusercontent.com/25465240/121798788-f929ad80-cc45-11eb-9a49-27cddc7f8cca.PNG)


Step 5:
Change the code in Git

When code is modified automatically source build happens in turn code buiold is triggered which finally deploys into ecs
