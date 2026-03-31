import sys
import boto3
from datetime import datetime, timezone
from botocore.exceptions import ClientError, NoCredentialsError

threshold_days=7
import datetime as dt
def audit_ec2(threshold_days):
    try:
        results = []
        ec2_client = boto3.client('ec2')
        response1 = ec2_client.describe_instances()
        
        for reservation in response1["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                current_state = instance["State"]["Name"]
                launch_time = instance["LaunchTime"]
                name_tag = instance["Tags"][0]["Value"]

                tags = instance.get("Tags", []) 
                name_tag = "Unnamed"
                for t in tags:
                    if t["Key"] == "Name":
                        name_tag = t["Value"]
                        break
            

                dt=datetime.fromisoformat(launch_time)
                timestamp = dt.timestamp()
                td=datetime.now(timezone.utc)
                timestamp2 = td.timestamp()

                running_days = int((timestamp2 - timestamp)/60/60/24)
                if running_days > threshold_days:
                    results.append(Finding("EC2",instance_id,f"{name_tag} has been running for {running_days} days","LOW"))
        return results
    except ClientError as e:
        sys.exit(f"AWS API error: {e}")
        return 
    except boto3.exceptions.NoCredentialsError:
        sys.exit("Check the AWS config credentials again")
        return 

    #fetches all EC2 using boto3
    #running continuously > 7 days
        #mark as risks
        #return risk list as dict
        #dict contains: ec2 name, ec2 id, cost of a day, nu of continuos days running, cost of total days
    ...    
def audit_s3():
    #fetches all S3 buckets
    #checking public acess of each
    #if public open:
        #Critical
        #return critical list as dict
        #dict contains: s3 name, s3 id, how publically open
    ...
def audit_iam():
    #fetches all IAM users login details
    #last login > 90 days
        #issue
        #return issue list as dict
        #dict contains, iam name, iam id, how many day upto now after last login.
    ...
def classify_risk():
    #parameters: ec2 dict, S3 dict, IAM dict
    #classify into Lows, Mediums, Highs
    ...
def generate_report():
    #High risks summary at top, actions need
    #Medium risks at middle, actions need
    #Low risks at bottom, actions need
    #terminal summary
    ...

def main():
    #call audit_ec2, audit_s3, audit_iam
    #call classify_risk
    #call generate_report
    ...

if __name__=="__main__":
    main()