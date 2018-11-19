# this script uploads an object(text file) to all available s3 buckets

import boto3

# create an s3 object
s3=boto3.resource('s3')

# create a file object
data=open("foo.txt","rb")

# looping through all buckets
for a in s3.buckets.all():
    s3.Bucket(a.name).put_object(Key='foo.txt',Body=data)
print("Object",data.name,"placed in all buckets")
