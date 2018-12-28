#!/usr/bin/python3
'''
We need to add a SNS trigger to this lambda function PostReader_ConvertToAudio
and then issue the subscribe command to SNS 

This is an example of how to add SNS triggers to lambda programmatically.

'''
import boto3
import json
import os
import sys
sys.path.append('./lib')
import myutils

lam = boto3.client('lambda')
sns = boto3.client('sns')
topic_name=os.environ.get('TOPIC_NAME', 'new_polly_events')

'''
policy = "{"Version":"2012-10-17",
		"Id":"default",
		"Statement":[
			{"Sid":"lambda-43c3a095-abd0-4bdf-9fd5-xxxxx",
			 "Effect":"Allow",
   			 "Principal":
				{"Service":"sns.amazonaws.com"},
			 "Action":"lambda:InvokeFunction",
			 "Resource":"arn:aws:lambda:us-east-1:xxxxx:function:PostReader_ConvertToAudio",
			 "Condition":{"ArnLike":
					{"AWS:SourceArn":"arn:aws:sns:us-east-1:xxxx:new_posts"}
				     }
			}
		]
	   }"
'''
function_name = 'PostReader_ConvertToAudio'
res = lam.get_function(FunctionName=function_name)
function_arn = res['Configuration']['FunctionArn']
topics = sns.list_topics()
for topic in topics["Topics"]:
	if topic_name in str(topic['TopicArn']):
		topic_arn = topic['TopicArn']
response = lam.add_permission(
			FunctionName=function_name,
			StatementId= "lambda-policy-for-sns-invoke-1",
			Action= "lambda:InvokeFunction",
			Principal= "sns.amazonaws.com",
			SourceArn= topic_arn
			)

fname = f'Adding IAM permission for SNS to invoke Lambda function {function_name}'
myutils.myprint ('INFO', fname, response)
#print (json.dumps(response, indent=4, sort_keys=True, default=str))

'''
 {
            "SubscriptionArn": "arn:aws:sns:us-east-1:xxxxxx:new_posts:1f4c82a1-4a02-4650-8a03-xxxx",
            "Owner": "xxxxxx",
            "Protocol": "lambda",
            "Endpoint": "arn:aws:lambda:us-east-1:xxxxx:function:PostReader_ConvertToAudio",
            "TopicArn": "arn:aws:sns:us-east-1:xxxxxx:new_posts"
        }
'''
# set the sns subscription for the lambda function
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='lambda',
    Endpoint=function_arn,
    ReturnSubscriptionArn=True
)
fname = f'Adding SNS subscription for Lambda function {function_name}'
myutils.myprint ('INFO', fname, response)
#print (json.dumps(response, indent=4, sort_keys=True, default=str))