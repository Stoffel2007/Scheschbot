from Functions import timed_messages
from datetime import datetime, timedelta


def cook(message, param):
    user_name = message.from_user.first_name
    food = param.title()  # auf Großschreibung achten

    # Dauer/Nachricht
    messages = [[15, 'koche Wass0 für ' + user_name + '....'],
                [15, 'koche ' + food + ' für ' + user_name + '....'],
                [15, food + ' für ' + user_name + ' sind fertig! :3']]

    add_messages_to_database(messages, message.chat_id)

    return 'Ok, wird gemacht....'


def add_messages_to_database(messages, chat_id):
    value_2d_array = []
    send_time = datetime.now()

    for message in messages:
        # Sekunden zu aktueller Zeit addieren
        send_time += timedelta(seconds=message[0])

        value_2d_array += [[message[1], send_time, chat_id]]

    timed_messages.insert_timedmessages(value_2d_array)
