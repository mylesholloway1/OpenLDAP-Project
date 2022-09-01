import boto3
cli = boto3.client('ec2', region_name='us-east-1')
res = cli.decribe_instances()
print(res)