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
