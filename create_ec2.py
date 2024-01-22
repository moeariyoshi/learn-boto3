import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId='ami-12345678',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

# Print the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"Launched EC2 instance with ID: {instance_id}")
