import db_connect
from Util import StringUtils


def get_answer(message):
    print('input =', message)

    output = ''
    input_ids = []
    input_table = db_connect.select('answer_input')

    for line in input_table:
        required_input = line[1]

        # boolsche Werte setzen (0: False, 1: True)
        text_before = line[2] == 1
        text_after = line[3] == 1
        is_question = line[4] == 1
        contains_specialchars = line[5] == 1

        # falls Frage gesucht wird: hat die Nachricht ein Fragezeichen am Ende?
        if not is_question or (is_question and message.endswith('?')):
            # Sonderzeichen entfernen und alles klein schreiben
            # (außer der gesuchte String enthält ebenfalls Sonderzeichen)
            if not contains_specialchars:
                message = StringUtils.cut_specialchars(message)
                message = message.lower()

            # Leerzeichen am Anfang und Ende entfernen
            # doppelte Leerzeichen kürzen
            message = StringUtils.cut_spaces(message)

            # Fall 1: gesuchter Text kann an beliebiger Stelle in der Nachricht sein
            # Fall 2: gesuchter Text muss am Ende der Nachricht sein
            # Fall 3: gesuchter Text muss am Anfang der Nachricht sein
            # Fall 3: gesuchter Text muss mit der Nachricht identisch sein
            if (text_before and text_after and required_input in message)\
                    or (text_before and message.endswith(required_input))\
                    or (text_after and message.startswith(required_input))\
                    or message == required_input:
                # Übereinstimmung mit der Nachricht gefunden
                input_ids.append(line[0])

    if len(input_ids) > 0:  # falls Übereinstimmungen mit der Nachricht gefunden wurden
        # Input-IDs durch Komma trennen (für SQL-Abfrage)
        input_ids_string = ', '.join(str(input_id) for input_id in input_ids)

        possible_outputs = db_connect.select('answer_relations AS rel '
                                             'JOIN answer_output AS output ON rel.output_id = output.id',
                                             'output',
                                             'input_id IN (' + input_ids_string + ')')
        print('possible_outputs =', possible_outputs)

    return output


if __name__ == '__main__':
    print('answer =', get_answer('bot?!?'))
    print('answer =', get_answer('lustig    LuStig'))
    print('answer =', get_answer('lustig lustig'))
    print('answer =', get_answer('schnauze ANDI!'))
