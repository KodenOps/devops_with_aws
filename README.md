## Overview:
This learning repo is in line with my study on each of the AWS services. The goal is to learn to provision and manage the services swifly using either the CLI or Programmatially using Python. Also, this repo is an avenue for me to practice Python which is a new language that i am trying to master. As a DevOps Engineer, it is important to learn AWS beyond the console. Especially when most activities are meant to be automated and handled by external applications (ansible, terraform, jenkins, etc.). It is important to understand the workings of AWS services beyond the console to improve efficiency and flexibility.

## Stacks used:
- Python
- Boto3
- AWS Services
- AWS Identity Management
- 

## Pre-Requisite
- Install Python on your local environment and ensure the path is added to the environment variable
- Install the following dependencies
```
boto3
python-dotenv # this is important to ensure you can fetch data from .env

```
- Generate access key in AWS IAM console and save it in .env file within this directory
```
AWS_ACCESS_ID=xxxxxxxxxxxxxxx
AWS_SECRET_KEY=xxxxxxxxxxxxxxxx

```
- Grab a bottle of soda/beer/water and let's dive into AWS awesomeness

### Resources 
- Check-out the Boto3 documentation : ["DOCUMENTATION"](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html) 
- Check-out the EC2 video for more understanding : ["Watch EC2 Video"](https://www.youtube.com/watch?v=PL0hRXzXbmE&t=980s)
- Check-out the S3 video for more understanding : ["Watch S3 Video"](https://www.youtube.com/watch?v=25PttcmnbRc&t=5s)

<video src="https://www.youtube.com/watch?v=25PttcmnbRc&t=5s" autoplay loop controls/>