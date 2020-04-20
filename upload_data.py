import os
import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME_SOURCE = os.environ.get('SRC_BKT_NAME')
PREFIX = 'input/data/training/'

s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/iris.csv", PREFIX + 'iris.csv')