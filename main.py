import requests
import json
from pymongo import MongoClient
import re
from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
from misc.variables import *
from misc import smtp_server as smtp

app = Flask(__name__)
sslify = SSLify(app)


def db_sync(data, chat_id):
    db = MongoClient('localhost', 27017)
    db = db.telegram_bot
    collection = db[str(chat_id)]
    for elem in collection.find({}):
        if elem['chat_id'] == chat_id:
            collection.replace_one(elem, data)
            return 'done'
        else:
            continue
    try:
        data['_id'] = collection.count_documents({}) + 1
    except:
        data['_id'] = 0
    collection.insert_one(data)


def load_data(chat_id):
    db = MongoClient('localhost', 27017)
    table = db['telegram_bot']
    for elem in table[str(chat_id)].find({}):
        return elem


def send_message(chat_id, text=WELCOME_MESSAGE):
    requests.post(f"{URL}sendmessage", {'chat_id': chat_id, 'text': text})


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        chat_id = data["message"]["chat"]["id"]
        message = data["message"]["text"]
        user_data = {
            'chat_id': chat_id,
            'subject': None,
            'title': None,
            'text': None,
            'user_id': data["message"]["from"]["id"],
            'user_name': data["message"]["from"]["username"]
        }
        user_data = load_data(chat_id)
        print(user_data)
        if '/start' in message:
            send_message(chat_id)

        if r'/write'.lower() in message:
            send_message(chat_id, 'введите почту куда отправить (пример: #to example@example.com)')

        if '#to' in message:
            user_data['subject'] = message.replace('#to', '')
            db_sync(user_data, chat_id)
            print(user_data)
            send_message(chat_id, 'введите название письма (пример: #title Привет)')

        if '#title' in message:
            user_data['title'] = message.replace('#title', '')
            db_sync(user_data, chat_id)
            print(user_data)

        if '#text' in message:
            user_data['text'] = message.replace('#text', '')
            db_sync(user_data, chat_id)
            print(user_data)

        if '/send' in message:
            if None not in user_data.values():
                smtp.send_mail()
        return jsonify(data)

    return '<h1>Hello im a bot</h1>'


if __name__ == '__main__':
    # main()
    app.run()
    # mikettestbot_db({'elena': 'my role', 'chat_id': '123123123'}, '123123123')
    # load_data('123123123')
