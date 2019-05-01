import constants
from Process_Update import Main


def get_message_list(edited_message):
    # Nachricht in Einzelteile zerlegen
    command, botname, param = Main.get_message_args(edited_message.text)

    if botname == constants.botname:  # Kommando war an den Scheschbot gerichtet
        params_dict = {'chat_id': edited_message.chat_id,
                       'text': 'bearbeitete Nachricht',
                       'message_id': edited_message.message_id}
        return [{'action': 'text', 'params_dict': params_dict}]
    return []  # Kommando ging an anderen Bot
