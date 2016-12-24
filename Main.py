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
                # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben (core.telegram.org/bots/api#update)
                print("update =", update)

                # Inline-Query abfragen
                if update.inline_query and update.inline_query.query:
                    params_dict = {'inline_query_id': update.inline_query.id,
                                   'results': get_inline_results(update.inline_query.query)}
                    send_reaction(bot, 'inline', params_dict)

                # Nachricht abfragen
                if update.message and update.message.text == "/kochnudeln":
                    params_dict = {'chat_id': update.message.chat_id,
                                   'text': 'Ok, wird gemacht....'}
                    send_reaction(bot, 'text', params_dict)
                    event = koch_nudeln(update.message)
                    event_handler.add_event(event)

                # like_percentage des Users zufällig neu setzen
                user = get_user(update)
                like_percentage = random.randint(0, 100)
                mood.set_mood(user, like_percentage)

                # Update-ID hochzählen
                last_update_id = update.update_id + 1

            # Events abfragem
            # if event_handler.update_available():
            for event_update in event_handler.get_update():
                message = event_update[0]
                text = event_update[1]
                params_dict = {'chat_id': message.chat_id,
                               'text': text,
                               'message_id': message.message_id}
                send_reaction(bot, 'text', params_dict)

            if temp is not last_update_id:
                print("last_update_id =", last_update_id)
            time.sleep(1)
        except telegram.error.NetworkError as error:
            print(error)
            print("Verbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            time.sleep(10)


# ID des letzten unverarbeiteten Updates holen
def get_last_update_id(bot):
    while True:
        try:
            return bot.getUpdates()[-1].update_id
        except IndexError:  # falls keine Updates
            return None
        except telegram.error.NetworkError as error:
            print(error)
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


def get_inline_results(query_string):
    text = "Oh, hallo, Herr " + query_string + "!"
    input_text = telegram.InputTextMessageContent(text)
    return [telegram.InlineQueryResultArticle('test_inline_query', "Mederer", input_text)]


def koch_nudeln(message):
    name = message.from_user.first_name
    kochnudeln = Event(message, [[5, "koche Wass0 für " + name + "...."],
                                 [5, "koche Nudeln für " + name + "...."],
                                 [5, "Nudeln für " + name + " sind fertig! :3"]])
    return kochnudeln


def send_reaction(bot, action, params_dict):
        if action == 'text':
            print(params_dict.get('message_id', None))
            bot.send_message(chat_id=params_dict['chat_id'],
                             text=params_dict['text'],
                             reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'photo':
            bot.send_photo(chat_id=params_dict['chat_id'],
                           text=params_dict['photo'],
                           caption=params_dict['caption'],
                           reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'gif':
            bot.send_document(chat_id=params_dict['chat_id'],
                              text=params_dict['gif'],
                              caption=params_dict['caption'],
                              reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'video':
            bot.send_video(chat_id=params_dict['chat_id'],
                           text=params_dict['gif'],
                           caption=params_dict['caption'],
                           reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'inline':
            bot.answer_inline_query(inline_query_id=params_dict['inline_query_id'],
                                    results=params_dict['results'])


if __name__ == '__main__':
    main()
