import db_connect
from datetime import datetime
from Util import StringUtils


def insert_timedmessages(value_2d_array):
    db_connect.insert('timed_messages',
                      ['message', 'send_time', 'chat_id'],
                      value_2d_array)


# liefert die fälligen Nachrichten und löscht diese aus der Datenbank
def get_due_messages():
    where_expression = 'send_time <= "' + StringUtils.convert_datetime_to_string(datetime.now()) + '"'

    due_messages = db_connect.select('timed_messages',
                                     'chat_id, message',
                                     where_expression)

    db_connect.delete('timed_messages',
                      where_expression)

    return due_messages
