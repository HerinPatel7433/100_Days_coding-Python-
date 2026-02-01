"""Simple Email Sending program // please add require details and setup your gmail for app password"""
import smtplib as sm

my_email = "Your Email"
password = "Your app password"

connection = sm.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="receiver's email", msg="Subject:Hello\n\nThis is the body of my email")
