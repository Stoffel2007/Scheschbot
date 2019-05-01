import random
import telegram
import db_connect
import Main
import constants
from Process_Update import Main
from Functions import aggronyme, cook, answer


def get_message_list(message):
    if message.text:
        return get_message_list_for_text(message)
    if message.audio:
        return get_message_list_for_audio(message)
    if message.document:
        return get_message_list_for_document(message)
    if message.animation:
        return get_message_list_for_animation(message)
    if message.game:
        return get_message_list_for_game(message)
    if message.photo:
        return get_message_list_for_photo(message)
    if message.sticker:
        return get_message_list_for_sticker(message)
    if message.sticker:
        return get_message_list_for_video(message)
    if message.voice:
        return get_message_list_for_voice(message)
    if message.video_note:
        return get_message_list_for_video_note(message)
    if message.location:
        return get_message_list_for_location(message)
    if message.venue:
        return get_message_list_for_venue(message)
    if message.poll:
        return get_message_list_for_poll(message)
    if message.new_chat_members:
        return get_message_list_for_new_chat_members(message)
    if message.left_chat_members:
        return get_message_list_for_left_chat_members(message)
    if message.new_chat_title:
        return get_message_list_for_new_chat_title(message)
    if message.new_chat_photo:
        return get_message_list_for_new_chat_photo(message)
    if message.delete_chat_photo:
        return get_message_list_for_delete_chat_photo(message)


def get_message_list_for_text(message):
    # Nachricht in Einzelteile zerlegen
    command, botname, param = Main.get_message_args(message.text)

    # Kommando war an den Scheschbot gerichtet
    # oder Nachricht enthielt kein Kommando
    if botname == constants.botname:
        # passendes Kommando suchen
        # TODO: Kommandos generisch in Array ablegen
        if command == 'koch':
            text = cook.cook(message, param)
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

            if admin_ids is not False:  # Datenbankabfrage war erfolgreich
                for i in range(len(admin_ids)):
                    params_dict = {'chat_id': admin_ids[i][0],
                                   'text': '"' + param + '" akzeptieren oder ablehnen?',
                                   'reply_markup': keyboard}
                    message_list.append({'action': 'text', 'params_dict': params_dict})

            return message_list

        output = answer.get_answer(message)

        if output != '':
            params_dict = {'chat_id': message.chat_id,
                           'text': output}
            return [{'action': 'text', 'params_dict': params_dict}]

        return []  # kein passendes Kommando gefunden
    return []  # Kommando ging an anderen Bot


def get_message_list_for_audio(message):
    output = __get_random_message_for_message_type('audio')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_document(message):
    output = __get_random_message_for_message_type('document')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_animation(message):
    output = __get_random_message_for_message_type('animation')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_game(message):
    output = __get_random_message_for_message_type('game')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_photo(message):
    output = __get_random_message_for_message_type('photo')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_sticker(message):
    output = __get_random_message_for_message_type('sticker')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_video(message):
    output = __get_random_message_for_message_type('video')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_voice(message):
    output = __get_random_message_for_message_type('voice')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_video_note(message):
    output = __get_random_message_for_message_type('video_note')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_location(message):
    output = __get_random_message_for_message_type('location')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_venue(message):
    output = __get_random_message_for_message_type('venue')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_poll(message):
    output = __get_random_message_for_message_type('poll')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_new_chat_members(message):
    output = __get_random_message_for_message_type('new_chat_members')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_left_chat_members(message):
    output = __get_random_message_for_message_type('left_chat_members')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_new_chat_title(message):
    output = __get_random_message_for_message_type('new_chat_title')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_new_chat_photo(message):
    output = __get_random_message_for_message_type('new_chat_photo')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_delete_chat_photo(message):
    output = __get_random_message_for_message_type('delete_chat_photo')
    if output == '':
        return []

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def __get_random_message_for_message_type(message_type):
    # Zufallsnachrichten für Typ holen
    random_messages_for_type = db_connect.select('random_messages m JOIN message_types t '
                                                 'ON m.fk_message_type_id = t.message_type_id',
                                                 'message, probability_percentage',
                                                 'message_type = "' + message_type + '"',
                                                 'probability_percentage DESC')

    # Wahrscheinlichkeiten aufsummieren
    probability_sum = sum(line[1] for line in random_messages_for_type)

    # individuelle Wahrscheinlichkeit für Nachrichtentyp miteinbeziehen
    message_type_probability = __get_probabilty_for_message_type(message_type)
    probability_sum *= 100
    probability_sum /= message_type_probability
    print('Summe:', probability_sum)

    # Zufallszahl generieren
    ranint = random.randint(1, probability_sum * 100) / 100
    print('ranint:', ranint)

    # aus Zahlenbereich entsprechende Nachricht (oder keine Nachricht) ziehen
    temp = 0
    for line in random_messages_for_type:
        temp += line[1]
        print('temp:', temp)
        if ranint <= temp:
            return line[0]

    return ''


def __get_probabilty_for_message_type(message_type):
    probability = db_connect.select('message_types',
                                    'message_type_probability_percentage',
                                    'message_type ="' + message_type + '"')

    if probability:
        return probability[0][0]

    return 100
