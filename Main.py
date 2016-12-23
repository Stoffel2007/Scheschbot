import threading

import telegram
import time
import constants
import db_connect
from Async.AsyncHandler import *
from Async.Event import Event
from Async.Task import Task

def main():
    # Beispiel-Query
    result = db_connect.query('SELECT * FROM users')
    for line in result:
        for value in line:
            print(value, end="\t")
        print()

    # Bot-Objekt erstellen
    bot = telegram.Bot(constants.scheschkey)

    # ID des letzten unverarbeiteten Updates holen
    handler = AsyncHandler()
    try:
        last_update_id = bot.getUpdates()[-1].update_id
    except IndexError:  # falls keine Updates
        last_update_id = None
    print("last_update_id = ", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        for update in bot.getUpdates(offset=last_update_id):
            # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
            print("update = ", update)
            if update.message:
                if update.message.text == "/kochnudeln":
                    bot.send_message(update.message.chat_id, "Ok, wird gemacht....")
                    koch_nudeln()
                if handler.updateavailable():
                    for eventupdate in handler.getupdate():
                        bot.send_message(eventupdate[0], eventupdate[1])
            last_update_id = update.update_id + 1

        if temp is not last_update_id:
            print("last_update_id", last_update_id)

        time.sleep(3)


def koch_nudeln():


def set_event():
    print("Nudeln sind fertig!")


if __name__ == '__main__':
    main()
