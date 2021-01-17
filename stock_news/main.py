import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "ca078bf4a5eb4856a1aa8b1cdaf9bad9"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

STOCK_API_KEY = 'AINB644NNUQM4606'
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

TWILIO_SID = "AC75a69cf3f04be0994dcf47cf73238b8f"
TWILIO_TOKEN = "4022dba396eacb45f49321d5710cebaa"


response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

stock_difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if stock_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent_difference = round((stock_difference / yesterday_closing_price) * 100)

# If percent difference is greater than 5, get latest news
if abs(percent_difference) > 1:
    response = requests.get(NEWS_ENDPOINT, news_parameters)
    response.raise_for_status()
    news_data = response.json()["articles"]
    first_three_articles = news_data[:3]


    formatted_articles_list = [f"{STOCK_NAME}: {up_down} {abs(percent_difference)}% \n" \
                               f"Headline: {article['title']}. \n" \
                               f"Description: {article['description']}"
                               for article in first_three_articles]

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in formatted_articles_list:
        message = client.message.create(
            body=article,
            from_='+12149150387',
            to='+13156634576'
        )

