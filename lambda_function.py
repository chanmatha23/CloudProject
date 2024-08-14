import json
import os
import requests
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# LINE Bot configuration
line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

# Alpha Vantage API key
API_KEY = "TNXIX9B96VKUOQDF"  # Your Alpha Vantage API key

def get_stock_price(symbol):
    # Alpha Vantage API URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    
    # Make the API request
    response = requests.get(url)
    data = response.json()
    
    # Parse the JSON data to extract the latest stock price
    try:
        time_series = data['Time Series (5min)']
        latest_time = sorted(time_series.keys())[0]
        latest_price = time_series[latest_time]['1. open']
        return latest_price
    except KeyError:
        return None

def lambda_handler(event, context):
    # Parse the incoming LINE message
    msg = json.loads(event['body'])
    user_message = msg['events'][0]['message']['text']
    
    # Get the stock price
    stock_price = get_stock_price(user_message)
    
    if stock_price:
        reply_text = f"The latest price for {user_message} is ${stock_price}."
    else:
        reply_text = f"Could not retrieve data for {user_message}. Please check the stock symbol."
    
    # Reply to the user
    line_bot_api.reply_message(
        msg['events'][0]['replyToken'],
        TextSendMessage(text=reply_text)
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }
