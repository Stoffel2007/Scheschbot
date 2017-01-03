import db_connect
from Util import StringUtils


def get_answer(message):
    output = ''
    input_id = None
    input_table = db_connect.select('answer_input')

    print('input_table =')

    for line in input_table:
        print("\t", line)
        required_input = line[1]

        # boolsche Werte setzen (0: False, 1: True)
        text_before = line[2] == 1
        text_after = line[3] == 1
        is_question = line[4] == 1
        contains_specialchars = line[5] == 1

        # Sonderzeichen entfernen (außer der gesuchte String enthält ebenfalls Sonderzeichen)
        if not contains_specialchars:
            message = StringUtils.cut_specialchars(message)

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
            input_id = line[0]
            break

    if input_id is not None:  # falls Übereinstimmung mit der Nachricht gefunden wurde
        possible_outputs = db_connect.select('answer_relations AS rel '
                                             'JOIN answer_output AS output ON rel.output_id = output.id',
                                             'output',
                                             'input_id = "' + input_id.__str__() + '"')
        print('possible_outputs =', possible_outputs)

    return output


if __name__ == '__main__':
    print('answer =', get_answer('!schnauze bot!'))
