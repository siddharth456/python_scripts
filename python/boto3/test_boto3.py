import boto3

# Lets use Amazon S3
s3=boto3.resource('s3')

# Print all buckets name
for bucket in s3.buckets.all():
   print(bucket.name)

# Upload a new file
data=open('foo.txt',rb)
s3.Bucket('legostorage').put_object(Key='foo.txt',Body=data)
