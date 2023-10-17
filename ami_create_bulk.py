import csv
import boto3

# Set the AWS region
aws_region = 'your_aws_region'  # Replace with your AWS region

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name=aws_region)

# Path to the CSV file
csv_file_path = 'path/to/your/csv/file.csv'  # Replace with the actual path to your CSV file

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
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name_tag = row['NameTag']
        instance_id = row['InstanceId']
        ami_name = row['AmiName']

        create_ami(instance_id, ami_name)
