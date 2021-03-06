import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIA5VZTIAOJXRWANKEK' #s3 관련 권한을 가진 IAM계정 정보
ACCESS_SECRET_KEY = 'Tx1LUyM2dcY9AB0SGCd8wYKDYYFPY7e6yaiRCXwR'
BUCKET_NAME = 'langhae-20220525'

def handle_upload_img(f): # f = 파일명
    data = open('plist/static/plist/img/artist/'+f+'.jpg', 'rb')
    # '로컬의 해당파일경로'+ 파일명 + 확장자
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(
        Key=f, Body=data, ContentType='image/jpg')