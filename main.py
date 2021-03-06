import smtplib, ssl
import requests
import json
from pprint import pprint
from misc.data import *

TOKEN = telegram_token
URL = 'https://api.telegram.org/bot' + TOKEN + '/'
SENDER_EMAIL = email_name
SENDER_EMAIL_PSW = email_password
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


def get_updates():
    server_answer = requests.get(URL + 'getupdates').json()
    pprint(server_answer)
    return server_answer


if __name__ == '__main__':
    get_updates()

#thats all for today