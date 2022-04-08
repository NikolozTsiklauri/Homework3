import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def old_version(name_of_bucket, file_name):
    try:
        response = s3.list_object_versions(
            Bucket=name_of_bucket, Prefix=file_name)['Versions']
        copy_source = {
            'Bucket': name_of_bucket,
            'Key': response[1]['Key'],
            'VersionId': response[1]['VersionId']
        }
        s3.copy_object(CopySource=copy_source, Bucket=name_of_bucket,
                       Key=copy_source['Key'], )
    except ClientError as ex:
        print(ex)
        return


if __name__ == '__main__':
    old_version('btu-test-lab4', 'v1')