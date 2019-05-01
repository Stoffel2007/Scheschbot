import random
import constants
from Functions import mood
from Process_Update import process_message, process_edited_message, process_inline_query, process_callback_query


def get_message_list(update):
    # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben (core.telegram.org/bots/api#update)
    print("\n\tupdate =", update)

    # sympathy_percentage des Users zufällig neu setzen
    user = __get_user(update)
    sympathy_percentage = random.randint(0, 100)
    mood.set_mood(user, sympathy_percentage)

    # Array mit zurückzuliefernden Nachrichten
    # jede message ist ein dictionary
    message_list = []

    # Update je nach Typ anders verarbeiten
    if update.message:
        message_list = process_message.get_message_list(update.message)
    elif update.edited_message:
        message_list = process_edited_message.get_message_list(update.edited_message)
    elif update.inline_query:
        message_list = process_inline_query.get_message_list(update.inline_query)
    elif update.callback_query:
        message_list = process_callback_query.get_message_list(update.callback_query)

    return message_list


# Kommando, Botname und Parameter aus einer Nachricht herausfiltern und zurückliefern
def get_message_args(message_text):
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
