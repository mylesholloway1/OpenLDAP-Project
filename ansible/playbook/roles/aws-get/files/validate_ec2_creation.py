import boto3

client = boto3.client('ec2')

Myec2=client.describe_instances()
for pythonins in Myec2['OLDAP0905_TEST']:
print(pythonins)