import telegram
import time
import constants
import db_connect
import mood


def main():
    # Beispiel-Query
    result = db_connect.query('SELECT * FROM users')
    if result:
        for line in result:
            for value in line:
                print(value, end="\t")
            print()

    # Bot-Objekt erstellen
    bot = telegram.Bot(constants.scheschkey)

    # ID des letzten unverarbeiteten Updates holen
    connected = False
    while not connected:
        try:
            last_update_id = bot.getUpdates()[-1].update_id
            connected = True
        except IndexError:  # falls keine Updates
            last_update_id = None
            connected = True
        except telegram.error.NetworkError:
            print("Verbindung fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)
    print("last_update_id = ", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        try:
            for update in bot.getUpdates(offset=last_update_id):
                # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
                print("update = ", update)
                if update.message:
                    mood.set_mood(update.message.from_user, 60)
                else:
                    print("Message ist None")
                last_update_id = update.update_id + 1
            if temp is not last_update_id:
                print("last_update_id", last_update_id)
            time.sleep(3)
        except telegram.error.NetworkError:
            print("Verbindung fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)


if __name__ == '__main__':
    main()
