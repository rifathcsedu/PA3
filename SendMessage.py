import threading
import time
import botocore
import os.path
import csv
import boto3
import thread
import socket
import random
def Send(region,url,ClientID):

        sqs = boto3.client('sqs',region_name=region)
        f=open("Data.txt","r")
        ST=f.read()      
        queue_url = url
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=0,
            MessageAttributes={
                'Client': {
                    'DataType': 'String',
                    'StringValue': ClientID
                },
            },
            MessageBody=(
                ST
    )
        )
url='https://sqs.us-east-1.amazonaws.com/621120329648/ServerQueue'
region='us-east-1'

Send(region,url,sys.argv[1])