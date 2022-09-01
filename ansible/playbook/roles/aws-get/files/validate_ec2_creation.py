import boto3
cli = boto3.client('ec2', region_name='us-east-1')
res = cli.instances.filter(
    InstanceIds=[
        {
            'Name': 'InstanceId',
            'Values': [
                'i-07121ff5aecbc50e1',
            ],
        },
    ],
)
print(res)