import json
import os
import boto3
from linebot import LineBotApi
from linebot.models import TextSendMessage

# LINE Bot configuration
line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LineBotUsers')  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    # Fetch all user IDs from DynamoDB
    response = table.scan()
    user_ids = [item['user_id'] for item in response.get('Items', [])]

    # Send a message to each user
    for user_id in user_ids:
        line_bot_api.push_message(user_id, TextSendMessage(text='Daily Message: All User'))

    return {
        'statusCode': 200,
        'body': json.dumps('Messages sent successfully!')
    }
