import csv
import subprocess
import os

# CSV File Name
csv_file_path = 'path/to/your/csv/file.csv'  

# AWS CLI command to create AMI
def create_ami(instance_id, ami_name):
    command = f"aws ec2 create-image --instance-id {instance_id} " \
              f"--name '{ami_name}' --description 'AMI for {instance_id}' " \
              "--no-reboot " \
              "--block-device-mappings '[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"DeleteOnTermination\":true,\"VolumeType\":\"gp2\"}}]' " \
              f"--region {os.environ['AWS_REGION']} --query 'ImageId' --output text"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"AMI created for instance {instance_id}: {result.stdout.strip()}")
    else:
        print(f"Failed to create AMI for instance {instance_id}. Error: {result.stderr.strip()}")


# Read data from CSV and create AMIs
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name_tag = row['NameTag']
        instance_id = row['InstanceId']
        ami_name = row['AmiName']

        create_ami(instance_id, ami_name)
