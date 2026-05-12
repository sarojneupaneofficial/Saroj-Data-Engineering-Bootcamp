## Week 6 – Day 2 Notes — Boto3 & AWS Lambda

Today we learned about Boto3 and AWS Lambda.

## What is Boto3?

Boto3 is the official Python SDK for AWS.

It allows Python programs to interact with AWS services like:

S3
EC2
Lambda
DynamoDB

## Install Boto3:

pip install boto3

## Import Boto3:

import boto3

## Example — Connecting to S3

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
print(bucket['Name'])

## AWS Lambda

AWS Lambda is a serverless computing service.

It runs code without managing servers.

## Lambda Features

Event-driven execution
Auto scaling
Pay only for usage
Supports multiple programming languages
Lambda Workflow
Upload code
Configure trigger
Execute function
AWS handles infrastructure automatically

## Simple Lambda Function Example

def lambda_handler(event, context):
return {
'statusCode': 200,
'body': 'Hello from Lambda'
}

## What I Learned Today

- Introduction to Boto3
- Connecting Python with AWS services
- Listing S3 buckets using Python
- Basics of AWS Lambda
- Understanding serverless architecture
- Creating simple Lambda functions
