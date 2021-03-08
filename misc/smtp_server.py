import smtplib, ssl
from .variables import *


def send_mail(sending_data):
    context = ssl.create_default_context()
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    message = f"""\
    {sending_data['title']}\n
    \n
    \n
    \n
    {sending_data['text']}
    """
    try:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)
        server.sendmail(SENDER_EMAIL, sending_data['subject'], message)
    except Exception as e:
        print(e)
        server.quit()


if __name__ == '__main__':
    send_mail()
