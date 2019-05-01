import random

import telegram
import db_connect
import Main
import constants
from Process_Update import Main
from Functions import aggronyme, cook, answer


def get_message_list(message):
    message_list = []

    if message.text:
        message_list = get_message_list_for_text(message)
    elif message.audio:
        message_list = get_message_list_for_audio(message.audio)
    elif message.document:
        message_list = get_message_list_for_document(message)
    elif message.animation:
        message_list = get_message_list_for_animation(message.animation)
    elif message.game:
        message_list = get_message_list_for_game(message.game)
    elif message.photo:
        message_list = get_message_list_for_photo(message.photo)
    elif message.sticker:
        message_list = get_message_list_for_sticker(message.sticker)
    elif message.sticker:
        message_list = get_message_list_for_video(message.video)
    elif message.voice:
        message_list = get_message_list_for_voice(message.voice)
    elif message.video_note:
        message_list = get_message_list_for_video_note(message.video_note)
    elif message.location:
        message_list = get_message_list_for_location(message.location)
    elif message.venue:
        message_list = get_message_list_for_venue(message.venue)
    elif message.poll:
        message_list = get_message_list_for_poll(message.poll)
    elif message.new_chat_members:
        message_list = get_message_list_for_new_chat_members(message.new_chat_members)
    elif message.left_chat_members:
        message_list = get_message_list_for_left_chat_members(message.left_chat_members)
    elif message.new_chat_title:
        message_list = get_message_list_for_new_chat_title(message.new_chat_title)
    elif message.new_chat_photo:
        message_list = get_message_list_for_new_chat_photo(message.new_chat_photo)
    elif message.delete_chat_photo:
        message_list = get_message_list_for_delete_chat_photo(message.delete_chat_photo)

    return message_list


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


def get_message_list_for_audio(audio):
    return []


def get_message_list_for_document(message):
    output = __get_random_message_for_message_type('document')

    params_dict = {'chat_id': message.chat_id,
                   'text': output}
    return [{'action': 'text', 'params_dict': params_dict}]


def get_message_list_for_animation(animation):
    return []


def get_message_list_for_game(game):
    return []


def get_message_list_for_photo(photo):
    return []


def get_message_list_for_sticker(sticker):
    return []


def get_message_list_for_video(video):
    return []


def get_message_list_for_voice(voice):
    return []


def get_message_list_for_video_note(video_note):
    return []


def get_message_list_for_location(location):
    return []


def get_message_list_for_venue(venue):
    return []


def get_message_list_for_poll(poll):
    return []


def get_message_list_for_new_chat_members(new_chat_members):
    return []


def get_message_list_for_left_chat_members(left_chat_members):
    return []


def get_message_list_for_new_chat_title(new_chat_title):
    return []


def get_message_list_for_new_chat_photo(new_chat_photo):
    return []


def get_message_list_for_delete_chat_photo(delete_chat_photo):
    return []


def __get_random_message_for_message_type(message_type):
    probabilty_treshold = random.randint(1, 10001) / 100

    print(probabilty_treshold)

    random_messages_for_type = db_connect.select('random_messages m JOIN message_types t '
                                                 'ON m.fk_message_type_id = t.message_type_id',
                                                 'message, probability_percentage',
                                                 'message_type = "' + message_type + '" '
                                                 'AND probability_percentage <= ' + str(probabilty_treshold),
                                                 'probability_percentage ASC')
    for line in random_messages_for_type:
        print('\t', end='')
        for value in line:
            print(value, end="\t")
        print()

    return ['Mederer']
