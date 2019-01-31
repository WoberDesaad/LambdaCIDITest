import json
import datetime
import boto3
import os


def handler(event, context):
    queue_client = boto3.client("sqs")
    ec2_client = boto3.client("ec2")

    # Get information on all instnaces
    response = ec2_client.describe_instances()

    # For each instance, write to queue
    queue_client.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody=response)

