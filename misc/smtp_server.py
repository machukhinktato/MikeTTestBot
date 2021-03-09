import smtplib, ssl
from .variables import *


def send_mail(sending_data):
    """
    Функция отправляет письма
    На вход принимает словарь
    """
    context = ssl.create_default_context()
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    message = f"""\
    {sending_data['title']}\n
    \n
    \n
    \n
    {sending_data['text']}
    \n
    {sending_data['user_id']}
    {sending_data['user_name']}
    """
    try:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_EMAIL_PSW)
        server.sendmail(SENDER_EMAIL, sending_data['subject'], message)
    except Exception as e:
        print(e)
        server.quit()


if __name__ == '__main__':
    send_mail()
