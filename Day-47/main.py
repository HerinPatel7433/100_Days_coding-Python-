import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

price_whole = soup.find(class_="a-price-whole").text.replace(".", "")
price_fraction = soup.find(class_="a-price-fraction").text

current_price = float(f"{price_whole}.{price_fraction}")
print(f"Current Price: ${current_price:.2f}")

load_dotenv()

BUY_PRICE = 100.00
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RE_EMAIL")

if current_price < BUY_PRICE:
    message = f"Subject: Instant Pot Price Drop Alert!\n\nThe Instant Pot is now ${current_price:.2f}!\nBuy it here: {url}"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=message.encode('utf-8')  
        )
    print("Price drop email sent!")
else:
    print(f"Price is still too high (${current_price}). No email sent.")