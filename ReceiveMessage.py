import threading
import time
import botocore
import os.path
import csv
import boto3
import thread
import socket
import random
import sys
def Receive(region,url,id):
        while(True):
            try:
                sqs = boto3.client('sqs',region_name=region)        
                queue_url = url
                response = sqs.receive_message(
                   QueueUrl=queue_url,
                   AttributeNames=[
                            'SentTimestamp'
                    ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                            'All'
                        ],
                VisibilityTimeout=0,
                WaitTimeSeconds=0
                    )
                
                if(response['ResponseMetadata']['HTTPHeaders']['content-length']!='240'):
                    #print response        
                    message = response['Messages'][0]
                    receipt_handle = message['ReceiptHandle']
                    client=message['MessageAttributes']['Client']['StringValue']
                    print(message)
                    print(client)
                    if(str(client)==id):
                    	sqs.delete_message(
                            QueueUrl=queue_url,
                            ReceiptHandle=receipt_handle
                        )
                        break
                else:
                	break
                        
            except ValueError as e:
                print("Value error")

url='https://sqs.us-east-1.amazonaws.com/621120329648/ServerQueue'
region='us-east-1'                
Receive(region,url,sys.argv[1])