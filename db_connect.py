import pymysql
import time


def query(query_string):
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
        print("Error connecting to the database")
        return False
