import boto3
import json
s3=boto3.client('s3')
response1 = s3.list_buckets()
print(response1)

client = boto3.client('iam')
response3 = client.list_users()
print(json.dumps(response3, indent=2, default=str))
for user in response3["Users"]:
    print(user["UserName"])

ec2 = boto3.client('ec2')
response2 = ec2.describe_instances()
print(json.dumps(response2, indent=2, default=str))
for reservation in response2["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["Tags"][0]["Value"])
        print(instance["LaunchTime"])


for bucket in response1["Buckets"]:
    print(bucket["Name"])
    