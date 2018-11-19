
import boto3

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
for instance in instances:
    print(dir(instance))
