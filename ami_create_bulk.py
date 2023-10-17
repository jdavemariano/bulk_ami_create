import csv
import boto3

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

# Path to the CSV file
csv_file_path = 'bulk_create.csv'  # Replace with the actual path to your CSV file

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
