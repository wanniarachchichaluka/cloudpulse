import boto3
import json
client = boto3.client('iam')
response3 = client.list_users()
print(json.dumps(response3, indent=2, default=str))
for user in response3["Users"]:
    print(user["UserName"])
    print("hhhhhhhhhhhhhhhhhhh")
    keys=client.list_access_keys(UserName=user["UserName"])
    print(json.dumps(keys["AccessKeyMetadata"], indent=2, default=str))