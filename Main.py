import telegram
import constants
import db_connect
import mood
import time
import random
from Events.EventHandler import *
from Events.Event import Event


def main():
    # Beispiel-Query
    result = db_connect.select('users')
    # beim Fehlschlagen der Datenbankabfrage wird False zurückgeliefert
    if result:
        for line in result:
            for value in line:
                print(value, end="\t")
            print()

    # Bot-Objekt erstellen
    bot = telegram.Bot(constants.scheschkey)

    # EventHandler für zeitbasierte Events
    event_handler = EventHandler()

    # ID des letzten unverarbeiteten Updates holen
    last_update_id = get_last_update_id(bot)
    print("last_update_id =", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        try:
            for update in bot.getUpdates(offset=last_update_id):
                # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
                print("update =", update)

                # Inline-Query abfragen
                if update.inline_query and update.inline_query.query:
                    bot.answer_inline_query(update.inline_query.id, answer_inline(update.inline_query))

                # Nachricht abfragen
                if update.message:
                    if update.message.text == "/kochnudeln":
                        bot.send_message(update.message.chat_id, "Ok, wird gemacht....")
                        event_handler.add_event(koch_nudeln(update.message.chat_id))

                # like_percentage des Users zufällig neu setzen
                user = get_user(update)
                like_percentage = random.randint(0, 100)
                mood.set_mood(user, like_percentage)

                # Update-ID hochzählen
                last_update_id = update.update_id + 1

            # Events abfragem
            if event_handler.update_available():
                for eventupdate in event_handler.get_update():
                    bot.send_message(eventupdate[0], eventupdate[1])

            if temp is not last_update_id:
                print("last_update_id =", last_update_id)
            time.sleep(3)
        except telegram.error.NetworkError:
            print("Verbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)


# ID des letzten unverarbeiteten Updates holen
def get_last_update_id(bot):
    while True:
        try:
            return bot.getUpdates()[-1].update_id
        except IndexError:  # falls keine Updates
            return None
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


def answer_inline(inline_query):
    text = "Oh, hallo, Herr " + inline_query.query + "!"
    input_text = telegram.InputTextMessageContent(text)
    return [telegram.InlineQueryResultArticle('test_inline_query', "Mederer", input_text)]


def koch_nudeln(eventid):
    kochnudeln = Event(eventid, [[5, "backe Mandarinen"],
                                 [5, "esse SToffel"]])
    return kochnudeln


if __name__ == '__main__':
    main()
