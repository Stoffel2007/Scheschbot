import pymysql
import datetime
from Util import StringUtils


def __query(query_string):
    try:
        # Connection herstellen
        connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     passwd='',
                                     db='scheschbot')

        # Verbindungsart Cursor
        cursor = connection.cursor()
        connection.set_charset('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        # print('\t' + query_string)
        # start = time.time()
        cursor.execute(query_string)
        # end = time.time()
        # delta = end - start
        # print('\tAbfrage dauerte ' + delta.__str__() + ' Sekungeden')
        connection.commit()

        # Ergebnis in Array speichern
        result = []
        for line in cursor:
            line_array = []
            for value in line:
                line_array.append(value)
            result.append(line_array)

        # Cursor und Connection schließen
        cursor.close()
        connection.close()

        return result
    except pymysql.err.OperationalError:
        print('\tVerbindung zur Datenbank fehlgeschlagen')
        return False


# SELECT-Abfrage auf der Datenbank
def select(table, column="*", where_expression="1 = 1"):
    query_string = 'SELECT ' + column + ' ' +\
                   'FROM ' + table + ' ' +\
                   'WHERE ' + where_expression

    return __query(query_string)


# UPDATE-Abfrage auf der Datenbank
def update(table, column_array, value_array, where_expression):
    # Fehler werfen, wenn die Anzahl an Spalten nicht mit der Anzahl an Werten übereinstimmt
    if len(column_array) != len(value_array):
        raise IndexError("Anzahl an Spalten und Wertem stimmt nicht überein")

    # Werte für die SQL-Query vorbereiten (Anführungszeichen, NULL)
    for i in range(0, len(value_array)):
        value_array[i] = __prepare_for_query(value_array[i])

    # Spaltennamen und Spaltenwerte zusammenführen
    set_string = ''
    for i in range(0, len(column_array)):
        set_string += column_array[i] + ' = ' + value_array[i].__str__()
        # bei letztem Durchlauf kein Komma mehr setzen
        if i < len(column_array) - 1:
            set_string += ', '

    query_string = 'UPDATE ' + table + ' ' +\
                   'SET ' + set_string + ' ' +\
                   'WHERE ' + where_expression

    result = __query(query_string)

    return result is not False


# INSERT-Abfrage auf der Datenbank
def insert(table, column_array, value_2d_array):
    value_string = '('

    # über Wertezeilen iterieren
    for i in range(len(value_2d_array)):
        # Fehler werfen, wenn die Anzahl an Spalten nicht mit der Anzahl an Werten übereinstimmt
        if len(column_array) != len(value_2d_array[i]):
            raise IndexError("Anzahl an Spalten und Wertem stimmt nicht überein")

        # Werte für die SQL-Query vorbereiten (Anführungszeichen, NULL)
        for j in range(len(value_2d_array[i])):
            value_2d_array[i][j] = __prepare_for_query(value_2d_array[i][j])

        # Wertezeile in String umwandeln
        value_2d_array[i] = ','.join(str(x) for x in value_2d_array[i])

    # Wertezeilen in Gesamt-String umwandeln
    value_string += '),('.join(value_2d_array)
    value_string += ')'

    '''
    # Werte durch Kommata trennen
    for i in range(0, len(value_2d_array)):
        value_string += value_2d_array[i].__str__()
        # bei letztem Durchlauf kein Komma mehr setzen
        if i < len(value_2d_array) - 1:
            value_string += ', '
    '''

    # Spaltennamen durch Kommata trennen
    column_string = ','.join(column_array)
    '''
    for i in range(0, len(column_array)):
        column_string += column_array[i]
        # bei letztem Durchlauf kein Komma mehr setzen
        if i < len(column_array) - 1:
            column_string += ', '
    '''

    query_string = 'INSERT INTO ' + table + ' ' +\
                   '(' + column_string + ') ' +\
                   'VALUES ' + value_string

    result = __query(query_string)

    return result is not False


# INSERT-Abfrage auf der Datenbank
def delete(table, where_expression):
    query_string = 'DELETE FROM ' + table + ' ' +\
                   'WHERE ' + where_expression

    result = __query(query_string)

    if result is not False:
        return True
    return False


# Wert für die SQL-Query vorbereiten
def __prepare_for_query(value):
    # überprüft, ob ein Objekt ein Integer ist
    def is_int(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    if value is None or value == '':  # 'None' durch NULL ersetzen
        return 'NULL'
    if isinstance(value, datetime.datetime):  # Datetime formatieren
        return '"' + StringUtils.convert_datetime_to_string(value) + '"'
    if not is_int(value):  # String mit Anführungszeichen versehen
        return '"' + str(value) + '"'
    return value  # Zahlen werden nicht verändert
