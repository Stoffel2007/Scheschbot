import random
import db_connect
from Util import StringUtils


def get_answer(message):
    original_input = message.text

    output = ''
    input_id = None
    input_table = db_connect.select('answer_input')

    # Input-Tabelle nach einem passenden Eintrag durchsuchen
    # erster passender Eintrag wird genommen
    for line in input_table:
        required_input = line[1]  # Input dieser Zeile in der Tabelle

        # boolsche Werte setzen (0: False, 1: True)
        text_before = line[2] == 1
        text_after = line[3] == 1
        is_question = line[4] == 1
        contains_specialchars = line[5] == 1

        # verhindert, dass Modifikationen im ersten Durchlauf nicht mehr rückgängig gemacht werden können
        temp_input = original_input

        # falls Frage gesucht wird: hat die Nachricht ein Fragezeichen am Ende?
        if not is_question or (is_question and temp_input.endswith('?')):
            # Sonderzeichen entfernen und alles klein schreiben
            # (außer der gesuchte String enthält ebenfalls Sonderzeichen)
            if not contains_specialchars:
                temp_input = StringUtils.cut_specialchars(temp_input)
                temp_input = temp_input.lower()

            # Leerzeichen am Anfang und Ende entfernen
            # doppelte Leerzeichen kürzen
            temp_input = StringUtils.cut_spaces(temp_input)

            # Fall 1: gesuchter Text kann an beliebiger Stelle in der Nachricht sein
            # Fall 2: gesuchter Text muss am Ende der Nachricht sein
            # Fall 3: gesuchter Text muss am Anfang der Nachricht sein
            # Fall 3: gesuchter Text muss mit der Nachricht identisch sein
            if (text_before and text_after and required_input in temp_input)\
                    or (text_before and temp_input.endswith(required_input))\
                    or (text_after and temp_input.startswith(required_input))\
                    or temp_input == required_input:
                # Übereinstimmung mit der Nachricht gefunden
                input_id = line[0]
                break

    if input_id is not None:  # falls eine Übereinstimmung mit der Nachricht gefunden wurden
        possible_outputs = db_connect.select('answer_relations AS rel '
                                             'JOIN answer_output AS output ON rel.output_id = output.id',
                                             'output, output.id, previous_output_id',
                                             'input_id = ' + input_id.__str__())

        possible_outputs_with_pre = []
        possible_outputs_without_pre = []

        last_output_id = __get_last_output_id(message.chat.id)

        for output_line in possible_outputs:
            if output_line[2] is not None:
                if output_line[2] == last_output_id:
                    possible_outputs_with_pre.append(output_line)
            else:
                possible_outputs_without_pre.append(output_line)

        if len(possible_outputs_with_pre) > 0:
            possible_outputs = possible_outputs_with_pre
        else:
            possible_outputs = possible_outputs_without_pre

        if len(possible_outputs) > 0:
            # aus den möglichen Antworten eine zufällig wählen
            output_index = random.randint(0, len(possible_outputs) - 1)
            output = possible_outputs[output_index][0]

            # ID des letzten Outputs merken
            __set_last_output_id(possible_outputs[output_index][1], message.chat.id)

    return output


# ID des letzten Outputs aus dem Chat holen
# liefert None, falls noch kein Eintrag zu diesem Chat existiert
def __get_last_output_id(chat_id):
    last_update_id = None

    result = db_connect.select('answer_last_output',
                               'last_output_id',
                               'chat_id = ' + chat_id.__str__())

    # falls Ergebnis herauskam
    if len(result) > 0:
        last_update_id = result[0][0]

    return last_update_id


# letzten Output für einen bestimmten Chat in Datenbank speichern
def __set_last_output_id(last_output_id, chat_id):
    # überprüfen, ob zu diesem Chat bereits ein Eintrag existiert
    old_output_id = __get_last_output_id(chat_id)

    if old_output_id is not None:  # Eintrag existiert bereits
        db_connect.update('answer_last_output',
                          ['last_output_id'],
                          [last_output_id],
                          'chat_id = ' + chat_id.__str__())
    else:  # Eintrag existiert noch nicht
        db_connect.insert('answer_last_output',
                          ['chat_id', 'last_output_id'],
                          [chat_id, last_output_id])
