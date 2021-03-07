from .data import *

TOKEN = telegram_token
URL = 'https://api.telegram.org/bot' + TOKEN + '/'
SENDER_EMAIL = email_name
SENDER_EMAIL_PSW = email_password
PORT = 587
SMTP_SERVER = "smtp.gmail.com"
global MSG_UPD_ID
MSG_UPD_ID = 0
WELCOME_MESSAGE = """
Уважаемый пользователь, добрый день\n
Меня зовут Тестбот и я готов Вам помочь в отправлении электронной почты\n
Для того, чтобы начать оформление письма, используйте команду\n
/написать\n
"""
# RECEIVER_EMAIL = "tarabrinmv@gmail.com"
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
