# import json
# import os
# import requests
# from linebot import LineBotApi, WebhookHandler
# from linebot.models import MessageEvent, TextMessage, TextSendMessage

# # LINE Bot configuration
# line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
# handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

# # Alpha Vantage API key
# API_KEY = "TNXIX9B96VKUOQDF"  # Your Alpha Vantage API key

# def get_stock_price(symbol):
#     # Alpha Vantage API URL
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    
#     # Make the API request
#     response = requests.get(url)
#     data = response.json()
    
#     # Parse the JSON data to extract the latest stock price
#     try:
#         time_series = data['Time Series (5min)']
#         latest_time = sorted(time_series.keys())[0]
#         latest_price = time_series[latest_time]['1. open']
#         return latest_price
#     except KeyError:
#         return None

# def lambda_handler(event, context):
#     # Parse the incoming LINE message
#     msg = json.loads(event['body'])
#     user_message = msg['events'][0]['message']['text']
    
#     # Get the stock price
#     stock_price = get_stock_price(user_message)
    
#     if stock_price:
#         reply_text = f"The latest price for {user_message} is ${stock_price}."
#     else:
#         reply_text = f"Could not retrieve data for {user_message}. Please check the stock symbol."
    
#     # Reply to the user
#     line_bot_api.reply_message(
#         msg['events'][0]['replyToken'],
#         TextSendMessage(text=reply_text)
#     )
    
#     return {
#         "statusCode": 200,
#         "body": json.dumps({"message": 'ok'})
#     }




# import json
# import os
# import requests
# from linebot import LineBotApi, WebhookHandler
# from linebot.models import (
#     CarouselTemplate, CarouselColumn, TextSendMessage, TextMessage, TemplateSendMessage, URIAction
# )

# # LINE Bot configuration
# line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
# handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

# # Alpha Vantage API key
# API_KEY = "TNXIX9B96VKUOQDF"  # Your Alpha Vantage API key

# # List of NASDAQ 100 symbols
# NASDAQ_100_SYMBOLS = [
#     "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "FB", "TSLA", "AVGO", "ADBE", "CSCO",
#     "PEP", "INTC", "NFLX", "TXN", "CMCSA", "QCOM", "COST", "PYPL", "SBUX", "AMD",
#     "INTU", "AMAT", "BKNG", "ADP", "MDLZ", "ISRG", "HON", "MU", "GILD", "FISV",
#     # Add all NASDAQ 100 symbols here
# ]

# def get_stock_price(symbol):
#     # Alpha Vantage API URL
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    
#     # Make the API request
#     response = requests.get(url)
#     data = response.json()
    
#     # Parse the JSON data to extract the latest stock price
#     try:
#         time_series = data['Time Series (5min)']
#         latest_time = sorted(time_series.keys())[0]
#         latest_price = time_series[latest_time]['1. open']
#         return latest_price
#     except KeyError:
#         return None

# def get_most_active_nasdaq_stocks():
#     # Alpha Vantage API URL for top gainers/losers
#     url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}"
    
#     # Make the API request
#     response = requests.get(url)
#     data = response.json()

#     # Extract the most actively traded stocks from NASDAQ 100
#     most_active_stocks = []
#     try:
#         for stock in data['most_actively_traded']:
#             if stock['ticker'] in NASDAQ_100_SYMBOLS:
#                 most_active_stocks.append({
#                     "symbol": stock['ticker'],
#                     "price": stock['price'],
#                     "change": stock['change_percentage'],
#                     "volume": stock['volume'],
#                     "image_url": f"https://logo.clearbit.com/{stock['ticker'].lower()}.com",  # Using Clearbit Logo API
#                     "link": f"https://www.example.com/{stock['ticker']}"
#                 })
#             if len(most_active_stocks) >= 5:
#                 break
#     except KeyError:
#         pass
    
#     return most_active_stocks

# def create_most_active_carousel():
#     carousel_columns = []

#     # Fetch the top 5 most active NASDAQ stocks
#     most_active_stocks = get_most_active_nasdaq_stocks()

#     # Create Carousel Columns
#     for stock in most_active_stocks:
#         column = CarouselColumn(
#             thumbnail_image_url=stock['image_url'],
#             title=f"{stock['symbol']} - ${stock['price']}",
#             text=f"Change: {stock['change']}\nVolume: {stock['volume']}",
#             actions=[
#                 URIAction(label='Read more', uri=stock['link'])
#             ]
#         )
#         carousel_columns.append(column)

#     # Create Carousel Template
#     carousel_template = CarouselTemplate(columns=carousel_columns)
#     return TemplateSendMessage(alt_text="Top 5 Most Active NASDAQ Stocks", template=carousel_template)

# def lambda_handler(event, context):
#     # Parse the incoming LINE message
#     msg = json.loads(event['body'])
#     user_message = msg['events'][0]['message']['text'].upper()  # Convert to uppercase for consistency

#     if user_message == "MOST ACTIVE":
#         # Create the Carousel Template message
#         carousel_message = create_most_active_carousel()

#         # Reply to the user with the carousel
#         line_bot_api.reply_message(
#             msg['events'][0]['replyToken'],
#             carousel_message
#         )
#     else:
#         # Try to get the stock price
#         stock_price = get_stock_price(user_message)
        
#         if stock_price:
#             reply_text = f"The latest price for {user_message} is ${stock_price}."
#         else:
#             reply_text = f"Could not retrieve data for {user_message}. Please check the stock symbol."

#         # Reply to the user with the stock price or error message
#         line_bot_api.reply_message(
#             msg['events'][0]['replyToken'],
#             TextSendMessage(text=reply_text)
#         )
    
#     return {
#         "statusCode": 200,
#         "body": json.dumps({"message": 'ok'})
#     }










import json
import os
import boto3
import requests
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage, StickerSendMessage, CarouselTemplate, 
    CarouselColumn, TemplateSendMessage, URIAction
)



# LINE Bot configuration
line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])


# Alpha Vantage API key
API_KEY = "TNXIX9B96VKUOQDF"  # Your Alpha Vantage API key

# List of NASDAQ 100 symbols
NASDAQ_100_SYMBOLS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "FB", "TSLA", "AVGO", "ADBE", "CSCO",
    "PEP", "INTC", "NFLX", "TXN", "CMCSA", "QCOM", "COST", "PYPL", "SBUX", "AMD",
    "INTU", "AMAT", "BKNG", "ADP", "MDLZ", "ISRG", "HON", "MU", "GILD", "FISV",
    # Add all NASDAQ 100 symbols here
]

def store_user_id(user_id):
    # Check if the user_id already exists in DynamoDB
    # DynamoDB configuration
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LineBotUsers')  # Replace with your DynamoDB table name
    response = table.get_item(Key={'user_id': user_id})
    if 'Item' not in response:
        # Store user_id in DynamoDB table if it doesn't exist
        table.put_item(Item={'user_id': user_id})
        print(f"User ID {user_id} added to DynamoDB.")
        return True  # Indicates that this is a new user
    else:
        print(f"User ID {user_id} already exists in DynamoDB. Skipping...")
        return False  # Indicates that the user is already in the database

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

def get_most_active_nasdaq_stocks():
    # Alpha Vantage API URL for top gainers/losers
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}"
    
    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Extract the most actively traded stocks from NASDAQ 100
    most_active_stocks = []
    try:
        for stock in data['most_actively_traded']:
            if stock['ticker'] in NASDAQ_100_SYMBOLS:
                most_active_stocks.append({
                    "symbol": stock['ticker'],
                    "price": stock['price'],
                    "change": stock['change_percentage'],
                    "volume": stock['volume'],
                    "image_url": f"https://logo.clearbit.com/{stock['ticker'].lower()}.com",  # Using Clearbit Logo API
                    "link": f"https://www.example.com/{stock['ticker']}"  # Replace with actual link
                })
            if len(most_active_stocks) >= 5:
                break
    except KeyError:
        pass
    
    return most_active_stocks

def create_most_active_carousel():
    carousel_columns = []

    # Fetch the top 5 most active NASDAQ stocks
    most_active_stocks = get_most_active_nasdaq_stocks()

    # Create Carousel Columns
    for stock in most_active_stocks:
        column = CarouselColumn(
            thumbnail_image_url=stock['image_url'],
            title=f"{stock['symbol']} - ${stock['price']}",
            text=f"Change: {stock['change']}\nVolume: {stock['volume']}",
            actions=[
                URIAction(label='Read more', uri=stock['link'])
            ]
        )
        carousel_columns.append(column)

    # Create Carousel Template
    carousel_template = CarouselTemplate(columns=carousel_columns)
    return TemplateSendMessage(alt_text="Top 5 Most Active NASDAQ Stocks", template=carousel_template)

def lambda_handler(event, context):
    try:
        # Parse the incoming LINE message
        msg = json.loads(event['body'])
        user_id = msg['events'][0]['source']['userId']  # Extract user ID
        user_message = msg['events'][0]['message']['text'].upper()  # Convert to uppercase for consistency

        # Store the user ID in DynamoDB and check if it's a new user
        # is_new_user = store_user_id(user_id)
        if store_user_id(user_id):
            # Send a welcome message and a sticker to the new user
            line_bot_api.reply_message(
                msg['events'][0]['replyToken'],
                [
                    TextSendMessage(text="Welcome! You have been added to the daily message list."),
                    # StickerSendMessage(package_id='1', sticker_id='1')  # Replace with your desired sticker IDs
                ]
            )
        if user_message == "MOST ACTIVE":
            # Create the Carousel Template message
            carousel_message = create_most_active_carousel()

            # Reply to the user with the carousel
            line_bot_api.reply_message(
                msg['events'][0]['replyToken'],
                carousel_message
            )
        else:
            # Try to get the stock price
            stock_price = get_stock_price(user_message)
            
            if stock_price:
                reply_text = f"The latest price for {user_message} is ${stock_price}."
            else:
                reply_text = f"Could not retrieve data for {user_message}. Please check the stock symbol."

            # Reply to the user with the stock price or error message
            line_bot_api.reply_message(
                msg['events'][0]['replyToken'],
                TextSendMessage(text=reply_text)
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Request handled successfully!')
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred.')
        }
