from fileinput import filename
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def download_file(name_of_bucket, file_name, path="./"):
    try:
        s3.download_file(Bucket=name_of_bucket, Key=file_name,
                         Filename=path + file_name if path else file_name)
    except ClientError as ex:
        print(ex)
        return
    print(f'file {file_name} has been downloaded')


if __name__ == '__main__':
    download_file('btu-test-lab4', 'test.html',)