import pymysql
import time


def query(query_string):
    # maximal 10 mal versuchen, Verbindung zur Datenbank herstellen
    # ansonsten False zurückliefern
    try_counter = 0
    while try_counter < 10:
        try:
            # Connection herstellen
            connection = pymysql.connect(host='localhost',
                                         port=3306,
                                         user='root',
                                         passwd='',
                                         db='scheschbot')

            # Verbindungsart Cursor
            cursor = connection.cursor()
            start = time.time()
            cursor.execute(query_string)
            end = time.time()
            delta = end - start
            print("Abfrage dauerte " + delta.__str__() + " Sekunden")
            connection.commit()

            # Cursor und Connection schließen
            cursor.close()
            connection.close()

            return cursor
        except pymysql.err.OperationalError:
            print("Verbindung zur Datenbank fehlgeschlagen. Nächster Versuch in 10 Sekunden....")
            # hochzählen
            try_counter += 1
            time.sleep(10)
    print("10 Fehlversuche beim Verbinden zur Datenbank => return False")
    return False


# SELECT-Abfrage auf der Datenbank
def select(table, column, where_expression):
    query_string = 'SELECT ' + column + ' ' +\
                   'FROM ' + table + ' ' +\
                   'WHERE ' + where_expression
    return query(query_string)


# UPDATE-Abfrage auf der Datenbank
def update(table, column_array, value_array, where_expression):
    # überprüft, ob ein Objekt ein Integer ist
    def is_int(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    # Fehler werfen, wenn die Anzahl an Spalten nicht mit der Anzahl an Werten übereinstimmt
    if len(column_array) != len(value_array):
        raise IndexError("Anzahl an Spalten und Wertem stimmt nicht überein")

    # Anführungszeichen bei Strings anfügen
    for i in range(0, len(value_array)):
        if not is_int(value_array[i]):
            value_array[i] = '"' + value_array[i] + '"'

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

    query(query_string)


# INSERT-Abfrage auf der Datenbank
def insert(table, column_array, value_array):
    # überprüft, ob ein Objekt ein Integer ist
    def is_int(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    # Fehler werfen, wenn die Anzahl an Spalten nicht mit der Anzahl an Werten übereinstimmt
    if len(column_array) != len(value_array):
        raise IndexError("Anzahl an Spalten und Wertem stimmt nicht überein")

    print(value_array);
    # Anführungszeichen bei Strings anfügen
    for i in range(0, len(value_array)):
        if not is_int(value_array[i]):
            value_array[i] = '"' + value_array[i] + '"'

    # Werte durch Kommata trennen
    value_string = ''
    for i in range(0, len(value_array)):
        value_string += value_array[i].__str__()
        # bei letztem Durchlauf kein Komma mehr setzen
        if i < len(value_array) - 1:
            value_string += ', '

    # Spaltennamen durch Kommata trennen
    column_string = ''
    for i in range(0, len(column_array)):
        column_string += column_array[i]
        # bei letztem Durchlauf kein Komma mehr setzen
        if i < len(column_array) - 1:
            column_string += ', '

    query_string = 'INSERT INTO ' + table + ' ' +\
                   '(' + column_string + ') ' +\
                   'VALUES (' + value_string + ')'

    query(query_string)
