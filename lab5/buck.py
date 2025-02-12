import boto3
import sys
import botocore



choice = input("Enter your choice: 1 for Manage S3 Buckets , 2 for Manage EC2 Instances , 3 to exit : ").strip()
def manage_s3():
    user_choice = input("Enter 1 for display all existing s3 buckets , 2 for create bucket , 3 for delete the bucket : ").strip()
    s3_client = boto3.client("s3")
    if user_choice == "1":
        response = s3_client.list_buckets()
        print("S3 Buckets:")
        for bucket in response["Buckets"]:
            print(f"- {bucket['Name']}")
    elif user_choice == "2":
        bucket_name = input("Enter the name of the bucket: ").strip()
        print(f"Creating bucket {bucket_name}...")
        # if bucket_name in [bucket['Name'] for bucket in s3_client.list_buckets()["Buckets"]]:
        #     print(f"Bucket {bucket_name} already exists.")
        # else:
        #     print("Bucket does not exist")
        try:
            s3_client.create_bucket(Bucket=bucket_name)
        except Exception :
            print("Error : Bucket already exists")
        else:
            print(f"Bucket {bucket_name} created successfully.")
    elif user_choice == "3":    
        bucket_name = input("Enter the name of the bucket: ").strip()
        try:
            s3_client.delete_bucket(Bucket=bucket_name)
        except Exception :    
            print("Error : cannot delete this Bucket")
        else:
            print(f"Bucket {bucket_name} deleted successfully")   
    else:
        print("Invalid choice, please try again.")        
        
def manage_ec2():
    ec2_client = boto3.client("ec2")
    user_choice = input("Enter 1 for list all instances , 2 for start instance , 3 for stop instance , 4 for terminate instance , 5 to exit : ").strip()
    try:
        if user_choice == "1":
            ec2_client.describe_instances()
        elif user_choice == "2":
            instance_id = input("Enter the instance ID: ").strip()
            ec2_client.start_instance(instance_id)
        elif user_choice == "3":
            instance_id = input("Enter the instance ID: ").strip()
            ec2_client.stop_instance(instance_id)
        elif user_choice == "4":
            instance_id = input("Enter the instance ID: ").strip()
            ec2_client.terminate_instance(instance_id)
        elif user_choice == "5":
            print("Exiting EC2 Management...")
        else:
            print("Invalid choice. Please try again.")
    except Exception : 
        print("Error : cannot perform this operation")
        
        
        
        
        
        
        
        
    # response = ec2_client.describe_instances()
    # for reservation in response["Reservations"]:
    #     for instance in reservation["Instances"]:
    #         print(f"Instance ID: {instance['InstanceId']}")
    #         print(f"Instance Type: {instance['InstanceType']}")
    #         print(f"Instance State: {instance['State']['Name']}")
    #         print(f"Public DNS: {instance['PublicDnsName']}")
    #         print(f"Public IP: {instance['PublicIpAddress']}")
    #         print(f"Private IP: {instance['PrivateIpAddress']}")
    #         print()


if choice == "1":
    manage_s3()
elif choice == "2":
    manage_ec2()
elif choice == "3":
    print("Exiting program...")
    sys.exit(0)
else:
    print("Invalid choice, please try again.")



#     if bucket_name in [bucket["Name"] for bucket in s3_client.list_buckets()["Buckets"]]:
#         print(f"Bucket {bucket_name} already exists.")
# except ClientError as e:
#     print(f"An error  , The bucket {bucket_name} is already exists") 
##########################
# # Creating an S3 client
# # Creating an S3 client
# s3_client = boto3.client("s3")

# # Creating an S3 resource
# s3_resource = boto3.resource("s3")

# response = s3_client.list_buckets()

# print("S3 Buckets:")
# for bucket in response["Buckets"]:
#     print(f"- {bucket['Name']}")
    
# ec2_client = boto3.client("ec2")
# ec2_resource = boto3.resource("ec2")
# response = ec2_client.describe_instances()
# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         print(f"Instance ID: {instance['InstanceId']}")
#         print(f"Instance Type: {instance['InstanceType']}")
#         print(f"Instance State: {instance['State']['Name']}")
#         print(f"Public DNS: {instance['PublicDnsName']}")
#         print(f"Public IP: {instance['PublicIpAddress']}")
#         print(f"Private IP: {instance['PrivateIpAddress']}")
#         print()