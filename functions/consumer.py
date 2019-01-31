import json
import datetime
import os
import boto3
import datetime

def handler(event, context):
    sns_client = boto3.client('sns')
    
    message = "Hello. These are all the running instances:\n"
    ec2 = []
    
    instances = json.loads(event["Records"][0]["body"].replace("\'", "\""))
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    ec2.append(tag["Value"])

    for e in ec2:
        message = message + e + "\n"

    sns_client.publish(TopicArn=os.environ["SNS_TOPIC"], Message=message)

