# EC2: Understanding the AWS Infrastructure as a Service

## Stacks:

- Python
- Boto3 client
- Aws connection strings
- load_dotenv package

## Environment setup

- clone repo
- create a .env file in the src
- on AWS portal, create new user and assign the right policy
- Generate access key and note the Access Key ID and Secret key
- Install Python, Boto3, python-dotenv,

### AWS Authentication A

```
# Create a .env in your directory. Then copy and paste the ID and Secret_key into the file like this here
AWS_ACCESS_ID=
AWS_SECRET_KEY=

```

## AWS Authentication B

- Download AWS cli on your system
- run `aws configure` and fill the same ID and Secret_key
- You can set the output format to JSON and leave the rest as default

## Running Codes

- Scroll to the bottom of the code till RunMe() function
- Un-comment the function you want and run the code
