import json
import datetime
import boto3
import os


def handler(event, context):
    queue_client = boto3.client("sqs")
    ec2_client = boto3.client("ec2")
    queue_url = queue_client.get_queue_url(QueueName=os.environ["QUEUE_NAME"], QueueOwnerAWSAccountId=os.environ["ACCOUNT_ID"])


    # Get information on all instnaces
    response = ec2_client.describe_instances()

    # For each instance, write to queue
    queue_client.send_message(QueueUrl=queue_url["QueueUrl"], MessageBody=str(response))

