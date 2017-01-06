import random
import telegram
import constants
import db_connect
import inline_results
from Functions import aggronyme, cook, mood, answer


def get_message_list(update, event_handler):
    # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben (core.telegram.org/bots/api#update)
    print("\n\tupdate =", update)

    # like_percentage des Users zufällig neu setzen
    user = __get_user(update)
    like_percentage = random.randint(0, 100)
    mood.set_mood(user, like_percentage)

    # Array mit zurückzuliefernden Nachrichten
    # jede message ist ein dictionary
    message_list = []

    # Update je nach Typ anders verarbeiten
    if update.message:
        message_list = __process_message(update.message, event_handler)
    elif update.edited_message:
        message_list = __process_edited_message(update.edited_message)
    elif update.inline_query and update.inline_query.query:
        message_list = __process_inline_query(update.inline_query)
    elif update.callback_query:
        message_list = __process_callback_query(update.callback_query)

    return message_list


def __process_message(message, event_handler):
    # Nachricht in Einzelteile zerlegen
    command, botname, param = __get_message_args(message.text)

    if botname == constants.botname:  # Kommando war an den Scheschbot gerichtet
        # passendes Kommando suchen
        # TODO: Kommandos generisch in Datenbank ablegen
        if command == 'koch':
            text = cook.cook(message, param, event_handler)
            params_dict = {'chat_id': message.chat_id,
                           'text': text}
            return [{'action': 'text', 'params_dict': params_dict}]
        if command == 'aggro':
            text = aggronyme.aggro(param)
            params_dict = {'chat_id': message.chat_id,
                           'text': text}
            return [{'action': 'text', 'params_dict': params_dict}]
        if command == 'feedme':
            # Buttons zum akzeptieren und ablehnen in  Keyboard ablegen
            button1 = telegram.InlineKeyboardButton('Akzeptieren', callback_data='yes ' + param)
            button2 = telegram.InlineKeyboardButton('Ablehnen', callback_data='no ' + param)
            keyboard = telegram.InlineKeyboardMarkup([[button1, button2]])

            # User-IDs der Admins aus der Datenbank holen
            admin_ids = db_connect.select('users', 'telegram_id', where_expression='is_admin = 1')

            message_list = []

            for i in range(len(admin_ids)):
                params_dict = {'chat_id': admin_ids[i][0],
                               'text': '"' + param + '" akzeptieren oder ablehnen?',
                               'reply_markup': keyboard}
                message_list.append({'action': 'text', 'params_dict': params_dict})

            return message_list

        output = answer.get_answer(message.text)
        print('output =', output)
        if output != '':
            params_dict = {'chat_id': message.chat_id,
                           'text': output}
            return [{'action': 'text', 'params_dict': params_dict}]

        return []  # kein passendes Kommando gefunden
    return []  # Kommando ging an anderen Bot


def __process_edited_message(edited_message):
    # Nachricht in Einzelteile zerlegen
    command, botname, param = __get_message_args(edited_message.text)

    if botname == constants.botname:  # Kommando war an den Scheschbot gerichtet
        params_dict = {'chat_id': edited_message.chat_id,
                       'text': 'bearbeitete Nachricht',
                       'message_id': edited_message.message_id}
        return [{'action': 'text', 'params_dict': params_dict}]
    return []  # Kommando ging an anderen Bot


def __process_inline_query(inline_query,):
    params_dict = {'inline_query_id': inline_query.id,
                   'results': inline_results.get_inline_results(inline_query.query)}
    return [{'action': 'inline', 'params_dict': params_dict}]


def __process_callback_query(callback_query,):
    params_dict = {'chat_id': callback_query.message.chat.id,
                   'message_id': callback_query.message.message_id}

    data_array = callback_query.data.split(' ', 1)
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


# Kommando, Botname und Parameter aus einer Nachricht herausfiltern und zurückliefern
def __get_message_args(message_text):
    # Default-Werte
    command = ''
    botname = constants.botname
    param = ''

    if message_text.startswith('/'):  # Kommando
        if ' ' in message_text:  # Kommando mit Parametern
            param = message_text.split(' ', 1)[1]

        command_string = message_text.split(' ', 1)[0]
        if '@' in command_string:  # Botname in Kommando enthalten (@Scheschbot)
            # Kommando-String in Kommando und Botname aufteilen
            command_string = command_string.split('@')
            command = command_string[0]
            botname = command_string[1]
        else:  # Kommando ohne Botname
            command = command_string

        # Kommando und Botname kleine schreiben (vereinfacht spätere if-Abfragen)
        command = command.lower()
        botname = botname.lower()

        # Backslash abschneiden
        command = command[1:]
    else:  # kein Kommando
        param = message_text

    return command, botname, param


# User-Objekt aus dem Update-Objekt holen
# je nach Update-Art (Nachricht, Inline Query, usw. liegt das User-Objekt in einem anderen Teil des Update-Objekts
def __get_user(update):
    if update.message:  # wenn eine Nachricht gesendet wurde
        return update.message.from_user
    if update.edited_message:  # wenn eine Nachricht bearbeitet wurde
        return update.edited_message.from_user
    if update.inline_query:  # wenn eine Inline Query bearbeitet wurde
        return update.inline_query.from_user
    if update.callback_query:  # wenn eine Inline Query bearbeitet wurde
        return update.callback_query.from_user
