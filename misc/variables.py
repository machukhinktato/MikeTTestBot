from .data import *

TOKEN = telegram_token
URL = 'https://api.telegram.org/bot' + TOKEN + '/'
SENDER_EMAIL = email_name
SENDER_EMAIL_PSW = email_password
PORT = 587
SMTP_SERVER = "smtp.gmail.com"
WELCOME_MESSAGE = """
Уважаемый пользователь, добрый день\n
Меня зовут Тестбот и я готов Вам помочь в отправлении электронной почты\n
Для того, чтобы начать оформление письма, используйте команду\n
/write\n
"""
