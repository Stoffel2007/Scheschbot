import random
import db_connect
from Functions import answer_special
from Util import StringUtils


def get_answer(message):
    answer = ''

    # Nachricht anhand von Satzzeichen in einzelne Sätze aufteilen
    sentence_array = __split_message(message.text)

    for sentence in sentence_array:
        # auf jeden Satz einzeln reagieren
        output = __get_output(sentence, message.chat.id)
        if output != '':
            answer += output + '\n'

    return answer


# sucht zu einem bestimmten Input den passenden Output aus der Datenbank
def __get_output(message, chat_id):
    input_id = __get_input_id(message)

    if input_id is not None:  # falls eine Übereinstimmung mit der Nachricht gefunden wurde
        # 2D-Array in der Form [[output, output_id, previous_output_id], ....]
        possible_outputs = __get_possible_outputs(input_id, chat_id)

        if len(possible_outputs) > 0:  # passender Output gefunden
            # aus den möglichen Antworten eine zufällig wählen
            output_index = random.randint(0, len(possible_outputs) - 1)

            # ID des letzten Outputs in Datenbank ablegen
            __set_last_output(possible_outputs[output_index], chat_id)

            return possible_outputs[output_index]

    # keine passende Antwort gefunden
    # in den Sonderfällen nach einer Antwort suchen
    return answer_special.get_answer(message)


# teilt eine Nachricht in einzelne Sätze auf (anhand von Satzzeichen)
def __split_message(message):
    sentence_array = []
    delimiters = ['.', '!', '?']
    last_index = 0

    for i in range(len(message)):
        for char in delimiters:
            if message[i] == char:
                sentence = message[last_index:i + 1]
                sentence_array.append(sentence)
                last_index = i + 1

    # falls kein Satzzeichen am Ende steht
    # letzten Satz auch noch hinzufügen
    if last_index < len(message):
        sentence = message[last_index:len(message)]
        sentence_array.append(sentence)

    return sentence_array


# sucht zu einer Nachricht den passenden Eintrag in der Datenbank und liefert dessen ID zurück
def __get_input_id(original_input):
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

            # Text ist identisch mit dem gesuchten Input
            text_is_input = temp_input == required_input
            # gesuchter Input ist am Anfang des Textes (mit Leerzeichen)
            text_at_start = temp_input.startswith(required_input + ' ')
            # gesuchter Input ist am Ende des Textes (mit Leerzeichen)
            text_at_end = temp_input.endswith(' ' + required_input)
            # gesuchter Input ist in der Mitte des Textes (mit Leerzeichen)
            text_in_input = ' ' + required_input + ' ' in temp_input

            # Fall 1: gesuchter Text kann an beliebiger Stelle in der Nachricht sein
            case1 = text_before and text_after and (text_is_input or text_at_start or text_at_end or text_in_input)
            # Fall 2: gesuchter Text muss am Ende der Nachricht sein
            case2 = text_before and (text_is_input or text_at_end)
            # Fall 3: gesuchter Text muss am Anfang der Nachricht sein
            case3 = text_after and (text_is_input or text_at_start)
            # Fall 4: gesuchter Text muss mit der Nachricht identisch sein
            case4 = text_is_input

            if case1 or case2 or case3 or case4:
                # Übereinstimmung mit der Nachricht gefunden
                return line[0]
    return None


# liefert zu einer Input-ID die möglichen Outputs zurück
# Output mit erfülltr Vorbedingung haben Vorrang
def __get_possible_outputs(input_id, chat_id):
    possible_outputs = db_connect.select('answer_relations AS rel '
                                         'JOIN answer_output AS output ON rel.output_id = output.id '
                                         'LEFT JOIN answer_output AS pre ON rel.previous_output_id = pre.id',
                                         'output.output, pre.output',
                                         'input_id = ' + input_id.__str__())

    possible_outputs_with_pre = []
    possible_outputs_without_pre = []

    last_output = __get_last_output(chat_id)

    for output_line in possible_outputs:
        if output_line[1] is not None:
            if output_line[1] == last_output:
                possible_outputs_with_pre.append(output_line[0])  # Vorbedingung ist erfüllt
        else:
            possible_outputs_without_pre.append(output_line[0])  # Vorbedingung ist nicht erfüllt

    if len(possible_outputs_with_pre) > 0:  # mindestens ein Output mit erfüllter Vorbedingung wurde gefunden
        return possible_outputs_with_pre
    else:  # kein Output mit erfüllter Vorbedingung wurde gefunden
        return possible_outputs_without_pre


# ID des letzten Outputs aus dem Chat holen
# liefert None, falls noch kein Eintrag zu diesem Chat existiert
def __get_last_output(chat_id):
    last_update_id = None

    result = db_connect.select('answer_last_output',
                               'last_output',
                               'chat_id = ' + chat_id.__str__())

    # falls Ergebnis herauskam
    if len(result) > 0:
        last_update_id = result[0][0]

    return last_update_id


# letzten Output für einen bestimmten Chat in Datenbank speichern
def __set_last_output(last_output, chat_id):
    # überprüfen, ob zu diesem Chat bereits ein Eintrag existiert
    old_output_id = __get_last_output(chat_id)

    if old_output_id is not None:  # Eintrag existiert bereits
        db_connect.update('answer_last_output',
                          ['last_output'],
                          [last_output],
                          'chat_id = ' + chat_id.__str__())
    else:  # Eintrag existiert noch nicht
        db_connect.insert('answer_last_output',
                          ['chat_id', 'last_output'],
                          [chat_id, last_output])
