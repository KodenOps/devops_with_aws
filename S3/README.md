# S3: Understanding the storage options
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

### Alternative A
```
# copy and paste the ID and Secret_key here
AWS_ACCESS_ID=xxxxx
AWS_SECRET_KEY=xxxxx

```

## Alternative B
- Download AWS cli on your system
- run  `` aws configure `` and fill the same ID and Secret_key
- You can set the output format to JSON and leave the rest as default

## Running Codes
- Scroll to the bottom of the code till RunMe() function
- Un-comment the function you want and run the code
