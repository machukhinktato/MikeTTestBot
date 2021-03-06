import smtplib, ssl
from .variables import *


def send_mail(receiver_email, message):
    context = ssl.create_default_context()
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    try:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)
        server.sendmail(SENDER_EMAIL, receiver_email, message)
    except Exception as e:
        print(e)
        server.quit()
