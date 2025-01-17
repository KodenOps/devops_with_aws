import boto3
from dotenv import load_dotenv
import os
import random
load_dotenv()

# fetch aws credentials
aws_id = os.getenv("AWS_ACCESS_ID")
aws_secret = os.getenv("AWS_SECRET_KEY")

# item name
ec2_item_name = "segun_ec2_instance"

# onboard and authorize 
ec2_client=boto3.client("ec2", region_name="us-east-1", aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
response = ""
# generate key pair
def generate_key_pair():
    response = ec2_client.create_key_pair(
    KeyName= ec2_item_name,
    KeyType='rsa',
    KeyFormat='pem',
    DryRun=False
)
    print("Keypair: ", response.get("KeyPairId"))
    print("KeyFingerprint: ", response.get("KeyFingerprint"))
    print("KeyName: ",response.get("KeyName"))
    print("KeyMaterial: \n" ,response.get("KeyMaterial"))

# delete keypair
def delete_key_pair():
    response = ec2_client.delete_key_pair(
    KeyName=ec2_item_name,
    # KeyPairId='string', # enter the key id here or just comment it out
    DryRun=False
)
    print(ec2_item_name, "key pair deleted succesfully")
    print(response)

# generate ec2 instance
def create_ec2():
    delete_key_pair()
    generate_key_pair()
    response = ec2_client.run_instances(
    ImageId='ami-05576a079321f21f8', # you can get this on the AMI Catalog on EC2 console
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    KeyName=ec2_item_name,
    Monitoring={
        'Enabled': False
    },
    SubnetId='subnet-04d387865b75b993d',
)

def runMe():
    # generate_key_pair()
    # delete_key_pair()
    create_ec2()

runMe()