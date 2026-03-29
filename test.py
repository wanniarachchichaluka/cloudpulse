import boto3
import json
s3=boto3.client('s3')
response1 = s3.list_buckets()
print(json.dumps(response1, indent=2, default=str))
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
for bucket in response1["Buckets"]:
    print(bucket["Name"])
    try:
        pub = s3.get_public_access_block(Bucket=bucket["Name"])
        print(json.dumps(pub["PublicAccessBlockConfiguration"], indent=2))
    except Exception as e:
        print(f"Error: {e}")