import requests
import json
import re
from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
from misc.variables import *
from misc import smtp_server as smtp

app = Flask(__name__)

sslify = SSLify(app)


def write_json(data, filename='answer.json'):
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


"""
def get_updates():
    # делаем запросы на сервера телеграма, что не актуально для вебхука
    server_answer = requests.get(URL + 'getupdates').json()
    # write_json(server_answer)
    return server_answer


def get_message():
    data = get_updates()
    msg_upd_id = data['result'][-1]['update_id']
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    global MSG_UPD_ID
    if msg_upd_id != MSG_UPD_ID:
        MSG_UPD_ID = msg_upd_id
        message = {
            'chat_id': chat_id,
            'text': message_text,
        }
        return message
"""


def send_message(chat_id, text=WELCOME_MESSAGE):
    requests.post(f"{URL}sendmessage", {'chat_id': chat_id, 'text': text})


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        user_data = {
            'subject': '',
            'title': '',
            'text': '',
            'user_id': data["message"]["from"]["id"],
            'user_name': data["message"]["from"]["username"]
        }
        write_json(data)
        chat_id = data["message"]["chat"]["id"]
        message = data["message"]["text"]
        if '/start' in message:
            send_message(chat_id)
        if r'написать'.lower() in message:
            send_message(chat_id, 'введите почту куда отправить (пример: #to example@example.com)')

        if r'#to' in message:
            send_message(chat_id, 'good')
        return jsonify(data)
    return '<h1>Hello im a bot</h1>'


def Banana:
    pass

"""
def main():
    while True:
        data = get_message()
        if data != None:
            chat_id = data["chat_id"]
            text = data["text"]
            if '/start' in text:
                send_message(chat_id)
        else:
            continue
"""

if __name__ == '__main__':
    # main()
    app.run()
