import sys
import boto3

ec2_region    = sys.argv[1]
instance_name = sys.argv[2]

cli = boto3.client('ec2', region_name=ec2_region)
res = cli.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                instance_name,
            ]
        },
    ],
)

print(res)