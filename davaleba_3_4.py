import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def list_of_bucket(name_of_bucket):
    files = {}
    try:
        result = s3.list_objects(Bucket=name_of_bucket)
        for result in result.get("Contents", []):
            extension = (result.get("Key").split(".")[-1])
            if extension in files.keys():
                files[extension] = files.get(extension) + 1
            else:
                files[extension] = 1
        print(files)
    except ClientError as ex:
        print(ex)
        return


if __name__ == '__main__':
    list_of_bucket('btu-test-lab4')