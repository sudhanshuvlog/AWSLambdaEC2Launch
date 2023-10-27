import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)
    instance_params = {
    'ImageId': 'ami-06791f9213cbb608b', 
    'InstanceType': 't2.micro', 
    'MinCount': 1,
    'MaxCount': 1,
    'NetworkInterfaces': [
        {
            'DeviceIndex': 0,
            'SubnetId': "subnet-09cd954372068aad0",
            'Groups': ['sg-009c41b5f69b0bc17']  
        }
    ],
    }

    # Launch the EC2 instance
    response = ec2.run_instances(**instance_params)
    print("instance launched succefully")
