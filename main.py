import requests
from misc.variables import *
from misc import smtp_server as smtp


def get_updates():
    server_answer = requests.get(URL + 'getupdates').json()
    return server_answer


def get_message():
    data = get_updates()
    msg_upd_id = data['result'][-1]['update_id']
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {
        'chat_id': chat_id,
        'text': message_text,
        'last_upd_id': msg_upd_id,
    }
    return message


def send_message(chat_id, text="Hello i'm Mike's bot!"):
    requests.get(f"{URL}sendmessage?chat_id={chat_id}&text={text}")


def main():

    while True:
        data = get_message()
        last_upd_id = data["last_upd_id"]
        chat_id = data["chat_id"]
        text = data["text"]
        output_data = send_message(chat_id, 'what do you want?')
        if 'eat' in text:
            send_message(chat_id, 'which one?')


if __name__ == '__main__':
    get_message()
