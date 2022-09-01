import sys
import boto3

ec2_region    = sys.argv[1]
instance_name = sys.argv[2]

ec2 = boto3.client('ec2', region_name=ec2_region)
res = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                instance_name,
            ]
        },
    ],
)

if res['Reservations'] != []:
    print ('ec2 is valid')
else:
    print ('error creating ec2')