import boto3
import json
ec2 = boto3.client('ec2')
response2 = ec2.describe_instances()
print(json.dumps(response2, indent=2, default=str))
for reservation in response2["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["Tags"][0]["Value"])
        print(instance["LaunchTime"])