import telegram
import time

import db_connect


def main():
    # Beispiel-Query
    result = db_connect.query('SELECT * FROM users')
    for line in result:
        for value in line:
            print(value, end="\t")
        print()

    # Bot-Objekt erstellen
    token = '134973318:AAHUxunH8j8-KOa69SoEfy3qG4KnvzscR2U'
    bot = telegram.Bot(token)

    # ID des letzten unverarbeiteten Updates holen
    try:
        last_update_id = bot.getUpdates()[-1].update_id
    except IndexError: # falls keine Updates
        last_update_id = None
    print("last_update_id = ", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        for update in bot.getUpdates(offset=last_update_id):
            # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
            print("update = ", update)
            last_update_id = update.update_id + 1
        if temp is not last_update_id:
            print("last_update_id", last_update_id)
        time.sleep(3)


if __name__ == '__main__':
    main()
