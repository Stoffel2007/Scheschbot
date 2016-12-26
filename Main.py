import telegram
import aggronyme
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
            print('\t', end='')
            for value in line:
                print(value, end="\t")
            print()

    # Bot-Objekt erstellen
    bot = telegram.Bot(constants.scheschkey)

    # EventHandler für zeitbasierte Events
    event_handler = EventHandler()

    # ID des letzten unverarbeiteten Updates holen
    last_update_id = get_last_update_id(bot)
    print("last_update_id =", last_update_id, '\n')

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        try:
            for update in bot.getUpdates(offset=last_update_id):
                # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben (core.telegram.org/bots/api#update)
                print("\tupdate =", update)

                # Inline-Query abfragen
                if update.inline_query and update.inline_query.query:
                    params_dict = {'inline_query_id': update.inline_query.id,
                                   'results': get_inline_results(update.inline_query.query)}
                    send_reaction(bot, 'inline', params_dict)

                # Nachricht abfragen
                if update.message and update.message.text.startswith("/kochnudeln"):
                    params_dict = {'chat_id': update.message.chat_id,
                                   'text': 'Ok, wird gemacht....'}
                    send_reaction(bot, 'text', params_dict)
                    event = koch_nudeln(update.message)
                    event_handler.add_event(event)

                # Nachricht abfragen
                if update.message and update.message.text.startswith("/aggro"):
                    params = update.message.text.split(' ', 1)[1]
                    message = aggronyme.aggro(params)
                    params_dict = {'chat_id': update.message.chat_id,
                                   'text': message}
                    send_reaction(bot, 'text', params_dict)

                # Inline-Button wurde gedrückt
                if update.callback_query:
                    params_dict = {'chat_id': update.callback_query.message.chat_id,
                                   'message_id': update.callback_query.message.message_id}

                    data_array = update.callback_query.data.split(' ', 1)
                    params = data_array[1]
                    if data_array[0] == 'yes':
                        if aggronyme.insert_words(params) is True:
                            params_dict['text'] = 'legg0 :3\n' \
                                                  '"' + params + '" erfolgreich zur Datenbank hinzugefügt'
                        else:
                            # Artikel rausnehmen, falls vorhanden
                            if params.startswith('der ') or params.startswith('die ') or params.startswith('die '):
                                word = params.split(' ', 1)[1]
                            else:
                                word = params

                            vote_incremented = aggronyme.increment_vote(word)
                            if not vote_incremented:
                                print('\tkonnte Votes von ' + word + ' nicht inkrementieren')
                            params_dict['text'] = '"' + params + '"  konnte nicht zur Datenbank hinzugefügt werden\n' +\
                                                  'Eventuell ist dieses Wort bereits vorhanden'
                    elif data_array[0] == 'no':
                        params_dict['text'] = '"' + params + '" abgelehnt'

                    send_reaction(bot, 'edit_message', params_dict)

                # Nachricht abfragen
                if update.message and update.message.text.startswith("/feedme"):
                    params = update.message.text.split(' ', 1)[1]
                    button1 = telegram.InlineKeyboardButton('Akzeptieren', callback_data='yes ' + params)
                    button2 = telegram.InlineKeyboardButton('Ablehnen', callback_data='no ' + params)
                    keyboard = telegram.InlineKeyboardMarkup([[button1, button2]])

                    # User-IDs von Alexey, Andi, Stoffel
                    admin_ids = db_connect.select('users', 'telegram_id, first_name', where_expression='is_admin = 1')

                    for i in range(len(admin_ids)):
                        params_dict = {'chat_id': admin_ids[i][0],
                                       'text': '"' + params + '" akzeptieren oder ablehnen?',
                                       'reply_markup': keyboard}
                        try:
                            send_reaction(bot, 'text', params_dict)
                        except telegram.error.Unauthorized:
                            print('\t' + admin_ids[i][1].__str__() + ' hat den Bot nicht gestartet')

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
                print('last_update_id =', last_update_id, '\n')
            time.sleep(1)
        except telegram.error.NetworkError:
            print('\tVerbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....')
            time.sleep(10)


# ID des letzten unverarbeiteten Updates holen
def get_last_update_id(bot):
    while True:
        try:
            return bot.getUpdates()[-1].update_id
        except IndexError:  # falls keine Updates
            return None
        except telegram.error.NetworkError as error:
            print('\tVerbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....')
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
    if update.callback_query:  # wenn eine Inline Query bearbeitet wurde
        return update.callback_query.from_user


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
    try:
        if action == 'text':
            bot.send_message(chat_id=params_dict['chat_id'],
                             text=params_dict['text'],
                             reply_to_message_id=params_dict.get('message_id', None),
                             reply_markup=params_dict.get('reply_markup', None))
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
        elif action == 'edit_message':
            bot.edit_message_text(chat_id=params_dict['chat_id'],
                                  message_id=params_dict['message_id'],
                                  text=params_dict['text'])
        else:
            print('\tfalsche action-Variable (' + action + ')')
    except KeyError as error:
        print('\tFehler im Parameter-Array:')
        print('\t', end='')
        print(params_dict)


if __name__ == '__main__':
    main()
