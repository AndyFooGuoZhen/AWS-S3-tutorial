from fastapi import FastAPI
from dotenv import load_dotenv
import os 
import boto3

load_dotenv()
app = FastAPI()
# aws_key = os.getenv("AWS_ACCESS_KEY_ID")

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

s3_bucket = 'filemanagertutorial'

#Prining all buckets
# print(s3_client.list_buckets())

#Print contents of a bucket
# response = s3_client.list_objects_v2(Bucket=s3_bucket)
# for obj in response['Contents']:
#     print(obj)

#Uploding a file
#Note : ACL is Access Control List, it is set to public-read so that the file is publically accessible
with open('./Images/senior.png', 'rb') as f:
    s3_client.upload_fileobj(f, s3_bucket, 'testImage.png', ExtraArgs={'ACL': 'public-read'})





@app.get("/")
async def get_hello():
    print(s3_client.list_buckets())
    return {"message": "as"}


