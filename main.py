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
    global MSG_UPD_ID
    if msg_upd_id != MSG_UPD_ID:
        MSG_UPD_ID = msg_upd_id
        message = {
            'chat_id': chat_id,
            'text': message_text,
        }
        return message


def send_message(chat_id, text="Hello i'm Mike's bot!"):
    requests.get(f"{URL}sendmessage?chat_id={chat_id}&text={text}")


def main():
    while True:
        data = get_message()
        if data != None:
            chat_id = data["chat_id"]
            text = data["text"]
            if '/start' in text:
                send_message(chat_id, 'hello, how can i help you?')
        else:
            continue


if __name__ == '__main__':
    main()
