import telegram
import db_connect
import Main
import constants
from Process_Update import Main
from Functions import aggronyme, cook, answer


def get_message_list(message):
    if message.text:
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
