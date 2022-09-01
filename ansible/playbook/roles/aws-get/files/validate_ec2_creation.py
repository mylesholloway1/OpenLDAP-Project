import boto3
print(boto3.__version__)


#cli = boto3.client('ec2')
#res = cli.describe_instances(
#    Filters=[
#        {
#            'Name': 'Instance-id',
#            'Values': [
#                'i-07121ff5aecbc50e1',
#            ],
#        },
#    ],
#)
#print(res)