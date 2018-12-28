#!/bin/bash
# This is the global environment file
# for our Polly demo

# USE Absolute path for PROJECT DIR
export PROJECT_DIR='/home/username/polly-project'
export LOG_DIR='logs'
export LOG_FILE='app-deployment.log'

# dynamodb vars
export REGION='us-east-1'
export TABLE_NAME='PollyProject'

#S3
export BUCKET_IN='user-pollybucket-in'
export BUCKET_OUT='user-pollybucket-out'

#SNS
export TOPIC_NAME='new_polly_events'

#IAM
export LAMBDA_POLICY='user-lambda-policy'
export LAMBDA_ROLE='user-lambda-role'

#API GATEWAY
export API_NAME='ServerLessPollyAPI'
export API_STAGE_NAME='development'




