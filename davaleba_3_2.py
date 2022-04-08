import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def delete_file(name_of_bucket, file_name):
    try:
        s3.delete_object(Bucket=name_of_bucket, Key=file_name)
    except ClientError as ex:
        print(ex)
        return
    print('file has been deleted')


if __name__ == '__main__':
    delete_file('test.html',)