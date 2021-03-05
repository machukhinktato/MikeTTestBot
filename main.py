import smtplib, ssl
import requests
import json
from pprint import pprint
from conf.data import *


token = telegram_token
sender_email = email_name
sender_email_psw = email_password
port = 587
smtp_server = "smtp.gmail.com"
receiver_email = "tarabrinmv@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

def launch_server():
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, sender_email_psw)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:

        print(e)
    finally:
        server.quit()


def tester():
    url = 'https://api.telegram.org/bot1689484585:AAFu2z-9QnR7luTGBYHg3kY2ILbSquy4BOM/getupdates'
    server_answer = requests.get(url)
    pprint(server_answer.text)


if __name__ == '__main__':
    tester()
