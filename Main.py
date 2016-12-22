import telegram
import constants
import db_connect
import mood
import time
import random


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
    last_update_id = None
    connected = False
    while not connected:
        try:
            last_update_id = bot.getUpdates()[-1].update_id
            connected = True
        except IndexError:  # falls keine Updates
            connected = True
        except telegram.error.NetworkError:
            print("Verbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)
    print("last_update_id = ", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        try:
            for update in bot.getUpdates(offset=last_update_id):
                # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
                print("update = ", update)

                # like_percentage des Users zufällig neu setzen
                user = get_user(update)
                like_percentage = random.randint(0, 100)
                mood.set_mood(user, like_percentage)

                # like_percentage des Users neu setzen in der Datenbank
                last_update_id = update.update_id + 1
            if temp is not last_update_id:
                print("last_update_id", last_update_id)
            time.sleep(3)
        except telegram.error.NetworkError:
            print("Verbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)


# User-Objekt aus dem Update-Objekt holen
# je nach Update-Art (Nachricht, Inline Query, usw. liegt das User-Objekt in einem anderen Teil des Update-Objekts
def get_user(update):
    if update.message:  # wenn eine Nachricht gesendet wurde
        return update.message.from_user
    if update.edited_message:  # wenn eine Nachricht bearbeitet wurde
        return update.edited_message.from_user
    if update.inline_query:  # wenn eine Inline Query bearbeitet wurde
        return update.inline_query.from_user
    if update.channel_post:  # wenn eine Kanalnachricht gesendet wurde
        return update.channel_post.from_user
    if update.edited_channel_post:  # wenn eine Kanalnachricht bearbeitet wurde
        return update.edited_channel_post.from_user


if __name__ == '__main__':
    main()
