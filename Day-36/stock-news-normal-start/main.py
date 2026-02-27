import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Put Your API Keys and Numbers here to Run the Project 
STOCK_API_KEY = os.environ.get("STOCK_API_KEY", "YOUR_ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "YOUR_NEWSAPI_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID", "YOUR_TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "YOUR_TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER", "YOUR_TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER", "YOUR_TWILIO_VERIFIED_NUMBER")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json().get("Time Series (Daily)")

if not data:
    print("Error fetching stock data:", response.text)
else:
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    up_down = None
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    diff_percent = round((abs(difference) / float(day_before_yesterday_closing_price)) * 100)

    if diff_percent >= 5: 
        news_params = {
            "qInTitle": COMPANY_NAME,
            "apiKey": NEWS_API_KEY,
            "sortBy": "publishedAt",
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        news_response.raise_for_status()
        articles = news_response.json().get("articles", [])

        three_articles = articles[:3]

        formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER
            )
            print(f"Message sent! status: {message.status}")
    else:
        print(f"Stock price difference is {diff_percent}%, which is not >= 5%. No news sent.")
