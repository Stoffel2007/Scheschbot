import time
import telegram
import constants
import db_connect
import process_update
from Events.EventHandler import *


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
    bot = telegram.Bot(constants.botkey)

    # EventHandler für zeitbasierte Events
    event_handler = EventHandler()

    # ID des letzten unverarbeiteten Updates holen
    last_update_id = get_last_update_id(bot)
    print("\nlast_update_id =", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        try:
            # neueste Updates von Telegram holen
            for update in bot.getUpdates(offset=last_update_id):
                # Update verarbeiten
                message_list = process_update.get_message_list(update, event_handler)

                # erhaltene Nachrichten abschicken
                for message in message_list:
                    try:
                        send_reaction(bot, message['action'], message['params_dict'])
                    except telegram.error.Unauthorized:
                        print('\tEin Benutzer (ID: ' + message['params_dict']['chat_id'].__str__() +
                              ' hat den Bot nicht gestartet')

                # Update-ID hochzählen
                last_update_id = update.update_id + 1

            # nach neuen Events fragen
            for event_update in event_handler.get_update():
                message = event_update[0]
                text = event_update[1]
                params_dict = {'chat_id': message.chat_id,
                               'text': text,
                               'message_id': message.message_id}
                send_reaction(bot, 'text', params_dict)

            if temp is not last_update_id:
                print('\nlast_update_id =', last_update_id)

            # 1 Sekunde warten (Überlastung des Servers vorbeugen)
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
        except telegram.error.NetworkError:
            print('\tVerbindung zum Bot fehlgeschlagen. Nächster Versuch in 10 Sekunden....')
            time.sleep(10)


# Nachricht verschiedener Art absenden
def send_reaction(bot, action, params_dict):
    try:
        if action == 'text':  # Textnachricht senden
            bot.send_message(chat_id=params_dict['chat_id'],
                             text=params_dict['text'],
                             reply_to_message_id=params_dict.get('message_id', None),
                             reply_markup=params_dict.get('reply_markup', None))
        elif action == 'photo':  # Foto senden
            bot.send_photo(chat_id=params_dict['chat_id'],
                           text=params_dict['photo'],
                           caption=params_dict['caption'],
                           reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'gif':  # GIF senden
            bot.send_document(chat_id=params_dict['chat_id'],
                              text=params_dict['gif'],
                              caption=params_dict['caption'],
                              reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'video':  # Video senden
            bot.send_video(chat_id=params_dict['chat_id'],
                           text=params_dict['gif'],
                           caption=params_dict['caption'],
                           reply_to_message_id=params_dict.get('message_id', None))
        elif action == 'inline':  # Inline-Menü senden
            bot.answer_inline_query(inline_query_id=params_dict['inline_query_id'],
                                    results=params_dict['results'])
        elif action == 'edit_message':  # Textnachricht verändern
            bot.edit_message_text(chat_id=params_dict['chat_id'],
                                  message_id=params_dict['message_id'],
                                  text=params_dict['text'])
        else:
            print('\tfalsche action-Variable (' + action + ')')
    except KeyError:
        print('\tFehler im Parameter-Array:')
        print('\t', end='')
        print(params_dict)


if __name__ == '__main__':
    main()
