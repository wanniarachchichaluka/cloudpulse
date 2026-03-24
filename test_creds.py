import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def test_credentials():
    """Test AWS credentials and permissions for CloudPulse."""
    
    print("Testing AWS credentials and permissions...\n")
    
    try:
        # Test EC2 access
        print("Testing EC2 access...")
        ec2 = boto3.client('ec2')
        
        # Don't use MaxResults parameter, or use >= 5
        # Option 1: No MaxResults (returns all instances)
        instances = ec2.describe_instances()
        
        # Count instances
        instance_count = 0
        for reservation in instances['Reservations']:
            instance_count += len(reservation['Instances'])
        
        print(f"  ✓ EC2 access successful - found {instance_count} EC2 instances")
        
        # Test S3 access
        print("\nTesting S3 access...")
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()
        bucket_count = len(buckets['Buckets'])
        print(f"  ✓ S3 access successful - found {bucket_count} S3 buckets")
        
        # Test IAM access
        print("\nTesting IAM access...")
        iam = boto3.client('iam')
        users = iam.list_users()
        user_count = len(users['Users'])
        print(f"  ✓ IAM access successful - found {user_count} IAM users")
        
        # Test STS (Security Token Service) to confirm identity
        print("\nTesting identity...")
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"  ✓ Identity confirmed: {identity['Arn']}")
        
        print("\n" + "="*50)
        print("✅ ALL PERMISSIONS WORKING CORRECTLY!")
        print("="*50)
        print("\nYour CloudPulse tool is ready to use!")
        
    except NoCredentialsError:
        print("❌ No AWS credentials found!")
        print("Please run: aws configure")
        print("Or set environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY")
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        print(f"❌ AWS API Error: {error_code}")
        print(f"   Message: {error_message}")
        
        if error_code == 'AccessDenied':
            print("\n🔧 Fix: Your IAM user needs read-only permissions.")
            print("   Attach these policies:")
            print("   - AmazonEC2ReadOnlyAccess")
            print("   - AmazonS3ReadOnlyAccess")
            print("   - IAMReadOnlyAccess")
        elif error_code == 'InvalidClientTokenId':
            print("\n🔧 Fix: Your access key ID appears to be invalid.")
            print("   Check your credentials with: aws configure list")
        elif error_code == 'SignatureDoesNotMatch':
            print("\n🔧 Fix: Your secret access key is incorrect.")
            print("   Re-run: aws configure")
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("   Check your network connection and AWS service status.")

if __name__ == "__main__":
    test_credentials()
    