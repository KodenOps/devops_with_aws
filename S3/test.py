import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# fetch aws credentials
aws_id = os.getenv("AWS_ACCESS_ID")
aws_secret = os.getenv("AWS_SECRET_KEY")

# onboard and authorize 
s3_client=boto3.client("s3", region_name="us-east-1", aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)

# Create Bucket
def create_bucket():
    create_buk = s3_client.create_bucket(Bucket="djfsromdfgkmfedfmkdmfoes") # change string to the bucket name you want
    print("Bucket created")

# Delete Bucket
def delete_bucket():
    delete_resp = s3_client.delete_bucket(Bucket='djfsromdfgkmfedfmkdmfoes') # change string to the bucket name you want
    print("success")

# List Bucket
def list_bucket():
    resp = s3_client.list_buckets()
    print(resp)
    for a in resp["Buckets"]:
        print ( "Bucket Name:" , a['Name'])
        # print("")

# upload files to bucket
def upload_file():
    s3_client.upload_file('/home/pelumi/devops/S3/src/README.md', 'djfsromdfgkmfedfmkdmfoes', 'readme2.txt') # change to the folder you have the file to upload
    s3_client.upload_file('/home/pelumi/devops/S3/src/README.md', 'djfsromdfgkmfedfmkdmfoes', 'readme.txt') # change to the folder you have the file to upload
    print('files uploaded successfully')

# download file
def download_file():
    # s3_client.download_file('bucket name', 'key name/file name', 'location to save the file')
    s3_client.download_file('djfsromdfgkmfedfmkdmfoes', 'readme2.txt', '/home/pelumi/devops/S3/new_readme2.txt') # change the folder to download 
    print("success")

def generate_presigned_url():
    response = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'djfsromdfgkmfedfmkdmfoes', # change string to the bucket name you want
            'Key': 'readme2.txt'
        }, 
        ExpiresIn=60
    )

    print(response)

# delete objects (multiple items)
def delete_objects(a,b):
    s3_client.delete_objects(
        Bucket='djfsromdfgkmfedfmkdmfoes', # change string to the bucket name you want
        Delete={
            'Objects':[
                {'Key': a},
                {'Key': b}
            ]
        }
   
    )
    print("Items deleteted")


# run activities
def runMe():
    ""
    # create_bucket()
    # list_bucket()   
    # upload_file()
    # download_file()
    # generate_presigned_url()
    # delete_objects('readme2.txt', 'readme.txt')
    # delete_bucket()

runMe()
""
# Learn from the docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
