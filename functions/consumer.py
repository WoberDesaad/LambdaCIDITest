import json
import datetime
import os
import boto3

def handler(event, context):
    sns_client = boto3.client('sns')
    sns_client.publish(TopicArn=os.environ["SNS_TOPIC"], Message=event)
