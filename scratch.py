import boto3
s3=boto3.client('s3')
response1 = s3.list_buckets()
#print(response1)

client = boto3.client('iam')
response3 = client.list_users()
print(response3)

ec2 = boto3.client('ec2')
response2 = ec2.describe_instances()
#print(response2)