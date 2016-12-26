import random
import telegram
import aggronyme
import db_connect
import mood
from Events.Event import Event


def get_messages(update, event_handler):
    # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben (core.telegram.org/bots/api#update)
    print("\n\tupdate =", update)

    # Array mit zurückzuliefernden Nachrichten
    # jede message ist ein dictionary
    message_list = []

    # Update je nach Typ anders verarbeiten
    if update.message:
        message_list = __process_message(update.message)
    elif update.edited_message:
        message_list = __process_edited_message(update.edited_message)
    elif update.edited_message:
        message_list = __process_edited_message(update.edited_message)
    elif update.inline_query and update.inline_query.query:
        message_list = __process_inline_query(update.inline_query)
    elif update.callback_query:
        message_list = __process_callback_query(update.callback_query)

    print('\tmessage_list:\n\t', end='')
    for message in message_list:
        print(message)

    # like_percentage des Users zufällig neu setzen
    user = get_user(update)
    like_percentage = random.randint(0, 100)
    mood.set_mood(user, like_percentage)

    # Inline-Query abfragen
    if update.inline_query and update.inline_query.query:
        params_dict = {'inline_query_id': update.inline_query.id,
                       'results': get_inline_results(update.inline_query.query)}
        return [{'action': 'inline', 'params_dict': params_dict}]

    # Nachricht abfragen
    if update.message and update.message.text.startswith("/kochnudeln"):
        params_dict = {'chat_id': update.message.chat_id,
                       'text': 'Ok, wird gemacht....'}
        event = koch_nudeln(update.message)
        event_handler.add_event(event)
        return [{'action': 'text', 'params_dict': params_dict}]

    # Nachricht abfragen
    if update.message and update.message.text.startswith("/aggro"):
        params = update.message.text.split(' ', 1)[1]
        message = aggronyme.aggro(params)
        params_dict = {'chat_id': update.message.chat_id,
                       'text': message}
        return [{'action': 'text', 'params_dict': params_dict}]

    # Inline-Button wurde gedrückt
    if update.callback_query:
        params_dict = {'chat_id': update.callback_query.message.chat.id,
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
                params_dict['text'] = '"' + params + '"  konnte nicht zur Datenbank hinzugefügt werden\n' + \
                                      'Eventuell ist dieses Wort bereits vorhanden'
        elif data_array[0] == 'no':
            params_dict['text'] = '"' + params + '" abgelehnt'

        return [{'action': 'edit_message', 'params_dict': params_dict}]

    # Nachricht abfragen
    if update.message and update.message.text.startswith("/feedme"):
        params = update.message.text.split(' ', 1)[1]
        button1 = telegram.InlineKeyboardButton('Akzeptieren', callback_data='yes ' + params)
        button2 = telegram.InlineKeyboardButton('Ablehnen', callback_data='no ' + params)
        keyboard = telegram.InlineKeyboardMarkup([[button1, button2]])

        # User-IDs von Alexey, Andi, Stoffel
        admin_ids = db_connect.select('users', 'telegram_id', where_expression='is_admin = 1')

        message_list = []

        for i in range(len(admin_ids)):
            params_dict = {'chat_id': admin_ids[i][0],
                           'text': '"' + params + '" akzeptieren oder ablehnen?',
                           'reply_markup': keyboard}
            message_list.append({'action': 'text', 'params_dict': params_dict})

        return message_list

    return []


def __process_message(message):
    params_dict = {'chat_id': message.chat_id,
                   'text': 'Funktion __process_message()'}
    return [{'action': 'text', 'params_dict': params_dict}]


def __process_edited_message(edited_message):
    params_dict = {'chat_id': edited_message.chat_id,
                   'text': 'Funktion __process_edited_message()'}
    return [{'action': 'text', 'params_dict': params_dict}]


def __process_inline_query(inline_query):
    params_dict = {'inline_query_id': inline_query.id,
                   'results': get_inline_results(inline_query.query)}
    return [{'action': 'inline', 'params_dict': params_dict}]


def __process_callback_query(callback_query):
    params_dict = {'chat_id': callback_query.message.chat.id,
                   'text': 'Funktion __process_callback_query()'}
    return [{'action': 'text', 'params_dict': params_dict}]


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
