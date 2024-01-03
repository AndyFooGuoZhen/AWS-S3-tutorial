from fastapi import FastAPI, status, File, UploadFile
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
#     print(obj['Key'])

#Uploding a file
#Note : ACL is Access Control List, it is set to public-read so that the file is publically accessible
# TO add to a specific folder just change name of thir parameter
# EX : s3_client.upload_fileobj(f, s3_bucket , 'Images/testImage.png', ExtraArgs={'ACL': 'public-read'})

# with open('./Images/senior.png', 'rb') as f:
#     s3_client.upload_fileobj(f, s3_bucket , 'testImage.png', ExtraArgs={'ACL': 'public-read'})



@app.get("/getFiles")
async def get_files():
    response = s3_client.list_objects_v2(Bucket=s3_bucket)
    files = []
    for obj in response['Contents']:
        files.append(obj['Key'])
    return {"files": files}


@app.post("/uploadFile/", status_code=status.HTTP_201_CREATED)
async def upload_File (file: UploadFile = File(...)):
    s3_client.upload_fileobj(file.file, s3_bucket , file.filename, ExtraArgs={'ACL': 'public-read'})
    return {"message": "File Uploaded Successfully"}

@app.delete("/deleteFile/{fileName}", status_code=status.HTTP_200_OK)
async def delete_file(fileName: str):
    s3_client.delete_object(Bucket=s3_bucket, Key=fileName)
    return {"message": "File Deleted Successfully"}