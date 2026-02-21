"""Simple daily Quotes Sender"""
import datetime as dt
import smtplib as sm
import random

MY_EMAIL = "Your Email"
MY_PASSWORD = "Your App Password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("Day-32\\daily_quotes_sender\\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with sm.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )