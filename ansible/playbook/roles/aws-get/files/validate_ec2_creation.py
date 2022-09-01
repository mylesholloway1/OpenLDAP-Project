import boto3
cli = boto3.client('ec2', region_name='us-east-1')
res = cli.describe_instances(
    Filters=[
        {
            'Name': 'Instance-id',
            'Values': [
                'i-07121ff5aecbc50e1',
            ],
        },
        {
            'Name': 'location',
            'Values': [
                'us-east-1',
            ],
        },
    ],
)
print(res)