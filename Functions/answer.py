import db_connect
from Util import StringUtils


def get_answer(message):
    output = ''
    input_id = None
    input_table = db_connect.select('answer_input')
    print('input_table =', input_table)

    for line in input_table:
        required_input = line[1]

        # boolsche Werte setzen (0: False, 1: True)
        text_before = line[2] == 1
        text_after = line[3] == 1
        is_question = line[4] == 1
        contains_specialchars = line[5] == 1

        if not contains_specialchars:
            message = StringUtils.cut_spaces(message)

        if text_before and text_after:
            if required_input in message:
                input_id = line[0]
                break
        elif text_before:
            if message.endswith(required_input):
                input_id = line[0]
                break
        elif text_after:
            if message.startswith(required_input):
                input_id = line[0]
                break
        else:
            if message == required_input:
                input_id = line[0]
                break

    if input_id is not None:
        possible_outputs = db_connect.select('answer_relations AS rel '
                                             'JOIN answer_output AS output ON rel.output_id = output.id',
                                             'output',
                                             'input_id = "' + input_id.__str__() + '"')
        print('possible_outputs =', possible_outputs)

    return output


if __name__ == '__main__':
    print('answer =', get_answer('bot'))
