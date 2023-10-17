import csv
import boto3
import os

aws_region = os.environ['Region']

region_lookup = {
	"USEA":"us-east-1",
	"USWE":"us-west-1",
	"CACE":"ca-central-1",
	"EUWE":"eu-west-1",
	"EUCE":"eu-cemtral-1",
	"APSP":"ap-southeast-1",
	"APAU":"ap-southeast-2"
}

aws_region = region_lookup[aws_region]

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name=aws_region)

# Function to create AMI for EC2 instance
def create_ami(instance_id, ami_name):
    response = ec2_client.create_image(
        Description=f'AMI for {instance_id}',
        InstanceId=instance_id,
        Name=ami_name,
        NoReboot=True
    )
    print(f"AMI created for instance {instance_id}: {response['ImageId']}")


# Read data from CSV and create AMIs
with open('bulk_create.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name_tag = row[0]
        instance_id = row[1]
        ami_name = row[2]

        create_ami(instance_id, ami_name)
